from __future__ import annotations
from typing import Any, Dict, List

class PatchGate:
    """Pre-write gate. It does not apply patches; it classifies readiness and blockers."""
    PROTECTED_PATTERNS = ['/aos_core/kernel/', '/aos_core/runtime/', '/aos_identity/system_truth.json', '/aos_identity/OPERATIONAL_IDENTITY.md', '/aos_identity/SYSTEM_CONSTITUTION.md']

    def assess(self, target_paths: List[str], intent: Dict[str, Any] | None, matrix: Dict[str, Any]) -> Dict[str, Any]:
        intent = intent or {}
        risk = intent.get('risk_level') or 'unknown'
        may_modify = bool(intent.get('may_modify_files'))
        blockers=[]; required=[]
        if not may_modify:
            blockers.append('intent_is_not_write_capable')
        for p in target_paths:
            normalized='/' + p.replace('\\','/')
            if any(pattern in normalized for pattern in self.PROTECTED_PATTERNS):
                required.append('human_approval_for_core_or_identity_change')
        if (matrix.get('duplicate_scan') or {}).get('exact_duplicate_count', 0):
            required.append('review_exact_duplicates_before_write')
        if (matrix.get('conflict_scan') or {}).get('conflict_count', 0):
            required.append('review_conflicts_before_write')
        status='blocked' if blockers else ('approval_required' if required or risk in {'high','critical'} else 'allowed')
        return {'status': status, 'blockers': blockers, 'required_next_steps': sorted(set(required)), 'target_paths': target_paths, 'risk_level': risk}
