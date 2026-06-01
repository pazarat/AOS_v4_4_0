from __future__ import annotations

from typing import Any, Dict, List


class TruthGuard:
    """Truth maturity hints derived from file evidence."""

    def assess(self, records: List[Dict[str, Any]], diagnostics: Dict[str, Any] | None = None) -> Dict[str, Any]:
        diagnostics = diagnostics or {}
        truth_files = [r['path'] for r in records if r.get('role') == 'local_project_truth' or 'truth' in r.get('path','').lower() or 'contract' in r.get('path','').lower()]
        return {
            'truth_like_file_count': len(truth_files),
            'truth_like_files': truth_files[:100],
            'incomplete_truth_signals': diagnostics.get('maturity_issue_count', 0),
            'status': 'mature_or_usable' if truth_files and not diagnostics.get('maturity_issue_count', 0) else ('incomplete_or_missing' if not truth_files or diagnostics.get('maturity_issue_count', 0) else 'unknown'),
        }
