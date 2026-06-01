from __future__ import annotations

from typing import Any, Dict
from aos_capabilities.truth_runtime.truth_sufficiency.checker import TruthSufficiencyChecker


class ResponseGroundingValidator:
    def validate(self, packet: Dict[str, Any], response_text: str | None = None) -> Dict[str, Any]:
        suff = packet.get('sufficiency') or TruthSufficiencyChecker().check(packet)
        decision = suff.get('decision')
        return {
            'operation': 'truth.validate_response',
            'decision': 'BLOCK' if decision == 'BLOCK' else ('MATURE' if decision == 'MATURE' else 'ALLOW'),
            'response_must_label': ['assumption','unknown'] if decision in {'WARN','MATURE'} else [],
            'response_must_not': ['promote_assumptions_to_fact','claim_from_filename_only','hide_incomplete_truth'],
            'sufficiency': suff,
        }
