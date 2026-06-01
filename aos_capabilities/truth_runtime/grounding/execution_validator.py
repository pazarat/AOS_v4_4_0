from __future__ import annotations

from typing import Any, Dict
from aos_capabilities.truth_runtime.truth_sufficiency.checker import TruthSufficiencyChecker


class ExecutionGroundingValidator:
    def validate(self, packet: Dict[str, Any], plan: Dict[str, Any] | None = None) -> Dict[str, Any]:
        suff = packet.get('sufficiency') or TruthSufficiencyChecker().check(packet)
        decision = suff.get('decision')
        if decision in {'BLOCK','MATURE','WARN'}:
            status = 'BLOCK' if decision == 'BLOCK' else 'MATURE'
        else:
            status = 'ALLOW'
        return {
            'operation': 'truth.validate_execution',
            'decision': status,
            'requires': ['impact_scan','write_gate','post_write_verification','receipt'] if status == 'ALLOW' else ['repair_or_mature_truth_before_execution'],
            'sufficiency': suff,
        }
