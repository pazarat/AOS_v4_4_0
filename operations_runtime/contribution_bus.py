from __future__ import annotations

from typing import Any, Dict, List


class ContributionBus:
    """Normalizes layer outputs into typed contributions."""

    REQUIRED = {'layer', 'mode', 'value', 'evidence', 'risks', 'next_needs', 'ignored_noise'}

    def normalize(self, contribution: Dict[str, Any]) -> Dict[str, Any]:
        out = dict(contribution or {})
        out.setdefault('layer', 'unknown')
        out.setdefault('mode', 'unspecified')
        out.setdefault('value', '')
        out.setdefault('evidence', [])
        out.setdefault('risks', [])
        out.setdefault('next_needs', [])
        out.setdefault('ignored_noise', [])
        out.setdefault('confidence', 'derived')
        return out

    def merge(self, contributions: List[Dict[str, Any]]) -> Dict[str, Any]:
        by_layer = {c.get('layer'): self.normalize(c) for c in contributions}
        next_needs: List[str] = []
        risks: List[Dict[str, Any]] = []
        for c in by_layer.values():
            for need in c.get('next_needs') or []:
                if need not in next_needs:
                    next_needs.append(need)
            risks.extend(c.get('risks') or [])
        return {'by_layer': by_layer, 'next_needs': next_needs, 'risks': risks[:20], 'contribution_count': len(contributions)}
