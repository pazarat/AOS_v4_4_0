from __future__ import annotations
from typing import Any, Dict, List

class MigrationReader:
    def extract(self, records: List[Dict[str, Any]]) -> Dict[str, Any]:
        migrations = []
        for r in records:
            path = r.get('path','').lower()
            if 'migration' in path or r.get('role') == 'database_migration':
                migrations.append({'path': r['path'], 'language': r.get('language'), 'size_bytes': r.get('size_bytes')})
        return {'migration_count': len(migrations), 'migrations': migrations[:500]}
