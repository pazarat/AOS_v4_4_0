import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run_cmd(*args):
    r = subprocess.run([sys.executable, str(ROOT / 'aos.py'), '--root', str(ROOT), *args], text=True, capture_output=True, check=True, timeout=30)
    return json.loads(r.stdout)


class IntentCognitionRuntimeTests(unittest.TestCase):
    def test_intent_is_hypothesis_not_decision(self):
        data = run_cmd('packet', 'أريد إصلاح طبقة الملفات لأنها سبب المشكلة', '--verbose')
        cognition = data['intent_cognition']
        self.assertEqual(cognition['initial_intent_status'], 'hypothesis_not_decision')
        self.assertTrue(cognition['truth_grounding']['required_before_decision'])
        self.assertIn('user_diagnosis_is_signal_not_verified_cause', cognition['expressed_diagnosis']['status'])

    def test_metaphor_is_signal_not_literal_architecture(self):
        data = run_cmd('intent', 'أريد فتح الشرايين وجعلها مثل قمرة قيادة لا متاهة', '--verbose')
        cognition = data['intent_cognition']
        self.assertTrue(cognition['signal_interpretation']['metaphor_or_signal_detected'])
        self.assertEqual(cognition['signal_interpretation']['conversion_required'], 'signal_to_standard_before_action')

    def test_simple_identity_does_not_trigger_artifact_cockpit(self):
        data = run_cmd('packet', 'من أنت؟', '--verbose')
        cognition = data['intent_cognition']
        self.assertEqual(cognition['layer_needs']['artifact_cockpit'], 'none_or_cached_identity_truth')
        self.assertIn(data['file_matrix']['packet_mode'], {'operations_identity_minimal_no_artifact_scan','operations_fast_contribution_matrix','recent_operations_cache'})
        self.assertIn(data['file_matrix']['authority'], {'not_invoked_for_simple_intent','cache_summary_not_truth'})

    def test_project_status_uses_hot_truth_not_goal_runtime(self):
        data = run_cmd('packet', 'من أنت وما وضع مشروعي؟', '--verbose')
        cognition = data['intent_cognition']
        self.assertEqual(cognition['layer_needs']['artifact_cockpit'], 'hot_truth_packet_only')
        self.assertEqual(cognition['layer_needs']['goal_runtime'], 'not_required_for_normal_answer')
        self.assertIn(data['file_matrix']['packet_mode'], {'operations_fast_contribution_matrix','recent_operations_cache'})

    def test_repeated_failure_activates_goal_need(self):
        data = run_cmd('packet', 'لم ينجح الإصلاح وما زالت نفس المشكلة تتكرر بعد عدة إصدارات', '--verbose')
        cognition = data['intent_cognition']
        self.assertTrue(cognition['continuity']['repeated_failure_signal'])
        self.assertEqual(cognition['layer_needs']['goal_runtime'], 'required_for_repeated_failure_or_root_cause')
        self.assertIn(cognition['layer_needs']['artifact_cockpit'], {'focused_root_cause', 'deep_required'})

    def test_layer_identity_and_api_exist(self):
        self.assertTrue((ROOT / 'aos_core' / 'intent' / 'LAYER_IDENTITY.md').exists())
        self.assertTrue((ROOT / 'aos_core' / 'intent' / 'INTENT_COGNITION_API.yaml').exists())
        txt = (ROOT / 'aos_core' / 'intent' / 'LAYER_IDENTITY.md').read_text(encoding='utf-8')
        self.assertIn('Initial Intent is Hypothesis', txt)
        self.assertIn('User Metaphor is Signal', txt)


if __name__ == '__main__':
    unittest.main()
