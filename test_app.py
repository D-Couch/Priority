import unittest
import re
import knowledge


class KnowledgeTests(unittest.TestCase):
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
    def test_commander_damage_retrieves_rule_903_10a(self):
        sources=knowledge.retrieve([{'role':'user','content':'In Commander, a particular commander has dealt me 12 combat damage while controlled by Alice and then 9 while controlled by Bob. Do those add together for commander damage, even though its controller changed?'}],[])
        self.assertIn('CR 903.10a',{s['id'] for s in sources})

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
    def test_trample_evidence(self):
        sources=knowledge.retrieve([{'role':'user','content':'How does trample work when the blocking creature has indestructible?'}],[])
        self.assertIn('CR 702.19b',{s['id'] for s in sources})
        self.assertIn('CR 702.12a',{s['id'] for s in sources})

if __name__=='__main__':
    unittest.main()
