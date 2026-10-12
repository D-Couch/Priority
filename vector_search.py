"""Optional local semantic rule retrieval; SQLite float32 blobs, exact cosine search."""
from array import array
from contextlib import closing
import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import sqlite3
import tempfile
import time
import urllib.parse
import urllib.request

import knowledge

MODEL = 'text-embedding-nomic-embed-text-v1.5'
INDEX = Path(os.environ.get('MTG_VECTOR_INDEX', knowledge.DATA/'rule-vectors.sqlite'))
FORMAT = 1
_CACHE = {}


def api(path, payload=None):
    base = os.environ.get('LM_STUDIO_URL', 'http://127.0.0.1:1234/v1').rstrip('/')
    if urllib.parse.urlparse(base).hostname not in ('localhost','127.0.0.1','::1'):
        raise ValueError('Embeddings must use a loopback LM Studio server.')
    headers = {'Content-Type':'application/json'}
    token = os.environ.get('LM_STUDIO_API_KEY')
    if token: headers['Authorization'] = 'Bearer '+token
    url = base.removesuffix('/v1')+path if path.startswith('/api/') else base+path
    request = urllib.request.Request(url, data=json.dumps(payload).encode() if payload is not None else None, headers=headers)
    with urllib.request.urlopen(request, timeout=120) as response:
        return json.load(response)


def model_identity():
    models = api('/api/v1/models')['models']
    model = next((m for m in models if m.get('key') == MODEL and m.get('type') == 'embedding'), None)
    if model is None: raise ValueError('The configured local Nomic embedding model is unavailable.')
    return {k:model.get(k) for k in ('key','quantization','size_bytes','format','max_context_length')}


def normalize(vector):
    if not vector or not all(isinstance(x,(int,float)) and math.isfinite(x) for x in vector):
        raise ValueError('Invalid embedding values')
    norm = math.sqrt(sum(x*x for x in vector))
    if not norm: raise ValueError('Zero embedding vector')
    return [x/norm for x in vector]


def embed(texts, prefix):
    data = api('/embeddings', {'model':MODEL,'input':[prefix+text for text in texts]})
    rows = sorted(data['data'], key=lambda row:row['index'])
    if [r['index'] for r in rows] != list(range(len(texts))):
        raise ValueError('Incomplete embedding batch')
    vectors = [normalize(r['embedding']) for r in rows]
    if len({len(v) for v in vectors}) != 1: raise ValueError('Mixed embedding dimensions')
    return vectors


def rule_rows():
    with closing(knowledge.connect()) as conn:
        return [(r['number'],r['body']) for r in conn.execute('SELECT number,body FROM rules ORDER BY number')]


def fingerprint(rows):
    return hashlib.sha256(json.dumps(rows,ensure_ascii=False,separators=(',',':')).encode()).hexdigest()


def chunks(rows):
    rules = dict(rows)
    for number,body in rows:
        chapter = rules.get(number.split('.')[0], '')
        # Small overlapping chunks avoid exceeding the installed 2048-token embedding context.
        # Retrieval always returns the complete original rule, not truncated chunk text.
        for start in range(0,len(body),1000):
            yield number, f'Rule {number}. {chapter}\n'+body[start:start+1200]
            if start+1200 >= len(body): break


