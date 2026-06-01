from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List


@dataclass(frozen=True)
class OperationContract:
    """Authoritative contract created by Operations Runtime before any layer call."""

    operation_id: str
    request_text: str
    created_at: str
    actor: str = 'user'
    owner: str = 'operations_runtime'
    surface: str = 'unresolved'
    intent_type: str = 'unresolved'
    risk_level: str = 'read_only'
    read_allowed: bool = True
    write_allowed: bool = False
    status: str = 'initialized'
    laws: List[str] = field(default_factory=lambda: [
        'no_layer_call_without_operation_contract',
        'no_scope_without_scope_plan',
        'no_claim_without_truth_or_explicit_uncertainty',
        'no_fixture_contamination_on_runtime_surface',
        'delivery_must_pass_grounding_gate',
    ])

    @classmethod
    def from_envelope(cls, envelope: Any) -> 'OperationContract':
        intent = envelope.intent or {}
        return cls(
            operation_id=envelope.operation_id,
            request_text=envelope.request_text or '',
            created_at=getattr(envelope, 'created_at', None) or datetime.now(timezone.utc).isoformat(),
            surface=getattr(envelope, 'surface', None) or intent.get('surface') or 'unresolved',
            intent_type=intent.get('intent_type') or 'unresolved',
            risk_level=intent.get('risk_level') or 'read_only',
            write_allowed=bool(intent.get('may_modify_files')),
            status='surface_bound' if intent else 'initialized',
        )

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class ScopePlan:
    """Governed filesystem and truth scope for one operation."""

    operation_id: str
    surface: str
    primary_scope: str
    primary_root: str
    include_roots: List[str]
    exclude_roots: List[str]
    allowed_roots: List[str]
    active_project_role: str = 'primary_truth_when_surface_is_project'
    fixture_policy: str = 'not_applicable'
    truth_profile: str = 'generic_project_truth'
    reason: str = ''

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    def allowed_path(self, path: str | Path) -> bool:
        resolved = Path(path).resolve()
        allowed = [Path(p).resolve() for p in self.allowed_roots]
        return any(resolved == root or root in resolved.parents for root in allowed)


@dataclass(frozen=True)
class TruthContext:
    """Loaded governing truth context before layer execution."""

    operation_id: str
    profile: str
    governing_sources: List[Dict[str, Any]]
    required_truth: List[str]
    missing_required_truth: List[str]
    active_project_role: str
    status: str
    policy: Dict[str, Any]

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
