from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List


class OwnershipResolver:
    """Resolves likely owning artifacts for a write or concept."""

    OWNER_ROLES = {'local_project_truth', 'configuration_or_contract', 'documentation'}

    def resolve(self, records: List[Dict[str, Any]], concept: str = '', target_path: str = '') -> Dict[str, Any]:
        concept_l = (concept or '').lower()
        target_stem = Path(target_path or '').stem.lower()
        candidates: List[Dict[str, Any]] = []
        for rec in records:
            path = rec.get('path', '')
            text = (rec.get('sample') or '').lower()
            score = 0
            if rec.get('role') in self.OWNER_ROLES:
                score += 1
            if concept_l and (concept_l in path.lower() or concept_l in text):
                score += 4
            if target_stem and target_stem in path.lower():
                score += 3
            if 'manifest' in path.lower() or 'contract' in path.lower() or 'canon' in path.lower():
                score += 2
            if score:
                candidates.append({'path': path, 'score': score, 'role': rec.get('role'), 'surface': rec.get('surface')})
        candidates = sorted(candidates, key=lambda x: (-x['score'], x['path']))[:20]
        return {'concept': concept, 'target_path': target_path, 'candidates': candidates, 'resolved': candidates[0] if candidates else None}
