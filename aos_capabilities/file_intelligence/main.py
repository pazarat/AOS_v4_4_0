from __future__ import annotations

from pathlib import Path
from typing import Any, Dict

from aos_capabilities.file_intelligence.adapter import FileIntelligenceRuntime
from operations_runtime.context import context_scope_plan, is_valid_operations_intent


def _blocked(operation: str) -> Dict[str, Any]:
    return {
        'capability': 'file_intelligence',
        'operation': operation,
        'status': 'blocked',
        'direct_layer_access': 'blocked_by_operations_runtime_context_guard',
        'authority': 'denied_without_operations_context',
        'reason': 'File Intelligence main API can be invoked only by Operations Runtime Kernel.',
        'project_condition': 'UNSCANNED_DIRECT_ACCESS_BLOCKED',
        'file_count': 0,
        'summary': {'project_condition': 'UNSCANNED_DIRECT_ACCESS_BLOCKED'},
        'records': [],
        'diagnostics': {'mode': 'blocked', 'issue_count': 0, 'blocking_count': 1, 'maturity_issue_count': 0},
    }


class ArtifactMatrixAPI:
    """File Intelligence mini-runtime gateway behind Operations Runtime."""

    layer_id = 'artifact_matrix'

    def __init__(self) -> None:
        self.adapter = FileIntelligenceRuntime()

    def describe(self) -> Dict[str, Any]:
        return {
            'layer_id': self.layer_id,
            'role': 'read-only artifact intelligence, diagnostics, construction context, and verification',
            'commands': ['artifact.inspect', 'artifact.doctor'],
            'entrypoint': 'aos_capabilities.file_intelligence.main.ArtifactMatrixAPI',
        }

    def healthcheck(self) -> Dict[str, Any]:
        return {'status': 'healthy', 'layer_id': self.layer_id}

    def validate_contract(self) -> Dict[str, Any]:
        return {'passed': True, 'issues': [], 'required_context': 'operations_runtime_context'}

    def execute(self, command: Any) -> Dict[str, Any]:
        data = command.to_dict() if hasattr(command, 'to_dict') else dict(command or {})
        payload = data.get('payload') or {}
        context = data.get('context') or payload.get('intent')
        cmd = data.get('command')
        if cmd in {'artifact.inspect', 'inspect'}:
            result = self.inspect(payload.get('root', '.'), query=payload.get('query', ''), changed_paths=payload.get('changed_paths') or [], intent=context)
        elif cmd in {'artifact.doctor', 'doctor'}:
            result = self.doctor(payload.get('root', '.'), query=payload.get('query', ''), changed_paths=payload.get('changed_paths') or [], intent=context)
        else:
            result = _blocked(str(cmd or 'unknown')) | {'reason': 'unsupported_command'}
        return {'operation_id': data.get('operation_id'), 'layer_id': self.layer_id, 'command': cmd, 'status': result.get('status', 'ok'), 'data': result}

    def inspect(self, root: str | Path, *, query: str = '', changed_paths: list[str] | None = None, intent: Dict[str, Any] | None = None) -> Dict[str, Any]:
        if not is_valid_operations_intent(intent):
            return _blocked('artifact.inspect')
        if not self._within_scope(Path(root), intent):
            out = _blocked('artifact.inspect')
            out['reason'] = 'requested_root_outside_operation_scope'
            return out
        out = self.adapter.scan(Path(root), query=query, changed_paths=changed_paths or [], intent=intent)
        out['called_through'] = 'operations_runtime'
        return out

    def doctor(self, root: str | Path, *, query: str = '', changed_paths: list[str] | None = None, intent: Dict[str, Any] | None = None) -> Dict[str, Any]:
        if not is_valid_operations_intent(intent):
            return _blocked('artifact.doctor')
        if not self._within_scope(Path(root), intent):
            out = _blocked('artifact.doctor')
            out['reason'] = 'requested_root_outside_operation_scope'
            return out
        out = self.adapter.doctor(Path(root), query=query, changed_paths=changed_paths or [], intent=intent)
        out['called_through'] = 'operations_runtime'
        return out

    def _within_scope(self, root: Path, intent: Dict[str, Any] | None) -> bool:
        plan = context_scope_plan(intent)
        allowed = [Path(p).resolve() for p in plan.get('allowed_roots') or []]
        if not allowed:
            return False
        target = root.resolve()
        return any(target == a or a in target.parents for a in allowed)


def create() -> ArtifactMatrixAPI:
    return ArtifactMatrixAPI()
