from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List

from aos_capabilities.file_intelligence.file_matrix import FileMatrix


API_SURFACE = [
    'file.health',
    'file.preflight',
    'file.build_context',
    'file.validate_plan',
    'file.diagnose',
    'file.verify_after_write',
    'file.plan_repair',
    'file.doctor',
    'file.receipt',
]


def run(root: str | Path, query: str | None = None, changed_paths: List[str] | None = None, intent: Dict[str, Any] | None = None) -> Dict[str, Any]:
    return FileMatrix(Path(root)).scan(query=query, changed_paths=changed_paths, intent=intent)


class FileIntelligenceRuntime:
    """Stable adapter-level API exposed to the AOS port.

    It keeps the internal engines hidden behind high-level file.* operations.
    All methods are read-only except future patch application hooks, which must
    pass the same governance/receipt flow before writing.
    """

    def health(self, root: str | Path) -> Dict[str, Any]:
        root = Path(root)
        return {
            'status': 'healthy' if root.exists() else 'missing_root',
            'capability': 'file_intelligence',
            'runtime': 'artifact_governance_construction_runtime',
            'api_surface': API_SURFACE,
            'root': root.resolve().as_posix() if root.exists() else root.as_posix(),
        }

    def scan(self, root: str | Path, query: str | None = None, changed_paths: List[str] | None = None, intent: Dict[str, Any] | None = None) -> Dict[str, Any]:
        return run(root, query=query, changed_paths=changed_paths, intent=intent)

    def preflight(self, root: str | Path, query: str | None = None, changed_paths: List[str] | None = None, intent: Dict[str, Any] | None = None) -> Dict[str, Any]:
        report = self.scan(root, query=query, changed_paths=changed_paths, intent=intent)
        return {
            'operation': 'file.preflight',
            'decision': report.get('artifact_governance', {}).get('policy_decision', {}).get('decision'),
            'construction_gate': report.get('construction_runtime', {}).get('gate'),
            'diagnostics_summary': self._diag_summary(report),
            'receipt': report.get('receipt'),
        }

    def build_context(self, root: str | Path, query: str | None = None, changed_paths: List[str] | None = None, intent: Dict[str, Any] | None = None) -> Dict[str, Any]:
        report = self.scan(root, query=query, changed_paths=changed_paths, intent=intent)
        return {
            'operation': 'file.build_context',
            'context': report.get('construction_runtime', {}).get('context'),
            'generation_guidance': report.get('construction_runtime', {}).get('generation_guidance'),
            'search': report.get('search'),
            'content_knownness_map': report.get('content_knownness_map'),
            'receipt': report.get('receipt'),
        }

    def diagnose(self, root: str | Path, query: str | None = None, changed_paths: List[str] | None = None, intent: Dict[str, Any] | None = None) -> Dict[str, Any]:
        report = self.scan(root, query=query, changed_paths=changed_paths, intent=intent)
        return {
            'operation': 'file.diagnose',
            'diagnostics': report.get('diagnostics'),
            'governance': report.get('artifact_governance'),
            'receipt': report.get('receipt'),
        }

    def verify_after_write(self, root: str | Path, query: str | None = None, changed_paths: List[str] | None = None, intent: Dict[str, Any] | None = None) -> Dict[str, Any]:
        report = self.scan(root, query=query, changed_paths=changed_paths, intent=intent)
        return {
            'operation': 'file.verify_after_write',
            'verification': report.get('verification'),
            'diagnostics_summary': self._diag_summary(report),
            'receipt': report.get('receipt'),
        }

    def validate_plan(self, root: str | Path, query: str | None = None, changed_paths: List[str] | None = None, intent: Dict[str, Any] | None = None) -> Dict[str, Any]:
        return self.preflight(root, query=query, changed_paths=changed_paths, intent=intent)

    def plan_repair(self, root: str | Path, query: str | None = None, changed_paths: List[str] | None = None, intent: Dict[str, Any] | None = None) -> Dict[str, Any]:
        report = self.scan(root, query=query, changed_paths=changed_paths, intent=intent)
        issues = (report.get('diagnostics') or {}).get('issues', [])
        candidates = []
        for issue in issues[:100]:
            candidates.append({
                'path': issue.get('path'),
                'severity': issue.get('severity'),
                'code': issue.get('code'),
                'recommendation': issue.get('recommendation'),
                'requires_gate': True,
            })
        return {
            'operation': 'file.plan_repair',
            'mode': 'plan_only_no_write',
            'repair_candidates': candidates,
            'policy_decision': report.get('artifact_governance', {}).get('policy_decision'),
            'receipt': report.get('receipt'),
        }

    def doctor(self, root: str | Path, query: str | None = None, changed_paths: List[str] | None = None, intent: Dict[str, Any] | None = None) -> Dict[str, Any]:
        report = self.scan(root, query=query, changed_paths=changed_paths, intent=intent)
        return {
            'operation': 'file.doctor',
            'mode': 'read_only',
            'status': 'passed' if report.get('verification', {}).get('passed') else 'attention_required',
            'summary': report.get('summary'),
            'diagnostics': report.get('diagnostics'),
            'governance': report.get('artifact_governance'),
            'verification': report.get('verification'),
            'receipt': report.get('receipt'),
        }

    def receipt(self, root: str | Path, query: str | None = None, changed_paths: List[str] | None = None, intent: Dict[str, Any] | None = None) -> Dict[str, Any]:
        return {'operation': 'file.receipt', 'receipt': self.scan(root, query=query, changed_paths=changed_paths, intent=intent).get('receipt')}

    def _diag_summary(self, report: Dict[str, Any]) -> Dict[str, Any]:
        d = report.get('diagnostics') or {}
        return {
            'issue_count': d.get('issue_count', 0),
            'blocking_count': d.get('blocking_count', 0),
            'maturity_issue_count': d.get('maturity_issue_count', 0),
            'decision_hint': d.get('decision_hint'),
        }
