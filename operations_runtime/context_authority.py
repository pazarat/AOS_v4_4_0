from __future__ import annotations

from typing import Any, Dict

from operations_runtime.context import make_operation_context, revoke_operation_context


class ContextAuthority:
    """Kernel-owned authority for issuing layer-call contexts."""

    def issue(self, operation_id: str, purpose: str, *, scope_plan: Dict[str, Any] | None = None, layer_id: str | None = None) -> Any:
        return make_operation_context(operation_id, purpose, scope_plan=scope_plan, layer_id=layer_id)

    def revoke(self, token: str) -> None:
        revoke_operation_context(token)
