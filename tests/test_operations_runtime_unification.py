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


class OperationsRuntimeUnificationTests(unittest.TestCase):
    def test_no_duplicate_operations_section_exists(self):
        self.assertTrue((ROOT / 'operations_runtime' / 'main.py').exists())
        self.assertFalse((ROOT / ('operations' + '_control_room')).exists(), 'duplicate legacy operation section must not exist')

    def test_registry_is_owned_by_operations_runtime(self):
        registry = (ROOT / 'operations_runtime' / 'layer_registry' / 'OPERATIONS_LAYER_REGISTRY.yaml').read_text(encoding='utf-8')
        self.assertIn('owner: operations_runtime', registry)
        self.assertIn('aos_core/intent/main.py', registry)
        self.assertIn('aos_capabilities/file_intelligence/main.py', registry)
        self.assertNotIn('operations' + '_control_room', registry)

    def test_boot_and_packet_are_owned_by_single_runtime(self):
        boot = json.loads(cli('boot', '--verbose'))
        self.assertEqual(boot['entry_owner'], 'operations_runtime')
        self.assertIn('4.2.0', boot['system_version'])
        packet = json.loads(cli('packet', QUERY, '--verbose'))
        self.assertEqual(packet['operations_runtime']['entry_owner'], 'operations_runtime')
        self.assertNotIn('operations' + '_control_room', json.dumps(packet, ensure_ascii=False))

    def test_direct_file_intelligence_block_uses_runtime_context(self):
        sys.path.insert(0, str(ROOT))
        from aos_core.ports.file_intelligence_port import FileIntelligencePort
        result = FileIntelligencePort().inspect(ROOT)
        self.assertEqual(result['status'], 'blocked')
        self.assertEqual(result['direct_layer_access'], 'blocked_by_operations_runtime_context_guard')