def build(path=INDEX):
    path = Path(path); path.parent.mkdir(parents=True,exist_ok=True)
    rows = rule_rows(); documents = list(chunks(rows)); start = time.perf_counter()
    identity = model_identity()
    fd, temporary = tempfile.mkstemp(prefix='vector-build-',suffix='.sqlite',dir=path.parent)
    os.close(fd)
    try:
        with closing(sqlite3.connect(temporary)) as conn:
            conn.executescript('CREATE TABLE metadata (key TEXT PRIMARY KEY, value TEXT); CREATE TABLE vectors (number TEXT, embedding BLOB);')
            dimension = None
            for offset in range(0,len(documents),32):
                batch = documents[offset:offset+32]
                vectors = embed([text for _,text in batch], 'search_document: ')
                for (number,_),vector in zip(batch,vectors):
                    if dimension is not None and len(vector)!=dimension: raise ValueError('Embedding dimensions changed during build')
                    dimension=len(vector)
                    packed=array('f',vector)
                    # Portable little endian storage.
                    import sys
                    if sys.byteorder!='little': packed.byteswap()
                    conn.execute('INSERT INTO vectors VALUES (?,?)',(number,packed.tobytes()))
                if offset%320==0: print(f'Embedded {min(offset+32,len(documents))}/{len(documents)} rule chunks',flush=True)
            meta={'format':FORMAT,'model':MODEL,'model_identity':identity,'rules_sha256':fingerprint(rows),'dimensions':dimension,
                  'chunks':len(documents),'rules':len(rows),'build_seconds':round(time.perf_counter()-start,3),
                  'document_prefix':'search_document: ','query_prefix':'search_query: ',
                  'chunk_characters':1200,'overlap_characters':200}
            conn.executemany('INSERT INTO metadata VALUES (?,?)',[(k,json.dumps(v)) for k,v in meta.items()])
            conn.commit()
        os.replace(temporary,path)
        print(json.dumps({**meta,'bytes':path.stat().st_size},indent=2))
        return meta
    finally:
        if os.path.exists(temporary):os.unlink(temporary)


def load(path=INDEX):
    path=Path(path)
    if not path.exists(): raise ValueError('Build the local semantic index with .venv/bin/python vector_search.py build before enabling hybrid retrieval.')
    key=(str(path.resolve()),path.stat().st_mtime_ns,path.stat().st_size)
    if key not in _CACHE:
        with closing(sqlite3.connect(f'{path.resolve().as_uri()}?mode=ro',uri=True)) as conn:
            meta={k:json.loads(v) for k,v in conn.execute('SELECT key,value FROM metadata')}
            if meta.get('format')!=FORMAT or meta.get('model')!=MODEL: raise ValueError('Incompatible semantic index; rebuild it.')
            vectors=[]
            for number,blob in conn.execute('SELECT number,embedding FROM vectors'):
                vector=array('f');vector.frombytes(blob)
                import sys
                if sys.byteorder!='little':vector.byteswap()
                if len(vector)!=meta['dimensions']:raise ValueError('Corrupt semantic index dimensions')
                vectors.append((number,vector))
        _CACHE.clear();_CACHE[key]=(meta,vectors)
    meta,vectors=_CACHE[key]
    if meta['rules_sha256']!=fingerprint(rule_rows()):raise ValueError('Rules changed; rebuild the semantic index before using hybrid retrieval.')
    return meta,vectors


def search(question, limit=24):
    meta,vectors=load()
    if model_identity()!=meta['model_identity']:raise ValueError('Embedding model changed; rebuild the semantic index.')
    query=embed([question[:1200]],'search_query: ')[0]
    if len(query)!=meta['dimensions']:raise ValueError('Embedding model dimensions differ from index; rebuild it.')
    scores={}
    for number,vector in vectors:
        score=sum(a*b for a,b in zip(query,vector))
        scores[number]=max(scores.get(number,-math.inf),score)
    return sorted(scores,key=lambda n:(-scores[n],n))[:limit]


def fuse(lexical,semantic,k=60):
    scores={}
    for ranking in (lexical,semantic):
        for rank,number in enumerate(dict.fromkeys(ranking),1):
            scores[number]=scores.get(number,0)+1/(k+rank)
    return sorted(scores,key=lambda n:(-scores[n],n))


def configuration():
    mode=os.environ.get('MTG_RETRIEVAL','lexical')
    if mode not in ('lexical','hybrid'):raise ValueError('MTG_RETRIEVAL must be lexical or hybrid')
    result={'mode':mode}
    if mode=='hybrid':
        meta,_=load()
        with INDEX.open('rb') as f: digest=hashlib.file_digest(f,'sha256').hexdigest()
        result.update(model=MODEL,index_sha256=digest,index_metadata=meta,fusion='rrf',rrf_k=60,semantic_limit=24,query_characters=1200)
    return result


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command',choices=['build'])
    parser.add_argument('--frozen',action='store_true',help='Build against the benchmark corpus instead of live knowledge')
    args=parser.parse_args()
    if args.frozen:
        from benchmark import frozen_corpus
        with frozen_corpus():build()
    else:build()
