from __future__ import annotations

import json
import subprocess
import sys
import time
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUNTIME_QUERY = 'مازال الاداء ضعيف ومختلط ومركز العمليات لا يفرض الحوكمة على طبقة الحقيقة'


def cli(*args: str, timeout: int = 20) -> str:
    r = subprocess.run([sys.executable, str(ROOT / 'aos.py'), '--root', str(ROOT), *args], cwd=str(ROOT), text=True, capture_output=True, timeout=timeout)
    if r.returncode != 0:
        raise AssertionError(r.stdout + r.stderr)
    return r.stdout.strip()


class OperationsRuntimeV44SurfaceBudgetTests(unittest.TestCase):
    def test_runtime_question_is_bound_before_payload_loading(self):
        packet = json.loads(cli('packet', RUNTIME_QUERY, '--verbose'))
        self.assertEqual(packet['intent']['surface'], 'aos_environment')
        state = packet['scope']['active_project_state']
        self.assertEqual(state['state'], 'intentionally_not_loaded_for_surface')
        self.assertIsNone(state['project_name'])
        self.assertIsNone(state['project_root'])
        self.assertEqual(packet['scope']['scope_plan']['active_project_role'], 'fixture_only_excluded_from_runtime_truth')

    def test_runtime_hot_path_skips_project_truth_goal_and_real_artifact_scan(self):
        packet = json.loads(cli('packet', RUNTIME_QUERY, '--verbose'))
        plan = packet['intent']['contribution_plan']
        self.assertEqual(plan['performance_budget']['profile'], 'runtime_hot_answer')
        self.assertEqual(plan['artifact_depth'], 'none')
        self.assertEqual(plan['goal_runtime'], 'not_required')
        calls = packet['operations']['matrix_invocation']['call_names']
        self.assertNotIn('project_truth', calls)
        self.assertNotIn('goal_runtime', calls)
        self.assertIn('artifact_matrix', calls)  # minimal no-scan contribution only
        self.assertEqual(packet['file_matrix']['diagnostics']['mode'], 'not_run_for_simple_intent')

    def test_runtime_answer_does_not_leak_active_payload_identity(self):
        out = cli('answer', RUNTIME_QUERY)
        forbidden = ['pazarat', 'Pazarat', 'بازارات', 'User Management', 'إدارة المستخدمين']
        for term in forbidden:
            self.assertNotIn(term, out)

    def test_answer_path_completes_without_deep_diagnostic_latency(self):
        start = time.perf_counter()
        cli('answer', RUNTIME_QUERY, timeout=10)
        elapsed = time.perf_counter() - start
        self.assertLess(elapsed, 10.0)


if __name__ == '__main__':
    unittest.main()
