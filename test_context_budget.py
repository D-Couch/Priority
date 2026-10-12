import unittest
from context_budget import pack_context, OUTPUT_TOKENS, TEMPLATE_MARGIN


def count(messages):
    # A deliberately pessimistic tokenizer makes boundary tests deterministic.
    return sum(len(m['content'].encode()) + 10 for m in messages)


def source(identifier, body, kind='rule'):
    return {'id': identifier, 'title': identifier, 'text': body, 'kind': kind}


class ContextBudgetTests(unittest.TestCase):
    def test_output_reserve_and_complete_excerpts(self):
        sources = [source('CR 101.1', 'x' * 100), source('CR 101.2', 'y' * 900)]
        history = [{'role': 'user', 'content': 'Question'}]
        messages, chosen, info = pack_context('Judge', sources, history, count, OUTPUT_TOKENS + TEMPLATE_MARGIN + 300)
        self.assertLessEqual(count(messages) + OUTPUT_TOKENS + TEMPLATE_MARGIN, info['context_length'])
        self.assertEqual(chosen, sources[:1])
        self.assertIn('x' * 100, messages[0]['content'])
        self.assertNotIn('y' * 20, messages[0]['content'])

    def test_oversized_question_fails_before_inference(self):
        with self.assertRaisesRegex(ValueError, 'latest question'):
            pack_context('Judge', [], [{'role': 'user', 'content': 'x' * 500}], count, OUTPUT_TOKENS + 200)

    def test_keeps_current_question_when_dropping_old_turns(self):
        history = [{'role': 'user', 'content': 'old' * 200}, {'role': 'assistant', 'content': 'prior'}, {'role': 'user', 'content': 'current'}]
        messages, _, info = pack_context('Judge', [], history, count, OUTPUT_TOKENS + 200)
        self.assertEqual(messages[-1], history[-1])
        self.assertGreater(info['omitted_turns'], 0)

    def test_card_oracle_precedes_dated_rulings(self):
        sources = [source('C1', 'dated' * 40, 'ruling'), source('C2', 'Oracle', 'card')]
        _, chosen, _ = pack_context('Judge', sources, [{'role': 'user', 'content': '?'}], count, OUTPUT_TOKENS + TEMPLATE_MARGIN + 130)
        self.assertEqual([s['id'] for s in chosen], ['C2'])

    def test_short_rule_family_is_not_split(self):
        sources = [source('CR 101.1', 'Parent'), source('CR 101.1a', 'Child' * 30)]
        with self.assertRaisesRegex(ValueError, 'No complete reference'):
            pack_context('Judge', sources, [{'role': 'user', 'content': '?'}], count, OUTPUT_TOKENS + TEMPLATE_MARGIN + 130)


if __name__ == '__main__':
    unittest.main()
