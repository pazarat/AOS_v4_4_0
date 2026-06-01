from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUNTIME_QUERY = 'المشكلة في الوكيل ومركز العمليات وطبقة الحقيقة، مشروع الاختبار ليس الحقيقة الأساسية'


def cli(*args: str, timeout: int = 40) -> str:
    r = subprocess.run([sys.executable, str(ROOT / 'aos.py'), '--root', str(ROOT), *args], cwd=str(ROOT), text=True, capture_output=True, timeout=timeout)
    if r.returncode != 0:
        raise AssertionError(r.stdout + r.stderr)
    return r.stdout.strip()


class TruthBoundLayerRuntimeStandardTests(unittest.TestCase):
    def test_runtime_surface_excludes_active_project_as_primary_truth(self):
        packet = json.loads(cli('packet', RUNTIME_QUERY, '--verbose'))
        self.assertEqual(packet['intent']['surface'], 'aos_environment')
        self.assertEqual(packet['scope']['scope_plan']['primary_scope'], 'aos_runtime_architecture')
        self.assertEqual(packet['scope']['scope_plan']['active_project_role'], 'fixture_only_excluded_from_runtime_truth')
        self.assertNotIn('project_truth', packet['operations']['matrix_invocation']['call_names'])

    def test_truth_context_loads_before_layer_fanout_and_truth_after_merge(self):
        packet = json.loads(cli('packet', RUNTIME_QUERY, '--verbose'))
        nodes = [x['node'] for x in packet['operations_runtime']['graph_trace']]
        self.assertLess(nodes.index('load_truth_context'), nodes.index('invoke_layer_matrix'))
        self.assertLess(nodes.index('merge_contributions'), nodes.index('ground_truth_after_merge'))
        self.assertEqual(packet['scope']['truth_context']['profile'], 'aos_runtime_truth')
        self.assertIn(packet['truth']['packet']['arbiter']['decision'], {'ALLOW', 'ANSWER_WITH_LIMITS', 'BLOCK'})

    def test_layer_gateways_expose_runtime_contract(self):
        boot = json.loads(cli('boot', '--verbose'))
        layers = boot['layer_registry']['registered_layers']
        for layer in ['intent_cognition', 'truth_runtime', 'artifact_matrix', 'goal_runtime']:
            self.assertTrue(layers[layer]['gateway'])
            self.assertTrue(layers[layer]['contract']['passed'])
            self.assertTrue(layers[layer]['manifest']['exists'])

    def test_fake_context_is_rejected(self):
        sys.path.insert(0, str(ROOT))
        from aos_capabilities.truth_runtime.main import create as truth_create
        from aos_core.config import AOSPaths
        api = truth_create(AOSPaths(ROOT))
        fake = {'called_by': 'operations_runtime', 'operation_context_required': True, 'operation_id': 'fake', 'token': 'fake'}
        result = api.resolve_requirement('x', intent=fake, surface='aos_environment')
        self.assertEqual(result['status'], 'blocked')

    def test_agent_runtime_contains_no_fixture_specific_name(self):
        forbidden = ['pazarat', 'Pazarat', 'بازارات']
        roots = [ROOT / 'operations_runtime', ROOT / 'aos_capabilities', ROOT / 'aos_core']
        for root in roots:
            for p in root.rglob('*'):
                if p.is_file() and p.suffix.lower() in {'.py', '.md', '.yaml', '.yml', '.json', '.txt'}:
                    text = p.read_text(encoding='utf-8', errors='ignore')
                    for word in forbidden:
                        self.assertNotIn(word, text, f'{word} leaked into {p.relative_to(ROOT)}')


if __name__ == '__main__':
    unittest.main()
