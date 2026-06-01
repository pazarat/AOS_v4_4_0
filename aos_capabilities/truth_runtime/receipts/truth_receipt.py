from __future__ import annotations

from typing import Any, Dict
from datetime import datetime, timezone
import uuid


class TruthReceiptBuilder:
    def build(self, operation: str, packet: Dict[str, Any] | None = None, decision: Dict[str, Any] | None = None) -> Dict[str, Any]:
        packet = packet or {}
        decision = decision or packet.get('sufficiency') or {}
        return {
            'id': f"truth_receipt_{uuid.uuid4().hex[:12]}",
            'created_at': datetime.now(timezone.utc).isoformat(),
            'operation': operation,
            'truth_depth': (packet.get('requirement') or {}).get('truth_depth'),
            'decision': decision.get('decision'),
            'evidence_count': len(packet.get('evidence') or []),
            'high_value_source_count': len(packet.get('high_value_sources') or []),
            'incomplete_truth_status': (packet.get('incomplete_truth') or {}).get('status'),
            'law': 'truth is value/provenance/relationship/intent/canon aware, not file-size or filename biased',
        }
