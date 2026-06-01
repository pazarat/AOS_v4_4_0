from __future__ import annotations

from typing import Any, Dict, List


class PhilosophySyncAdvisor:
    """Read-only advisor for operational identity synchronization.

    It does not edit identity files. It emits an obligation whenever a new law,
    layer philosophy, or capability behavior appears in the truth packet.
    """

    def advise(self, packet: Dict[str, Any]) -> Dict[str, Any]:
        req = packet.get('requirement') or {}
        semantics = packet.get('truth_value_semantics') or {}
        obligations: List[Dict[str, Any]] = []
        if req.get('truth_depth', 0) >= 4:
            obligations.append({
                'target': 'aos_identity/OPERATIONAL_IDENTITY.md',
                'reason': 'Higher-truth/canon changes must stay synchronized with operating identity.',
                'mode': 'propose_update_before_next_release',
            })
        if semantics.get('empty_declared_target_count') or semantics.get('declared_missing_artifact_count'):
            obligations.append({
                'target': 'aos_capabilities/truth_runtime/LAYER_IDENTITY.md',
                'reason': 'Truth semantics changed or detected construction-target/missing-artifact laws.',
                'mode': 'ensure_layer_identity_mentions_the_law',
            })
        return {
            'operation': 'identity_sync.advice',
            'status': 'obligations_present' if obligations else 'no_sync_required',
            'obligations': obligations,
            'law': 'new_governance_philosophy_must_sync_to_operating_identity_and_owning_layer_identity',
        }
