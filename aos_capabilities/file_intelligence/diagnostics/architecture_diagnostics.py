from __future__ import annotations

from typing import Any, Dict, List

from .issue_model import DiagnosticIssue


class ArchitectureDiagnostics:
    """Layer/scope diagnostics for AOS and arbitrary projects."""

    def scan(self, records: List[Dict[str, Any]], graphs: Dict[str, Any] | None = None) -> List[DiagnosticIssue]:
        issues: List[DiagnosticIssue] = []
        by_path = {r.get('path'): r for r in records}
        for rec in records:
            path = rec.get('path') or ''
            if '__pycache__' in path or path.endswith('.pyc'):
                issues.append(DiagnosticIssue(
                    severity='warn',
                    category='architecture',
                    code='architecture.generated_cache_present',
                    message='Generated Python cache artifact is present in the distribution surface.',
                    path=path,
                    recommendation='Generated caches should not be shipped as source truth.',
                ))
            if path.startswith('aos_core/files/'):
                issues.append(DiagnosticIssue(
                    severity='block',
                    category='architecture',
                    code='architecture.file_layer_inside_core',
                    message='File intelligence must remain a capability/port, not a core layer.',
                    path=path,
                    recommendation='Move file handling to aos_capabilities/file_intelligence and expose it via aos_core/ports/file_intelligence_port.py.',
                ))
            if path.startswith('aos_core/') and rec.get('is_code'):
                for imp in rec.get('imports') or []:
                    mod = imp.get('module', '')
                    if mod.startswith('aos_capabilities.file_intelligence.') and not path.endswith('aos_core/ports/file_intelligence_port.py'):
                        issues.append(DiagnosticIssue(
                            severity='block',
                            category='architecture',
                            code='architecture.core_imports_capability_internals',
                            message='Core must use the FileIntelligencePort, not capability internals.',
                            path=path,
                            line=imp.get('line'),
                            evidence={'module': mod},
                            recommendation='Route through aos_core/ports/file_intelligence_port.py.',
                        ))
        return issues
