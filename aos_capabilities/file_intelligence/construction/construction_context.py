from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List


class ConstructionContextBuilder:
    """Builds pre-write context and guidance inputs without mutating files."""

    def build(self, records: List[Dict[str, Any]], query: str = '', intent: Dict[str, Any] | None = None, changed_paths: List[str] | None = None) -> Dict[str, Any]:
        intent = intent or {}
        changed_paths = changed_paths or []
        requested = self._extract_targets(query, intent, changed_paths)
        owners = self._owner_candidates(records, query, requested)
        existing_paths = {r.get('path') for r in records}
        return {
            'mode': 'pre_write_context',
            'query': query,
            'requested_targets': requested,
            'owner_candidates': owners[:20],
            'existing_target_status': [{'path': p, 'exists': p in existing_paths} for p in requested],
            'surface_hint': intent.get('surface') or 'unknown',
            'risk_level': intent.get('risk_level') or 'unknown',
            'may_modify_files': bool(intent.get('may_modify_files')),
            'generation_guidance': self._guidance(query, intent, requested),
        }

    def _extract_targets(self, query: str, intent: Dict[str, Any], changed_paths: List[str]) -> List[str]:
        targets: List[str] = []
        for p in changed_paths:
            if p and p not in targets:
                targets.append(p.replace('\\', '/'))
        for key in ('target_path', 'entrypoint', 'file', 'path'):
            value = intent.get(key)
            if isinstance(value, str) and ('/' in value or '.' in Path(value).name):
                normalized = value.replace('\\', '/')
                if normalized not in targets:
                    targets.append(normalized)
        return targets[:50]

    def _owner_candidates(self, records: List[Dict[str, Any]], query: str, targets: List[str]) -> List[Dict[str, Any]]:
        q = (query or '').lower()
        candidates: List[Dict[str, Any]] = []
        for r in records:
            score = 0
            path = r.get('path', '')
            if q and q in (r.get('sample') or '').lower():
                score += 4
            if q and q in path.lower():
                score += 3
            for target in targets:
                if Path(target).stem and Path(target).stem.lower() in path.lower():
                    score += 3
            if r.get('role') in {'local_project_truth', 'configuration_or_contract', 'documentation'}:
                score += 1
            if score:
                candidates.append({'path': path, 'score': score, 'role': r.get('role'), 'surface': r.get('surface')})
        return sorted(candidates, key=lambda x: (-x['score'], x['path']))

    def _guidance(self, query: str, intent: Dict[str, Any], targets: List[str]) -> Dict[str, Any]:
        return {
            'required_before_generation': [
                'resolve_owner_artifact',
                'check_duplicate_or_existing_target',
                'load_relevant_canon_or_truth_contract',
                'classify whether operation is create/update/repair',
            ],
            'forbidden_generation_shortcuts': [
                'direct write without preflight',
                'inventing local standards when owner truth is incomplete',
                'creating new artifact when existing owner should be updated',
                'changing generated/cache files as source truth',
            ],
            'target_paths': targets,
            'draft_policy': 'drafts may be proposed; production-oriented writes require validation and receipt',
        }
