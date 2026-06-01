from __future__ import annotations
from typing import Any, Dict, List
from aos_capabilities.file_intelligence.common import tokenize

class KeywordSearch:
    def search(self, records: List[Dict[str, Any]], query: str, limit: int = 20) -> List[Dict[str, Any]]:
        terms = set(tokenize(query))
        if not terms:
            return []
        out = []
        for r in records:
            text = ' '.join([r.get('path',''), ' '.join((r.get('semantic') or {}).get('top_terms', []))])
            hay = set(tokenize(text + ' ' + r.get('sample','')))
            hits = sorted(terms & hay)
            if hits:
                out.append({'path': r['path'], 'score': len(hits), 'hits': hits, 'role': r.get('role'), 'surface': r.get('surface')})
        return sorted(out, key=lambda x: (-x['score'], x['path']))[:limit]
