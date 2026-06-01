from __future__ import annotations

from typing import Any, Dict


class WriteGuard:
    """Canonical write rule for the file intelligence capability."""

    def assess(self, policy_decision: Dict[str, Any]) -> Dict[str, Any]:
        decision = policy_decision.get('decision')
        return {
            'write_allowed': decision in {'ALLOW', 'WARN'},
            'requires_truth_maturity': decision == 'MATURE',
            'blocked': decision == 'BLOCK',
            'rule': 'no production write without preflight, impact, diagnostics, policy, verification, and receipt',
            'policy_decision': decision,
        }
