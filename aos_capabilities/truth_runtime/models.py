from __future__ import annotations

from dataclasses import dataclass, field, asdict
from typing import Any, Dict, List, Optional
from datetime import datetime, timezone
import uuid


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def new_id(prefix: str) -> str:
    return f"{prefix}_{uuid.uuid4().hex[:12]}"


@dataclass
class TruthRequirement:
    request_text: str
    surface: str = 'active_project_payload'
    intent_type: str = 'unknown'
    risk_level: str = 'read_only'
    truth_depth: int = 2
    depth_label: str = 'structural'
    required_layers: List[str] = field(default_factory=list)
    required_scopes: List[str] = field(default_factory=list)
    required_relations: List[str] = field(default_factory=list)
    execution_sensitive: bool = False
    reason: str = ''
    id: str = field(default_factory=lambda: new_id('truth_req'))
    created_at: str = field(default_factory=utc_now)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class TruthPacket:
    requirement: Dict[str, Any]
    evidence: List[Dict[str, Any]] = field(default_factory=list)
    high_value_sources: List[Dict[str, Any]] = field(default_factory=list)
    relationship_evidence: Dict[str, Any] = field(default_factory=dict)
    incomplete_truth: Dict[str, Any] = field(default_factory=dict)
    sufficiency: Dict[str, Any] = field(default_factory=dict)
    source_truth_store: Dict[str, Any] = field(default_factory=dict)
    id: str = field(default_factory=lambda: new_id('truth_packet'))
    created_at: str = field(default_factory=utc_now)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
