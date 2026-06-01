from __future__ import annotations

from dataclasses import dataclass, asdict
from datetime import datetime, timedelta, timezone
from typing import Any, Dict
import secrets

_CONTEXT_MARKER = 'operations_runtime'
_CONTEXT_TTL_SECONDS = 900
_ISSUED_CONTEXTS: Dict[str, Dict[str, Any]] = {}


@dataclass(frozen=True)
class OperationContext:
    """Runtime token proving that a layer call is owned by the Runtime Kernel."""

    caller: str
    operation_id: str
    purpose: str
    token: str
    layer_id: str | None = None

    def to_intent(self, **extra: Any) -> Dict[str, Any]:
        data = asdict(self)
        data['called_by'] = _CONTEXT_MARKER
        data['operation_context_required'] = True
        data.update(extra)
        return data


def make_operation_context(operation_id: str, purpose: str, *, scope_plan: Dict[str, Any] | None = None, layer_id: str | None = None) -> OperationContext:
    token = secrets.token_hex(16)
    expires_at = datetime.now(timezone.utc) + timedelta(seconds=_CONTEXT_TTL_SECONDS)
    _ISSUED_CONTEXTS[token] = {
        'caller': _CONTEXT_MARKER,
        'operation_id': operation_id,
        'purpose': purpose,
        'layer_id': layer_id,
        'scope_plan': scope_plan or {},
        'expires_at': expires_at.isoformat(),
        'revoked': False,
    }
    return OperationContext(caller=_CONTEXT_MARKER, operation_id=operation_id, purpose=purpose, token=token, layer_id=layer_id)


def revoke_operation_context(token: str) -> None:
    if token in _ISSUED_CONTEXTS:
        _ISSUED_CONTEXTS[token]['revoked'] = True


def get_context_record(token: str | None) -> Dict[str, Any] | None:
    if not token:
        return None
    return _ISSUED_CONTEXTS.get(token)


def is_valid_operations_intent(intent: Dict[str, Any] | None) -> bool:
    if not isinstance(intent, dict):
        return False
    if intent.get('called_by') != _CONTEXT_MARKER or not bool(intent.get('operation_context_required')):
        return False
    token = intent.get('token')
    record = get_context_record(token)
    if not record or record.get('revoked'):
        return False
    if record.get('operation_id') != intent.get('operation_id'):
        return False
    try:
        expires = datetime.fromisoformat(record['expires_at'])
    except Exception:
        return False
    if datetime.now(timezone.utc) > expires:
        return False
    if intent.get('layer_id') and record.get('layer_id') and intent.get('layer_id') != record.get('layer_id'):
        return False
    return True


def context_scope_plan(intent: Dict[str, Any] | None) -> Dict[str, Any]:
    if not isinstance(intent, dict):
        return {}
    record = get_context_record(intent.get('token'))
    return dict((record or {}).get('scope_plan') or {})
