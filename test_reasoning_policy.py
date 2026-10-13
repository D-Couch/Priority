import unittest

from reasoning_policy import select_effort


def messages(question):
    return [{'role': 'user', 'content': question}]


class ReasoningPolicyTests(unittest.TestCase):
    def test_fixed_modes_keep_their_existing_mapping(self):
        self.assertEqual(select_effort('off', messages('A simple question?')), 'none')
        self.assertEqual(select_effort('low', messages('A simple question?')), 'low')
        self.assertEqual(select_effort('on', messages('A simple question?')), 'xhigh')

    def test_adaptive_mode_uses_low_for_observed_high_risk_rules(self):
        questions = [
            'How does trample and deathtouch work here?',
            'The triggered ability goes on the stack.',
            'My lifelink damage is prevented.',
            'Who orders these replacement effects?',
            'My creature fights another creature.',
            'I copy a creature and get counters?',
            'My attacker is blocked. How much damage gets through?',
            'Do I get priority after casting this spell?',
            'Can I respond to the legend rule?',
            'Do I get priority after casting this spell?',
        ]
        for question in questions:
            with self.subTest(question=question):
                self.assertEqual(select_effort('adaptive', messages(question)), 'low')

    def test_adaptive_mode_uses_off_for_unflagged_questions(self):
        questions = [
            'Can I respond to a Forest tapping for mana?',
            'A death ability triggers when the creature dies.',
            'No replacement effects apply, and the attacker does not have trample.',
            'Assuming I have priority, can I target my creature?',
        ]
        for question in questions:
            with self.subTest(question=question):
                self.assertEqual(select_effort('adaptive', messages(question)), 'none')

    def test_adaptive_mode_reads_user_turns_only(self):
        history = [
            {'role': 'user', 'content': 'Can I target my own creature?'},
            {'role': 'assistant', 'content': 'This involves trample and deathtouch.'},
        ]
        self.assertEqual(select_effort('adaptive', history), 'none')

    def test_unknown_mode_is_rejected(self):
        with self.assertRaises(ValueError):
            select_effort('fast', messages('Question?'))


if __name__ == '__main__':
    unittest.main()
