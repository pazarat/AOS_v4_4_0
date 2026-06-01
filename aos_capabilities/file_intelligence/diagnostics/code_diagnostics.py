from __future__ import annotations

import json
import re
from typing import Any, Dict, List

from .issue_model import DiagnosticIssue


class CodeDiagnostics:
    """Read-only code diagnostics using existing extracted issues plus light contract checks."""

    def scan(self, records: List[Dict[str, Any]], graphs: Dict[str, Any] | None = None) -> List[DiagnosticIssue]:
        issues: List[DiagnosticIssue] = []
        all_calls = set()
        for rec in records:
            for c in rec.get('calls') or []:
                if c.get('name'):
                    all_calls.add(c['name'].split('.')[-1])
        for rec in records:
            if not rec.get('is_code'):
                continue
            path = rec.get('path')
            for raw in rec.get('issues') or []:
                severity = 'block' if str(raw).startswith('python_syntax_error') else 'warn'
                line = self._extract_line(raw)
                issues.append(DiagnosticIssue(
                    severity=severity,
                    category='code',
                    code='code.parser_issue',
                    message='Code parser reported an issue.',
                    path=path,
                    line=line,
                    evidence={'raw_issue': raw, 'language': rec.get('language')},
                    recommendation='Fix syntax/parser issue before relying on symbol, graph, or impact analysis.',
                ))
            text = rec.get('sample_full') or rec.get('sample') or ''
            if re.search(r'\b(pass|TODO|NotImplementedError|throw new NotImplementedException|not implemented)\b', text, re.I):
                issues.append(DiagnosticIssue(
                    severity='warn',
                    category='code',
                    code='code.placeholder_implementation',
                    message='Potential placeholder implementation found in source code.',
                    path=path,
                    evidence={'language': rec.get('language')},
                    recommendation='Confirm whether this is deliberate scaffolding or incomplete implementation.',
                ))
            self._unused_private_symbols(rec, all_calls, issues)
        return issues

    def _extract_line(self, raw: str) -> int | None:
        parts = str(raw).split(':')
        if len(parts) >= 2 and parts[1].isdigit():
            return int(parts[1])
        return None

    def _unused_private_symbols(self, rec: Dict[str, Any], all_calls: set[str], issues: List[DiagnosticIssue]) -> None:
        # Conservative: only private-like functions in non-test Python files.
        if rec.get('language') != 'python' or rec.get('role') == 'test_code':
            return
        for sym in rec.get('symbols') or []:
            name = sym.get('name', '')
            if sym.get('kind') == 'function' and name.startswith('_') and not name.startswith('__') and name not in all_calls:
                issues.append(DiagnosticIssue(
                    severity='info',
                    category='code',
                    code='code.private_symbol_unreferenced',
                    message='Private-like function was not observed in the lightweight call graph.',
                    path=rec.get('path'),
                    line=sym.get('line'),
                    evidence={'symbol': name},
                    recommendation='Verify with tests/LSP before deleting; this is a navigation hint, not a deletion decision.',
                ))
