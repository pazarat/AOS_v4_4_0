from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List, Optional
import json

from aos_capabilities.file_intelligence.common import safe_read_text, tokenize, classify_project_condition
from aos_capabilities.file_intelligence.inventory.scanner import InventoryScanner
from aos_capabilities.file_intelligence.inventory.classifier import ContentClassifier
from aos_capabilities.file_intelligence.fingerprints.content_fingerprint import ContentFingerprinter
from aos_capabilities.file_intelligence.fingerprints.semantic_fingerprint import SemanticFingerprinter
from aos_capabilities.file_intelligence.search.keyword_search import KeywordSearch
from aos_capabilities.file_intelligence.search.concept_search import ConceptSearch
from aos_capabilities.file_intelligence.search.semantic_search import SemanticLiteSearch
from aos_capabilities.file_intelligence.code_intelligence.symbol_extractor import SymbolExtractor
from aos_capabilities.file_intelligence.code_intelligence.ast_bridge import ASTBridge
from aos_capabilities.file_intelligence.code_intelligence.lsp_bridge import LSPBridge
from aos_capabilities.file_intelligence.code_intelligence.call_graph import CallGraphBuilder
from aos_capabilities.file_intelligence.code_intelligence.import_graph import ImportGraphBuilder
from aos_capabilities.file_intelligence.database_intelligence.schema_reader import SchemaReader
from aos_capabilities.file_intelligence.database_intelligence.migration_reader import MigrationReader
from aos_capabilities.file_intelligence.database_intelligence.orm_mapper import ORMMapper
from aos_capabilities.file_intelligence.database_intelligence.relation_graph import RelationGraphBuilder
from aos_capabilities.file_intelligence.api_intelligence.route_extractor import RouteExtractor
from aos_capabilities.file_intelligence.api_intelligence.endpoint_mapper import EndpointMapper
from aos_capabilities.file_intelligence.api_intelligence.openapi_mapper import OpenAPIMapper
from aos_capabilities.file_intelligence.impact.duplicate_scan import DuplicateScanner
from aos_capabilities.file_intelligence.impact.conflict_scan import ConflictScanner
from aos_capabilities.file_intelligence.impact.impact_scan import ImpactScanner
from aos_capabilities.file_intelligence.patch_gate.patch_gate import PatchGate
from aos_capabilities.file_intelligence.construction.construction_context import ConstructionContextBuilder
from aos_capabilities.file_intelligence.construction.construction_gate import ConstructionGate
from aos_capabilities.file_intelligence.diagnostics.diagnostic_engine import DiagnosticEngine
from aos_capabilities.file_intelligence.governance.artifact_policy import ArtifactPolicyEngine
from aos_capabilities.file_intelligence.governance.canon_guard import CanonGuard
from aos_capabilities.file_intelligence.governance.truth_guard import TruthGuard
from aos_capabilities.file_intelligence.governance.write_guard import WriteGuard
from aos_capabilities.file_intelligence.governance.scope_guard import ScopeGuard
from aos_capabilities.file_intelligence.verification.verification_engine import VerificationEngine
from aos_capabilities.file_intelligence.receipts.operation_receipt import OperationReceiptBuilder
from aos_capabilities.truth_runtime.truth_requirement.resolver import TruthRequirementResolver
from aos_capabilities.truth_runtime.truth_value.artifact_semantics import ArtifactTruthSemantics

