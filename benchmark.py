#!/usr/bin/env python3
"""Versioned end-to-end benchmark; use the real chat handler, never feed it labels."""
import argparse
from contextlib import closing, contextmanager
from datetime import datetime, timezone
import gzip
import hashlib
import json
import math
from pathlib import Path
import platform
import re
import shutil
import sqlite3
import statistics
import subprocess
import tempfile
import threading
import time
import urllib.request
import urllib.error

import knowledge
import server

ROOT = Path(__file__).resolve().parent
BENCH = ROOT / 'benchmarks'
SUITE = BENCH / 'scenarios.json'
CITATION = re.compile(r'\[(CR \d{3}(?:\.\d+[a-z]?)?|C\d+)\]')


def read(path):
    return json.loads(Path(path).read_text())


def write(path, value):
    path = Path(path)
    temporary = path.with_suffix(path.suffix+'.tmp')
    temporary.write_text(json.dumps(value, indent=2, ensure_ascii=False)+'\n')
    temporary.replace(path)


def sha(path):
    with Path(path).open('rb') as f:
        return hashlib.file_digest(f, 'sha256').hexdigest()


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT, text=True).strip()


def validate_suite(suite):
    if suite.get('schema_version') != 1 or len(suite['cases']) != 20:
        raise ValueError('Expected gameplay-v1 schema with 20 cases; version suite changes explicitly.')
    ids = [c['id'] for c in suite['cases']]
    if len(set(ids)) != len(ids):
        raise ValueError('Duplicate scenario IDs')
    references = read(BENCH/'references.json')
    with closing(knowledge.connect()) as conn:
        for case in suite['cases']:
            if len(case['cards']) != len(case['card_ids']):
                raise ValueError('Card IDs do not match names')
            for name, cid in zip(case['cards'], case['card_ids']):
                r = conn.execute('SELECT name FROM cards WHERE id=?',(cid,)).fetchone()
                if not r or r['name'] != name:
                    raise ValueError('Missing or mismatched Oracle card: '+name)
            if not case['criteria'] or len({c['id'] for c in case['criteria']}) != len(case['criteria']):
                raise ValueError('Missing or duplicate rubric criteria')
            for group in case['evidence_groups']:
                if not group['any_of']:
                    raise ValueError('Empty evidence group')
                for key in group['any_of']:
                    reference = references[key]
                    if key.startswith('CR '):
                        row = conn.execute('SELECT body FROM rules WHERE number=?',(key[3:],)).fetchone()
                    else:
                        row = conn.execute('SELECT body FROM cards WHERE name=?',(key[5:],)).fetchone()
                    if not row or hashlib.sha256(row['body'].encode()).hexdigest() != reference['sha256']:
                        raise ValueError('Reference changed: '+key)


def source_key(source):
    return 'CARD '+source['title'] if source['kind']=='card' else source['id']


def measure_evidence(case, sources, answer):
    found = {source_key(s) for s in sources}
    groups = case['evidence_groups']
    hits = [bool(set(g['any_of']) & found) for g in groups]
    ids = {s['id'] for s in sources}
    cited = set(CITATION.findall(answer))
    return {'evidence_recall':sum(hits)/len(hits), 'all_evidence_found':all(hits),
            'missing_evidence':[g['label'] for g, hit in zip(groups,hits) if not hit],
            'retrieved_count':len(sources), 'context_characters':sum(len(s['text']) for s in sources),
            'citations':sorted(cited), 'invalid_citations':sorted(cited-ids),
            'citation_id_precision':len(cited & ids)/len(cited) if cited else None}


def percentile(values, q):
    return sorted(values)[max(0,math.ceil(len(values)*q)-1)] if values else None


