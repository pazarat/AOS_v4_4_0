from __future__ import annotations

from collections import Counter
from typing import Any, Dict, List

from .architecture_diagnostics import ArchitectureDiagnostics
from .code_diagnostics import CodeDiagnostics
from .contract_diagnostics import ContractDiagnostics
from .issue_model import DiagnosticIssue, normalize_issue
from .text_diagnostics import TextDiagnostics


class DiagnosticEngine:
    """Composes all read-only diagnostic engines into one stable report."""

    def run(self, records: List[Dict[str, Any]], context: Dict[str, Any] | None = None) -> Dict[str, Any]:
        context = context or {}
        raw: List[DiagnosticIssue | Dict[str, Any]] = []
        raw.extend(TextDiagnostics().scan(records))
        raw.extend(CodeDiagnostics().scan(records, context.get('graphs') or {}))
        raw.extend(ContractDiagnostics().scan(records))
        raw.extend(ArchitectureDiagnostics().scan(records, context.get('graphs') or {}))
        raw.extend(self._duplicate_issues(context.get('duplicate_scan') or {}))
        raw.extend(self._conflict_issues(context.get('conflict_scan') or {}))
        issues = sorted((normalize_issue(x) for x in raw), key=lambda x: (-x.get('rank', 0), x.get('path') or '', x.get('code') or ''))
        counts = Counter(i['severity'] for i in issues)
        by_category = Counter(i['category'] for i in issues)
        blocking = [i for i in issues if i.get('severity') in {'block', 'critical'}]
        mature = [i for i in issues if i.get('severity') == 'mature']
        return {
            'mode': 'read_only',
            'issue_count': len(issues),
            'blocking_count': len(blocking),
            'maturity_issue_count': len(mature),
            'counts_by_severity': dict(counts),
            'counts_by_category': dict(by_category),
            'issues': issues[:500],
            'truncated': len(issues) > 500,
            'decision_hint': self._decision_hint(blocking, mature),
        }

    def _duplicate_issues(self, duplicate_scan: Dict[str, Any]) -> List[DiagnosticIssue]:
        issues: List[DiagnosticIssue] = []
        if duplicate_scan.get('exact_duplicate_count', 0):
            issues.append(DiagnosticIssue(
                severity='mature',
                category='duplication',
                code='duplication.exact_duplicates',
                message='Exact duplicate artifacts detected.',
                evidence={'exact_duplicate_count': duplicate_scan.get('exact_duplicate_count'), 'examples': duplicate_scan.get('exact_duplicates', [])[:5]},
                recommendation='Resolve ownership before creating or modifying related artifacts.',
            ))
        if duplicate_scan.get('semantic_duplicate_count', 0):
            issues.append(DiagnosticIssue(
                severity='warn',
                category='duplication',
                code='duplication.semantic_duplicates',
                message='Semantic duplicate artifacts detected.',
                evidence={'semantic_duplicate_count': duplicate_scan.get('semantic_duplicate_count'), 'examples': duplicate_scan.get('semantic_duplicates', [])[:5]},
                recommendation='Check whether the concept has multiple owners or needs consolidation.',
            ))
        return issues

    def _conflict_issues(self, conflict_scan: Dict[str, Any]) -> List[DiagnosticIssue]:
        count = conflict_scan.get('conflict_count', 0)
        if not count:
            return []
        return [DiagnosticIssue(
            severity='mature',
            category='contract',
            code='contract.conflicts_detected',
            message='Potential conflicts detected by the file intelligence conflict scanner.',
            evidence={'conflict_count': count, 'examples': conflict_scan.get('conflicts', [])[:5]},
            recommendation='Resolve contract conflicts before execution that depends on these artifacts.',
        )]

    def _decision_hint(self, blocking: List[Dict[str, Any]], mature: List[Dict[str, Any]]) -> str:
        if blocking:
            return 'BLOCK_UNTIL_REPAIRED'
        if mature:
            return 'MATURE_TRUTH_OR_ACCEPT_TEMPORARY_RISK'
        return 'ALLOW_WITH_STANDARD_GATES'
