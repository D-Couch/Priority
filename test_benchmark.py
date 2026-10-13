import copy
import hashlib
import unittest
import benchmark

class BenchmarkTests(unittest.TestCase):
    def case(self):
        return {'id':'case','criteria':[{'id':'one'},{'id':'two'}], 'evidence_groups':[{'label':'a','any_of':['CR 1','CR 2']},{'label':'card','any_of':['CARD Example']} ]}

    def test_frozen_corpus_leaves_live_database_unchanged(self):
        original=benchmark.knowledge.DB
        original_hash=benchmark.sha(original) if original.exists() else None
        with benchmark.frozen_corpus() as path:
            self.assertNotEqual(path,original)
            self.assertEqual(benchmark.sha(path),benchmark.read(benchmark.BENCH/'corpus/manifest.json')['database_sha256'])
            with benchmark.closing(benchmark.knowledge.connect()) as conn:
                self.assertGreater(conn.execute('SELECT count(*) FROM rules').fetchone()[0],3000)
        self.assertEqual(benchmark.knowledge.DB,original)
        self.assertFalse(path.exists())
        self.assertEqual(benchmark.sha(original) if original.exists() else None,original_hash)

    def test_evidence_alternatives_do_not_reward_irrelevant_context(self):
        sources=[{'id':'CR 2','kind':'rule','title':'Rule 2','text':'x'},{'id':'CR 3','kind':'rule','title':'Rule 3','text':'irrelevant'}]
        result=benchmark.measure_evidence(self.case(),sources,'Example [CR 999.1]')
        self.assertEqual(result['evidence_recall'],.5)
        self.assertEqual(result['invalid_citations'],['CR 999.1'])
        self.assertEqual(result['citation_id_precision'],0)

    def test_no_citation_is_not_perfect_precision(self):
        self.assertIsNone(benchmark.measure_evidence(self.case(),[],'No citation')['citation_id_precision'])

    def test_missing_review_never_counts_as_correct(self):
        run={'expected_attempts':1,'results':[{'metrics':{'evidence_recall':1,'all_evidence_found':True,'citations':[],'invalid_citations':[]},'timing':{'total_seconds':2}}]}
        result=benchmark.summary(run)
        self.assertIsNone(result['reviewed_accuracy'])
        self.assertEqual(result['reviewed'],0)

    def test_complete_answer_gate_rejects_truncation_and_unknown_telemetry(self):
        rows=[{'metrics':{'evidence_recall':1,'all_evidence_found':True,'citations':[],'invalid_citations':[]},
               'timing':{'total_seconds':1},'review':{'fully_correct':True,'rubric_score':1},
               'diagnostics':{'finish_reason':finish}} for finish in ('stop','length')]
        run={'expected_attempts':2,'results':rows}
        result=benchmark.summary(run)
        self.assertEqual(result['fully_correct'],2)
        self.assertEqual(result['correct_and_complete'],1)
        self.assertEqual(result['truncated_answers'],1)
        rows[1]['diagnostics']={}
        self.assertIsNone(benchmark.summary(run)['correct_and_complete'])
        self.assertEqual(benchmark.summary(run)['unknown_finish_reason'],1)

    def test_error_not_in_successful_latency(self):
        run={'expected_attempts':2,'results':[{'error':error,'metrics':{'evidence_recall':0,'all_evidence_found':False,'citations':[],'invalid_citations':[]},'timing':{'total_seconds':t}} for error,t in [(None,10),('failed',.1)]]}
        self.assertEqual(benchmark.summary(run)['median_seconds'],10)
        self.assertEqual(benchmark.summary(run)['errors'],1)

    def test_comparison_rejects_changed_corpus_and_sampling(self):
        run={'status':'complete','expected_attempts':1,'corpus_sha256':'a','results':[{'sampling':{'temperature':.1}}]}
        other=copy.deepcopy(run);other['corpus_sha256']='b';other['results'][0]['sampling']['temperature']=.7
        self.assertEqual(set(benchmark.validate_comparison(run,other)),{'corpus_sha256','sampling'})

    def test_declared_reasoning_experiment_still_rejects_temperature_change(self):
        old={'status':'complete','expected_attempts':1,'results':[{'sampling':{'temperature':.1}}]}
        new=copy.deepcopy(old);new['results'][0]['sampling']['reasoning_effort']='low'
        self.assertEqual(benchmark.validate_comparison(old,new,['sampling.reasoning_effort']),[])
        new['results'][0]['sampling']['temperature']=.7
        self.assertIn('sampling',benchmark.validate_comparison(old,new,['sampling.reasoning_effort']))

    def test_pre_generation_error_without_sampling_does_not_block_comparison(self):
        base={'model':'qwen','temperature':.1,'max_tokens':3500,'stream':True,'seed':42,'reasoning_effort':'low'}
        old={'status':'complete','expected_attempts':2,'results':[{'sampling':dict(base)},{'sampling':dict(base)}]}
        new=copy.deepcopy(old)
        new['results'][0]['sampling']['reasoning_effort']='none'
        new['results'][1]={'error':'prompt preparation failed','sampling':None}
        self.assertEqual(benchmark.validate_comparison(old,new,['sampling.reasoning_effort']),[])

    def test_prompt_budget_experiment_requires_explicit_allowance(self):
        old={'suite_sha256':'s','references_sha256':'r','corpus_sha256':'c','model':'m','model_runtime':{},'seeds':[42],'repeats':1,'mode':'full','case_order':['a'],'warmup':True,'retrieval':{'mode':'lexical'},'context_budget':{'max_prompt_tokens':4600},'status':'complete','expected_attempts':1,'results':[{'sampling':{'temperature':0.1}}]}
        new={**old,'context_budget':{'max_prompt_tokens':2800}}
        self.assertIn('context_budget',benchmark.validate_comparison(old,new))
        self.assertEqual(benchmark.validate_comparison(old,new,['context_budget.max_prompt_tokens']),[])
        historical={**old,'context_budget':None,'model_runtime':{'/api/v1/models':{'loaded_configs':[{'context_length':8192}]}}}
        self.assertEqual(benchmark.recorded_prompt_limit(historical),8192-3500-benchmark.context_budget.TEMPLATE_MARGIN)
        with self.assertRaisesRegex(ValueError,'Unsupported'):
            benchmark.validate_comparison(old,new,['corpus_sha256'])

    def test_parallel_runtime_experiment_allows_only_parallel_count_change(self):
        old={'status':'complete','expected_attempts':1,'model_runtime':{'/api/v1/models':{'loaded_configs':[{'context_length':8192,'parallel':4,'flash_attention':True}]}},'results':[{'sampling':{'temperature':.1}}]}
        new=copy.deepcopy(old);new['model_runtime']['/api/v1/models']['loaded_configs'][0]['parallel']=1
        self.assertIn('model_runtime',benchmark.validate_comparison(old,new))
        self.assertEqual(benchmark.validate_comparison(old,new,['model_runtime.parallel']),[])
        new['model_runtime']['/api/v1/models']['loaded_configs'][0]['context_length']=4096
        self.assertIn('model_runtime',benchmark.validate_comparison(old,new,['model_runtime.parallel']))

    def test_eval_batch_experiment_allows_only_batch_size_change(self):
        old={'status':'complete','expected_attempts':1,'model_runtime':{'/api/v1/models':{'loaded_configs':[{'context_length':8192,'eval_batch_size':2048,'parallel':1}]}},'results':[{'sampling':{'temperature':.1}}]}
        new=copy.deepcopy(old);new['model_runtime']['/api/v1/models']['loaded_configs'][0]['eval_batch_size']=4096
        self.assertIn('model_runtime',benchmark.validate_comparison(old,new))
        self.assertEqual(benchmark.validate_comparison(old,new,['model_runtime.eval_batch_size']),[])
        new['model_runtime']['/api/v1/models']['loaded_configs'][0]['parallel']=4
        self.assertIn('model_runtime',benchmark.validate_comparison(old,new,['model_runtime.eval_batch_size']))

    def test_physical_batch_experiment_allows_only_microbatch_change(self):
        old={'status':'complete','expected_attempts':1,'model_runtime':{'/api/v1/models':{'loaded_configs':[{'context_length':8192,'eval_batch_size':2048,'physical_batch_size':512,'parallel':1}]}},'results':[{'sampling':{'temperature':.1}}]}
        new=copy.deepcopy(old);new['model_runtime']['/api/v1/models']['loaded_configs'][0]['physical_batch_size']=1024
        self.assertIn('model_runtime',benchmark.validate_comparison(old,new))
        self.assertEqual(benchmark.validate_comparison(old,new,['model_runtime.physical_batch_size']),[])
        new['model_runtime']['/api/v1/models']['loaded_configs'][0]['eval_batch_size']=4096
        self.assertIn('model_runtime',benchmark.validate_comparison(old,new,['model_runtime.physical_batch_size']))

    def test_speculative_depth_experiment_allows_only_draft_depth_change(self):
        old={'status':'complete','expected_attempts':1,'model_runtime':{'/api/v1/models':{'loaded_configs':[{'context_length':8192,'eval_batch_size':2048,'physical_batch_size':512,'parallel':1,'speculative_draft_mtp':True,'speculative_draft_max_tokens':3}]}},'results':[{'sampling':{'temperature':.1}}]}
        new=copy.deepcopy(old);new['model_runtime']['/api/v1/models']['loaded_configs'][0]['speculative_draft_max_tokens']=5
        self.assertIn('model_runtime',benchmark.validate_comparison(old,new))
        self.assertEqual(benchmark.validate_comparison(old,new,['model_runtime.speculative_draft_max_tokens']),[])
        new['model_runtime']['/api/v1/models']['loaded_configs'][0]['speculative_draft_mtp']=False
        self.assertIn('model_runtime',benchmark.validate_comparison(old,new,['model_runtime.speculative_draft_max_tokens']))

    def test_review_bound_to_answer_and_checks_each_criterion(self):
        run={'run_id':'r','suite_sha256':'s','results':[{'case_id':'case','repeat':1,'answer':'No.'}]}
        review={'run_id':'r','suite_sha256':'s','reviewer':'test','review_method':'fixture','results':[{'case_id':'case','repeat':1,'answer_sha256':hashlib.sha256(b'No.').hexdigest(),'criteria':{'one':True,'two':False},'unsupported_or_contradictory_claims':False,'abstained':False,'notes':'Second requirement missing.'}]}
        result=benchmark.apply_review(run,review,{'cases':[self.case()]})
        self.assertFalse(result['results'][0]['review']['fully_correct'])
        self.assertEqual(result['results'][0]['review']['rubric_score'],.5)
        run['results'][0]['answer']='Yes.'
        with self.assertRaisesRegex(ValueError,'Answer changed'):
            benchmark.apply_review(run,review,{'cases':[self.case()]})

    def test_pending_rubric_rejected(self):
        run={'run_id':'r','suite_sha256':'s','results':[{'case_id':'case','repeat':1,'answer':'x'}]}
        review={'run_id':'r','suite_sha256':'s','reviewer':'test','review_method':'fixture','results':[{'case_id':'case','repeat':1,'answer_sha256':hashlib.sha256(b'x').hexdigest(),'criteria':{'one':None,'two':True}}]}
        with self.assertRaisesRegex(ValueError,'explicit boolean'):
            benchmark.apply_review(run,review,{'cases':[self.case()]})

    def test_retrieval_experiment_requires_explicit_allowance(self):
        old={'status':'complete','expected_attempts':1,'results':[{'sampling':{'temperature':.1}}]}
        new=copy.deepcopy(old);new['retrieval']={'mode':'hybrid','index_sha256':'example'}
        self.assertIn('retrieval',benchmark.validate_comparison(old,new))
        self.assertEqual(benchmark.validate_comparison(old,new,['retrieval']),[])
        new['corpus_sha256']='changed'
        self.assertIn('corpus_sha256',benchmark.validate_comparison(old,new,['retrieval']))

if __name__=='__main__':unittest.main()
