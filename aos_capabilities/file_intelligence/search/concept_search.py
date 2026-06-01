from __future__ import annotations
from typing import Any, Dict, List
from aos_capabilities.file_intelligence.common import CONCEPT_GROUPS

class ConceptSearch:
    def concepts_for_query(self, query: str) -> List[str]:
        low = query.lower()
        matched = []
        for concept, terms in CONCEPT_GROUPS.items():
            if any(t.lower() in low for t in terms) or concept.replace('_',' ') in low:
                matched.append(concept)
        return matched

    def search(self, records: List[Dict[str, Any]], query: str, limit: int = 20) -> List[Dict[str, Any]]:
        concepts = self.concepts_for_query(query)
        if not concepts:
            return []
        out = []
        for r in records:
            rc = r.get('concepts') or {}
            score = sum((rc.get(c) or {}).get('score', 0) for c in concepts)
            if score:
                out.append({'path': r['path'], 'score': score, 'matched_concepts': [c for c in concepts if c in rc], 'role': r.get('role'), 'surface': r.get('surface')})
        return sorted(out, key=lambda x: (-x['score'], x['path']))[:limit]
