from __future__ import annotations

from typing import List

from aos_core.contracts import ActionRequest, PolicyDecision


class PolicyEngine:
    """Deterministic policy gate.

    The engine receives ActionRequest and returns PolicyDecision. It must not
    know tool implementations. Intent and surface decide which policies apply.
    """

    HIGH_RISK = {'write_project', 'execute_code', 'network', 'destructive', 'high'}

    def decide(self, action: ActionRequest, current_state: str, has_project_truth: bool) -> PolicyDecision:
        reasons: List[str] = []
        next_steps: List[str] = []

        if action.risk_level in self.HIGH_RISK:
            reasons.append(f'Risk level {action.risk_level} requires human approval.')
            next_steps.append('human_approval')

        if 'mutates_project_payload' in action.side_effects and current_state not in {'POLICY_REVIEW', 'HUMAN_APPROVAL', 'SANDBOX_EXECUTION'}:
            reasons.append('Project mutation is not allowed outside policy/sandbox states.')
            next_steps.append('move_to_policy_review')

        if 'mutates_aos_core' in action.side_effects:
            reasons.append('AOS core mutation is blocked unless routed through self-development governance, sandbox, tests, and approval.')
            next_steps.append('self_development_workflow')
            next_steps.append('human_approval')

        if action.type.startswith('code.') and not has_project_truth:
            reasons.append('Code action blocked because project truth is not established.')
            next_steps.append('truth_building')

        if action.target == 'kernel.direct_mutation':
            reasons.append('Direct kernel mutation is forbidden. Use self-development workflow.')
            next_steps.append('self_development_workflow')

        if reasons:
            return PolicyDecision(action_id=action.id, status='blocked', reasons=sorted(set(reasons)), required_next_step=sorted(set(next_steps)))
        return PolicyDecision(action_id=action.id, status='allowed')
