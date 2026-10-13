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
    r'\b(?:trample|deathtouch|lifelink|fights?|replacement|apnap|priority|legend(?:ary)?|'
    r'trigger(?:s|ed|ing)?|copy|copied|copying|clone|blocked)\b|'
    r'\bgoes? on (?:the )?stack\b|'
    r'\b(?:damage is )?prevented\b',
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
    return 'low' if HIGH_RISK_QUERY.search(question) else 'none'
