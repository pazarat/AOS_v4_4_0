from __future__ import annotations

from typing import Any, Dict, List


class PlanningSolutionEngine:
    """Builds scope-specific operation packets; does not execute side effects."""

    def claim_ledger(self, packet: Dict[str, Any]) -> List[Dict[str, Any]]:
        ledger: List[Dict[str, Any]] = []
        scope = packet['intent']['surface']
        active = packet['scope']['active_project_state']
        fm = packet['file_matrix']

        def add(claim: str, grade: str, evidence=None, missing=None, blocked=None, allowed='state as graded'):
            ledger.append({'claim': claim, 'grade': grade, 'evidence': evidence or [], 'missing_for_upgrade': missing or [], 'blocked_surface': blocked or [], 'allowed_surface': allowed})

        add('AOS runtime is not the user project', 'confirmed', ['aos_identity/OPERATIONAL_IDENTITY.md'])
        add('Workshop is general truth and standards, not project payload', 'confirmed', ['workshop/_workshop_system/00_WORKSHOP_MANIFEST.md'])
        add('active project slot is not the project; PROJECT is the current-project payload gate', 'confirmed', [active.get('upload_gate') or active.get('slot')])
        if scope == 'active_project_payload':
            if active.get('state') == 'single_project_detected':
                add('real project root detected inside PROJECT gate', 'confirmed', [active.get('project_root')])
            elif active.get('state') == 'no_project_loaded':
                add('no current project is loaded in PROJECT', 'confirmed', [active.get('upload_gate')], allowed='project formation or upload mode')
            else:
                add('active project upload payload is not resolved', 'blocked', active.get('candidates', []), ['truth-marker project root or formation baseline inside PROJECT'], ['do not assess AOS/workshop as the user project'])
        if fm.get('project_condition'):
            add('project/file condition classified from current payload evidence', 'evidence_supported', [fm.get('project_condition')])
        weak = packet.get('maturity', {}).get('findings', [])
        if weak:
            add('some documented areas are incomplete or not execution-ready', 'confirmed', [x['path'] for x in weak[:12]])
        if packet['intent'].get('may_modify_files'):
            add('requested change requires governance before mutation', 'confirmed', packet['intent'].get('truth_requirements', []), ['policy approval, patch gate, validation'])
        return ledger