class FileMatrix:
    """Mature File Intelligence Matrix.

    The matrix is an evidence/navigation engine, not a replacement for current
    project files. It defaults to the project payload surface and keeps AOS
    operating files separate.
    """
    def __init__(self, root: Path):
        self.root = Path(root).resolve()
        self.scanner = InventoryScanner(self.root)
        self.classifier = ContentClassifier()
        self.content_fp = ContentFingerprinter()
        self.semantic_fp = SemanticFingerprinter()
        self.symbols = SymbolExtractor()

    def scan(self, query: str | None = None, changed_paths: Optional[List[str]] = None, intent: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        records = self.scanner.scan()
        for rec in records:
            path = self.root / rec['path']
            text = safe_read_text(path, limit=250_000) if rec.get('is_text') else ''
            rec['sample'] = text[:2000]
            # Keep a larger internal sample for extractors while preventing huge reports.
            rec['sample_full'] = text[:50_000]
            rec['fingerprints'] = self.content_fp.fingerprint_file(path)
            sem = self.semantic_fp.fingerprint_text(text)
            rec['semantic_fingerprint'] = sem
            rec['semantic'] = {'terms': [x['term'] for x in sem.get('top_terms', [])], 'top_terms': [x['term'] for x in sem.get('top_terms', [])]}
            classified = self.classifier.classify(text)
            rec.update(classified)
            if rec.get('is_code'):
                ci = self.symbols.extract(path, text, rec.get('language','unknown'))
                rec['symbols'] = ci.get('symbols', [])
                rec['imports'] = ci.get('imports', [])
                rec['calls'] = ci.get('calls', [])
                rec['issues'] = ci.get('issues', [])
            else:
                rec['symbols'] = []
                rec['imports'] = []
                rec['calls'] = []
                rec['issues'] = []

        project_condition = classify_project_condition(records)
        symbol_graph = self._symbol_graph(records)
        call_graph = CallGraphBuilder().build(records)
        import_graph = ImportGraphBuilder().build(records)
        schema_map = SchemaReader().extract(records)
        migration_map = MigrationReader().extract(records)
        orm_map = ORMMapper().extract(records)
        db_relation_graph = RelationGraphBuilder().build(records, schema_map)
        route_map = RouteExtractor().extract(records)
        api_map = EndpointMapper().map(route_map)
        openapi = OpenAPIMapper().extract(records)
        duplicate_scan = DuplicateScanner().scan(records)
        conflict_scan = ConflictScanner().scan(records, api_map)
        impact_map = ImpactScanner().scan(records, changed_paths=changed_paths, query=query or '')
        content_knownness_map = self._content_knownness(records)
        search_packet = self._search(records, query or '')
        patch_requested = bool(changed_paths) or bool((intent or {}).get('may_modify_files')) or any((intent or {}).get(k) for k in ('target_path','entrypoint','file','path'))
        patch_gate = PatchGate().assess(changed_paths or [], intent, {
            'duplicate_scan': duplicate_scan,
            'conflict_scan': conflict_scan,
        }) if patch_requested else {'status': 'not_requested'}
        truth_requirement = TruthRequirementResolver().resolve(query or '', intent=intent, surface=(intent or {}).get('surface') or (intent or {}).get('scope'))
        diagnostic_records = self._records_for_diagnostics(records, intent)
        construction_context = ConstructionContextBuilder().build(records, query=query or '', intent=intent, changed_paths=changed_paths or [])
        diagnostics = DiagnosticEngine().run(diagnostic_records, {
            'duplicate_scan': duplicate_scan,
            'conflict_scan': conflict_scan,
            'graphs': {
                'symbol_graph': symbol_graph,
                'call_graph': call_graph,
                'import_graph': import_graph,
                'database_relation_graph': db_relation_graph,
            },
        })
        construction_gate = ConstructionGate().assess(records, query=query or '', intent=intent, changed_paths=changed_paths or [], diagnostics=diagnostics)
        governance = ArtifactPolicyEngine().decide(diagnostics=diagnostics, construction_gate=construction_gate, patch_gate=patch_gate)
        canon_guard = CanonGuard().assess(records, query=query or '')
        truth_guard = TruthGuard().assess(records, diagnostics=diagnostics)
        scope_guard = ScopeGuard().assess(records)
        write_guard = WriteGuard().assess(governance)
        verification = VerificationEngine().verify(diagnostics, governance)
        truth_value_semantics = ArtifactTruthSemantics().analyze({'records': records, 'summary': summary if 'summary' in locals() else {}, 'duplicate_scan': duplicate_scan})
        receipt = OperationReceiptBuilder().build(
            operation='scan',
            scope=self.root.as_posix(),
            file_count=len(records),
            diagnostics=diagnostics,
            construction_gate=construction_gate,
            governance=governance,
        )
        summary = self._summary(records, project_condition, diagnostics)
        adapters = {
            'text_readers': True,
            'content_fingerprint': True,
            'semantic_lite': True,
            'python_ast': ASTBridge().readiness()['python_ast'],
            'regex_symbol_fallback': True,
            'lsp_bridge': LSPBridge().readiness()['lsp_bridge'],
            'dense_vector_search': 'extension_point',
            'graph_backend': 'json_state_extension_point',
        }
        # Remove bulky internal field from report after extraction.
        report_records=[]
        for r in records:
            slim=dict(r)
            slim.pop('sample_full', None)
            report_records.append(slim)
        report = {
            'version': '4.0',
            'capability': 'file_intelligence',
            'root': self.root.as_posix(),
            'project_condition': project_condition,
            'file_count': len(records),
            'payload_file_count': len([r for r in records if r.get('surface') == 'project_payload']),
            'aos_surface_file_count': len([r for r in records if r.get('surface') == 'aos_default_surface']),
            'summary': summary,
            'records': report_records,
            'content_knownness_map': content_knownness_map,
            'search': search_packet,
            'symbol_graph': symbol_graph,
            'call_graph': call_graph,
            'import_graph': import_graph,
            'database_intelligence': {
                'schemas': schema_map,
                'migrations': migration_map,
                'orm': orm_map,
                'relations': db_relation_graph,
            },
            'api_intelligence': {
                'routes': route_map,
                'endpoints': api_map,
                'openapi': openapi,
            },
            'duplicate_scan': duplicate_scan,
            'conflict_scan': conflict_scan,
            'impact_map': impact_map,
            'patch_gate': patch_gate,
            'construction_runtime': {
                'context': construction_context,
                'gate': construction_gate,
                'generation_guidance': construction_gate.get('generation_guidance'),
            },
            'diagnostics': diagnostics,
            'truth_requirement_hint': truth_requirement,
            'truth_value_semantics': truth_value_semantics,
            'artifact_governance': {
                'policy_decision': governance,
                'canon_guard': canon_guard,
                'truth_guard': truth_guard,
                'scope_guard': scope_guard,
                'write_guard': write_guard,
            },
            'verification': verification,
            'receipt': receipt,
            'api_surface': [
                'file.health',
                'file.preflight',
                'file.build_context',
                'file.validate_plan',
                'file.diagnose',
                'file.verify_after_write',
                'file.plan_repair',
                'file.doctor',
                'file.receipt',
            ],
            'adapter_readiness': adapters,
            'mandatory_rules': [
                'file intelligence is a capability, not a core layer',
                'capabilities produce evidence; core owns direction and decisions',
                'current files remain source of truth',
                'generated indexes are navigation only',
                'no strong project claim from file names alone',
                'truth required by intent must shape scan depth before response or execution',
                'no write without intent, impact scan, duplicate scan, policy, and evaluation',
                'construction governance must guide generation before writing',
                'diagnostics are read-only by default',
                'repair planning is separate from patch application',
                'every operation must produce a receipt',
            ],
        }
        self._write_state(report)
        return report

    def _records_for_diagnostics(self, records: List[Dict[str, Any]], intent: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        intent = intent or {}
        scope = intent.get('scope') or intent.get('surface') or ''
        if scope in {'aos', 'aos_environment'}:
            return [r for r in records if r.get('surface') != 'active_project_payload']
        return records

    def _summary(self, records: List[Dict[str, Any]], condition: str, diagnostics: Dict[str, Any] | None = None) -> Dict[str, Any]:
        by_ext={}; by_role={}; by_surface={}; issues=[]
        for r in records:
            by_ext[r.get('extension') or '<none>'] = by_ext.get(r.get('extension') or '<none>', 0)+1
            by_role[r.get('role')] = by_role.get(r.get('role'),0)+1
            by_surface[r.get('surface')] = by_surface.get(r.get('surface'),0)+1
            for issue in r.get('issues') or []:
                issues.append({'path': r['path'], 'issue': issue})
        diagnostics = diagnostics or {}
        return {
            'project_condition': condition,
            'by_extension': by_ext,
            'by_role': by_role,
            'by_surface': by_surface,
            'issue_count': len(issues),
            'issues': issues[:200],
            'diagnostic_issue_count': diagnostics.get('issue_count', 0),
            'diagnostic_blocking_count': diagnostics.get('blocking_count', 0),
            'diagnostic_maturity_issue_count': diagnostics.get('maturity_issue_count', 0),
        }

    def _content_knownness(self, records: List[Dict[str, Any]]) -> Dict[str, Any]:
        concept_status={}
        for r in records:
            if r.get('surface') != 'project_payload':
                continue
            for concept, data in (r.get('concepts') or {}).items():
                st=concept_status.setdefault(concept, {'evidence_count':0, 'evidence_files':[], 'score':0})
                st['evidence_count'] += 1
                st['score'] += int(data.get('score', 0))
                if len(st['evidence_files']) < 20:
                    st['evidence_files'].append(r['path'])
        blockers=[c for c,v in concept_status.items() if v['evidence_count'] >= 1]
        return {'purpose':'prevent_unknownness_claims_when_concept_is_documented_in_content', 'concept_status': concept_status, 'unknownness_claim_blockers': blockers}

    def _search(self, records: List[Dict[str, Any]], query: str) -> Dict[str, Any]:
        if not query:
            return {'query': query, 'lenses_used': [], 'results': []}
        keyword = KeywordSearch().search(records, query)
        concept = ConceptSearch().search(records, query)
        semantic = SemanticLiteSearch().search(records, query)
        return {'query': query, 'lenses_used': ['keyword','concept','semantic_lite'], 'keyword': keyword, 'concept': concept, 'semantic_lite': semantic, 'results': self._merge_results(keyword, concept, semantic)}

    def _merge_results(self, *groups: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        merged={}
        for group in groups:
            for item in group:
                m=merged.setdefault(item['path'], {'path': item['path'], 'score':0, 'lenses':[], 'role': item.get('role'), 'surface': item.get('surface')})
                m['score'] += item.get('score',0)
                m['lenses'].append(item)
        return sorted(merged.values(), key=lambda x: (-x['score'], x['path']))[:30]

    def _symbol_graph(self, records: List[Dict[str, Any]]) -> Dict[str, Any]:
        symbols=[]
        for r in records:
            for s in r.get('symbols') or []:
                symbols.append({'file': r['path'], **s})
        return {'symbol_count': len(symbols), 'symbols': symbols[:1000]}

    def _write_state(self, report: Dict[str, Any]) -> None:
        # Write acceleration state next to active project only when the directory is writable.
        runtime_root = self.root / '_aos_runtime_project_state'
        if not runtime_root.exists():
            return
        state = runtime_root / 'file_matrix_state'
        try:
            state.mkdir(parents=True, exist_ok=True)
            slim = {k: v for k, v in report.items() if k != 'records'}
            (state / 'last_matrix_summary.json').write_text(json.dumps(slim, ensure_ascii=False, indent=2), encoding='utf-8')
            (state / 'records_index.json').write_text(json.dumps(report.get('records', []), ensure_ascii=False, indent=2), encoding='utf-8')
        except Exception:
            pass
