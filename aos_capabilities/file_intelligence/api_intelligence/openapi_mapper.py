from __future__ import annotations
import json, re
from typing import Any, Dict, List

class OpenAPIMapper:
    def extract(self, records: List[Dict[str, Any]]) -> Dict[str, Any]:
        specs=[]
        for r in records:
            path=r.get('path','').lower()
            if 'openapi' not in path and 'swagger' not in path:
                continue
            text = r.get('sample_full') or r.get('sample') or ''
            paths=[]
            if r.get('language') == 'json':
                try:
                    data=json.loads(text)
                    paths=list((data.get('paths') or {}).keys())
                except Exception:
                    paths=[]
            else:
                paths=re.findall(r'^\s{0,4}(/[^:]+):\s*$', text, re.M)
            specs.append({'file': r['path'], 'path_count': len(paths), 'paths': paths[:200]})
        return {'spec_count': len(specs), 'specs': specs}
