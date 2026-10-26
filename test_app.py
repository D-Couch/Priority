import unittest
import re
import context_budget
import knowledge
import server


class KnowledgeTests(unittest.TestCase):
    def test_lm_studio_openai_effort_names(self):
        self.assertEqual(server.OPENAI_REASONING_EFFORTS['off'], 'none')
        self.assertEqual(server.OPENAI_REASONING_EFFORTS['on'], 'xhigh')
        self.assertEqual(server.OPENAI_REASONING_EFFORTS['low'], 'low')

    def test_rule_families_do_not_cross_numeric_prefixes(self):
        self.assertTrue(knowledge._related_rule('702.2c', '702.2'))
        self.assertFalse(knowledge._related_rule('702.20a', '702.2'))
        self.assertTrue(knowledge._related_rule('117.3c', '117'))
        self.assertFalse(knowledge._related_rule('1170.3c', '117'))

    def test_absent_effects_and_double_strike_do_not_request_replacement_topics(self):
        def topics(question):
            text = knowledge.search_question(question)
            return {root for pattern, roots in knowledge.TOPICS if re.search(pattern, text, re.I) for root in roots}
        self.assertNotIn('614', topics('A token is exiled. No replacement effects apply. Can it return?'))
        self.assertNotIn('614', topics('My creature has double strike.'))
        self.assertIn('510', topics('My creature has double strike.'))
        self.assertIn('614', topics('An effect doubles the damage.'))
        self.assertIn('614', topics('I have no replacement effects, but my opponent does.'))
        self.assertIn('614', topics('One replacement effect applies. No other replacement effects apply.'))

    def test_parser_keeps_subrules_and_examples(self):
        text='100. General\n\n100.1 First rule.\nExample: an example.\n\n100.1a Subrule.\n\n100.2 Next.\n'
        rules=knowledge.parse_rules(text)
        self.assertIn('Example: an example.',rules['100.1'])
        self.assertEqual(rules['100.1a'],'Subrule.')
        self.assertEqual(rules['100.2'],'Next.')

    @unittest.skipUnless(knowledge.DB.exists(),'Download knowledge first')
    def test_mana_ability_evidence(self):
        sources=knowledge.retrieve([{'role':'user','content':'Can I respond to a player tapping a land for mana?'}],[])
        self.assertIn('CR 605.3b',{s['id'] for s in sources})

    @unittest.skipUnless(knowledge.DB.exists(),'Download knowledge first')
    def test_additional_casting_cost_retrieves_order_and_priority_rules(self):
        card=next(c for c in knowledge.search_cards('Fling') if c['name']=='Fling')
        messages=[{'role':'user','content':'I cast Fling, sacrificing my creature as its additional cost. Can my opponent respond to stop me paying the cost?'}]
        ids={s['id'] for s in knowledge.retrieve(messages,[card['id']])}
        self.assertTrue({'CR 601.2a','CR 601.2h','CR 601.2i','CR 117.2e','CR 117.3c'}<=ids)

    @unittest.skipUnless(knowledge.DB.exists(),'Download knowledge first')
    def test_commander_dies_evidence_and_no_spurious_card(self):
        sources=knowledge.retrieve([{'role':'user','content':'If my commander dies, can I put it in the command zone? Does it still trigger dies abilities?'}],[])
        ids={s['id'] for s in sources}
        self.assertIn('CR 903.9a',ids)
        self.assertIn('CR 700.4',ids)
        self.assertFalse(any(s['kind']=='card' for s in sources))

    @unittest.skipUnless(knowledge.DB.exists(),'Download knowledge first')
    def test_commander_hand_replacement_rule_survives_context_packing(self):
        question='An effect would return my commander from the battlefield to my hand. May I choose the command zone instead, and is that a replacement effect or a later state-based action?'
        history=[{'role':'user','content':question}]
        sources=knowledge.retrieve(history,[])
        self.assertIn('CR 903.9b',{s['id'] for s in sources})
        def estimate_tokens(messages):
            return sum(len(message['content']) for message in messages)//4
        _, selected, _=context_budget.pack_context('Test system',sources,history,estimate_tokens,8192)
        self.assertIn('CR 903.9b',{s['id'] for s in selected})
        self.assertEqual(sources[0]['id'],'CR 903.9b')

    @unittest.skipUnless(knowledge.DB.exists(),'Download knowledge first')
    def test_replacement_retrieves_general_event_consequence(self):
        question='Rest in Peace replaces a creature going to a graveyard with exile. Does a dies ability trigger?'
        ids={s['id'] for s in knowledge.retrieve([{'role':'user','content':question}],[])}
        self.assertIn('CR 614.6',ids)

    @unittest.skipUnless(knowledge.DB.exists(),'Download knowledge first')
    def test_legend_rule_retrieves_state_based_action_sequence(self):
        question='Can I respond to the legend rule after a spell resolves, before choosing one to keep?'
        ids={s['id'] for s in knowledge.retrieve([{'role':'user','content':question}],[])}
        self.assertIn('CR 704.3',ids)

    @unittest.skipUnless(knowledge.DB.exists(),'Download knowledge first')
    def test_commander_damage_retrieves_rule_903_10a(self):
        sources=knowledge.retrieve([{'role':'user','content':'In Commander, a particular commander has dealt me 12 combat damage while controlled by Alice and then 9 while controlled by Bob. Do those add together for commander damage, even though its controller changed?'}],[])
        self.assertIn('CR 903.10a',{s['id'] for s in sources})

    @unittest.skipUnless(knowledge.DB.exists(),'Download knowledge first')
    def test_prototype_rules_are_prioritized_for_zone_characteristics(self):
        questions = [
            'An artifact creature cast as a prototype dies. What characteristics does it have in my graveyard?',
            'I cast this as a prototyped spell and it left the battlefield. Does its smaller power and toughness remain in the graveyard?',
        ]
        for question in questions:
            with self.subTest(question=question):
                ids={s['id'] for s in knowledge.retrieve([{'role':'user','content':question}],[])}
                self.assertTrue({'CR 718.3','CR 718.4'} <= ids)

    @unittest.skipUnless(knowledge.DB.exists(),'Download knowledge first')
    def test_mana_value_rules_are_prioritized(self):
        questions = [
            ('What is the mana value of an {X}{2}{R} spell with X=4 while it is on the stack?',
             {'CR 202.3','CR 202.3e','CR 107.3a'}),
            ('How do I calculate mana value for a card with two {2/W} symbols?',
             {'CR 202.3','CR 202.3f'}),
        ]
        for question, expected in questions:
            with self.subTest(question=question):
                ids={s['id'] for s in knowledge.retrieve([{'role':'user','content':question}],[])}
                self.assertTrue(expected <= ids)

    @unittest.skipUnless(knowledge.DB.exists(),'Download knowledge first')
    def test_initiative_rules_are_prioritized(self):
        question='One or more creatures I control deal combat damage to the player with the initiative. What ability triggers?'
        ids={s['id'] for s in knowledge.retrieve([{'role':'user','content':question}],[])}
        self.assertTrue({'CR 726.2','CR 726.5'} <= ids)

    @unittest.skipUnless(knowledge.DB.exists(),'Download knowledge first')
    def test_poison_loss_and_planeswalker_ability_rules_are_prioritized(self):
        questions = [
            ('I have nine poison counters and gain one more. When do I lose?', {'CR 104.3d'}),
            ('My planeswalker has three loyalty counters. Does a −3 loyalty ability still resolve if the planeswalker is put into the graveyard before the ability resolves?',
             {'CR 606.4','CR 704.5i','CR 113.7a'}),
        ]
        def estimate_tokens(messages):
            return sum(len(message['content']) for message in messages) // 4
        for question, expected in questions:
            with self.subTest(question=question):
                history=[{'role':'user','content':question}]
                sources=knowledge.retrieve(history,[])
                _, selected, _=context_budget.pack_context('Test system',sources,history,estimate_tokens,8192)
                self.assertTrue(expected <= {s['id'] for s in selected})

    @unittest.skipUnless(knowledge.DB.exists(),'Download knowledge first')
    def test_triggered_ability_source_removal_retrieves_and_packs_direct_rule(self):
        question='My Solemn Simulacrum enters and its search ability goes on the stack. My opponent destroys it before that ability resolves. May I still search?'
        history=[{'role':'user','content':question}]
        sources=knowledge.retrieve(history,[])
        self.assertIn('CR 113.7a',{s['id'] for s in sources})
        def estimate_tokens(messages):
            return sum(len(message['content']) for message in messages)//4
        _, selected, _=context_budget.pack_context('Test system',sources,history,estimate_tokens,8192)
        self.assertIn('CR 113.7a',{s['id'] for s in selected})

    @unittest.skipUnless(knowledge.DB.exists(),'Download knowledge first')
    def test_blocked_attacker_damage_retrieves_trample_rule_through_packing(self):
        question='My attacker is blocked. How much damage gets through to my opponent?'
        history=[{'role':'user','content':question}]
        sources=knowledge.retrieve(history,[])
        self.assertIn('CR 702.19b',{s['id'] for s in sources})
        def estimate_tokens(messages):
            return sum(len(message['content']) for message in messages) // 4
        _, selected, _=context_budget.pack_context('Test system',sources,history,estimate_tokens,8192)
        self.assertIn('CR 702.19b',{s['id'] for s in selected})

    @unittest.skipUnless(knowledge.DB.exists(),'Download knowledge first')
    def test_spell_copy_rule_is_prioritized(self):
        question='When an instant is copied, is the copy cast, and does it retain the original mode?'
        ids={s['id'] for s in knowledge.retrieve([{'role':'user','content':question}],[])}
        self.assertIn('CR 707.10',ids)

    @unittest.skipUnless(knowledge.DB.exists(),'Download knowledge first')
    def test_specific_mechanics_survive_context_packing(self):
        questions = [
            ('I cast a spell with casualty 2 and sacrifice a 2/2 as its additional cost. Does the spell get copied?', 'CR 702.153a'),
            ('If I copy an instant spell already on the stack, does the copy count as casting it?', 'CR 707.10'),
        ]
        def estimate_tokens(messages):
            return sum(len(message['content']) for message in messages) // 4
        for question, expected in questions:
            with self.subTest(question=question):
                history=[{'role':'user','content':question}]
                sources=knowledge.retrieve(history,[])
                _, selected, _=context_budget.pack_context('Test system',sources,history,estimate_tokens,8192)
                self.assertIn(expected,{s['id'] for s in selected})

    @unittest.skipUnless(knowledge.DB.exists(),'Download knowledge first')
    def test_card_attachment_has_oracle_text(self):
        card=next(c for c in knowledge.search_cards('Lightning Bolt') if c['name']=='Lightning Bolt')
        sources=knowledge.retrieve([{'role':'user','content':'Can this target a creature?'}],[card['id']])
        self.assertTrue(any(s['kind']=='card' and '3 damage to any target' in s['text'] for s in sources))

    @unittest.skipUnless(knowledge.DB.exists(),'Download knowledge first')
    def test_exact_bracketed_single_word_card(self):
        sources=knowledge.retrieve([{'role':'user','content':'What does [[Humility]] do?'}],[])
        self.assertTrue(any(s['title']=='Humility' and s['kind']=='card' for s in sources))

    @unittest.skipUnless(knowledge.DB.exists(),'Download knowledge first')
    def test_card_name_lookup_finds_exact_names_and_split_faces(self):
        messages=[{'role':'user','content':'Does Fire // Ice interact with Brazen Borrower?'}]
        sources=knowledge.retrieve(messages,[])
        names={s['title'] for s in sources if s['kind']=='card'}
        self.assertIn('Fire // Ice',names)
        self.assertIn('Brazen Borrower // Petty Theft',names)

    @unittest.skipUnless(knowledge.DB.exists(),'Download knowledge first')
    def test_trample_evidence(self):
        sources=knowledge.retrieve([{'role':'user','content':'How does trample work when the blocking creature has indestructible?'}],[])
        self.assertIn('CR 702.19b',{s['id'] for s in sources})
        self.assertIn('CR 702.12a',{s['id'] for s in sources})

    @unittest.skipUnless(knowledge.DB.exists(),'Download knowledge first')
    def test_random_paper_question_retrieves_procedure_and_legal_target_rules(self):
        question='How does a card that says to perform some action randomly actually work in paper Magic?'
        history=[{'role':'user','content':question}]
        sources=knowledge.retrieve(history,[])
        ids={s['id'] for s in sources}
        self.assertTrue({'CR 601.2c','CR 115.2','MTR 3.9'}<=ids)
        def estimate_tokens(messages):
            return sum(len(message['content']) for message in messages)//4
        _, selected, _=context_budget.pack_context('Test system',sources,history,estimate_tokens,8192)
        self.assertTrue({'CR 601.2c','CR 115.2','MTR 3.9'}<={s['id'] for s in selected})

    @unittest.skipUnless(knowledge.DB.exists(),'Download knowledge first')
    def test_random_target_with_protection_retrieves_protection_rule(self):
        question='A red spell says target creature chosen at random. Can a creature with protection from red be selected?'
        history=[{'role':'user','content':question}]
        sources=knowledge.retrieve(history,[])
        ids={s['id'] for s in sources}
        self.assertTrue({'CR 702.16b','CR 115.2','CR 601.2c'}<=ids)
        self.assertNotIn('MTR 3.9',ids)
        ordered={s['id']:i for i,s in enumerate(sources)}
        self.assertLess(ordered['CR 702.16b'],ordered['CR 115.2'])
        def estimate_tokens(messages):
            return sum(len(message['content']) for message in messages)//4
        _, selected, _=context_budget.pack_context('Test system',sources,history,estimate_tokens,8192)
        self.assertTrue({'CR 702.16b','CR 115.2','CR 601.2c'}<={s['id'] for s in selected})

if __name__=='__main__':
    unittest.main()
