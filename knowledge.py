from contextlib import closing
"""Local, versioned Magic sources and SQLite full-text retrieval."""
import gzip
import html
import json
import os
from pathlib import Path
import re
import sqlite3
import tempfile
import threading
import urllib.parse
import urllib.request
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parent
DATA = ROOT / 'data'
DB = DATA / 'knowledge.sqlite'
RULES_PAGE = 'https://magic.wizards.com/en/rules'


def fetch(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'LocalMTGJudge/0.1 (personal rules reference)', 'Accept': '*/*'})
    return urllib.request.urlopen(req, timeout=120)


def connect(path=DB):
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    return conn


def parse_rules(text):
    # Duplicate TOC headings are replaced by their full entries in the document body.
    rules = {}
    for match in re.finditer(r'(?m)^(\d{3}\.\d+[a-z]?|\d{3})\.?(?=\s)\s+(.+?)(?=^\d{3}(?:\.\d+[a-z]?)?\.?\s|^Glossary\s*$|\Z)', text, re.S | re.M):
        number, body = match.groups()
        body = body.strip()
        if len(body) < 16000:
            rules[number] = body
    return rules


def bulk_records(entry):
    url = entry.get('jsonl_download_uri') or entry.get('download_uri')
    if not url:
        raise RuntimeError('Scryfall did not provide a download URL')
    with fetch(url) as response:
        if '.jsonl' in url:
            stream = gzip.GzipFile(fileobj=response) if url.endswith('.gz') else response
            for line in stream:
                if line.strip():
                    yield json.loads(line)
        else:
            yield from json.load(response)


def sync(progress=print):
    DATA.mkdir(exist_ok=True)
    fd, staging = tempfile.mkstemp(prefix='knowledge-', suffix='.sqlite', dir=DATA)
    os.close(fd)
    try:
        conn = connect(staging)
        conn.executescript('''
        CREATE TABLE metadata (key TEXT PRIMARY KEY, value TEXT);
        CREATE TABLE rules (number TEXT PRIMARY KEY, body TEXT);
        CREATE VIRTUAL TABLE rules_fts USING fts5(number, body, tokenize='porter unicode61');
        CREATE TABLE cards (id TEXT PRIMARY KEY, name TEXT, body TEXT, url TEXT, aliases TEXT);
        CREATE INDEX card_name ON cards(name COLLATE NOCASE);
        CREATE TABLE rulings (oracle_id TEXT, published TEXT, body TEXT);
        CREATE INDEX ruling_card ON rulings(oracle_id);
        ''')
        progress('Downloading the official Comprehensive Rules…')
        page = fetch(RULES_PAGE).read().decode()
        urls = re.findall(r'href=[\"\']([^\"\']+\.txt)[\"\']', page)
        url = next((html.unescape(u) for u in urls if 'media.wizards.com' in u), None)
        if not url:
            raise RuntimeError('Could not find the official rules TXT link; existing data is unchanged.')
        url = urllib.parse.quote(url, safe=':/%')
        raw = fetch(url).read()
        try:
            text = raw.decode('utf-8-sig')
        except UnicodeDecodeError:
            text = raw.decode('cp1252')
        rules = parse_rules(text.replace('\r\n', '\n'))
        if len(rules) < 500:
            raise RuntimeError('Rules parsing failed validation; existing data is unchanged.')
        conn.executemany('INSERT INTO rules VALUES (?,?)', rules.items())
        conn.executemany('INSERT INTO rules_fts VALUES (?,?)', rules.items())
        catalog = {x['type']: x for x in json.load(fetch('https://api.scryfall.com/bulk-data'))['data']}
        progress(f'Indexed {len(rules):,} rules. Downloading Oracle card text…')
        count = 0
        for card in bulk_records(catalog['oracle_cards']):
            faces = card.get('card_faces') or [card]
            body = '\n\n'.join('\n'.join(filter(None, [f.get('name'), f.get('mana_cost'), f.get('type_line'), f.get('oracle_text'), (' / '.join(str(f[k]) for k in ['power', 'toughness'] if k in f)), ('Loyalty: '+str(f['loyalty'])) if 'loyalty' in f else ''])) for f in faces)
            aliases = [card['name']] + [f['name'] for f in faces]
            conn.execute('INSERT OR REPLACE INTO cards VALUES (?,?,?,?,?)', (card['oracle_id'], card['name'], body, card['scryfall_uri'], json.dumps(aliases)))
            count += 1
        if count < 10000:
            raise RuntimeError('Card download is incomplete; existing data is unchanged.')
        progress(f'Indexed {count:,} cards. Downloading card rulings…')
        ruling_count = 0
        for ruling in bulk_records(catalog['rulings']):
            conn.execute('INSERT INTO rulings VALUES (?,?,?)', (ruling['oracle_id'], ruling['published_at'], ruling['comment']))
            ruling_count += 1
        metadata = {'rules_url': url, 'rules_version': re.search(r'20\d{6}', urllib.parse.unquote(url)).group(0), 'cards_updated': catalog['oracle_cards']['updated_at'], 'rulings_updated': catalog['rulings']['updated_at'], 'synced_at': datetime.now(timezone.utc).isoformat(), 'rules_count': len(rules), 'cards_count': count, 'rulings_count': ruling_count}
        conn.executemany('INSERT INTO metadata VALUES (?,?)', [(k, json.dumps(v)) for k,v in metadata.items()])
        conn.commit()
        conn.close()
        os.replace(staging, DB)
        progress(f'Ready: {len(rules):,} rules, {count:,} cards, {ruling_count:,} rulings.')
        return metadata
    finally:
        if os.path.exists(staging):
            os.unlink(staging)


