from __future__ import annotations

from typing import Any, Dict, List


class ContradictionResolver:
    """Detects contradictions that require a second pass or maturity decision."""

    def resolve(self, merged: Dict[str, Any]) -> List[Dict[str, Any]]:
        needs = set(merged.get('next_needs') or [])
        contradictions: List[Dict[str, Any]] = []
        if 'resolve_duplicate_functional_truth_owner' in needs:
            contradictions.append({
                'type': 'duplicate_functional_truth',
                'decision': 'MATURE_BEFORE_EXECUTION',
                'meaning': 'functional branches share content or meaning; runtime must not infer missing differences',
            })
        if 'close_or_defer_missing_declared_artifacts' in needs:
            contradictions.append({
                'type': 'missing_declared_truth_promise',
                'decision': 'CLOSE_OR_DEFER',
                'meaning': 'declared truth targets must be created, matured, or explicitly deferred before downstream execution',
            })
        return contradictions
