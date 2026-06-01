#!/usr/bin/env python3
from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent

SMOKE_SUITES = [
    'tests.test_operations_runtime_v44_surface_budget',
    'tests.test_truth_bound_layer_runtime_standard',
]

LEGACY_CONTRACT_SUITES = [
    'tests.test_operations_runtime_kernel',
    'tests.test_operations_runtime_unification',
    'tests.test_operations_runtime_v42_contracts',
]


def run_suites(suites: list[str], *, timeout_per_suite: int = 90) -> int:
    failures = 0
    for suite in suites:
        print(f'== {suite} ==', flush=True)
        try:
            r = subprocess.run([sys.executable, '-m', 'unittest', suite, '-q'], cwd=str(ROOT), text=True, timeout=timeout_per_suite)
        except subprocess.TimeoutExpired:
            print(f'TIMEOUT: {suite}', file=sys.stderr, flush=True)
            failures += 1
            continue
        if r.returncode != 0:
            failures += 1
    return 1 if failures else 0


if __name__ == '__main__':
    if '--full' in sys.argv:
        suite = unittest.defaultTestLoader.discover(str(ROOT / 'tests'))
        result = unittest.TextTestRunner(verbosity=1).run(suite)
        raise SystemExit(0 if result.wasSuccessful() else 1)
    if '--legacy' in sys.argv:
        raise SystemExit(run_suites(LEGACY_CONTRACT_SUITES, timeout_per_suite=120))
    raise SystemExit(run_suites(SMOKE_SUITES, timeout_per_suite=90))
