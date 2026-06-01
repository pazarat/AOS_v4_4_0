from __future__ import annotations

from typing import Any, Dict, List


class CanonGuard:
    """Detects whether likely canon/standard artifacts exist for governed work."""

    CANON_TERMS = ('canon', 'standard', 'policy', 'contract', 'manifest', 'معيار', 'قانون', 'حوكمة')

    def assess(self, records: List[Dict[str, Any]], query: str = '') -> Dict[str, Any]:
        canon_files = [r['path'] for r in records if any(t in r.get('path','').lower() for t in self.CANON_TERMS)]
        return {
            'canon_like_file_count': len(canon_files),
            'canon_like_files': canon_files[:100],
            'status': 'present' if canon_files else 'missing',
            'query': query,
        }
