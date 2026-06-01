from __future__ import annotations

from typing import Any, Dict

from .evidence_builder import EvidencePacketBuilder
from .receipt_model import OperationReceipt


class OperationReceiptBuilder:
    def build(self, *, operation: str, scope: str, file_count: int, diagnostics: Dict[str, Any], construction_gate: Dict[str, Any], governance: Dict[str, Any]) -> Dict[str, Any]:
        evidence = EvidencePacketBuilder().build(
            file_count=file_count,
            diagnostics=diagnostics,
            construction_gate=construction_gate,
            governance=governance,
        )
        receipt = OperationReceipt(
            operation=operation,
            scope=scope,
            decision=governance.get('decision', 'UNKNOWN'),
            evidence_summary=evidence,
            blockers=governance.get('blockers', []),
            required_next_steps=governance.get('required_next_steps', []),
            warnings=governance.get('warnings', []),
        )
        return receipt.to_dict()