def summary(run):
    rows = run['results']
    completed = [r for r in rows if not r.get('error')]
    times = [r['timing']['total_seconds'] for r in completed]
    first = [r['timing']['first_visible_token_seconds'] for r in completed if r['timing'].get('first_visible_token_seconds') is not None]
    reviewed = [r for r in rows if r.get('review')]
    valid_count = sum(len(r['metrics']['citations'])-len(r['metrics']['invalid_citations']) for r in rows)
    cited_count = sum(len(r['metrics']['citations']) for r in rows)
    return {'completed':len(completed), 'attempted':len(rows), 'errors':len(rows)-len(completed),
            'expected_attempts':run['expected_attempts'],
            'mean_evidence_recall':statistics.mean(r['metrics']['evidence_recall'] for r in rows) if rows else None,
            'all_evidence_cases':sum(r['metrics']['all_evidence_found'] for r in rows),
            'answers_with_citations':sum(bool(r['metrics']['citations']) for r in completed),
            'citation_id_precision':valid_count/cited_count if cited_count else None,
            'median_seconds':statistics.median(times) if times else None,
            'p95_seconds':percentile(times,.95),
            'median_first_visible_token_seconds':statistics.median(first) if first else None,
            'reviewed':len(reviewed), 'fully_correct':sum(r['review']['fully_correct'] for r in reviewed),
            'reviewed_accuracy':sum(r['review']['fully_correct'] for r in reviewed)/len(reviewed) if reviewed else None,
            'mean_rubric_score':statistics.mean(r['review']['rubric_score'] for r in reviewed) if reviewed else None}


def fmt(value, percent=False):
    if value is None:
        return 'pending / n/a'
    return f'{value:.1%}' if percent else f'{value:.2f}' if isinstance(value,float) else str(value)


def report(run, path):
    s = run['summary']
    lines = [f"# {run['label']}", '',f"Status: **{run['status']}** · implementation commit `{run['git']['commit']}`",'',
             f"Suite `{run['suite_id']}` · model `{run['model']}` · {run['repeats']} repetition(s) · seed(s) {run['seeds']}", '',
             '| Metric | Result |','| --- | --- |',
             f"| Completed requests | {s['completed']}/{s['expected_attempts']} |",
             f"| Request errors | {s['errors']} |",
             f"| Mean expected-evidence recall | {fmt(s['mean_evidence_recall'],True)} |",
             f"| Cases retrieving every expected evidence group | {s['all_evidence_cases']}/{s['attempted']} |",
             f"| Answers with citations | {s['answers_with_citations']}/{s['completed']} |",
             f"| Citation ID validity (not semantic support) | {fmt(s['citation_id_precision'],True)} |",
             f"| Reviewed fully correct | {s['fully_correct']}/{s['reviewed']} reviewed |",
             f"| Reviewed accuracy | {fmt(s['reviewed_accuracy'],True)} |",
             f"| Mean reviewed rubric score | {fmt(s['mean_rubric_score'],True)} |",
             f"| Median successful response | {fmt(s['median_seconds'])} s |",
             f"| p95 successful response | {fmt(s['p95_seconds'])} s |",
             f"| Median first visible answer token | {fmt(s['median_first_visible_token_seconds'])} s |",'',
             'These are development scenarios, not a held-out accuracy claim. Citation validity only checks source IDs. '
             'Evidence recall measures the authored reference groups, not all potentially relevant rules. '
             'Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.', '',
             '| Scenario | Evidence recall | Reviewed result | Total s |','| --- | --- | --- | --- |']
    for r in run['results']:
        grade = ('correct' if r['review']['fully_correct'] else r['review']['outcome']) if r.get('review') else 'pending'
        if r.get('error'):
            grade = 'request error'
        lines.append(f"| {r['case_id']} (r{r['repeat']}) | {fmt(r['metrics']['evidence_recall'],True)} | {grade} | {fmt(r['timing']['total_seconds'])} |")
    lines += ['', '## Answers and review notes','']
    for r in run['results']:
        lines += [f"### {r['case_id']} / repetition {r['repeat']}", '',r['messages'][-1]['content'],'',r['answer'] or '(No answer.)','']
        if r.get('error'):
            lines += ['Request error: '+r['error'],'']
        if r.get('review'):
            v=r['review'];lines += [f"Review: **{v['outcome']}**. {v['notes']}",f"Reviewer: {v['reviewer']}",'']
        lines += ['Missing reference groups: '+(', '.join(r['metrics']['missing_evidence']) or 'none'), '']
    Path(path).write_text('\n'.join(lines)+'\n')


def prepare_review(run):
    suite = read(SUITE)
    cases = {c['id']:c for c in suite['cases']}
    return {'schema_version':1,'run_id':run['run_id'],'suite_sha256':run['suite_sha256'],
            'reviewer':'', 'review_method':'',
            'results':[{'case_id':r['case_id'],'repeat':r['repeat'],
                        'answer_sha256':hashlib.sha256(r['answer'].encode()).hexdigest(),
                        'criteria':{x['id']:None for x in cases[r['case_id']]['criteria']},
                        'unsupported_or_contradictory_claims':None,'abstained':None,'notes':''} for r in run['results']]}


