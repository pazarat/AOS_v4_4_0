from __future__ import annotations

from pathlib import Path
from typing import Any, List

from operations_runtime.operation_contract import ScopePlan


class ScopePlanner:
    """Builds hard scope plans from resolved surface, not from curiosity or folder traversal."""

    AOS_INCLUDE = [
        'operations_runtime',
        'aos_identity',
        'aos_core/intent',
        'aos_core/surface',
        'aos_core/workspace',
        'aos_capabilities/truth_runtime',
        'aos_capabilities/goal_runtime',
        'aos_capabilities/file_intelligence',
        'tests',
    ]
    AOS_EXCLUDE = [
        'workshop/active_project/PROJECT',
        'runtime_state',
        'reports',
        'audit',
        '__pycache__',
    ]

    def __init__(self, paths: Any) -> None:
        self.paths = paths
        self.root = Path(paths.root).resolve()

    def plan(self, envelope: Any) -> ScopePlan:
        surface = getattr(envelope, 'surface', None) or 'active_project_payload'
        op_id = getattr(envelope, 'operation_id', 'unknown_operation')
        if surface == 'aos_environment':
            include_roots = [self._p(rel).as_posix() for rel in self.AOS_INCLUDE if self._p(rel).exists()]
            primary = self._p('operations_runtime')
            return ScopePlan(
                operation_id=op_id,
                surface=surface,
                primary_scope='aos_runtime_architecture',
                primary_root=primary.as_posix(),
                include_roots=include_roots,
                exclude_roots=[self._p(rel).as_posix() for rel in self.AOS_EXCLUDE],
                allowed_roots=include_roots,
                active_project_role='fixture_only_excluded_from_runtime_truth',
                fixture_policy='active_project_payload_may_only_be_used_for_behavior_reproduction_when_explicitly_requested',
                truth_profile='aos_runtime_truth',
                reason='The request targets the agent/runtime/operations kernel; project payload is not primary truth.',
            )
        if surface == 'workshop_general_truth':
            root = Path(self.paths.workshop_system).resolve()
            return ScopePlan(
                operation_id=op_id,
                surface=surface,
                primary_scope='workshop_general_truth',
                primary_root=root.as_posix(),
                include_roots=[root.as_posix()],
                exclude_roots=[Path(self.paths.project_upload).resolve().as_posix()],
                allowed_roots=[root.as_posix()],
                active_project_role='excluded_unless_user_requests_project_application',
                fixture_policy='project_payload_not_loaded_for_workshop_method_questions',
                truth_profile='workshop_truth',
                reason='The request targets general workshop standards, not a concrete project payload.',
            )
        project_root = Path((getattr(envelope, 'active_project_state', None) or {}).get('project_root') or self.paths.project_upload).resolve()
        return ScopePlan(
            operation_id=op_id,
            surface='active_project_payload',
            primary_scope='active_project_payload',
            primary_root=project_root.as_posix(),
            include_roots=[project_root.as_posix()],
            exclude_roots=[self._p('operations_runtime').as_posix(), self._p('aos_capabilities').as_posix(), self._p('aos_core').as_posix()],
            allowed_roots=[project_root.as_posix()],
            active_project_role='primary_truth',
            fixture_policy='not_applicable',
            truth_profile='active_project_truth',
            reason='The request targets the active project payload.',
        )

    def _p(self, rel: str) -> Path:
        return (self.root / rel).resolve()
