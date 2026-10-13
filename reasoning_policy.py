"""Small, opt-in routing policy for local model reasoning effort."""
import re


OPENAI_EFFORTS = {
    'off': 'none',
    'low': 'low',
    'medium': 'medium',
    'high': 'high',
    'xhigh': 'xhigh',
    'on': 'xhigh',
}

# Keep reasoning on for rule families that were unreliable in prior off-mode
# evaluations. This is deliberately a small keyword policy, not a correctness
# classifier; callers must still review benchmark results before enabling it.
HIGH_RISK_QUERY = re.compile(
    r'\b(?:trample|deathtouch|lifelink|fights?|replacement|apnap|legend(?:ary)?|'
    r'copy|copied|copying|clone|blocked)\b|'
    r'\bwhose\b[^.!?]{0,100}\b(?:triggers?|triggered abilit(?:y|ies)|abilit(?:y|ies))\b[^.!?]{0,100}\bresolve(?:s|d)?\b|'
    r'\bpriority (?:again|after)\b|\bpass(?:es|ing)? priority\b|\bwho (?:has|gets|receives?) priority\b|'
    r'\bgoes? on (?:the )?stack\b|'
    r'\b(?:damage is )?prevented\b',
    re.IGNORECASE,
)

NEGATED_RISK = re.compile(
    r'\bno (?:other )?replacement effects? apply\b|'
    r'\b(?:not|no|without|does not have|doesn\'t have) (?:any )?trample\b',
    re.IGNORECASE,
)


def select_effort(mode, messages):
    """Return LM Studio's OpenAI-compatible effort for one user request."""
    if mode != 'adaptive':
        try:
            return OPENAI_EFFORTS[mode]
        except KeyError as exc:
            raise ValueError('Reasoning effort must be off, low, medium, high, xhigh, on, or adaptive.') from exc
    question = '\n'.join(
        message.get('content', '')
        for message in messages
        if message.get('role') == 'user' and isinstance(message.get('content'), str)
    )
    question = NEGATED_RISK.sub(' ', question)
    return 'low' if HIGH_RISK_QUERY.search(question) else 'none'
