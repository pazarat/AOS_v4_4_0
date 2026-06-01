from __future__ import annotations

from typing import Any, Dict, List


class Evaluator:
    """Minimal deterministic evaluator for testable gates."""

    def evaluate_plan(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        issues: List[str] = []
        if not plan.get('steps'):
            issues.append('plan_has_no_steps')
        if 'intent_resolved' not in plan.get('gates', []):
            issues.append('missing_intent_resolved_gate')
        if 'policy_review' not in plan.get('gates', []) and plan.get('surface') != 'aos_environment':
            issues.append('missing_policy_review_gate')
        if 'evaluation_required' not in plan.get('gates', []) and plan.get('surface') != 'aos_environment':
            issues.append('missing_evaluation_gate')
        if not plan.get('surface'):
            issues.append('missing_operational_surface')
        if not plan.get('entrypoint'):
            issues.append('missing_entrypoint')
        return {'passed': not issues, 'issues': issues}
