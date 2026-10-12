import unittest
import knowledge


class KnowledgeTests(unittest.TestCase):
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
    def test_commander_dies_evidence_and_no_spurious_card(self):
        sources=knowledge.retrieve([{'role':'user','content':'If my commander dies, can I put it in the command zone? Does it still trigger dies abilities?'}],[])
        ids={s['id'] for s in sources}
        self.assertIn('CR 903.9a',ids)
        self.assertIn('CR 700.4',ids)
        self.assertFalse(any(s['kind']=='card' for s in sources))

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