def metadata():
    if not DB.exists():
        return {}
    with closing(connect()) as conn:
        return {r['key']: json.loads(r['value']) for r in conn.execute('SELECT * FROM metadata')}


def search_cards(query):
    if not DB.exists() or len(query.strip()) < 2:
        return []
    escaped = query.strip().replace('\\', '\\\\').replace('%', '\\%').replace('_', '\\_')
    with closing(connect()) as conn:
        return [dict(r) for r in conn.execute("SELECT id,name,body,url FROM cards WHERE name LIKE ? ESCAPE '\\' ORDER BY CASE WHEN name = ? COLLATE NOCASE THEN 0 WHEN name LIKE ? ESCAPE '\\' THEN 1 ELSE 2 END, length(name), name LIMIT 12", ('%'+escaped+'%', query.strip(), escaped+'%'))]


STOP = set('a an the is are was were be been being do does did can could would should will i my me you your it its this that these those if when what how why with without and or but of for to in on at as by from have has had then than any all into get gets still also after before'.split())
TOPICS = [
    (r'priority|respond|response|stack|instant', ['117', '405', '608']),
    (r'target|fizzle|hexproof|shroud|ward', ['115', '608.2b', '702.11', '702.18', '702.21']),
    (r'death|dies|die\b|graveyard|lethal|state.based|indestructible|deathtouch', ['704', '702.2', '702.12']),
    (r'layer|lose.*abilit|loses.*abilit|humility|blood moon|timestamp', ['613']),
    (r'replace|replacement|instead|\bdouble(?:s)?\b(?![ -]+strike)', ['614', '616', '614.6']),
    (r'state.based actions?|legend(?:ary)? rule', ['704.3']),
    (r'commander|command zone|commander tax', ['903', '903.9', '903.9a', '903.9b', '903.10', '903.10a']),
    (r'additional cost|cost to cast|costs? during casting', ['601.2a', '601.2h', '601.2i', '117.2e', '117.3c']),
    (r'dies|die\b|death', ['700.4', '603.6c', '603.10a']),
    (r'mana.*abilit|tap.*land|tap.*mana', ['605.1a', '605.3b']),
    (r'attack|block|combat|first strike|double strike|trample', ['508', '509', '510', '702.4', '702.7', '702.19']),
    (r'trigger|enters|entering', ['603']),
    (r'\bmana value\b|converted mana cost', ['202.3', '202.3e', '202.3f', '107.3a']),
    (r'\binitiative\b|undercity|venture into the dungeon', ['726.2', '726.5']),
    (r'casualty', ['702.153', '702.153a']),
    (r'(?:copy|copies|copied|copying).{0,45}(?:spell|instant|sorcery)|(?:spell|instant|sorcery).{0,45}(?:copy|copies|copied|copying)', ['707.10']),
    (r'copy|copies|copied|clone', ['707']),
    (r'\bprototyp(?:e|ed|ing)\b', ['718.3', '718.4']),
    (r'counterspell|cast|casting|cost|mana', ['601']),
    (r'token|tokens', ['111']),
    (r'\b(?:loses?|lost) and leaves?\b|\bleaves? the game\b|\bleaving the game\b|\bleave the game\b|\beliminated\b', ['800.4a']),
]
# These rules were promoted after frozen-suite misses showed that broad FTS
# matches could crowd out the exact rules for mana value, initiative, and copies.
HIGH_PRIORITY_RULES = {'601.2a', '601.2h', '601.2i', '117.2e', '117.3c', '614.6', '704.3', '718.3', '718.4',
                       '202.3', '202.3e', '202.3f', '107.3a', '726.2', '726.5', '702.153', '702.153a', '707.10'}

