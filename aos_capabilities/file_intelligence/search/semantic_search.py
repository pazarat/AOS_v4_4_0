from __future__ import annotations
from typing import Any, Dict, List
from aos_capabilities.file_intelligence.common import tokenize

class SemanticLiteSearch:
    """Dependency-free semantic-lite search using token overlap and role boosts."""
    ROLE_BOOSTS = {
        'aos_project_truth': 3,
        'documentation': 2,
        'configuration_or_contract': 2,
        'source_code': 1,
    }

    def search(self, records: List[Dict[str, Any]], query: str, limit: int = 20) -> List[Dict[str, Any]]:
        q = set(tokenize(query))
        if not q:
            return []
        out = []
        for r in records:
            terms = set((r.get('semantic') or {}).get('terms', []))
            if not terms:
                terms = set(tokenize((r.get('sample') or '') + ' ' + r.get('path','')))
            overlap = q & terms
            if overlap:
                score = len(overlap) + self.ROLE_BOOSTS.get(r.get('role'), 0)
                out.append({'path': r['path'], 'score': score, 'overlap': sorted(overlap)[:20], 'role': r.get('role'), 'surface': r.get('surface')})
        return sorted(out, key=lambda x: (-x['score'], x['path']))[:limit]
