from __future__ import annotations

import re
from pathlib import PurePosixPath
from typing import Any, Dict, List, Set


class ArtifactTruthSemantics:
    """Interprets artifact value and meaning beyond file size/name.

    This is the layer that distinguishes an empty construction target from a
    broken declared path, and a high-value small file from a bulky but weak file.
    """

    PATH_RE = re.compile(r"[`'\"]?([A-Za-z0-9_./\-]+\.(?:md|yaml|yml|json|py|ts|tsx|js|jsx|sql|cs|xml|toml))[`'\"]?")
    HIGH_VALUE_MARKERS = {
        'contract': 6,
        'truth_index': 6,
        'constitution': 6,
        'layer_identity': 5,
        'identity': 4,
        'canon': 5,
        'standard': 5,
        'governance': 5,
        'decision': 5,
        'manifest': 4,
        'api': 3,
        'schema': 3,
        'readme': 2,
        'entrypoint': 5,
        'memory': 4,
    }

    def analyze(self, matrix: Dict[str, Any]) -> Dict[str, Any]:
        records = matrix.get('records') or []
        paths: Set[str] = {self._norm(r.get('path') or '') for r in records if r.get('path')}
        by_path = {self._norm(r.get('path') or ''): r for r in records if r.get('path')}
        empty_targets: List[Dict[str, Any]] = []
        high_value: List[Dict[str, Any]] = []
        declared_missing: List[Dict[str, Any]] = []
        declared_edges: List[Dict[str, Any]] = []

        for r in records:
            p = self._norm(r.get('path') or '')
            if not p or p.endswith('/.keep') or p.endswith('__init__.py'):
                continue
            value = self.value_score(r)
            if value['score']:
                high_value.append({**value, 'path': p, 'size_bytes': r.get('size_bytes'), 'role': r.get('role'), 'surface': r.get('surface')})
            state = r.get('content_state')
            if state == 'empty' and self._is_declared_target_path(p, r):
                empty_targets.append({
                    'path': p,
                    'meaning': 'empty_declared_construction_target',
                    'truth_status': 'declared_target_not_executable_truth',
                    'recommended_action': 'mature_owner_artifact_before_using_for_execution',
                    'value_score': value['score'],
                    'reason': 'An empty governed artifact reserves a planned construction path. It is a target to mature, not a basis for invented logic.',
                })
            text = r.get('sample_full') or r.get('sample') or ''
            for candidate in self._declared_paths(text):
                resolved = self._resolve_declared_path(p, candidate)
                if not resolved or resolved in paths:
                    if resolved in paths:
                        declared_edges.append({'from': p, 'to': resolved, 'status': 'declared_and_present'})
                    continue
                # Avoid counting common external docs URLs/fragments or package-like names.
                if candidate.startswith(('http', 'www.')) or '/site-packages/' in candidate:
                    continue
                if self._looks_project_local(resolved, paths):
                    declared_missing.append({
                        'declared_in': p,
                        'declared_path': candidate,
                        'normalized_path': resolved,
                        'truth_status': 'declared_but_missing_artifact',
                        'severity': 'mature',
                        'reason': 'A governed artifact references another artifact that is not present. This is a broken truth promise, not an empty target.',
                    })

        return {
            'empty_declared_targets': empty_targets[:200],
            'empty_declared_target_count': len(empty_targets),
            'declared_missing_artifacts': self._dedupe_missing(declared_missing)[:200],
            'declared_missing_artifact_count': len(self._dedupe_missing(declared_missing)),
            'declared_edges': declared_edges[:500],
            'high_value_sources': sorted(high_value, key=lambda x: (-x['score'], x['path']))[:100],
            'rule': 'truth_value_is_provenance_intent_role_and_relationship_not_file_size',
        }

    def value_score(self, record: Dict[str, Any]) -> Dict[str, Any]:
        path = (record.get('path') or '').lower()
        role = (record.get('role') or '').lower()
        sample = (record.get('sample') or '').lower()[:2000]
        score = 0
        reasons: List[str] = []
        for marker, weight in self.HIGH_VALUE_MARKERS.items():
            if marker in path or marker in role:
                score += weight
                reasons.append(marker)
        if any(x in sample for x in ['must', 'forbidden', 'law', 'قاعدة', 'ممنوع', 'يجب', 'حقيقة', 'حوكمة', 'truth_priority']):
            score += 2
            reasons.append('governing_language')
        if record.get('size_bytes', 0) == 0 and score:
            reasons.append('empty_but_declared_governed_target')
        return {'score': score, 'reasons': sorted(set(reasons))}

    def _declared_paths(self, text: str) -> List[str]:
        if not text:
            return []
        out: List[str] = []
        for match in self.PATH_RE.findall(text):
            c = match.strip().strip('`"\'')
            if len(c) > 220 or c.startswith('.'):
                continue
            if c.count('/') > 12:
                continue
            out.append(c)
        return out

    def _resolve_declared_path(self, current_path: str, candidate: str) -> str:
        c = candidate.replace('\\', '/').strip('/')
        if not c or c.startswith('#'):
            return ''
        if c.startswith('/'):
            return self._norm(c)
        # Try project-relative first when candidate starts with known top-level numbers/folders.
        top_prefixes = ('00_', '01_', '02_', '03_', '04_', '05_', '06_', '99_', 'aos_', 'workshop/', 'runtime_state/', 'schemas/')
        if c.startswith(top_prefixes):
            return self._norm(c)
        base = str(PurePosixPath(current_path).parent)
        return self._norm(str(PurePosixPath(base) / c))

    def _looks_project_local(self, resolved: str, existing_paths: Set[str]) -> bool:
        if not resolved or resolved.startswith(('http:', 'https:')):
            return False
        # If it shares top-level with existing project payload files, it is likely local.
        top = resolved.split('/')[0]
        return bool(top and any(p.split('/')[0] == top for p in existing_paths))

    def _is_declared_target_path(self, path: str, record: Dict[str, Any]) -> bool:
        low = path.lower()
        if record.get('role') in {'documentation', 'configuration_or_contract', 'local_project_truth'}:
            return True
        return any(x in low for x in ['prd', 'readme', 'contract', 'truth', 'standard', 'canon', 'manifest', 'identity'])

    def _norm(self, p: str) -> str:
        return str(PurePosixPath(str(p).replace('\\', '/'))).strip('./')

    def _dedupe_missing(self, items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        seen = set()
        out = []
        for item in items:
            key = (item.get('declared_in'), item.get('normalized_path'))
            if key in seen:
                continue
            seen.add(key)
            out.append(item)
        return out
