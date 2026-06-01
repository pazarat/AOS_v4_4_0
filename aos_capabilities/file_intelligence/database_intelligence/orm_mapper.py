from __future__ import annotations
import re
from typing import Any, Dict, List

class ORMMapper:
    def extract(self, records: List[Dict[str, Any]]) -> Dict[str, Any]:
        entities=[]
        for r in records:
            text = r.get('sample_full') or r.get('sample') or ''
            if not r.get('is_code'):
                continue
            for m in re.finditer(r'\bclass\s+([A-Za-z_][A-Za-z0-9_]*)\s*(?:\([^)]*Model[^)]*\)|:\s*(?:Base|Model|DbContext|Entity))?', text):
                name=m.group(1)
                window=text[m.start():m.start()+600]
                if any(x in window for x in ['Column','ForeignKey','relationship','DbSet','Key','Required','@Entity','@Table']):
                    entities.append({'name': name, 'file': r['path'], 'line': text[:m.start()].count('\n')+1})
            for m in re.finditer(r'DbSet\s*<\s*([A-Za-z_][A-Za-z0-9_]*)\s*>', text):
                entities.append({'name': m.group(1), 'file': r['path'], 'line': text[:m.start()].count('\n')+1, 'source':'ef_dbset'})
        return {'entity_count': len(entities), 'entities': entities[:500]}
