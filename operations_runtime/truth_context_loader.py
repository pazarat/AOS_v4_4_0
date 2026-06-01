from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List

from operations_runtime.operation_contract import ScopePlan, TruthContext


class TruthContextLoader:
    """Loads governing truth before layer fan-out.

    It is manifest/profile driven and project-neutral. It never names a fixture or
    embeds a project-specific example as runtime law.
    """

    AOS_REQUIRED = [
        'aos_identity/OPERATIONAL_IDENTITY.md',
        'aos_identity/SYSTEM_CONSTITUTION.md',
        'aos_identity/TRUTH_GROUNDED_RESPONSE_CONTRACT.md',
        'operations_runtime/OPERATIONS_RUNTIME_CONTRACT.yaml',
        'operations_runtime/LAYER_IDENTITY.md',
        'aos_capabilities/truth_runtime/TRUTH_RUNTIME_API.yaml',
        'aos_capabilities/truth_runtime/TRUTH_GOVERNANCE_LAWS.md',
        'aos_capabilities/goal_runtime/GOAL_RUNTIME_API.yaml',
        'aos_capabilities/file_intelligence/CAPABILITY_MANIFEST.yaml',
    ]
    PROJECT_REQUIRED = [
        '00_PROJECT_ENTRYPOINT.md',
        '01_PROJECT_CONTRACT.yaml',
        '02_PROJECT_TRUTH_INDEX.yaml',
        '99_PROJECT_MEMORY.yaml',
    ]
    WORKSHOP_REQUIRED = [
        'README.md',
    ]

    def __init__(self, paths: Any) -> None:
        self.paths = paths
        self.root = Path(paths.root).resolve()

    def load(self, scope_plan: ScopePlan) -> TruthContext:
        if scope_plan.truth_profile == 'aos_runtime_truth':
            required = self.AOS_REQUIRED
            base = self.root
            sources, missing = self._load_paths(base, required)
            policy = {
                'fixture_contamination': 'forbidden',
                'unsupported_claims': 'answer_with_limits_or_block',
                'truth_before_layers': True,
                'truth_after_merge': True,
            }
        elif scope_plan.truth_profile == 'workshop_truth':
            required = self.WORKSHOP_REQUIRED
            base = Path(scope_plan.primary_root)
            sources, missing = self._load_paths(base, required)
            policy = {'project_payload_contamination': 'forbidden_unless_application_requested'}
        else:
            required = self.PROJECT_REQUIRED
            base = Path(scope_plan.primary_root)
            sources, missing = self._load_paths(base, required)
            policy = {'project_local_truth_required': True, 'runtime_internals_hidden_unless_requested': True}
        status = 'ready' if not missing else 'partial'
        return TruthContext(
            operation_id=scope_plan.operation_id,
            profile=scope_plan.truth_profile,
            governing_sources=sources,
            required_truth=required,
            missing_required_truth=missing,
            active_project_role=scope_plan.active_project_role,
            status=status,
            policy=policy,
        )

    def _load_paths(self, base: Path, rels: List[str]) -> tuple[List[Dict[str, Any]], List[str]]:
        sources: List[Dict[str, Any]] = []
        missing: List[str] = []
        for rel in rels:
            path = (base / rel).resolve()
            if not self._inside(path, self.root) and not self._inside(path, base):
                missing.append(rel)
                continue
            if not path.exists():
                missing.append(rel)
                continue
            try:
                text = path.read_text(encoding='utf-8', errors='ignore')
            except Exception:
                text = ''
            sources.append({
                'id': self._source_id(rel),
                'path': rel,
                'exists': True,
                'size_bytes': path.stat().st_size,
                'sample': text[:1200],
                'role': self._role(rel),
            })
        return sources, missing

    def _inside(self, path: Path, root: Path) -> bool:
        try:
            path.relative_to(root)
            return True
        except ValueError:
            return False

    def _source_id(self, rel: str) -> str:
        return rel.lower().replace('/', '.').replace('_', '-').replace('.md', '').replace('.yaml', '')

    def _role(self, rel: str) -> str:
        low = rel.lower()
        if 'contract' in low or 'constitution' in low or 'governance' in low:
            return 'governing_contract'
        if 'identity' in low:
            return 'operating_identity'
        if 'api' in low or 'manifest' in low:
            return 'layer_api_or_manifest'
        if 'truth' in low:
            return 'truth_index_or_truth_law'
        return 'supporting_truth'
