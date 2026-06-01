from __future__ import annotations
from typing import Any, Dict, List

class CallGraphBuilder:
    def build(self, records: List[Dict[str, Any]]) -> Dict[str, Any]:
        edges = []
        for r in records:
            for call in r.get('calls') or []:
                edges.append({'from_file': r['path'], 'to_symbol': call.get('name'), 'line': call.get('line')})
        return {'edge_count': len(edges), 'edges': edges[:1000]}
