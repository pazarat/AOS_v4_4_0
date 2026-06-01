from __future__ import annotations
import re
from typing import Any, Dict, List

class RouteExtractor:
    def extract(self, records: List[Dict[str, Any]]) -> Dict[str, Any]:
        routes=[]
        for r in records:
            if not r.get('is_code') and r.get('language') not in {'json','yaml'}:
                continue
            text = r.get('sample_full') or r.get('sample') or ''
            patterns = [
                ('fastapi_flask', r'@(?:app|router|blueprint)\.(get|post|put|patch|delete)\(["\']([^"\']+)["\']'),
                ('express', r'\b(?:app|router)\.(get|post|put|patch|delete)\(["\']([^"\']+)["\']'),
                ('aspnet_attr', r'\[(HttpGet|HttpPost|HttpPut|HttpPatch|HttpDelete)(?:\(["\']?([^"\']*)["\']?\))?\]'),
                ('next_route', r'export\s+async\s+function\s+(GET|POST|PUT|PATCH|DELETE)\s*\('),
            ]
            for kind, pat in patterns:
                for m in re.finditer(pat, text, re.I):
                    if kind == 'express':
                        method, route = m.group(1).upper(), m.group(2)
                    elif kind == 'aspnet_attr':
                        method, route = m.group(1).replace('Http','').upper(), (m.group(2) or '')
                    elif kind == 'next_route':
                        method, route = m.group(1).upper(), self.next_route_from_path(r['path'])
                    else:
                        method, route = m.group(1).upper(), m.group(2)
                    routes.append({'method': method, 'path': route, 'file': r['path'], 'line': text[:m.start()].count('\n')+1, 'source': kind})
        return {'route_count': len(routes), 'routes': routes[:1000]}

    def next_route_from_path(self, path: str) -> str:
        # Best-effort derivation for Next.js app/api/**/route.ts
        if '/app/api/' in path:
            seg = path.split('/app/api/', 1)[1]
        elif path.startswith('app/api/'):
            seg = path[len('app/api/'):]
        else:
            return path
        parts = [p for p in seg.split('/') if p and not p.startswith('route.')]
        return '/api/' + '/'.join(parts)