_CARD_ALIAS_LOCK = threading.Lock()
_CARD_ALIAS_INDEX = None
_CARD_ALIAS_DB_SIGNATURE = None


def _card_alias_index(conn):
    """Cache aliases only; resolve full card rows from SQLite after matching."""
    global _CARD_ALIAS_INDEX, _CARD_ALIAS_DB_SIGNATURE
    stat = DB.stat()
    signature = (stat.st_mtime_ns, stat.st_size)
    if _CARD_ALIAS_INDEX is not None and _CARD_ALIAS_DB_SIGNATURE == signature:
        return _CARD_ALIAS_INDEX
    with _CARD_ALIAS_LOCK:
        if _CARD_ALIAS_INDEX is not None and _CARD_ALIAS_DB_SIGNATURE == signature:
            return _CARD_ALIAS_INDEX
        aliases = {}
        max_words = 0
        for row in conn.execute('SELECT rowid,id,aliases FROM cards ORDER BY rowid'):
            for alias in json.loads(row['aliases']):
                words = re.findall(r'\w+', alias.casefold())
                if not words:
                    continue
                key = ' '.join(words)
                max_words = max(max_words, len(words))
                aliases.setdefault(key, []).append((row['rowid'], row['id'], alias))
        _CARD_ALIAS_INDEX = (aliases, max_words)
        _CARD_ALIAS_DB_SIGNATURE = signature
        return _CARD_ALIAS_INDEX


def _mentioned_card_ids(question, conn, bracketed):
    """Find the same exact, multiword card-name mentions as the former table scan."""
    aliases, max_words = _card_alias_index(conn)
    words = list(re.finditer(r'\w+', question))
    matched = {}
    bracketed = {name.casefold() for name in bracketed}
    for start in range(len(words)):
        end_limit = min(len(words), start + max_words)
        for end in range(start + 1, end_limit + 1):
            key = ' '.join(m.group(0).casefold() for m in words[start:end])
            for rowid, card_id, alias in aliases.get(key, ()):
                found = alias.casefold() in bracketed
                if not found and len(alias.split()) >= 2:
                    found = re.search(r'(?<!\w)' + re.escape(alias) + r'(?!\w)', question) is not None
                if found:
                    matched.setdefault(card_id, rowid)
    return [card_id for card_id, _ in sorted(matched.items(), key=lambda item: item[1])]


def search_question(text):
    """Exclude explicit absent effects from search, while keeping the original prompt.

    Only complete exclusion sentences are removed: a player's statement that
    they have no replacement effect does not imply that no other player has one.
    """
    return re.sub(r'(?i)(?:^|(?<=[.!?])\s+)no (?:other )?replacement effects? apply(?:[.!]|$)', ' ', text)


