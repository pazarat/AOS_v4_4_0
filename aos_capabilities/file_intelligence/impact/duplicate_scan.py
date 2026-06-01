from __future__ import annotations
from typing import Any, Dict, List

class DuplicateScanner:
    def scan(self, records: List[Dict[str, Any]]) -> Dict[str, Any]:
        by_hash={}
        by_semantic={}
        for r in records:
            if r.get('size_bytes', 0) == 0:
                continue
            fp=(r.get('fingerprints') or {}).get('sha256')
            sfp=(r.get('semantic_fingerprint') or {}).get('semantic_sha1')
            if fp:
                by_hash.setdefault(fp, []).append(r['path'])
            if sfp and (r.get('semantic_fingerprint') or {}).get('token_count',0) > 25:
                by_semantic.setdefault(sfp, []).append(r['path'])
        exact=[{'sha256': k, 'paths': v} for k,v in by_hash.items() if len(v)>1]
        semantic=[{'semantic_sha1': k, 'paths': v} for k,v in by_semantic.items() if len(v)>1]
        return {'exact_duplicate_count': len(exact), 'semantic_duplicate_count': len(semantic), 'exact_duplicates': exact[:100], 'semantic_duplicates': semantic[:100]}
