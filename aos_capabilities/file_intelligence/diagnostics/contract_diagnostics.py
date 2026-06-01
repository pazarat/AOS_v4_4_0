from __future__ import annotations

import json
from typing import Any, Dict, List

from .issue_model import DiagnosticIssue

try:
    import yaml  # type: ignore
except Exception:  # pragma: no cover - yaml may not exist in minimal envs
    yaml = None


class ContractDiagnostics:
    """Diagnostics for JSON/YAML manifests, schemas, and contracts."""

    REQUIRED_CAPABILITY_KEYS = {'id', 'version', 'purpose', 'modules', 'outputs', 'adapter'}

    def scan(self, records: List[Dict[str, Any]]) -> List[DiagnosticIssue]:
        issues: List[DiagnosticIssue] = []
        for rec in records:
            path = rec.get('path') or ''
            lang = rec.get('language')
            text = rec.get('sample_full') or rec.get('sample') or ''
            if self._looks_truncated(rec, text):
                continue
            if lang == 'json':
                self._json(path, text, issues)
            elif lang == 'yaml':
                self._yaml(path, text, issues)
            if path.endswith('CAPABILITY_MANIFEST.yaml'):
                self._capability_manifest(path, text, issues)
        return issues

    def _looks_truncated(self, rec: Dict[str, Any], text: str) -> bool:
        try:
            return int(rec.get('size_bytes') or 0) > len((text or '').encode('utf-8', errors='replace')) + 16
        except Exception:
            return False

    def _json(self, path: str, text: str, issues: List[DiagnosticIssue]) -> None:
        if not text.strip():
            return
        try:
            json.loads(text)
        except Exception as exc:
            issues.append(DiagnosticIssue(
                severity='block',
                category='contract',
                code='contract.invalid_json',
                message='Invalid JSON contract/configuration file.',
                path=path,
                evidence={'error': str(exc)},
                recommendation='Repair JSON syntax before using this artifact as machine-readable truth.',
            ))

    def _yaml(self, path: str, text: str, issues: List[DiagnosticIssue]) -> None:
        if yaml is None or not text.strip():
            return
        try:
            yaml.safe_load(text)
        except Exception as exc:
            issues.append(DiagnosticIssue(
                severity='block',
                category='contract',
                code='contract.invalid_yaml',
                message='Invalid YAML contract/configuration file.',
                path=path,
                evidence={'error': str(exc)},
                recommendation='Repair YAML syntax before using this artifact as machine-readable truth.',
            ))

    def _capability_manifest(self, path: str, text: str, issues: List[DiagnosticIssue]) -> None:
        if yaml is None:
            return
        try:
            data = yaml.safe_load(text) or {}
        except Exception:
            return
        missing = sorted(self.REQUIRED_CAPABILITY_KEYS - set(data.keys()))
        if missing:
            issues.append(DiagnosticIssue(
                severity='mature',
                category='contract',
                code='contract.capability_manifest_incomplete',
                message='Capability manifest is missing required governance fields.',
                path=path,
                evidence={'missing_keys': missing},
                recommendation='Complete the manifest before treating the capability as fully governed.',
            ))