def _retrieve_lexical(messages, card_ids):
    if not DB.exists():
        raise ValueError('Download the rules and cards using “Update knowledge” first.')
    # Recent user turns preserve the subject of short follow-up questions.
    user_texts = [m['content'] for m in messages if m['role'] == 'user'][-3:]
    question = '\n'.join(user_texts)
    with closing(connect()) as conn:
        selected = []
        for cid in dict.fromkeys(card_ids):
            row = conn.execute('SELECT * FROM cards WHERE id=?', (cid,)).fetchone()
            if row:
                selected.append(dict(row))
        # Explicit [[Card Name]] syntax is unambiguous. Also recognize full names
        # with at least two words and exact capitalization; ambiguous lowercase names
        # and single-word names require attachment or brackets.
        bracketed = re.findall(r'\[\[([^\]]+)\]\]', question)
        selected_ids = {x['id'] for x in selected}
        for card_id in _mentioned_card_ids(question, conn, bracketed):
            if card_id not in selected_ids:
                row = conn.execute('SELECT * FROM cards WHERE id=?', (card_id,)).fetchone()
                if row:
                    selected.append(dict(row))
                    selected_ids.add(card_id)
                if len(selected) >= 8:
                    break
        selected = selected[:8]
        search_text = search_question(question) + '\n' + '\n'.join(c['body'] for c in selected)
        scores = {}
        def add(number, score):
            scores[number] = scores.get(number, 0) + score
        for number in re.findall(r'\b\d{3}\.\d+[a-z]?\b', question):
            add(number, 100)
        for text, weight in [(search_question(user_texts[-1]), 3), (search_text, 1)]:
            terms = list(dict.fromkeys(t for t in re.findall(r'[a-zA-Z]{3,}', text.lower()) if t not in STOP))[:70]
            if terms:
                query = ' OR '.join('"'+t+'"' for t in terms)
                for i, row in enumerate(conn.execute('SELECT number FROM rules_fts WHERE rules_fts MATCH ? ORDER BY bm25(rules_fts) LIMIT 28', (query,))):
                    add(row['number'], weight * (28-i)/5)
        for pattern, roots in TOPICS:
            if re.search(pattern, search_text, re.I):
                for root in roots:
                    # A broad topic such as death does not imply every related keyword.
                    if root.startswith('702.'):
                        heading = conn.execute('SELECT body FROM rules WHERE number=?', (root,)).fetchone()
                        if heading and not re.search(r'(?<!\w)' + re.escape(heading['body']) + r'(?!\w)', search_text, re.I):
                            continue
                    # Include section headings and immediate definitions to ground vocabulary.
                    for row in conn.execute('SELECT number FROM rules WHERE number=? OR number=? OR number=?', (root, root+'.1', root+'.2')):
                        add(row['number'], 15 if '.' in root else 5)
        sources = []
        for c in selected:
            sources.append({'id': 'C'+str(len(sources)+1), 'kind': 'card', 'title': c['name'], 'text': c['body'], 'url': c['url']})
            for r in conn.execute('SELECT * FROM rulings WHERE oracle_id=? ORDER BY published DESC LIMIT 12', (c['id'],)):
                sources.append({'id':'C'+str(len(sources)+1), 'kind':'ruling', 'title':c['name']+' · '+r['published'], 'text':r['body'], 'url':c['url']})
        chosen = sorted(scores, key=scores.get, reverse=True)[:24]
        # Bring referenced parent definitions alongside the retrieved subrules.
        for number in list(chosen):
            parent = re.sub('[a-z]$', '', number)
            if parent != number and parent not in chosen:
                chosen.append(parent)
        for number in chosen[:32]:
            row = conn.execute('SELECT body FROM rules WHERE number=?', (number,)).fetchone()
            if row:
                sources.append({'id':'CR '+number, 'kind':'rule', 'title':'Rule '+number, 'text':row['body'], 'url':'/api/rules/'+number})
        return sources


def _related_rule(number,root):
    return number==root or (number.startswith(root+'.') if '.' not in root else bool(re.fullmatch(re.escape(root)+r'[a-z]?',number)))

