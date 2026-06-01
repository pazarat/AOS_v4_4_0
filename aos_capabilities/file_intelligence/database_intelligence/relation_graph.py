from __future__ import annotations
import re
from typing import Any, Dict, List

class RelationGraphBuilder:
    def build(self, records: List[Dict[str, Any]], schemas: Dict[str, Any]) -> Dict[str, Any]:
        edges=[]
        for r in records:
            text = r.get('sample_full') or r.get('sample') or ''
            for m in re.finditer(r'FOREIGN\s+KEY\s*\(([^)]+)\)\s+REFERENCES\s+([A-Za-z_][\w\.]*)', text, re.I):
                edges.append({'from_file': r['path'], 'column': m.group(1).strip(), 'to_table': m.group(2)})
            for m in re.finditer(r'@relation\s*\(', text):
                edges.append({'from_file': r['path'], 'relation': 'prisma_relation', 'line': text[:m.start()].count('\n')+1})
        return {'edge_count': len(edges), 'edges': edges[:1000]}
