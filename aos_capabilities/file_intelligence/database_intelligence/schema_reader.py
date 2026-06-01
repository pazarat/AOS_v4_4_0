from __future__ import annotations
import re
from typing import Any, Dict, List

class SchemaReader:
    def extract(self, records: List[Dict[str, Any]]) -> Dict[str, Any]:
        tables = []
        for r in records:
            if r.get('language') != 'sql' and r.get('extension') not in {'.sql','.prisma'}:
                continue
            text = r.get('sample_full') or r.get('sample') or ''
            for m in re.finditer(r'CREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?["`\[]?([A-Za-z_][\w\.]*)(?:["`\]]?)\s*\(', text, re.I):
                tables.append({'name': m.group(1), 'file': r['path'], 'line': text[:m.start()].count('\n') + 1, 'source': 'sql_create_table'})
            for m in re.finditer(r'model\s+([A-Za-z_][A-Za-z0-9_]*)\s*\{', text):
                tables.append({'name': m.group(1), 'file': r['path'], 'line': text[:m.start()].count('\n') + 1, 'source': 'prisma_model'})
        return {'table_count': len(tables), 'tables': tables}
