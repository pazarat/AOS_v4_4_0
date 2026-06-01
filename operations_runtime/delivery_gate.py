from __future__ import annotations

from typing import Any, Dict, List


class DeliveryGroundingGate:
    """Final hard gate: validates rendered answer against operation truth policy."""

    def validate(self, answer: str, envelope: Any) -> Dict[str, Any]:
        issues: List[str] = []
        scope_plan = getattr(envelope, 'scope_plan', {}) or {}
        truth_packet = getattr(envelope, 'truth_packet', {}) or {}
        surface = getattr(envelope, 'surface', '')
        decision = ((truth_packet.get('arbiter') or {}).get('decision') or '').upper()

        if decision == 'BLOCK':
            issues.append('truth_arbiter_blocked_delivery')
        if surface == 'aos_environment' and scope_plan.get('active_project_role') == 'fixture_only_excluded_from_runtime_truth':
            project_name = ((getattr(envelope, 'active_project_state', {}) or {}).get('project_name') or '').strip()
            if project_name and project_name in answer:
                issues.append('fixture_contamination:active_project_name_in_runtime_answer')
            for term in ['workshop/active_project/PROJECT']:
                if term in answer:
                    issues.append(f'fixture_contamination:{term}')
        if truth_packet.get('sufficiency', {}).get('decision') == 'INSUFFICIENT' and 'غير مكتملة' not in answer and 'لا أملك' not in answer:
            issues.append('insufficient_truth_not_disclosed')
        return {
            'passed': not issues,
            'issues': issues,
            'policy': 'truth_bound_delivery_gate',
            'truth_decision': decision or truth_packet.get('sufficiency', {}).get('decision'),
        }
