from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUERY = 'اخبرني عنك من انت و ماهو عملك وظيفتك ومهامك ومهاراتك وكيف تتعامل مع مشروعي وتقيمك لوضعه الحالي وماهي اول خطوة تتخذه اتجاه المشروع'


def cli(*args: str, timeout: int = 30) -> str:
    r = subprocess.run([sys.executable, str(ROOT / 'aos.py'), '--root', str(ROOT), *args], cwd=str(ROOT), text=True, capture_output=True, timeout=timeout)
    if r.returncode != 0:
        raise AssertionError(r.stdout + r.stderr)
    return r.stdout.strip()


class OperationsRuntimeV42ContractTests(unittest.TestCase):
    def test_matrix_invokes_multiple_layer_services_not_single_artifact_scan(self):
        packet = json.loads(cli('packet', QUERY, '--verbose', timeout=40))
        matrix = packet['operations']['matrix_invocation']
        self.assertEqual(matrix['mode'], 'matrix_fanout_fanin')
        self.assertGreaterEqual(matrix['call_count'], 4)
        self.assertIn('project_truth', matrix['call_names'])
        self.assertIn('artifact_matrix', matrix['call_names'])
        self.assertIn('truth_requirement_preview', matrix['call_names'])
        self.assertIn('goal_runtime', matrix['call_names'])
        layers = {c['layer'] for c in packet['contributions']}
        self.assertIn('project_truth', layers)
        self.assertIn('artifact_cockpit', layers)
        self.assertIn('truth_runtime', layers)
        self.assertIn('truth_requirement', layers)
        self.assertIn('goal_runtime', layers)

    def test_layer_facades_block_direct_calls_without_operations_context(self):
        sys.path.insert(0, str(ROOT))
        from aos_core.intent.main import create as intent_create
        from aos_capabilities.file_intelligence.main import create as file_create
        from aos_capabilities.truth_runtime.main import create as truth_create
        from aos_capabilities.goal_runtime.main import create as goal_create
        from aos_core.config import AOSPaths
        paths = AOSPaths(ROOT)
        self.assertEqual(intent_create().resolve('x')['status'], 'blocked')
        self.assertEqual(file_create().inspect(ROOT)['status'], 'blocked')
        self.assertEqual(truth_create(paths).resolve_requirement('x', intent={}, surface='active_project_payload')['status'], 'blocked')
        self.assertEqual(goal_create(paths).experience_patterns(request_text='x')['status'], 'blocked')

    def test_truth_synthesis_uses_high_value_project_truth(self):
        packet = json.loads(cli('packet', QUERY, '--verbose', timeout=40))
        insight = packet['operations']['operational_insight']
        self.assertEqual(insight['project_identity']['name'], 'Pazarat')
        self.assertEqual(insight['stack_signal']['database'], 'PostgreSQL')
        self.assertEqual(insight['primary_owner']['label'], 'إدارة المستخدمين')
        summary = '\n'.join(insight['summary'])
        self.assertIn('Pazarat', summary)
        self.assertIn('ASP.NET', summary)
        self.assertIn('PostgreSQL', summary)
        self.assertIn('إدارة المستخدمين', summary)

    def test_second_pass_runs_when_contradictions_exist(self):
        packet = json.loads(cli('packet', QUERY, '--verbose', timeout=40))
        self.assertIn('second_pass_invocation', packet['intent'])
        self.assertGreaterEqual(packet['intent']['second_pass_invocation']['call_count'], 2)
        self.assertIn('project_truth_refocus', packet['intent']['second_pass_invocation']['call_names'])
        self.assertIn('artifact_refocus', packet['intent']['second_pass_invocation']['call_names'])


if __name__ == '__main__':
    unittest.main()
