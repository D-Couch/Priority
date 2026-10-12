import json
import unittest
from generation import VisibleText, decode_completion


def stream(events,done=True):
    for event in events:
        yield ('data: '+json.dumps(event)+'\n').encode()
    if done:
        yield b'data: [DONE]\n'

class GenerationTests(unittest.TestCase):
    def test_reasoning_tags_at_every_chunk_boundary(self):
        text='<think>private thought</think>Yes. [CR 117.4]'
        for cut in range(len(text)+1):
            reader=VisibleText()
            result=reader.feed(text[:cut])+reader.feed(text[cut:])+reader.finish()
            self.assertEqual(result,'Yes. [CR 117.4]')
            self.assertEqual(reader.hidden_characters,len('private thought'))

    def test_separate_reasoning_and_usage_only_event(self):
        events=[{'choices':[{'delta':{'reasoning_content':'hidden'}}]},
                {'choices':[{'delta':{'content':'No.'},'finish_reason':'stop'}]},
                {'choices':[],'usage':{'completion_tokens':10}}]
        result=list(decode_completion(stream(events)))
        self.assertEqual(result[0],{'type':'token','text':'No.'})
        self.assertEqual(result[-1]['usage']['completion_tokens'],10)
        self.assertEqual(result[-1]['reasoning_characters'],6)
        self.assertNotIn('hidden',json.dumps(result))

    def test_output_limit_without_answer_remains_visible_in_diagnostics(self):
        result=list(decode_completion(stream([{'choices':[{'delta':{'content':'<think>unfinished'},'finish_reason':'length'}]}])))
        self.assertEqual(len(result),1)
        self.assertEqual(result[0]['finish_reason'],'length')
        self.assertEqual(result[0]['visible_characters'],0)

    def test_transport_truncation_is_not_success(self):
        with self.assertRaisesRegex(RuntimeError,'completion marker'):
            list(decode_completion(stream([{'choices':[{'delta':{'content':'partial'}}]}],done=False)))

    def test_literal_less_than_and_unicode_preserved(self):
        reader=VisibleText()
        self.assertEqual(reader.feed('Toughness < 1; é')+reader.finish(),'Toughness < 1; é')

if __name__=='__main__':unittest.main()
