from __future__ import annotations
from typing import Any, Dict, List

class ImportGraphBuilder:
    def build(self, records: List[Dict[str, Any]]) -> Dict[str, Any]:
        edges = []
        for r in records:
            for imp in r.get('imports') or []:
                edges.append({'from_file': r['path'], 'to_module': imp.get('module'), 'line': imp.get('line'), 'kind': imp.get('kind')})
        return {'edge_count': len(edges), 'edges': edges[:1000]}