def apply_review(run, review, suite):
    if review['run_id'] != run['run_id'] or review['suite_sha256'] != run['suite_sha256']:
        raise ValueError('Review belongs to a different run or suite')
    if not review.get('reviewer') or not review.get('review_method'):
        raise ValueError('Name the reviewer and disclose whether review is human or AI-assisted')
    indexed = {(r['case_id'],r['repeat']):r for r in review['results']}
    if len(indexed) != len(review['results']) or len(indexed)!=len(run['results']):
        raise ValueError('Review must cover every result exactly once')
    cases={c['id']:c for c in suite['cases']}
    for row in run['results']:
        r=indexed[(row['case_id'],row['repeat'])]
        if r['answer_sha256'] != hashlib.sha256(row['answer'].encode()).hexdigest():
            raise ValueError('Answer changed after review')
        expected={c['id'] for c in cases[row['case_id']]['criteria']}
        if set(r['criteria']) != expected or not all(type(v) is bool for v in r['criteria'].values()):
            raise ValueError('Every rubric criterion must have an explicit boolean grade')
        if type(r['unsupported_or_contradictory_claims']) is not bool or type(r['abstained']) is not bool or not r['notes']:
            raise ValueError('Review needs explicit support/abstention flags and evidence notes')
        score=sum(r['criteria'].values())/len(expected)
        correct=all(r['criteria'].values()) and not r['unsupported_or_contradictory_claims'] and not r['abstained'] and not row.get('error')
        outcome='correct' if correct else 'error' if row.get('error') else 'abstained' if r['abstained'] else 'partial' if score else 'incorrect'
        row['review']={**r,'fully_correct':correct,'rubric_score':score,'outcome':outcome,
                       'reviewer':review['reviewer'],'review_method':review['review_method']}
    return run


def write_history():
    lines=['# Benchmark history','','Each report identifies the implementation commit tested. Results are committed afterward so the tested commit never has to refer to itself.','',
           '| Run | Tested commit | Reviewed correct | Evidence recall | Median s |','| --- | --- | --- | --- | --- |']
    for path in sorted((BENCH/'results').glob('*/run.json')):
        r=read(path)
        if r['status']!='complete':continue
        s=r['summary'];link=path.parent.relative_to(BENCH).as_posix()+'/report.md'
        lines.append(f"| [{r['label']}]({link}) | `{r['git']['commit'][:10]}` | {s['fully_correct']}/{s['reviewed']} reviewed | {fmt(s['mean_evidence_recall'],True)} | {fmt(s['median_seconds'])} |")
    (BENCH/'HISTORY.md').write_text('\n'.join(lines)+'\n')


EXPERIMENT_FIELDS = {'sampling.reasoning_effort', 'sampling.max_tokens'}


def validate_comparison(old, new, allow_changes=()):
    issues=[]
    for key in ['suite_sha256','references_sha256','corpus_sha256','model','model_runtime','seeds','repeats','mode','case_order','warmup']:
        if old.get(key)!=new.get(key):issues.append(key)
    unknown = set(allow_changes) - EXPERIMENT_FIELDS
    if unknown:
        raise ValueError('Unsupported experimental variables: '+', '.join(sorted(unknown)))
    def sampling(run):
        result = set()
        for row in run['results']:
            values = dict(row.get('sampling') or {})
            values.pop('stream_options',None)  # telemetry, not a sampling parameter
            for field in allow_changes:
                values.pop(field.removeprefix('sampling.'),None)
            result.add(json.dumps(values,sort_keys=True))
        return result
    if sampling(old)!=sampling(new):issues.append('sampling')
    if old['status']!='complete' or new['status']!='complete':issues.append('incomplete run')
    if len(old['results'])!=old['expected_attempts'] or len(new['results'])!=new['expected_attempts']:issues.append('missing results')
    return issues


