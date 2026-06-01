from __future__ import annotations

from typing import Any, Dict


class ArtifactPolicyEngine:
    """Converts diagnostics and construction state into a single governance decision."""

    def decide(self, diagnostics: Dict[str, Any] | None = None, construction_gate: Dict[str, Any] | None = None, patch_gate: Dict[str, Any] | None = None) -> Dict[str, Any]:
        diagnostics = diagnostics or {}
        construction_gate = construction_gate or {}
        patch_gate = patch_gate or {}
        blockers = []
        required = []
        warnings = []
        if diagnostics.get('blocking_count', 0):
            blockers.append('diagnostics_blocking_count_nonzero')
        if diagnostics.get('maturity_issue_count', 0):
            required.append('resolve_or_accept_maturity_issues')
        c_decision = construction_gate.get('decision')
        if c_decision == 'BLOCK':
            blockers.extend(construction_gate.get('blockers') or ['construction_gate_blocked'])
        elif c_decision == 'MATURE':
            required.extend(construction_gate.get('maturity_requirements') or ['construction_requires_truth_maturity'])
        elif c_decision == 'WARN':
            warnings.extend(construction_gate.get('warnings') or ['construction_gate_warned'])
        p_status = patch_gate.get('status')
        if p_status == 'blocked':
            blockers.extend(patch_gate.get('blockers') or ['patch_gate_blocked'])
        elif p_status == 'approval_required':
            required.extend(patch_gate.get('required_next_steps') or ['approval_required'])
        decision = 'ALLOW'
        if blockers:
            decision = 'BLOCK'
        elif required:
            decision = 'MATURE'
        elif warnings:
            decision = 'WARN'
        return {
            'decision': decision,
            'blockers': sorted(set(blockers)),
            'required_next_steps': sorted(set(required)),
            'warnings': sorted(set(warnings)),
            'policy': 'flexible_constitution',
            'meaning': {
                'ALLOW': 'operation may proceed through standard gates',
                'WARN': 'operation may proceed with explicit receipt warnings',
                'MATURE': 'reference/canon/truth must be matured or risk explicitly accepted before production write',
                'BLOCK': 'operation must stop until blockers are repaired',
            }.get(decision),
        }
