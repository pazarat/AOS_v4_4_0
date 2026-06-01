from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from typing import Any, Dict, List
import uuid


@dataclass
class OperationReceipt:
    operation: str
    scope: str
    decision: str
    evidence_summary: Dict[str, Any]
    blockers: List[str] = field(default_factory=list)
    required_next_steps: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    receipt_id: str = field(default_factory=lambda: f"receipt_{uuid.uuid4().hex[:12]}")
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
