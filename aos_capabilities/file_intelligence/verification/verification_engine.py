from __future__ import annotations

from typing import Any, Dict


class VerificationEngine:
    """Post-scan/post-write verification summary. It is read-only."""

    def verify(self, diagnostics: Dict[str, Any], governance: Dict[str, Any]) -> Dict[str, Any]:
        passed = diagnostics.get('blocking_count', 0) == 0 and governance.get('decision') in {'ALLOW', 'WARN'}
        return {
            'mode': 'read_only_verification',
            'passed': passed,
            'blocking_count': diagnostics.get('blocking_count', 0),
            'maturity_issue_count': diagnostics.get('maturity_issue_count', 0),
            'governance_decision': governance.get('decision'),
            'required_next_steps': governance.get('required_next_steps', []),
        }
