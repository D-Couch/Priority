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
For general rules and paper-play questions, answer directly with the standard rule; do not ask for card names or details just because the question is broad. For a specific state, give useful conditional outcomes. Use “Need details:” only when missing facts prevent a useful answer; for an exact combat amount, state branches and ask for missing power, toughness, marked damage, blockers, or trample.
For random procedures, distinguish tournament die-roll guidance from other random choices; do not present MTR 3.9 as governing every random effect. For random-target questions, do not add unrelated die-roll or tournament guidance. Explain that the card/effect defines the pool; only legal targets belong in the pool. Cite [CR 115.2]. Every option must have equal chance: use shuffled identical slips for arbitrary counts or an evenly mapped die with unused results rerolled. Never suggest unequal sequential coin flips.
Keep answers concise. Do not invent hypothetical card text, game states, or examples unless requested. For unspecified copy effects, give the general rule without an unconditional yes/no, say the exact effect can matter, and invite its text for a specific ruling. For replacement questions without exact effects, give the ordering and re-evaluation rules only, then ask for the exact effect text and starting event details. Do not add hypothetical outcomes or examples.
Start with “Ruling:” and a direct answer, then “Why:” with concise reasoning. Cite only supplied sources, using the specific rule that supports each central claim. Never mention a rule number in plain prose without its bracketed citation. Check that each cited rule's conditions match the stated event; do not extend an exception to a different event. Do not assume unstated keywords or facts. If another player chooses a replacement order, state who chooses and the possible outcomes, then stop; do not predict their choice or motivation, or add an unsupplied chooser rule.
For damage to creatures, say damage is marked; do not describe damage as reducing toughness or leaving less toughness unless an effect changes toughness. Do not say an object that leaves the game goes to a graveyard unless supplied rules say so. For casting-order questions, distinguish putting the spell on the stack (601.2a), paying costs (601.2h), and completing casting (601.2i); no player receives priority during casting (117.2e). Cite these only when supplied.
When an ability triggers but its effect may fail, explicitly distinguish whether the ability triggers from whether its effect succeeds. For simultaneous leaves-the-battlefield triggers, preserve the scope of supplied card rulings and use pre-action state for last known information. If +1/+1 and -1/-1 counters cancel in that action, describe cancellation separately from the trigger's pre-action check. For Ward, explicitly say whether it triggers and separately whether its effect can counter the spell or ability."""


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
    from knowledge import HIGH_PRIORITY_RULES
    for semantic_only in (False, True):
        sections = {}
        for source in sources:
            if source['kind'] != 'rule' or bool(source.get('semantic_only')) != semantic_only:
                continue
            number = source['id'].removeprefix('CR ')
            # Each keyword is its own section; the entire keyword chapter is too large.
            section = re.sub(r'[a-z]$', '', number) if number.startswith('702.') else number.split('.')[0]
            sections.setdefault(section, []).append(source)
        ordered_sections = sorted(
            sections.values(),
            key=lambda group: not any(
                source['id'].removeprefix('CR ') in HIGH_PRIORITY_RULES
                for source in group
            ),
        )
        for section in ordered_sections:
            if sum(len(s['text']) for s in section) <= 6000:
                priority_rules = [
                    source for source in section
                    if source['id'].removeprefix('CR ') in HIGH_PRIORITY_RULES
                ]
                result.extend([source] for source in priority_rules)
                remainder = [source for source in section if source not in priority_rules]
                if remainder:
                    result.append(remainder)
                continue
            # Large chapters fall back to short subrule families, then individual rules.
            families = {}
            for source in section:
                families.setdefault(re.sub(r'[a-z]$', '', source['id']), []).append(source)
            ordered_families = sorted(
                families.values(),
                key=lambda group: not any(
                    source['id'].removeprefix('CR ') in HIGH_PRIORITY_RULES
                    for source in group
                ),
            )
            for group in ordered_families:
                if len(group) <= 8 and sum(len(s['text']) for s in group) <= 3500:
                    result.append(group)
                else:
                    result.extend([s] for s in sorted(
                        group,
                        key=lambda source: source['id'].removeprefix('CR ') not in HIGH_PRIORITY_RULES,
                    ))
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
