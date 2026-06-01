from __future__ import annotations

from typing import Any, Dict


class EvidencePacketBuilder:
    def build(self, *, file_count: int, diagnostics: Dict[str, Any], construction_gate: Dict[str, Any], governance: Dict[str, Any]) -> Dict[str, Any]:
        return {
            'file_count': file_count,
            'diagnostics': {
                'issue_count': diagnostics.get('issue_count', 0),
                'blocking_count': diagnostics.get('blocking_count', 0),
                'maturity_issue_count': diagnostics.get('maturity_issue_count', 0),
                'decision_hint': diagnostics.get('decision_hint'),
            },
            'construction': {
                'decision': construction_gate.get('decision'),
                'target_paths': construction_gate.get('target_paths', []),
            },
            'governance': {
                'decision': governance.get('decision'),
                'blockers': governance.get('blockers', []),
                'required_next_steps': governance.get('required_next_steps', []),
            },
        }
