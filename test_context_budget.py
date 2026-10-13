import unittest
from context_budget import pack_context, make_messages, OUTPUT_TOKENS, TEMPLATE_MARGIN, MAX_PROMPT_TOKENS, ANSWER_CONTRACT


def count(messages):
    # A deliberately pessimistic tokenizer makes boundary tests deterministic.
    return sum(len(m['content'].encode()) + 10 for m in messages)


def capacity(headroom):
    overhead = count(make_messages('Judge', [], [{'role': 'user', 'content': '?'}]))
    return OUTPUT_TOKENS + TEMPLATE_MARGIN + overhead + headroom


def source(identifier, body, kind='rule'):
    return {'id': identifier, 'title': identifier, 'text': body, 'kind': kind}


class ContextBudgetTests(unittest.TestCase):
    def test_general_random_rules_guidance_limits_mtr_scope_and_requires_legal_target_pool(self):
        self.assertIn('do not present MTR 3.9 as governing every random effect',ANSWER_CONTRACT)
        self.assertIn('For random-target questions, do not add unrelated die-roll or tournament guidance',ANSWER_CONTRACT)
        self.assertIn('Never mention a rule number in plain prose without its bracketed citation',ANSWER_CONTRACT)
        self.assertIn('Do not assume an unstated keyword or game fact',ANSWER_CONTRACT)
        self.assertIn('describe damage to creatures as damage marked rather than toughness lost',ANSWER_CONTRACT)
        self.assertIn('only legal targets belong in the pool',ANSWER_CONTRACT)
        self.assertIn('Never suggest an unequal sequential coin-flip method',ANSWER_CONTRACT)
        self.assertIn('Do not invent hypothetical card text, game states, or examples',ANSWER_CONTRACT)
        self.assertIn('shuffled identical slips are a simple method',ANSWER_CONTRACT)
        self.assertIn('suggest a die only when its faces can be mapped evenly',ANSWER_CONTRACT)
        self.assertIn('without a hypothetical example or invented outcome',ANSWER_CONTRACT)
        self.assertIn('state the relevant branches instead of assuming it',ANSWER_CONTRACT)

    def test_tournament_rule_excerpt_is_packed_before_broad_rules(self):
        history=[{'role':'user','content':'How does a random die roll work?'}]
        sources=[{'id':'MTR 3.9','kind':'tournament_rule','title':'Die rolling','text':'Each result has equal chance.'},
                 {'id':'CR 100','kind':'rule','title':'General','text':'General rules.'}]
        estimate=lambda messages:sum(len(m['content']) for m in messages)//4
        _,selected,_=pack_context('system',sources,history,estimate,8192)
        self.assertEqual([s['id'] for s in selected],['MTR 3.9','CR 100'])

    def test_prompt_token_ceiling(self):
        sources = [source(f'CR {100+i}.1', str(i) * 900) for i in range(10)]
        messages, chosen, info = pack_context('Judge', sources,
            [{'role': 'user', 'content': 'Question'}], count,
            MAX_PROMPT_TOKENS + OUTPUT_TOKENS + TEMPLATE_MARGIN + 1000)
        self.assertLessEqual(count(messages), MAX_PROMPT_TOKENS)
        self.assertLess(len(chosen), len(sources))
        self.assertEqual(info['max_prompt_tokens'], MAX_PROMPT_TOKENS)

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

class RelevantRulingTests(unittest.TestCase):
    def test_vector_only_rules_are_lower_priority_than_lexical_rules(self):
        from context_budget import source_groups
        sources = [
            {'id':'CR 510.1','kind':'rule','text':'Lexical combat rule.'},
            {'id':'CR 506.4b','kind':'rule','text':'Lexical rule about tapping blockers.'},
            {'id':'CR 701.14a','kind':'rule','text':'Semantic suggestion.','semantic_only':True},
        ]
        packed = [s['id'] for group in source_groups(sources) for s in group]
        self.assertLess(packed.index('CR 506.4b'),packed.index('CR 701.14a'))

    def test_relevant_ruling_precedes_broad_rules_without_duplicates(self):
        from context_budget import source_groups
        sources = [
            {'id':'C1','kind':'card','text':'Vehicle with crew 1'},
            {'id':'C2','kind':'ruling','text':'A copied Vehicle does not become a creature.'},
            {'id':'C3','kind':'ruling','text':'Any untapped creature can pay the crew cost, even one that just came under your control.'},
            {'id':'CR 601.2','kind':'rule','text':'Casting spells.'},
        ]
        packed = [s['id'] for group in source_groups(sources, 'Can I tap a creature I just cast to pay crew?') for s in group]
        self.assertEqual(packed[:2], ['C1','C3'])
        self.assertEqual(len(packed), len(set(packed)))
        self.assertLess(packed.index('C3'), packed.index('CR 601.2'))

    def test_unmatched_and_oversized_rulings_do_not_take_reserved_space(self):
        from context_budget import relevant_rulings
        self.assertEqual(relevant_rulings([{'id':'C1','kind':'ruling','text':'crew '*400}], 'crew'), [])
        self.assertEqual(relevant_rulings([{'id':'C1','kind':'ruling','text':'Crew a vehicle.'}], 'poison counters'), [])
