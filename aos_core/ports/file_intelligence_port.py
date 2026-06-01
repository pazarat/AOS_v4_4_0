from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List, Optional

from aos_capabilities.file_intelligence.adapter import FileIntelligenceRuntime, run as run_file_intelligence
from operations_runtime.context import is_valid_operations_intent


class FileIntelligencePort:
    """Stable-spine port for artifact governance and file evidence.

    The kernel uses this port instead of importing capability internals.
    File intelligence returns evidence/navigation/governance artifacts only; it
    never declares final project truth or silently performs production writes.
    """

    capability_id = 'file_intelligence'

    def __init__(self) -> None:
        self.runtime = FileIntelligenceRuntime()

    def _guard(self, operation: str, intent: Optional[Dict[str, Any]]) -> Dict[str, Any] | None:
        if is_valid_operations_intent(intent):
            return None
        return {
            'capability': self.capability_id,
            'operation': operation,
            'status': 'blocked',
            'direct_layer_access': 'blocked_by_operations_runtime_context_guard',
            'authority': 'denied_without_operations_context',
            'reason': 'File Intelligence can be invoked only through Operations Runtime Kernel for runtime flows.',
            'project_condition': 'UNSCANNED_DIRECT_ACCESS_BLOCKED',
            'file_count': 0,
            'summary': {'project_condition': 'UNSCANNED_DIRECT_ACCESS_BLOCKED'},
            'records': [],
            'diagnostics': {'mode': 'blocked', 'issue_count': 0, 'blocking_count': 1, 'maturity_issue_count': 0},
        }

    def inspect(self, root: Path, query: Optional[str] = None, changed_paths: Optional[List[str]] = None, intent: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        blocked = self._guard('file.inspect', intent)
        if blocked is not None:
            return blocked
        report = run_file_intelligence(root, query=query, changed_paths=changed_paths or [], intent=intent)
        report['authority'] = 'evidence_only'
        report['authority_scope'] = 'evidence_and_governance_hints_only'
        report['spine_rule'] = 'capabilities_produce_evidence_and_governance_hints_core_owns_final_decision'
        return report

    def health(self, root: Path) -> Dict[str, Any]:
        return self.runtime.health(root)

    def preflight(self, root: Path, query: Optional[str] = None, changed_paths: Optional[List[str]] = None, intent: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        blocked = self._guard('file.preflight', intent)
        if blocked is not None:
            return blocked
        return self.runtime.preflight(root, query=query, changed_paths=changed_paths or [], intent=intent)

    def build_context(self, root: Path, query: Optional[str] = None, changed_paths: Optional[List[str]] = None, intent: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        blocked = self._guard('file.build_context', intent)
        if blocked is not None:
            return blocked
        return self.runtime.build_context(root, query=query, changed_paths=changed_paths or [], intent=intent)

    def validate_plan(self, root: Path, query: Optional[str] = None, changed_paths: Optional[List[str]] = None, intent: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        blocked = self._guard('file.validate_plan', intent)
        if blocked is not None:
            return blocked
        return self.runtime.validate_plan(root, query=query, changed_paths=changed_paths or [], intent=intent)

    def diagnose(self, root: Path, query: Optional[str] = None, changed_paths: Optional[List[str]] = None, intent: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        blocked = self._guard('file.diagnose', intent)
        if blocked is not None:
            return blocked
        return self.runtime.diagnose(root, query=query, changed_paths=changed_paths or [], intent=intent)

    def verify_after_write(self, root: Path, query: Optional[str] = None, changed_paths: Optional[List[str]] = None, intent: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        blocked = self._guard('file.verify_after_write', intent)
        if blocked is not None:
            return blocked
        return self.runtime.verify_after_write(root, query=query, changed_paths=changed_paths or [], intent=intent)

    def plan_repair(self, root: Path, query: Optional[str] = None, changed_paths: Optional[List[str]] = None, intent: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        blocked = self._guard('file.plan_repair', intent)
        if blocked is not None:
            return blocked
        return self.runtime.plan_repair(root, query=query, changed_paths=changed_paths or [], intent=intent)

    def doctor(self, root: Path, query: Optional[str] = None, changed_paths: Optional[List[str]] = None, intent: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        blocked = self._guard('file.doctor', intent)
        if blocked is not None:
            return blocked
        return self.runtime.doctor(root, query=query, changed_paths=changed_paths or [], intent=intent)

    def receipt(self, root: Path, query: Optional[str] = None, changed_paths: Optional[List[str]] = None, intent: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        blocked = self._guard('file.receipt', intent)
        if blocked is not None:
            return blocked
        return self.runtime.receipt(root, query=query, changed_paths=changed_paths or [], intent=intent)
