import math
import io
import tempfile
from pathlib import Path
from contextlib import redirect_stdout
import unittest
from unittest.mock import patch
import vector_search as vs

class VectorTests(unittest.TestCase):
    def test_fusion_rewards_agreement_and_deduplicates(self):
        ranking=vs.fuse(['a','b','b'],['c','b'])
        self.assertEqual(ranking[0],'b')
        self.assertEqual(set(ranking),{'a','b','c'})
        self.assertEqual(len(ranking),3)

    def test_normalization_and_invalid_embeddings(self):
        self.assertAlmostEqual(sum(x*x for x in vs.normalize([3,4])),1)
        for bad in ([],[0,0],[math.nan,1],[math.inf],['x']):
            with self.assertRaises(ValueError):vs.normalize(bad)

    def test_embedding_batches_must_be_complete_and_reordered(self):
        with patch.object(vs,'api',return_value={'data':[{'index':1,'embedding':[0,1]},{'index':0,'embedding':[1,0]}]}):
            self.assertEqual(vs.embed(['a','b'],'search_query: '),[[1,0],[0,1]])
        with patch.object(vs,'api',return_value={'data':[{'index':0,'embedding':[1,0]}]}):
            with self.assertRaisesRegex(ValueError,'Incomplete'):vs.embed(['a','b'],'search_query: ')

    def test_chunks_cover_rule_tail_without_changing_rule_identity(self):
        chunks=list(vs.chunks([('100','General'),('100.1','a'*2400+'TAIL')]))
        self.assertIn('TAIL',chunks[-1][1])
        self.assertTrue(all(n=='100.1' for n,t in chunks[1:]))
        self.assertTrue(all(len(t)<1300 for n,t in chunks))

    def test_hybrid_preserves_all_lexical_candidates_before_semantic_extras(self):
        import knowledge
        sources=[{'id':'C1','kind':'card','text':'Oracle'}]
        lexical=[{'id':'CR '+str(i),'kind':'rule','text':'lex-'+str(i)} for i in range(64)]
        bodies={str(i):'body-'+str(i) for i in range(96)}
        result=knowledge.append_semantic_rules(sources+lexical,['63','80','81']+list(map(str,range(100))),bodies)
        ids=[s['id'] for s in result]
        self.assertEqual(ids[:65],['C1']+['CR '+str(i) for i in range(64)])
        self.assertEqual(ids[65:],['CR 80','CR 81']+['CR '+str(i) for i in range(64,80)]+['CR '+str(i) for i in range(82,88)])
        self.assertLessEqual(len([s for s in result if s['kind']=='rule']),88)

    def test_remote_embedding_endpoint_rejected_before_network(self):
        with patch.dict('os.environ',{'LM_STUDIO_URL':'https://example.org/v1'}):
            with self.assertRaisesRegex(ValueError,'loopback'):vs.api('/embeddings',{})

    def test_atomic_build_and_stale_corpus_rejection(self):
        with tempfile.TemporaryDirectory() as directory:
            path=Path(directory)/'vectors.sqlite'
            rows=[('100','General'),('100.1','A rule.')]
            with patch.object(vs,'rule_rows',return_value=rows), patch.object(vs,'model_identity',return_value={'key':vs.MODEL}), patch.object(vs,'embed',side_effect=lambda texts,prefix:[[1.,0.] for t in texts]), redirect_stdout(io.StringIO()):
                vs.build(path)
                original=path.read_bytes()
                meta,vectors=vs.load(path)
                self.assertEqual(meta['rules'],2)
                self.assertEqual(len(vectors),2)
                with patch.object(vs,'embed',side_effect=ValueError('embedding service unavailable')):
                    with self.assertRaises(ValueError):vs.build(path)
                self.assertEqual(path.read_bytes(),original)
            with patch.object(vs,'rule_rows',return_value=[('100','Changed')]):
                with self.assertRaisesRegex(ValueError,'Rules changed'):vs.load(path)

if __name__=='__main__':unittest.main()
