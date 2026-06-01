from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUERY = 'اخبرني عنك من انت و ماهو عملك وظيفتك ومهامك ومهاراتك وكيف تتعامل مع مشروعي وتقيمك لوضعه الحالي وماهي اول خطوة تتخذه اتجاه المشروع'


def cli(*args: str, timeout: int = 20) -> str:
    r = subprocess.run([sys.executable, str(ROOT / 'aos.py'), '--root', str(ROOT), *args], cwd=str(ROOT), text=True, capture_output=True, timeout=timeout)
    if r.returncode != 0:
        raise AssertionError(r.stdout + r.stderr)
    return r.stdout.strip()


class OperationsRuntimeKernelTests(unittest.TestCase):
    def test_boot_uses_operations_runtime_owner(self):
        boot = json.loads(cli('boot', '--verbose'))
        self.assertEqual(boot['entry_owner'], 'operations_runtime')
        self.assertIn('4.2.0', boot['system_version'])
        self.assertIn('intent_cognition', boot['layer_registry']['registered_layers'])

    def test_answer_comes_from_operational_insight(self):
        out = cli('answer', QUERY, timeout=15)
        self.assertIn('مهندس مشروع', out)
        self.assertIn('قراءة الحقيقة الحالية', out)
        self.assertIn('أول خطوة', out)
        self.assertNotIn('GPT-5.5', out)
        self.assertNotIn('.zip', out)
        self.assertNotIn('RUN_TESTS.py', out)

    def test_packet_has_graph_trace_and_registered_layers(self):
        packet = json.loads(cli('packet', QUERY, '--verbose', timeout=20))
        self.assertEqual(packet['operations_runtime']['entry_owner'], 'operations_runtime')
        nodes = [x['node'] for x in packet['operations_runtime']['graph_trace']]
        self.assertIn('capture_intent_hypothesis', nodes)
        self.assertIn('invoke_layer_matrix', nodes)
        self.assertIn('synthesize_operational_insight', nodes)
        layers = {c['layer'] for c in packet['contributions']}
        self.assertIn('intent_cognition', layers)
        self.assertIn('truth_runtime', layers)
        self.assertIn('artifact_cockpit', layers)
        insight = packet['operations']['operational_insight']
        self.assertEqual(insight['evidence_mode'], 'synthesized_from_layer_contributions')

    def test_direct_file_intelligence_still_blocked_without_context(self):
        sys.path.insert(0, str(ROOT))
        from aos_core.ports.file_intelligence_port import FileIntelligencePort
        result = FileIntelligencePort().inspect(ROOT)
        self.assertEqual(result['status'], 'blocked')


if __name__ == '__main__':
    unittest.main()
