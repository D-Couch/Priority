"""Pack complete source excerpts against LM Studio's actual tokenizer."""
import re
from urllib.parse import urlparse

OUTPUT_TOKENS = 3500
TEMPLATE_MARGIN = 64
ANSWER_CONTRACT = """END REFERENCE EXCERPTS.
Follow this response contract:
If information needed to determine the ruling is missing, respond ONLY with "Need details:" and the specific clarifying questions. Do not add a rules tutorial, hypothetical rulings, or assurances.
Otherwise use "Ruling:" for the direct answer to every part of the question, then "Why:" with at most three concise explanatory sentences and supporting source citations. Address only the interaction asked about; do not add examples, unasked timing sequences, or extra caveats.
Check that each cited rule's conditions match the stated game state. An exception applies only to the event it describes. Do not extend it to a different event merely because similar words appear in the rules.
"""


def make_messages(system, sources, history):
    evidence = '\n\n'.join('[' + s['id'] + '] ' + s['title'] + '\n' + s['text'] for s in sources)
    return [{'role': 'system', 'content': system + '\n\nREFERENCE EXCERPTS:\n' + evidence + '\n\n' + ANSWER_CONTRACT}] + history


def source_groups(sources):
    """Keep compact sections intact so definitions travel with their exceptions."""
    result = [[s] for s in sources if s['kind'] == 'card']
    sections = {}
    for source in sources:
        if source['kind'] != 'rule':
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
    result.extend([s] for s in sources if s['kind'] == 'ruling')
    return result


def pack_context(system, sources, history, count_tokens, context_length):
    limit = context_length - OUTPUT_TOKENS - TEMPLATE_MARGIN
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
    for group in source_groups(sources):
        candidate = selected + group
        if count_tokens(make_messages(system, candidate, history)) <= limit:
            selected = candidate
    if sources and not selected:
        raise ValueError('No complete reference excerpt fits alongside this conversation. Start a new conversation or load a larger context in LM Studio.')
    messages = make_messages(system, selected, history)
    prompt_tokens = count_tokens(messages)
    return messages, selected, {'context_length': context_length, 'prompt_tokens': prompt_tokens,
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
