from __future__ import annotations

from typing import Any, Dict, List


class ScopeGuard:
    def assess(self, records: List[Dict[str, Any]]) -> Dict[str, Any]:
        by_surface: Dict[str, int] = {}
        for r in records:
            by_surface[r.get('surface') or 'unknown'] = by_surface.get(r.get('surface') or 'unknown', 0) + 1
        return {
            'by_surface': by_surface,
            'rule': 'do not mix active project payload, workshop truth, and AOS environment without explicit scope',
        }
