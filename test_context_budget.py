import unittest
from context_budget import pack_context, make_messages, OUTPUT_TOKENS, TEMPLATE_MARGIN


def count(messages):
    # A deliberately pessimistic tokenizer makes boundary tests deterministic.
    return sum(len(m['content'].encode()) + 10 for m in messages)


def capacity(headroom):
    overhead = count(make_messages('Judge', [], [{'role': 'user', 'content': '?'}]))
    return OUTPUT_TOKENS + TEMPLATE_MARGIN + overhead + headroom


def source(identifier, body, kind='rule'):
    return {'id': identifier, 'title': identifier, 'text': body, 'kind': kind}


class ContextBudgetTests(unittest.TestCase):
    def test_output_reserve_and_complete_excerpts(self):
        sources = [source('CR 101.1', 'x' * 100), source('CR 202.2', 'y' * 900)]
        history = [{'role': 'user', 'content': 'Question'}]
        messages, chosen, info = pack_context('Judge', sources, history, count, capacity(180))
        self.assertLessEqual(count(messages) + OUTPUT_TOKENS + TEMPLATE_MARGIN, info['context_length'])
        self.assertEqual(chosen, sources[:1])
        self.assertIn('x' * 100, messages[0]['content'])
        self.assertNotIn('y' * 20, messages[0]['content'])

    def test_oversized_question_fails_before_inference(self):
        with self.assertRaisesRegex(ValueError, 'latest question'):
            pack_context('Judge', [], [{'role': 'user', 'content': 'x' * 500}], count, capacity(100))

    def test_keeps_current_question_when_dropping_old_turns(self):
        history = [{'role': 'user', 'content': 'old' * 200}, {'role': 'assistant', 'content': 'prior'}, {'role': 'user', 'content': 'current'}]
        messages, _, info = pack_context('Judge', [], history, count, capacity(100))
        self.assertEqual(messages[-1], history[-1])
        self.assertGreater(info['omitted_turns'], 0)

    def test_card_oracle_precedes_dated_rulings(self):
        sources = [source('C1', 'dated' * 40, 'ruling'), source('C2', 'Oracle', 'card')]
        _, chosen, _ = pack_context('Judge', sources, [{'role': 'user', 'content': '?'}], count, capacity(70))
        self.assertEqual([s['id'] for s in chosen], ['C2'])

    def test_adjacent_definition_and_exception_travel_together(self):
        sources = [source('CR 201.7', 'Definition'), source('CR 201.8', 'Exception' * 30), source('CR 401.1', 'Other')]
        _, chosen, _ = pack_context('Judge', sources, [{'role': 'user', 'content': '?'}], count, capacity(100))
        self.assertEqual([s['id'] for s in chosen], ['CR 401.1'])
        _, chosen, _ = pack_context('Judge', sources, [{'role': 'user', 'content': '?'}], count, capacity(600))
        self.assertEqual([s['id'] for s in chosen], [s['id'] for s in sources])

    def test_short_rule_family_is_not_split(self):
        sources = [source('CR 101.1', 'Parent'), source('CR 101.1a', 'Child' * 30)]
        with self.assertRaisesRegex(ValueError, 'No complete reference'):
            pack_context('Judge', sources, [{'role': 'user', 'content': '?'}], count, capacity(70))


if __name__ == '__main__':
    unittest.main()
