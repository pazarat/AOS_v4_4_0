from __future__ import annotations

from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional
import json
import uuid


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def new_id(prefix: str) -> str:
    return f"{prefix}_{uuid.uuid4().hex[:12]}"


@dataclass
class Event:
    type: str
    actor: str
    subject: str
    data: Dict[str, Any] = field(default_factory=dict)
    id: str = field(default_factory=lambda: new_id('evt'))
    timestamp: str = field(default_factory=utc_now)
    correlation_id: Optional[str] = None
    causation_id: Optional[str] = None

    def to_json(self) -> str:
        return json.dumps(asdict(self), ensure_ascii=False)


@dataclass
class Fact:
    layer: str
    statement: str
    source: str
    confidence: float = 1.0
    status: str = 'verified'
    id: str = field(default_factory=lambda: new_id('fact'))
    created_at: str = field(default_factory=utc_now)


@dataclass
class SurfaceDecision:
    surface: str
    visible_scope: str
    user_facing_subject: str
    internal_scopes_allowed: List[str] = field(default_factory=list)
    hidden_scopes: List[str] = field(default_factory=list)
    truth_priority: List[str] = field(default_factory=list)
    response_mode: str = 'project_surface_only'
    response_rules: List[str] = field(default_factory=list)
    forbidden_exposure: List[str] = field(default_factory=list)
    reason: str = ''
    id: str = field(default_factory=lambda: new_id('surface'))
    created_at: str = field(default_factory=utc_now)


@dataclass
class IntentFrame:
    raw_request: str
    intent_type: str
    target: str
    surface: str
    entrypoint: str
    risk_level: str = 'read_only'
    explicit_aos_intent: bool = False
    requires_file_access: bool = False
    may_modify_files: bool = False
    ambiguity_level: str = 'low'
    truth_requirements: List[str] = field(default_factory=list)
    must_not_do: List[str] = field(default_factory=list)
    identity_behavior: str = 'operational_identity_first'
    user_facing_subject: str = 'active_project_payload'
    visible_scope: str = 'active_project_payload'
    hidden_scopes: List[str] = field(default_factory=list)
    response_mode: str = 'project_surface_only'
    response_contract: Dict[str, Any] = field(default_factory=dict)
    id: str = field(default_factory=lambda: new_id('intent'))
    created_at: str = field(default_factory=utc_now)


@dataclass
class ActionRequest:
    type: str
    actor: str
    target: str
    inputs: Dict[str, Any] = field(default_factory=dict)
    side_effects: List[str] = field(default_factory=list)
    risk_level: str = 'read_only'
    source_goal: Optional[str] = None
    source_intent: Optional[str] = None
    id: str = field(default_factory=lambda: new_id('act'))


@dataclass
class PolicyDecision:
    action_id: str
    status: str
    reasons: List[str] = field(default_factory=list)
    required_next_step: List[str] = field(default_factory=list)

    @property
    def allowed(self) -> bool:
        return self.status == 'allowed'


@dataclass
class Goal:
    text: str
    id: str = field(default_factory=lambda: new_id('goal'))
    status: str = 'draft'
    created_at: str = field(default_factory=utc_now)


@dataclass
class GoalPlan:
    goal_id: str
    condition: str
    steps: List[Dict[str, Any]]
    gates: List[str]
    risks: List[str]
    intent_id: Optional[str] = None
    surface: str = 'active_project_payload'
    entrypoint: str = 'project_goal_flow'
    created_at: str = field(default_factory=utc_now)
