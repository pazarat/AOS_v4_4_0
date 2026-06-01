from __future__ import annotations
from typing import Any, Dict, List
from pathlib import Path

class ImpactScanner:
    def scan(self, records: List[Dict[str, Any]], changed_paths: List[str] | None = None, query: str = '') -> Dict[str, Any]:
        changed=set(changed_paths or [])
        impacted=[]
        if changed:
            changed_stems={Path(p).stem.lower() for p in changed}
            for r in records:
                if r['path'] in changed:
                    continue
                hay=' '.join([r.get('path',''), r.get('sample',''), ' '.join(i.get('module','') for i in r.get('imports') or [])]).lower()
                if any(stem and stem in hay for stem in changed_stems):
                    impacted.append({'path': r['path'], 'reason':'name_or_import_reference_to_changed_path'})
        elif query:
            q=query.lower()
            for r in records:
                if q in (r.get('sample','') + ' ' + r.get('path','')).lower():
                    impacted.append({'path': r['path'], 'reason':'query_reference'})
        return {'changed_paths': sorted(changed), 'impact_count': len(impacted), 'impacted': impacted[:500]}
