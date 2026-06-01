from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any, Dict, Optional


SEVERITY_ORDER = {
    'info': 0,
    'warn': 1,
    'mature': 2,
    'block': 3,
    'critical': 4,
}


@dataclass(frozen=True)
class DiagnosticIssue:
    """Normalized diagnostic issue used by every file-intelligence engine.

    Diagnostics are evidence by default. They never mutate files and never
    authorize fixes. The kernel/governance layers decide what to do with them.
    """

    severity: str
    category: str
    code: str
    message: str
    path: Optional[str] = None
    line: Optional[int] = None
    evidence: Dict[str, Any] = field(default_factory=dict)
    recommendation: str = ''
    owner: str = 'file_intelligence'

    def to_dict(self) -> Dict[str, Any]:
        data = asdict(self)
        data['rank'] = SEVERITY_ORDER.get(self.severity, 0)
        return data


def normalize_issue(issue: Dict[str, Any] | DiagnosticIssue) -> Dict[str, Any]:
    if isinstance(issue, DiagnosticIssue):
        return issue.to_dict()
    normalized = dict(issue)
    normalized.setdefault('severity', 'warn')
    normalized.setdefault('category', 'general')
    normalized.setdefault('code', 'general.issue')
    normalized.setdefault('message', normalized.get('code', 'issue'))
    normalized.setdefault('evidence', {})
    normalized.setdefault('recommendation', '')
    normalized.setdefault('owner', 'file_intelligence')
    normalized['rank'] = SEVERITY_ORDER.get(str(normalized.get('severity')), 0)
    return normalized
