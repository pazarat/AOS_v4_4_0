from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List


class PlacementResolver:
    """Classifies target placement before writes."""

    GENERATED_SEGMENTS = {'__pycache__', '.pytest_cache', 'runtime_state', 'reports', 'audit', 'bin', 'obj', 'dist', 'build', '.next'}

    def assess(self, target_paths: List[str]) -> Dict[str, Any]:
        results = []
        blockers = []
        for raw in target_paths:
            p = raw.replace('\\', '/')
            parts = set(Path(p).parts)
            status = 'ok'
            reason = ''
            if parts & self.GENERATED_SEGMENTS or p.endswith('.pyc'):
                status = 'blocked'
                reason = 'generated_or_runtime_artifact'
                blockers.append({'path': p, 'reason': reason})
            elif p.startswith('aos_core/files/'):
                status = 'blocked'
                reason = 'file_intelligence_must_not_live_inside_core_files_layer'
                blockers.append({'path': p, 'reason': reason})
            results.append({'path': p, 'status': status, 'reason': reason})
        return {'targets': results, 'blockers': blockers, 'status': 'blocked' if blockers else 'ok'}