def compare(old, new, allow_changes=()):
    issues=validate_comparison(old,new,allow_changes)
    if issues:
        raise ValueError('Runs are not directly comparable: '+', '.join(issues))
    a,b=old['summary'],new['summary']
    lines=[f"# {old['label']} → {new['label']}",'',
           f"Implementation `{old['git']['commit']}` → `{new['git']['commit']}`",'',
           '| Metric | Before | After | Change |','| --- | --- | --- | --- |']
    if allow_changes:
        lines[4:4] = ['Declared experimental variables: '+', '.join(sorted(allow_changes))+'. All other checked settings remain matched.','']
        for field in sorted(allow_changes):
            key=field.removeprefix('sampling.')
            values=lambda run: sorted({json.dumps((r.get('sampling') or {}).get(key,'server default')) for r in run['results']})
            lines[4:4] = [f"- `{field}`: {values(old)} → {values(new)}"]
    for key,title,pct,lower in [('reviewed_accuracy','Reviewed accuracy',True,False),('mean_evidence_recall','Expected-evidence recall',True,False),('citation_id_precision','Citation ID validity',True,False),('median_seconds','Median latency (s)',False,True),('p95_seconds','p95 latency (s)',False,True),('errors','Request errors',False,True)]:
        av,bv=a[key],b[key]
        if key=='reviewed_accuracy' and (a['reviewed']!=a['expected_attempts'] or b['reviewed']!=b['expected_attempts']):
            av=bv=None
        delta='pending / n/a'
        if av is not None and bv is not None:
            d=bv-av;direction='unchanged' if abs(d)<1e-10 else 'improved' if (d<0)==lower else 'regressed'
            delta=(f'{d*100:+.1f} percentage points' if pct else f'{d:+.2f}')+' · '+direction
        lines.append(f'| {title} | {fmt(av,pct)} | {fmt(bv,pct)} | {delta} |')
    lines += ['', '| Scenario | Before | After | Change |','| --- | --- | --- | --- |']
    older={(r['case_id'],r['repeat']):r for r in old['results']}
    for row in new['results']:
        prior=older[(row['case_id'],row['repeat'])]
        get=lambda r:r.get('review',{}).get('outcome','pending')
        before,after=get(prior),get(row)
        lines.append(f"| {row['case_id']} / r{row['repeat']} | {before} | {after} | {'unchanged' if before==after else before+' → '+after} |")
    lines += ['', 'A single repetition is descriptive, not statistically significant. Use repeated runs on the same machine with no competing inference. Review changed answers and source passages before attributing quality changes to retrieval.','']
    return '\n'.join(lines)


def runtime():
    result={}
    for path in ['/api/v1/models','/api/v0/models']:
        try:
            url=server.LM_URL.removesuffix('/v1')+path
            headers={'Authorization':'Bearer '+server.TOKEN} if server.TOKEN else {}
            data=json.load(urllib.request.urlopen(urllib.request.Request(url,headers=headers),timeout=10))
            models=data.get('models',data.get('data',[]))
            match=next((m for m in models if m.get('key',m.get('id'))==server.MODEL),None)
            if match:
                # Exclude time-varying TTL and instance identity; capture actual load config.
                result[path]={k:match[k] for k in ['id','key','architecture','arch','quantization','format','selected_variant','loaded_context_length','max_context_length','capabilities'] if k in match}
                result[path]['loaded_configs']=[m['config'] for m in match.get('loaded_instances',[])]
        except Exception as e:
            result[path]={'unavailable':type(e).__name__}
    return result


@contextmanager
def frozen_corpus():
    """Keep benchmark reads isolated from live knowledge updates."""
    archive=BENCH/'corpus/baseline.sqlite.gz'
    manifest=read(BENCH/'corpus/manifest.json')
    if sha(archive)!=manifest['archive_sha256']:
        raise ValueError('Frozen corpus archive checksum mismatch')
    old_db,old_connect=knowledge.DB,knowledge.connect
    with tempfile.TemporaryDirectory(prefix='mtg-benchmark-') as directory:
        database=Path(directory)/'knowledge.sqlite'
        with gzip.open(archive,'rb') as src,database.open('wb') as dst:
            shutil.copyfileobj(src,dst)
        if sha(database)!=manifest['database_sha256']:
            raise ValueError('Frozen corpus database checksum mismatch')
        knowledge.DB=database
        knowledge.connect=lambda path=database:old_connect(path)
        try:
            yield database
        finally:
            knowledge.DB,knowledge.connect=old_db,old_connect


