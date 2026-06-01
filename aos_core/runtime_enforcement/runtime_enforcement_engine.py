from __future__ import annotations

from typing import Any, Dict


class RuntimeEnforcementEngine:
    """Final gate that decides whether an operation packet can be used for execution."""

    def assess(self, packet: Dict[str, Any]) -> Dict[str, Any]:
        intent = packet.get('intent', {})
        claim_ledger = packet.get('truth', {}).get('claim_ledger', [])
        blocked_claims = [c for c in claim_ledger if c.get('grade') == 'blocked']
        requires_change = bool(intent.get('may_modify_files'))
        required = ['intent', 'surface', 'truth', 'governance', 'evaluation']
        if requires_change:
            required += ['impact_scan', 'duplicate_scan', 'conflict_scan', 'patch_gate', 'human_approval_if_high_risk']
        permission = 'read_or_answer_allowed'
        if blocked_claims:
            permission = 'blocked_until_truth_resolution'
        elif requires_change:
            permission = 'blocked_until_patch_gate_and_approval'
        return {
            'single_exit': True,
            'permission': permission,
            'required_gates': required,
            'blocked_claims': blocked_claims,
            'no_bypass': True,
        }
