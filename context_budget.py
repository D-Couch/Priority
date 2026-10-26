"""Pack complete source excerpts against LM Studio's actual tokenizer."""
import re
import sqlite3
from contextlib import closing
from urllib.parse import urlparse

OUTPUT_TOKENS = 3500
TEMPLATE_MARGIN = 64
MAX_PROMPT_TOKENS = 4628
ANSWER_CONTRACT = """END REFERENCE EXCERPTS.
Follow this response contract:
For a general rules or paper-play question, answer directly with the standard rule or procedure; do not ask for a card name or game state just because the question is broad. If exact card text could change the details, give the general answer first and briefly invite the user to share that card for a precise ruling. For a specific game state, give useful conditional outcomes when possible. Use "Need details:" only when a missing fact prevents a useful answer to the actual situation.
For random procedures, distinguish the Tournament Rules guidance for die-roll game actions from other random choices; do not present MTR 3.9 as governing every random effect. Only discuss MTR 3.9 for questions about die rolls or when the user asks about tournament die-roll procedure. For random-target questions, do not add unrelated die-roll or tournament guidance. Explain that the eligible choice pool comes from the card/effect. If the random choice is a target, explicitly state that only legal targets belong in the pool and cite the supplied Comprehensive Rules.
Keep simple general answers to one short paragraph. Do not invent hypothetical card text, game states, or examples unless requested. For replacement questions without exact effects, give the ordering and re-evaluation rules only; do not add hypothetical outcomes. If a result depends on an unstated ability such as trample, state the branches. For random procedures, say that a random target must be legal [CR 115.2]; give no hypothetical example. Every option must have equal chance: use shuffled identical slips for arbitrary option counts, or an evenly mapped die with unused results rerolled. Never suggest unequal sequential coin flips.
Use "Ruling:" for a direct answer, then "Why:" with at most three concise explanatory sentences and supporting source citations. Cite the specific supplied rule that establishes each central claim, using its bracketed source ID; do not substitute a merely related rule. Never mention a rule number in plain prose without its bracketed citation: write "[CR 616.1]" rather than "Rule 616.1." Address the interaction asked about. For general conceptual questions, prefer the direct rule or procedure over a hypothetical example.
Check that each cited rule's conditions match the stated game state. An exception applies only to the event it describes. Do not extend it to a different event merely because similar words appear in the rules.
Do not assume an unstated keyword or game fact. If a missing detail changes the result, state the relevant conditional outcomes instead of choosing one as fact. Avoid exhaustive claims such as "only," "always," or "never" unless the supplied rules establish them. For damage to creatures, say damage is marked; do not describe damage as reducing toughness or leaving less toughness unless an effect actually changes toughness. When another player has a rules choice, state the legal options without predicting which option they will choose. Do not say an object that leaves the game goes to a graveyard unless the rules say that it does.
For casting-order questions, distinguish the card being put onto the stack at the start of casting (601.2a), costs being paid while it is already on the stack (601.2h), and the spell becoming cast after those steps are complete (601.2i). Players receive no priority during the casting process (117.2e). Never say that paying costs happens before the spell is put onto the stack. Cite these facts only when supported by supplied excerpts.
When a question involves a triggered ability and an effect that may fail, explicitly distinguish whether the ability triggers from whether its effect succeeds. Cite the rule governing the trigger separately from the rule governing the effect when both are supplied.
"""


def make_messages(system, sources, history):
    evidence = '\n\n'.join('[' + s['id'] + '] ' + s['title'] + '\n' + s['text'] for s in sources)
    return [{'role': 'system', 'content': system + '\n\nREFERENCE EXCERPTS:\n' + evidence + '\n\n' + ANSWER_CONTRACT}] + history


