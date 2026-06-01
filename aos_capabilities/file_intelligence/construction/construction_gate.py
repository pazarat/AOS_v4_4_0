from __future__ import annotations

from typing import Any, Dict, List

from .ownership_resolver import OwnershipResolver
from .placement_resolver import PlacementResolver
from .generation_guidance import GenerationGuidance


class ConstructionGate:
    """Pre-write gate with flexible constitution semantics.

    Decisions:
      ALLOW  - no known blockers; use standard gates.
      WARN   - may proceed with caution.
      MATURE - owner truth or local standard is incomplete; repair/accept risk first.
      BLOCK  - unsafe or invalid.
    """

    def assess(self, records: List[Dict[str, Any]], query: str = '', intent: Dict[str, Any] | None = None, changed_paths: List[str] | None = None, diagnostics: Dict[str, Any] | None = None) -> Dict[str, Any]:
        intent = intent or {}
        changed_paths = changed_paths or []
        diagnostics = diagnostics or {}
        targets = self._targets(intent, changed_paths)
        placement = PlacementResolver().assess(targets)
        owner = OwnershipResolver().resolve(records, concept=query, target_path=targets[0] if targets else '')
        blockers: List[str] = []
        maturity: List[str] = []
        warnings: List[str] = []
        if placement.get('status') == 'blocked':
            blockers.append('invalid_or_generated_target_path')
        if not intent.get('may_modify_files') and targets:
            maturity.append('intent_not_confirmed_as_write_capable')
        if targets and not owner.get('resolved'):
            maturity.append('owner_truth_not_resolved')
        if diagnostics.get('blocking_count', 0):
            blockers.append('blocking_diagnostics_present')
        if diagnostics.get('maturity_issue_count', 0):
            maturity.append('maturity_diagnostics_present')
        if not targets and intent.get('may_modify_files'):
            warnings.append('write_intent_without_explicit_target_paths')
        decision = 'ALLOW'
        if blockers:
            decision = 'BLOCK'
        elif maturity:
            decision = 'MATURE'
        elif warnings:
            decision = 'WARN'
        return {
            'decision': decision,
            'blockers': blockers,
            'maturity_requirements': maturity,
            'warnings': warnings,
            'target_paths': targets,
            'placement': placement,
            'owner_resolution': owner,
            'generation_guidance': GenerationGuidance().build(targets, owner),
        }

    def _targets(self, intent: Dict[str, Any], changed_paths: List[str]) -> List[str]:
        targets: List[str] = []
        for p in changed_paths:
            if p and p not in targets:
                targets.append(p.replace('\\', '/'))
        for key in ('target_path', 'entrypoint', 'file', 'path'):
            value = intent.get(key)
            if isinstance(value, str) and value and value not in targets:
                targets.append(value.replace('\\', '/'))
        return targets[:50]
