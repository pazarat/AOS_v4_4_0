from __future__ import annotations

from typing import Any, Dict


class TruthSufficiencyChecker:
    """Decides whether the truth packet can support answer/execution."""

    def check(self, packet: Dict[str, Any]) -> Dict[str, Any]:
        req = packet.get('requirement') or {}
        depth = int(req.get('truth_depth') or 2)
        evidence = packet.get('evidence') or []
        high_value = packet.get('high_value_sources') or []
        relationship = packet.get('relationship_evidence') or {}
        incomplete = packet.get('incomplete_truth') or {}
        blockers = int(incomplete.get('blocking_count') or 0)
        maturity = int(incomplete.get('maturity_issue_count') or 0)
        verified_or_derived = [e for e in evidence if e.get('grade') in {'verified','derived'}]
        relationship_signal = sum(1 for k,v in relationship.items() if isinstance(v, int) and v > 0)

        reasons=[]
        decision='ALLOW'
        if blockers:
            decision='BLOCK'
            reasons.append('blocking_incomplete_truth_detected')
        elif depth >= 5 and maturity:
            decision='MATURE'
            reasons.append('execution_requires_mature_truth_before_write')
        elif depth >= 4 and maturity:
            decision='MATURE'
            reasons.append('architecture_or_canon_truth_has_maturity_gaps')
        elif depth >= 3 and relationship_signal < 2:
            decision='MATURE'
            reasons.append('relational_intent_requires_more_relationship_evidence')
        elif not verified_or_derived and not high_value:
            decision='WARN'
            reasons.append('limited_direct_evidence_answer_must_label_unknowns_or_assumptions')
        else:
            reasons.append('sufficient_for_current_depth')

        return {
            'decision': decision,
            'truth_depth': depth,
            'depth_label': req.get('depth_label'),
            'evidence_count': len(evidence),
            'high_value_source_count': len(high_value),
            'relationship_signal_count': relationship_signal,
            'blocking_count': blockers,
            'maturity_issue_count': maturity,
            'reasons': reasons,
            'allowed_grades': ['verified','derived','assumption','unknown','blocked'],
        }