def relevant_rulings(sources, question):
    """Reserve room for two query-relevant card rulings, not every dated ruling."""
    from knowledge import STOP
    rulings = [s for s in sources if s['kind'] == 'ruling']
    terms = list(dict.fromkeys(t for t in re.findall(r'[a-zA-Z]{3,}', question.lower()) if t not in STOP))[:70]
    if not rulings or not terms:
        return []
    with closing(sqlite3.connect(':memory:')) as conn:
        conn.execute("CREATE VIRTUAL TABLE excerpts USING fts5(body, tokenize='porter unicode61')")
        conn.executemany('INSERT INTO excerpts(body) VALUES (?)', [(s['text'],) for s in rulings])
        query = ' OR '.join('"'+t+'"' for t in terms)
        ranked = conn.execute('SELECT rowid FROM excerpts WHERE excerpts MATCH ? ORDER BY bm25(excerpts), rowid', (query,))
        chosen = []
        for (rowid,) in ranked:
            source = rulings[rowid-1]
            if sum(len(s['text']) for s in chosen) + len(source['text']) <= 1600:
                chosen.append(source)
            if len(chosen) == 2:
                break
        return chosen


def source_groups(sources, question=''):
    """Keep compact sections intact so definitions travel with their exceptions."""
    result = [[s] for s in sources if s['kind'] == 'card']
    result.extend([[s] for s in sources if s['kind'] == 'tournament_rule'])
    priority = relevant_rulings(sources, question)
    result.extend([s] for s in priority)
    priority_ids = {s['id'] for s in priority}
    for semantic_only in (False, True):
        sections = {}
        for source in sources:
            if source['kind'] != 'rule' or bool(source.get('semantic_only')) != semantic_only:
                continue
            number = source['id'].removeprefix('CR ')
            # Each keyword is its own section; the entire keyword chapter is too large.
            section = re.sub(r'[a-z]$', '', number) if number.startswith('702.') else number.split('.')[0]
            sections.setdefault(section, []).append(source)
        for section in sections.values():
            if sum(len(s['text']) for s in section) <= 6000:
                result.append(section)
                continue
            # Large chapters fall back to short subrule families, then individual rules.
            families = {}
            for source in section:
                families.setdefault(re.sub(r'[a-z]$', '', source['id']), []).append(source)
            for group in families.values():
                if len(group) <= 8 and sum(len(s['text']) for s in group) <= 3500:
                    result.append(group)
                else:
                    result.extend([s] for s in group)
    result.extend([s] for s in sources if s['kind'] == 'ruling' and s['id'] not in priority_ids)
    return result


def pack_context(system, sources, history, count_tokens, context_length):
    limit = min(context_length - OUTPUT_TOKENS - TEMPLATE_MARGIN, MAX_PROMPT_TOKENS)
    history = list(history)
    dropped_turns = 0
    while count_tokens(make_messages(system, [], history)) > limit and len(history) > 1:
        # Discard oldest turns, never the current question.
        history.pop(0)
        dropped_turns += 1
    while len(history) > 1 and history[0]['role'] != 'user':
        history.pop(0)
        dropped_turns += 1
    if count_tokens(make_messages(system, [], history)) > limit:
        raise ValueError('Your latest question is too long for the loaded model context. Shorten it or load a larger context in LM Studio.')
    selected = []
    question = next((m['content'] for m in reversed(history) if m['role'] == 'user'), '')
    for group in source_groups(sources, question):
        candidate = selected + group
        if count_tokens(make_messages(system, candidate, history)) <= limit:
            selected = candidate
    if sources and not selected:
        raise ValueError('No complete reference excerpt fits alongside this conversation. Start a new conversation or load a larger context in LM Studio.')
    messages = make_messages(system, selected, history)
    prompt_tokens = count_tokens(messages)
    return messages, selected, {'context_length': context_length, 'max_prompt_tokens': limit, 'prompt_tokens': prompt_tokens,
                               'reserved_output_tokens': OUTPUT_TOKENS, 'template_margin': TEMPLATE_MARGIN,
                               'omitted_sources': len(sources) - len(selected), 'omitted_turns': dropped_turns}


def prepare_context(system, sources, history, lm_url, model_id):
    try:
        import lmstudio as lms
    except ImportError as exc:
        raise ValueError('Install the local tokenizer client with .venv/bin/python -m pip install -r requirements.txt, then launch with ./start.sh.') from exc
    host = urlparse(lm_url).netloc
    with lms.Client(host) as client:
        model = client.llm.model(model_id)
        def count(messages):
            chat = lms.Chat.from_history({'messages': messages})
            return len(model.tokenize(model.apply_prompt_template(chat)))
        messages, selected, budget = pack_context(system, sources, history, count, model.get_context_length())
        budget['tokenizer_client_version'] = lms.__version__
        return messages, selected, budget
