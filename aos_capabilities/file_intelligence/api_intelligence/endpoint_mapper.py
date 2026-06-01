from __future__ import annotations
from typing import Any, Dict, List

class EndpointMapper:
    def map(self, routes: Dict[str, Any]) -> Dict[str, Any]:
        by_path={}
        conflicts=[]
        for route in routes.get('routes', []):
            key=(route.get('method'), route.get('path'))
            by_path.setdefault(key, []).append(route)
        for key, items in by_path.items():
            if len(items)>1:
                conflicts.append({'method': key[0], 'path': key[1], 'definitions': items})
        return {'endpoint_count': len(by_path), 'duplicate_endpoint_count': len(conflicts), 'duplicate_endpoints': conflicts[:100]}
