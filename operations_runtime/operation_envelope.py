from __future__ import annotations

from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from typing import Any, Dict, List
from uuid import uuid4


@dataclass
class OperationEnvelope:
    """Single operation state owned by Operations Runtime Kernel.

    The envelope is the only mutable state that crosses nodes. Layers do not
    own the operation. They return typed contributions into this envelope.
    """

    request_text: str
    operation_id: str = field(default_factory=lambda: f"op_{uuid4().hex[:12]}")
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    surface: str = "active_project_payload"
    intent: Dict[str, Any] = field(default_factory=dict)
    active_project_state: Dict[str, Any] = field(default_factory=dict)
    operation_contract: Dict[str, Any] = field(default_factory=dict)
    scope_plan: Dict[str, Any] = field(default_factory=dict)
    truth_context: Dict[str, Any] = field(default_factory=dict)
    truth_requirement: Dict[str, Any] = field(default_factory=dict)
    artifact_matrix: Dict[str, Any] = field(default_factory=dict)
    truth_packet: Dict[str, Any] = field(default_factory=dict)
    contributions: List[Dict[str, Any]] = field(default_factory=list)
    contradictions: List[Dict[str, Any]] = field(default_factory=list)
    operational_insight: Dict[str, Any] = field(default_factory=dict)
    trace: List[Dict[str, Any]] = field(default_factory=list)
    delivery: Dict[str, Any] = field(default_factory=dict)

    def add_contribution(self, contribution: Dict[str, Any]) -> None:
        if contribution:
            self.contributions.append(contribution)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