def run_benchmark(args):
    suite=read(SUITE)
    validate_suite(suite)
    manifest=read(BENCH/'corpus/manifest.json')
    digest=sha(knowledge.DB)
    if digest!=manifest['database_sha256']:
        raise ValueError('Knowledge differs from the frozen corpus. Restore it before running this suite.')
    changed=[l for l in git('status','--porcelain').splitlines() if 'benchmarks/results/' not in l and 'benchmarks/HISTORY.md' not in l]
    if changed:
        raise ValueError('Commit source/harness changes before benchmarking: '+repr(changed))
    if args.repeats<1 or args.repeats>10:
        raise ValueError('Use 1–10 repetitions')
    out=Path(args.output).resolve()
    if out.exists():
        raise ValueError('Output already exists. Historical runs are immutable; choose a new directory.')
    out.mkdir(parents=True)
    stamp=datetime.now(timezone.utc).isoformat()
    seeds=[args.seed+i for i in range(args.repeats)]
    run={'schema_version':1,'run_id':out.name,'label':args.label,'created_at':stamp,'status':'running',
         'git':{'commit':git('rev-parse','HEAD'),'tree':git('rev-parse','HEAD^{tree}'),'dirty':False},
         'suite_id':suite['id'],'suite_sha256':sha(SUITE),'references_sha256':sha(BENCH/'references.json'),
         'corpus_sha256':digest,'corpus_metadata':knowledge.metadata(),'model':server.MODEL,
         'model_runtime':runtime() if args.mode=='full' else {},
         'environment':{'python':platform.python_version(),'sqlite':sqlite3.sqlite_version,'os':platform.system(),'machine':platform.machine()},
         'implementation_sha256':{p:sha(ROOT/p) for p in ['knowledge.py','server.py','generation.py','benchmark.py']},
         'mode':args.mode,'repeats':args.repeats,'seeds':seeds,'case_order':[c['id'] for c in suite['cases']],
         'expected_attempts':len(suite['cases'])*args.repeats,'warmup':args.mode=='full','results':[]}
    current={}
    real_retrieve=knowledge.retrieve
    real_lm=server.lm_request
    def measured_retrieve(messages,ids):
        start=time.perf_counter()
        try:
            sources=real_retrieve(messages,ids)
            current['sources']=sources
            return sources
        finally:
            current['retrieval_seconds']=time.perf_counter()-start
    def measured_lm(path,payload=None,timeout=10):
        if payload is not None:
            payload={**payload,'seed':current['seed']}
            current['sampling']={k:v for k,v in payload.items() if k not in ('messages','stream_options')}
            current['prompt_sha256']=hashlib.sha256(json.dumps(payload['messages'],sort_keys=True).encode()).hexdigest()
        return real_lm(path,payload,timeout)
    knowledge.retrieve=measured_retrieve
    server.lm_request=measured_lm
    http=None
    try:
        if args.mode=='full':
            if urllib.parse.urlparse(server.LM_URL).hostname not in ('localhost','127.0.0.1','::1'):
                raise ValueError('Benchmark inference must stay local')
            print('Warming up the configured model (excluded from timings)…',flush=True)
            warm={'model':server.MODEL,'messages':[{'role':'user','content':'Reply with only the word Ready.'}], 'temperature':.1,'max_tokens':3500,'stream':False,'seed':args.seed}
            with real_lm('/chat/completions',warm,timeout=300) as response:
                response.read()
            http=server.ThreadingHTTPServer(('127.0.0.1',0),server.Handler)
            threading.Thread(target=http.serve_forever,daemon=True).start()
        for repeat,seed in enumerate(seeds,1):
            for case in suite['cases']:
                current.clear();current['seed']=seed
                row={'case_id':case['id'],'repeat':repeat,'seed':seed,'messages':case['messages'],'card_ids':case['card_ids'],'answer':'','sources':[],'warnings':[],'error':None,'timing':{}}
                start=time.perf_counter();first=None
                try:
                    if args.mode=='retrieval':
                        measured_retrieve(case['messages'],case['card_ids'])
                    else:
                        # Only real user messages and selected cards; never expected_answer, criteria, or reference labels.
                        body=json.dumps({'messages':case['messages'],'card_ids':case['card_ids']}).encode()
                        req=urllib.request.Request(f'http://127.0.0.1:{http.server_port}/api/chat',data=body,headers={'Content-Type':'application/json'})
                        done=False
                        with urllib.request.urlopen(req,timeout=360) as response:
                            for line in response:
                                event=json.loads(line)
                                if event['type']=='token':
                                    if first is None and event['text'].strip():first=time.perf_counter()-start
                                    row['answer']+=event['text']
                                elif event['type']=='error':raise RuntimeError(event['error'])
                                elif event['type']=='done':row['warnings']=event['warnings'];row['diagnostics']=event.get('diagnostics',{});done=True
                        if not done:raise RuntimeError('Stream ended without a done event')
                        if not row['answer'].strip():raise RuntimeError('No final answer returned')
                except Exception as e:
                    row['error']=str(e)
                    if isinstance(e,urllib.error.HTTPError):row['error']+=' '+e.read().decode()[:1000]
                row['timing']={'total_seconds':round(time.perf_counter()-start,4),'retrieval_seconds':round(current.get('retrieval_seconds',0),4),'first_visible_token_seconds':round(first,4) if first is not None else None}
                row['sources']=current.get('sources',[])
                row['sampling']=current.get('sampling')
                row['prompt_sha256']=current.get('prompt_sha256')
                row['metrics']=measure_evidence(case,row['sources'],row['answer'])
                run['results'].append(row);run['summary']=summary(run)
                write(out/'run.json',run)
                print(f"{len(run['results']):02}/{run['expected_attempts']} {case['id']}: {row['timing']['total_seconds']:.1f}s; evidence {row['metrics']['evidence_recall']:.0%}; {'ERROR '+row['error'] if row['error'] else 'ok'}",flush=True)
        run['status']='complete'
    finally:
        knowledge.retrieve=real_retrieve;server.lm_request=real_lm
        if http:http.shutdown();http.server_close()
        run['finished_at']=datetime.now(timezone.utc).isoformat()
        if run['status']!='complete':run['status']='interrupted'
        run['summary']=summary(run)
        write(out/'run.json',run);write(out/'review.json',prepare_review(run));report(run,out/'report.md');write_history()
    print(json.dumps(run['summary'],indent=2),flush=True)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    sub=parser.add_subparsers(dest='command',required=True)
    p=sub.add_parser('run');p.add_argument('--label',required=True);p.add_argument('--output',required=True);p.add_argument('--mode',choices=['full','retrieval'],default='full');p.add_argument('--repeats',type=int,default=1);p.add_argument('--seed',type=int,default=42)
    p=sub.add_parser('review');p.add_argument('directory')
    p=sub.add_parser('compare');p.add_argument('before');p.add_argument('after');p.add_argument('--output',required=True);p.add_argument('--allow-change',action='append',choices=sorted(EXPERIMENT_FIELDS),default=[])
    sub.add_parser('validate')
    p=sub.add_parser('restore-corpus');p.add_argument('--output',required=True)
    args=parser.parse_args()
    if args.command=='run':
        with frozen_corpus():run_benchmark(args)
    elif args.command=='validate':
        validate_suite(read(SUITE));print('Validated 20 scenarios, frozen reference passages, and card IDs.')
    elif args.command=='review':
        path=Path(args.directory);r=read(path/'run.json')
        if sha(SUITE)!=r['suite_sha256']:raise ValueError('Suite changed since this run')
        apply_review(r,read(path/'review.json'),read(SUITE));r['summary']=summary(r);write(path/'run.json',r);report(r,path/'report.md');write_history();print(json.dumps(r['summary'],indent=2))
    elif args.command=='compare':
        result=compare(read(Path(args.before)/'run.json'),read(Path(args.after)/'run.json'),args.allow_change);Path(args.output).write_text(result);print(result)
    elif args.command=='restore-corpus':
        target=Path(args.output)
        if target.exists():raise ValueError('Refusing to overwrite an existing database; choose another path or move the old one aside first.')
        archive=BENCH/'corpus/baseline.sqlite.gz';manifest=read(BENCH/'corpus/manifest.json')
        if sha(archive)!=manifest['archive_sha256']:raise ValueError('Corpus archive checksum mismatch')
        target.parent.mkdir(parents=True,exist_ok=True)
        with gzip.open(archive,'rb') as src,target.open('wb') as dst:shutil.copyfileobj(src,dst)
        if sha(target)!=manifest['database_sha256']:
            target.unlink();raise ValueError('Restored database checksum mismatch')
        print('Restored frozen corpus to',target)

if __name__=='__main__':
    main()
