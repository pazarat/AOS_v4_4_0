from __future__ import annotations

from typing import Any, Dict


class FlexibleConstitutionPolicy:
    """Prevents the governance layer from becoming a brittle cage."""

    def classify(self, rule_present: bool, rule_covers_operation: bool, direct_risk: bool) -> Dict[str, Any]:
        if direct_risk:
            return {'decision': 'BLOCK', 'reason': 'direct_risk'}
        if not rule_present:
            return {'decision': 'MATURE', 'reason': 'missing_rule_requires_local_standard'}
        if not rule_covers_operation:
            return {'decision': 'MATURE', 'reason': 'rule_does_not_cover_operation'}
        return {'decision': 'ALLOW', 'reason': 'rule_present_and_covers_operation'}
