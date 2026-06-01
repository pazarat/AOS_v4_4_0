from __future__ import annotations

import re
from typing import Any, Dict, List

from .issue_model import DiagnosticIssue


class TextDiagnostics:
    """Read-only diagnostics for natural-language and documentation files."""

    VAGUE_TERMS = {
        'stuff', 'things', 'etc', 'misc', 'various', 'simple', 'easy',
        'أشياء', 'الخ', 'إلخ', 'بسيط', 'سهل', 'متفرقات'
    }

    def scan(self, records: List[Dict[str, Any]]) -> List[DiagnosticIssue]:
        issues: List[DiagnosticIssue] = []
        for rec in records:
            if not rec.get('is_text'):
                continue
            path = rec.get('path')
            text = rec.get('sample_full') or rec.get('sample') or ''
            role = rec.get('role')
            state = rec.get('content_state')
            if state == 'empty' and role in {'documentation', 'configuration_or_contract'}:
                issues.append(DiagnosticIssue(
                    severity='mature',
                    category='truth',
                    code='truth.empty_declared_target',
                    message='Empty governed artifact is a declared construction target, not a completed truth.',
                    path=path,
                    evidence={'role': role, 'content_state': state, 'size_bytes': rec.get('size_bytes')},
                    recommendation='Keep it visible as a target to mature; do not ignore it and do not invent its missing logic during execution.',
                ))
            elif state == 'thin' and role in {'documentation', 'configuration_or_contract'}:
                issues.append(DiagnosticIssue(
                    severity='mature' if role == 'documentation' else 'warn',
                    category='truth',
                    code='truth.thin_declared_reference',
                    message='Governed artifact exists but is too thin to carry execution truth reliably.',
                    path=path,
                    evidence={'role': role, 'content_state': state, 'size_bytes': rec.get('size_bytes')},
                    recommendation='Mature the owning artifact or classify it as incomplete truth before production-oriented execution.',
                ))
            if role in {'documentation', 'configuration_or_contract', 'local_project_truth'}:
                for hit in rec.get('placeholder_hits') or []:
                    issues.append(DiagnosticIssue(
                        severity='mature',
                        category='text',
                        code='text.placeholder_hit',
                        message='Placeholder/TODO language found in a governed artifact.',
                        path=path,
                        evidence={'placeholder': hit},
                        recommendation='Resolve the placeholder or mark the artifact as incomplete truth with an owner and repair path.',
                    ))
            self._repetition(path, text, issues)
            self._vague_terms(path, text, issues)
        return issues

    def _repetition(self, path: str, text: str, issues: List[DiagnosticIssue]) -> None:
        lines = [re.sub(r'\s+', ' ', x.strip()) for x in text.splitlines() if x.strip()]
        seen: Dict[str, int] = {}
        for idx, line in enumerate(lines, start=1):
            if len(line) < 35:
                continue
            key = line.lower()
            seen[key] = seen.get(key, 0) + 1
            if seen[key] == 2:
                issues.append(DiagnosticIssue(
                    severity='warn',
                    category='text',
                    code='text.duplicate_line',
                    message='Repeated long line suggests duplicate wording or copy/paste drift.',
                    path=path,
                    line=idx,
                    evidence={'line_sample': line[:180]},
                    recommendation='Verify whether the repetition is intentional or should be consolidated.',
                ))

    def _vague_terms(self, path: str, text: str, issues: List[DiagnosticIssue]) -> None:
        low = text.lower()
        hits = sorted({term for term in self.VAGUE_TERMS if term in low})
        if hits and len(text) > 200:
            issues.append(DiagnosticIssue(
                severity='info',
                category='text',
                code='text.vague_terms',
                message='Vague terms found; they may reduce construction precision if used in standards/contracts.',
                path=path,
                evidence={'terms': hits[:20]},
                recommendation='Prefer explicit owners, scopes, allowed behaviors, and forbidden behaviors in governing artifacts.',
            ))
