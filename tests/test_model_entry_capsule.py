import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ModelEntryCapsuleTests(unittest.TestCase):
    def test_model_start_file_exists_and_guides_hot_answer(self):
        p = ROOT / '00_START_HERE_FOR_ANY_MODEL.md'
        self.assertTrue(p.exists())
        text = p.read_text(encoding='utf-8')
        self.assertIn('python aos.py answer', text)
        self.assertIn('Do not begin by reading', text)

    def test_root_aos_py_is_tiny_shim_not_code_rabbit_hole(self):
        p = ROOT / 'aos.py'
        text = p.read_text(encoding='utf-8')
        self.assertLess(p.stat().st_size, 1800)
        self.assertIn('tiny', text.lower())
        self.assertIn('00_START_HERE_FOR_ANY_MODEL.md', text)
        self.assertNotIn('FileIntelligencePort', text)
        self.assertNotIn('AOSKernel', text)

    def test_simulate_entry_catches_package_entry_hygiene(self):
        r = subprocess.run([sys.executable, str(ROOT / 'aos.py'), '--root', str(ROOT), 'simulate-entry', '--verbose'], text=True, capture_output=True, check=True, timeout=20)
        self.assertIn('00_START_HERE_FOR_ANY_MODEL.md', r.stdout)
        self.assertIn('"passed": true', r.stdout)

    def test_hot_answer_path_is_fast_and_does_not_expose_internal_paths(self):
        r = subprocess.run([sys.executable, str(ROOT / 'aos.py'), '--root', str(ROOT), 'answer', 'اخبرني عنك وعن مشروعي الحالي وأول خطوة'], text=True, capture_output=True, check=True, timeout=12)
        out = r.stdout.strip()
        self.assertNotIn('أنا GPT', out[:800])
        self.assertNotIn('workshop/active_project/PROJECT', out)
        self.assertNotIn('aos_capabilities', out)
        self.assertIn('مهندس مشروع', out)


if __name__ == '__main__':
    unittest.main()
