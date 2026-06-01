from __future__ import annotations

from collections import Counter
from pathlib import Path
from typing import Any, Dict, List

from aos_core.config import AOSPaths


class StrategyEngine:
    """Converts evidence and workshop method into candidate strategy."""

    def __init__(self, paths: AOSPaths):
        self.paths = paths

    def applicable_workshop_sources(self, request: str, surface: str) -> Dict[str, Any]:
        sources = []
        for p in sorted(self.paths.workshop_system.glob('*.md')):
            text = p.read_text(encoding='utf-8', errors='ignore')
            sources.append({'path': p.relative_to(self.paths.root).as_posix(), 'title': self._title(text, p.stem), 'words': len(text.split())})
        return {
            'role': 'general_truth_silent_method' if surface == 'active_project_payload' else 'visible_general_truth_when_requested',
            'rule': 'Workshop provides standards and maturity lenses; local truth specializes what applies.',
            'selected_sources': sources[:30],
            'not_every_standard_applies': True,
        }

    def maturity_findings(self, file_matrix: Dict[str, Any]) -> List[Dict[str, Any]]:
        findings = []
        for r in file_matrix.get('records', []):
            if r.get('surface') != 'project_payload':
                continue
            state = r.get('content_state')
            role = r.get('role')
            concepts = r.get('concepts') or {}
            if state in {'empty', 'thin'}:
                findings.append({'path': r['path'], 'maturity': state, 'reason': 'payload file exists but has little/no usable content'})
            elif role in {'documentation', 'configuration_or_contract'} and concepts and len(r.get('readiness_hits') or []) < 3:
                findings.append({'path': r['path'], 'maturity': 'documented_but_not_execution_ready', 'reason': 'concept is documented but lacks enough readiness dimensions'})
        return findings[:80]

    def delivery_strategy(self, intent: Dict[str, Any], file_matrix: Dict[str, Any], active_state: Dict[str, Any]) -> Dict[str, Any]:
        condition = file_matrix.get('project_condition', 'UNKNOWN')
        mode = intent.get('intent_type')
        if active_state.get('state') == 'no_project_loaded' or condition == 'EMPTY_NEW_PROJECT':
            posture = 'project_formation'
            next_step = 'collect_minimum_project_truth_before_local_standards_or_execution'
        elif active_state.get('state') in {'unformed_or_scattered_slot', 'multi_project_ambiguity'}:
            posture = 'project_discovery_or_recovery'
            next_step = 'resolve_project_root_or_create_baseline_truth_map'
        elif mode in {'repair', 'refactor', 'implement'}:
            posture = 'governed_change_candidate'
            next_step = 'owner_impact_duplicate_conflict_patch_gate_validation'
        else:
            posture = 'assessment_or_planning'
            next_step = 'answer_with_claim_grades_and_maturity_findings'
        return {
            'posture': posture,
            'next_step': next_step,
            'forbidden': [
                'bypass_operation_packet',
                'surface_aos_as_project',
                'treat_workshop_standard_as_local_truth_without_specialization',
                'treat_documented_as_execution_ready_without_maturity',
                'upgrade_candidate_to_decision_without_evidence',
            ],
        }

    def _title(self, text: str, fallback: str) -> str:
        for line in text.splitlines():
            if line.startswith('#'):
                return line.lstrip('#').strip()
        return fallback