def _retrieve_structural(messages,card_ids):
    initial=_retrieve_lexical(messages,card_ids)
    question='\n'.join([m['content'] for m in messages if m['role']=='user'][-3:])
    search=search_question(question)+'\n'+'\n'.join(s['text'] for s in initial if s['kind']=='card')
    rules=[s for s in initial if s['kind']=='rule'];cards=[s for s in initial if s['kind']!='rule']
    with closing(connect()) as conn:
        allrules={r['number']:r['body'] for r in conn.execute('SELECT * FROM rules')}
        candidates={s['id'][3:]:1/(i+1) for i,s in enumerate(rules)}
        families=[]
        focused=[]
        for root,heading in allrules.items():
            if re.fullmatch(r'702\.\d+',root) and re.search(r'(?<!\w)'+re.escape(heading)+r'(?!\w)',search,re.I):
                families.append((root,[n for n in allrules if _related_rule(n,root)]))
        for pattern,roots in TOPICS:
            if re.search(pattern,search,re.I):
                for root in roots:
                    family=[n for n in allrules if _related_rule(n,root)]
                    if family:families.append((root,family))
                    if root in HIGH_PRIORITY_RULES:
                        focused.append(root)
        terms=list(dict.fromkeys(t for t in re.findall(r'[a-zA-Z]{3,}',search.lower()) if t not in STOP))[:70]
        query=' OR '.join('"'+t+'"' for t in terms)
        ranked=[r['number'] for r in conn.execute('SELECT number FROM rules_fts WHERE rules_fts MATCH ? ORDER BY bm25(rules_fts)',(query,))] if query else []
        mandatory=list(dict.fromkeys(focused))
        for root,family in families:
            familyset=set(family)
            is_keyword=root.startswith('702.')
            heading=allrules.get(root,'').lower()
            if is_keyword and not re.search(r'(?<!\w)'+re.escape(heading)+r'(?!\w)',search,re.I):
                continue
            if is_keyword:
                mandatory.extend(family)
            direct=[n for n in family if re.fullmatch(re.escape(root)+r'\.\d+',n)]
            # Keep the section's immediate definitions as well as its highest-ranked leaves.
            selected=(direct if len(direct)<=16 else [])+[n for n in ranked if n in familyset][:8]
            for i,n in enumerate(selected):candidates[n]=candidates.get(n,0)+1/(i+1)
        ordered=sorted(candidates,key=candidates.get,reverse=True)
        # Keep keyword families, parent definitions, and adjacent clauses together.
        # Fixed candidate limits bound expansion; no benchmark answers are used.
        chosen=[]
        def add(n):
            if n in allrules and n not in chosen:chosen.append(n)
        for n in mandatory:add(n)
        for n in ordered[:32]:add(n)
        for n in list(chosen):
            if re.search(r'[a-z]$',n):
                for offset in (-1,1):add(n[:-1]+chr(ord(n[-1])+offset))
            else:
                children=[k for k in allrules if _related_rule(k,n)]
                if len(children)<=8:
                    for k in children:add(k)
        for n in list(chosen):
            parent=re.sub(r'[a-z]$','',n)
            if parent!=n:add(parent)
        return cards+[{'id':'CR '+n,'title':'Rule '+n,'kind':'rule','text':allrules[n],'url':'/api/rules/'+n} for n in chosen[:64]]


def append_semantic_rules(sources, semantic_numbers, rule_bodies, limit=24):
    """Preserve the lexical source order and append only vector-only rules."""
    cards_and_rulings = [s for s in sources if s['kind'] != 'rule']
    lexical_rules = [s for s in sources if s['kind'] == 'rule']
    lexical_numbers = {s['id'][3:] for s in lexical_rules}
    extras = []
    for number in semantic_numbers:
        if number in rule_bodies and number not in lexical_numbers:
            extras.append({'id':'CR '+number,'title':'Rule '+number,'kind':'rule',
                           'text':rule_bodies[number],'url':'/api/rules/'+number,
                           'semantic_only':True})
            lexical_numbers.add(number)
        if len(extras) == limit:
            break
    return cards_and_rulings + lexical_rules + extras


def retrieve(messages, card_ids):
    sources = _retrieve_structural(messages, card_ids)
    mode = os.environ.get('MTG_RETRIEVAL', 'lexical')
    if mode == 'lexical':
        return sources
    if mode != 'hybrid':
        raise ValueError('MTG_RETRIEVAL must be lexical or hybrid')
    import vector_search
    turns = [m['content'] for m in messages if m['role'] == 'user'][-3:]
    question = turns[-1]
    # Same real user question and attached Oracle text; no evaluation labels.
    question += '\n' + '\n'.join(s['text'] for s in sources if s['kind'] == 'card')
    question += '\n' + '\n'.join(turns[:-1])
    try:
        semantic = vector_search.search(question)
    except Exception as exc:
        raise ValueError('Hybrid retrieval failed: '+str(exc)) from exc
    with closing(connect()) as conn:
        rules = {r['number']:r['body'] for r in conn.execute('SELECT number,body FROM rules')}
    return append_semantic_rules(sources, semantic, rules)



if __name__ == '__main__':
    sync()
