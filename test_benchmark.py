import copy
import hashlib
import unittest
import benchmark

class BenchmarkTests(unittest.TestCase):
    def case(self):
        return {'id':'case','criteria':[{'id':'one'},{'id':'two'}], 'evidence_groups':[{'label':'a','any_of':['CR 1','CR 2']},{'label':'card','any_of':['CARD Example']} ]}

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

    def test_error_not_in_successful_latency(self):
        run={'expected_attempts':2,'results':[{'error':error,'metrics':{'evidence_recall':0,'all_evidence_found':False,'citations':[],'invalid_citations':[]},'timing':{'total_seconds':t}} for error,t in [(None,10),('failed',.1)]]}
        self.assertEqual(benchmark.summary(run)['median_seconds'],10)
        self.assertEqual(benchmark.summary(run)['errors'],1)

    def test_comparison_rejects_changed_corpus_and_sampling(self):
        run={'status':'complete','expected_attempts':1,'corpus_sha256':'a','results':[{'sampling':{'temperature':.1}}]}
        other=copy.deepcopy(run);other['corpus_sha256']='b';other['results'][0]['sampling']['temperature']=.7
        self.assertEqual(set(benchmark.validate_comparison(run,other)),{'corpus_sha256','sampling'})

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

if __name__=='__main__':unittest.main()
