from __future__ import annotations
from typing import Any, Dict, List

class ConflictScanner:
    def scan(self, records: List[Dict[str, Any]], api_map: Dict[str, Any]) -> Dict[str, Any]:
        symbol_locations={}
        conflicts=[]
        for r in records:
            for s in r.get('symbols') or []:
                key=(s.get('kind'), s.get('name'))
                if not key[1]:
                    continue
                symbol_locations.setdefault(key, []).append({'path': r['path'], 'line': s.get('line')})
        for (kind,name), locs in symbol_locations.items():
            if len(locs)>1 and kind in {'class','interface'}:
                conflicts.append({'type':'duplicate_symbol_name', 'kind':kind, 'name':name, 'locations':locs[:20]})
        for c in api_map.get('duplicate_endpoints') or []:
            conflicts.append({'type':'duplicate_endpoint', **c})
        return {'conflict_count': len(conflicts), 'conflicts': conflicts[:200]}
