from __future__ import annotations

import hashlib
import re
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any, Dict, List

HIGH_VALUE_MARKERS = ('contract','truth','canon','standard','identity','manifest','decision','readme','api','schema','governance','policy','entrypoint')
TEXT_EXTS = {'.md','.yaml','.yml','.json','.txt','.py','.ts','.tsx','.js','.jsx','.cs','.sql','.xml','.html'}


class QuickArtifactCockpit:
    """Fast project-neutral artifact contribution builder.

    This is the Operations Runtime Kernel's fast artifact service. It does not
    return a raw inspection report to delivery. It builds multiple value lenses
    behind the runtime kernel, then returns a contribution the runtime kernel can weigh against
    intent and truth.
    """

    def scan(self, root: Path, query: str = '', surface: str = 'active_project_payload') -> Dict[str, Any]:
        root = Path(root)
        records: List[Dict[str, Any]] = []
        if root.exists():
            for p in sorted([x for x in root.rglob('*') if x.is_file() and x.name != '.keep'], key=lambda x: x.as_posix()):
                try:
                    size = p.stat().st_size
                    sample = p.read_text(encoding='utf-8', errors='ignore')[:2500] if p.suffix.lower() in TEXT_EXTS else ''
                except Exception:
                    size, sample = 0, ''
                rel = p.relative_to(root).as_posix()
                content_state = 'empty' if size == 0 else ('thin' if size < 300 else ('governing_or_contentful' if self._is_high_value(rel, sample) else 'contentful'))
                records.append({
                    'path': rel,
                    'name': p.name,
                    'extension': p.suffix.lower(),
                    'language': p.suffix.lower().strip('.') or 'unknown',
                    'size_bytes': size,
                    'is_text': p.suffix.lower() in TEXT_EXTS,
                    'is_code': p.suffix.lower() in {'.py','.ts','.tsx','.js','.jsx','.cs','.sql'},
                    'is_binary': p.suffix.lower() not in TEXT_EXTS,
                    'surface': 'project_payload' if surface == 'active_project_payload' else surface,
                    'role': self._role(rel),
                    'sample': sample[:1200],
                    'content_state': content_state,
                })
        matrix_started = time.perf_counter()
        with ThreadPoolExecutor(max_workers=5) as pool:
            summary_future = pool.submit(self._summary, records)
            duplicates_future = pool.submit(self._duplicates, root, records)
            search_future = pool.submit(self._search, records, query)
            value_map_future = pool.submit(self._value_map, records)
            summary = summary_future.result()
            duplicates = duplicates_future.result()
            search_results = search_future.result()
            value_map = value_map_future.result()
        semantics = self._truth_value_semantics(records, duplicates)
        owner_signal = self._owner_signal(records, semantics, duplicates)
        diagnostics = self._diagnostics(semantics, duplicates)
        matrix_invocation = {
            'mode': 'directed_artifact_matrix_fanout',
            'calls': ['summary', 'duplicate_truth', 'query_search', 'value_map', 'owner_signal'],
            'elapsed_ms': round((time.perf_counter() - matrix_started) * 1000, 3),
            'law': 'artifact cockpit provides matrix-ready contributions behind operations_runtime',
        }
        matrix = {
            'version': 'operations-fast-matrix-v2',
            'capability': 'quick_artifact_cockpit',
            'authority': 'contribution_only',
            'authority_scope': 'fast_value_extraction_not_full_diagnostics',
            'root': root.as_posix(),
            'project_condition': self._condition(records),
            'file_count': len(records),
            'payload_file_count': len(records) if surface == 'active_project_payload' else 0,
            'aos_surface_file_count': 0 if surface == 'active_project_payload' else len(records),
            'summary': summary,
            'records': records,
            'search': {'query': query, 'lenses_used': ['fast_value_extraction'], 'results': search_results},
            'duplicate_scan': {'duplicates': duplicates},
            'conflict_scan': {'conflicts': []},
            'truth_value_semantics': semantics,
            'owner_signal': owner_signal,
            'value_map': value_map,
            'diagnostics': diagnostics,
            'artifact_governance': {'policy_decision': {'decision': 'MATURE' if diagnostics['maturity_issue_count'] else 'ALLOW', 'meaning': 'fast contribution gate; deep doctor only when explicitly requested'}},
            'matrix_invocation': matrix_invocation,
            'packet_mode': 'operations_fast_contribution_matrix',
        }
        return matrix

    def contribution(self, matrix: Dict[str, Any]) -> Dict[str, Any]:
        sem = matrix.get('truth_value_semantics') or {}
        diagnostics = matrix.get('diagnostics') or {}
        condition = matrix.get('project_condition')
        empty = sem.get('empty_declared_target_count', 0) or 0
        missing = sem.get('declared_missing_artifact_count', 0) or 0
        high = sem.get('high_value_sources') or []
        duplicates = (matrix.get('duplicate_scan') or {}).get('duplicates') or []
        owner = matrix.get('owner_signal') or {}
        value_map = matrix.get('value_map') or {}
        value_lines: List[str] = []
        if condition == 'SPEC_ONLY_PROJECT':
            value_lines.append('القيمة الحالية ليست في جاهزية الكود؛ القيمة في حقيقة عليا حاكمة مع فجوة ترجمة إلى مواصفات تنفيذية مغلقة.')
        elif condition == 'EMPTY_NEW_PROJECT':
            value_lines.append('لا توجد مادة مشروع كافية؛ التعامل الصحيح هو تكوين حقيقة المشروع الأولى لا تخمين تقييم مشروع غير موجود.')
        else:
            value_lines.append('يوجد محتوى قابل للفهم، ويجب استخراج قيمته بحسب النية قبل أي حكم أو تنفيذ.')
        if owner.get('label'):
            value_lines.append(f"أقوى عقدة إنضاج مشتقة من الأدلة هي {owner.get('label')} لأنها تجمع حقيقة مالكة مع فراغات/تكرار/وعود تابعة.")
        if high:
            value_lines.append('مصادر القيمة الأعلى ليست الأكبر حجمًا؛ هي العقود والمعايير والملفات الحاكمة التي تفسر معنى بقية الملفات.')
        if empty:
            value_lines.append('الفراغات المؤثرة تُقرأ كأهداف بناء معلنة لا كفشل عشوائي ولا كحقيقة مكتملة.')
        if missing:
            value_lines.append('الملفات المعلنة وغير الموجودة تُقرأ كوعود حقيقة مكسورة يجب إغلاقها أو تأجيلها قبل البناء عليها.')
        if duplicates:
            value_lines.append('التطابق بين فروع وظيفية مختلفة يُقرأ كحقيقة ناقصة؛ لا يسمح بتخمين الفرق بل يفرض تحديد المالك والمعنى.')
        return {
            'layer': 'artifact_cockpit',
            'mode': matrix.get('packet_mode'),
            'value': ' '.join(value_lines),
            'evidence': [
                {'type': 'condition', 'value': condition},
                {'type': 'high_value_sources', 'value': high[:8]},
                {'type': 'owner_signal', 'value': owner},
                {'type': 'value_map', 'value': value_map},
            ],
            'risks': diagnostics.get('top_issues', []),
            'next_needs': self._next_needs(empty, missing, duplicates, owner),
            'ignored_noise': ['raw record dump', 'file counts as visible truth', 'file size as truth priority', 'internal paths in user-visible answer'],
        }

    def _role(self, rel: str) -> str:
        low = rel.lower()
        if any(m in low for m in ('contract','truth','manifest','schema','api','.yaml','.json')):
            return 'configuration_or_contract'
        if any(m in low for m in ('identity','canon','standard','policy','decision','readme')):
            return 'governing_documentation'
        if low.endswith(('.py','.ts','.tsx','.js','.jsx','.cs','.sql')):
            return 'source_code'
        return 'documentation'

    def _is_high_value(self, rel: str, sample: str) -> bool:
        low = (rel + '\n' + sample[:1500]).lower()
        return any(m in low for m in HIGH_VALUE_MARKERS) or any(x in low for x in ('ممنوع','يجب','حقيقة','حوكمة','قاعدة','دستور'))

    def _summary(self, records: List[Dict[str, Any]]) -> Dict[str, Any]:
        by_ext: Dict[str, int] = {}; by_role: Dict[str, int] = {}; by_surface: Dict[str, int] = {}
        for r in records:
            by_ext[r.get('extension') or '<none>'] = by_ext.get(r.get('extension') or '<none>', 0) + 1
            by_role[r.get('role') or '<none>'] = by_role.get(r.get('role') or '<none>', 0) + 1
            by_surface[r.get('surface') or '<none>'] = by_surface.get(r.get('surface') or '<none>', 0) + 1
        return {'project_condition': self._condition(records), 'by_extension': by_ext, 'by_role': by_role, 'by_surface': by_surface}

    def _condition(self, records: List[Dict[str, Any]]) -> str:
        if not records:
            return 'EMPTY_NEW_PROJECT'
        code_count = len([r for r in records if r.get('is_code')])
        if code_count >= 5:
            return 'ACTIVE_ENGINEERING_PROJECT'
        if all(r.get('extension') in {'.md','.yaml','.yml','.json'} for r in records):
            return 'SPEC_ONLY_PROJECT'
        return 'LEGACY_COMPLEX_PROJECT'

    def _duplicates(self, root: Path, records: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        groups: Dict[str, List[str]] = {}
        for r in records:
            if r.get('size_bytes', 0) <= 0:
                continue
            p = root / (r.get('path') or '')
            try:
                data = p.read_bytes()
            except Exception:
                continue
            digest = hashlib.sha256(data).hexdigest()
            groups.setdefault(digest, []).append(r.get('path'))
        return [{'sha256': h, 'paths': ps} for h, ps in groups.items() if len(ps) > 1][:20]

    def _truth_value_semantics(self, records: List[Dict[str, Any]], duplicates: List[Dict[str, Any]]) -> Dict[str, Any]:
        paths = {r['path'] for r in records}
        empty_targets = [r for r in records if r.get('size_bytes') == 0 and self._is_declared_target_path(r.get('path',''))]
        declared_edges: List[Dict[str, str]] = []
        missing: List[Dict[str, str]] = []
        path_re = re.compile(r'([A-Za-z0-9_./-]+\.(?:md|yaml|yml|json|py|ts|tsx|js|jsx|cs|sql))')
        for r in records:
            base_dir = str(Path(r['path']).parent)
            sample = r.get('sample') or ''
            for m in path_re.findall(sample):
                if m.startswith(('http','www')):
                    continue
                normalized = str(Path(base_dir) / m).replace('\\','/') if not m.startswith(('.', '/')) else m.strip('./')
                normalized = normalized.replace('\\','/')
                declared_edges.append({'declared_in': r['path'], 'normalized_path': normalized})
                if normalized not in paths and m not in paths:
                    missing.append({'declared_in': r['path'], 'normalized_path': normalized})
        high_value = []
        for r in records:
            score = 0
            low = (r.get('path','') + ' ' + r.get('role','') + ' ' + (r.get('sample') or '')[:1000]).lower()
            score += sum(1 for m in HIGH_VALUE_MARKERS if m in low)
            if any(x in low for x in ('must','forbidden','law','ممنوع','يجب','حقيقة','حوكمة','قاعدة','دستور')):
                score += 2
            if score:
                high_value.append({'path': r['path'], 'role': r.get('role'), 'size_bytes': r.get('size_bytes'), 'score': score, 'reason': 'value_role_marker_not_size'})
        return {
            'empty_declared_target_count': len(empty_targets),
            'declared_missing_artifact_count': len(missing),
            'empty_declared_targets': [{'path': r['path'], 'interpretation': 'declared construction target'} for r in empty_targets[:50]],
            'declared_missing_artifacts': missing[:50],
            'declared_edges': declared_edges[:100],
            'high_value_sources': sorted(high_value, key=lambda x: (-x['score'], x['path']))[:30],
            'duplicate_functional_truth_count': len(duplicates),
            'rule': 'truth value is role/provenance/relationship/intent fit, not file size',
        }

    def _value_map(self, records: List[Dict[str, Any]]) -> Dict[str, Any]:
        governing = [r for r in records if r.get('role') in {'configuration_or_contract', 'governing_documentation'} or self._is_high_value(r.get('path',''), r.get('sample',''))]
        contentful = [r for r in records if r.get('content_state') in {'governing_or_contentful','contentful'}]
        empty = [r for r in records if r.get('content_state') == 'empty']
        code = [r for r in records if r.get('is_code')]
        return {
            'governing_truth_present': bool(governing),
            'contentful_artifacts_present': bool(contentful),
            'declared_targets_present': bool(empty),
            'implementation_code_present': bool(code),
            'interpretation': 'governing_truth_strong_but_execution_truth_not_closed' if governing and empty and not code else 'scope_specific_review_required',
        }

    def _owner_signal(self, records: List[Dict[str, Any]], semantics: Dict[str, Any], duplicates: List[Dict[str, Any]]) -> Dict[str, Any]:
        scores: Dict[str, Dict[str, Any]] = {}
        generic = {'modules','business','financial','operations','system','marketing','smart_data','A_dashboards','04_PROJECT_ARTIFACTS','03_PROJECT_COGNITIVE_TUNNEL'}

        # The first path segment is the uploaded project root name. It is a scope
        # holder, not an actionable maturity owner. Owners must be derived from
        # functional/module segments beneath it.
        def candidate_segments(path: str) -> List[str]:
            parts = [p for p in Path(path).parts if p and p not in {'.'}]
            if parts and not parts[0].startswith(('00_', '01_', '02_', '03_', '04_', '05_', '06_', '99_')):
                parts = parts[1:]
            parents = list(parts[:-1])
            candidates: List[str] = []
            for c in reversed(parents):
                if c in generic or c.endswith('.md') or c.endswith('.yaml'):
                    continue
                if c.startswith(('00_', '01_', '02_', '03_', '04_', '05_', '06_', '99_')):
                    continue
                candidates.append(c)
            return candidates

        def add(path: str, weight: int, reason: str):
            cands = candidate_segments(path)
            if not cands:
                return
            for idx, chosen in enumerate(cands[:4]):
                # score multiple ancestors so a real owner like User_Management
                # wins over leaf pages such as all_users/profile/verification.
                scaled = max(1, weight - idx)
                item = scores.setdefault(chosen, {'key': chosen, 'score': 0, 'reasons': set(), 'paths': []})
                item['score'] += scaled
                item['reasons'].add(reason)
                if path not in item['paths']:
                    item['paths'].append(path)

        for item in semantics.get('empty_declared_targets', [])[:50]:
            add(item.get('path',''), 3, 'declared_empty_targets')
        for item in semantics.get('declared_missing_artifacts', [])[:50]:
            add(item.get('declared_in',''), 2, 'declared_missing_promises')
        for dup in duplicates:
            for p in dup.get('paths', [])[:4]:
                add(p, 4, 'duplicate_functional_truth')
        for hv in semantics.get('high_value_sources', [])[:12]:
            add(hv.get('path',''), 1, 'high_value_truth_owner')
        if not scores:
            return {}
        ranked = sorted(scores.values(), key=lambda x: (-x['score'], x['key']))
        top = ranked[0]
        label = self._humanize_key(top['key'])
        return {
            'key': top['key'],
            'label': label,
            'score': top['score'],
            'reasons': sorted(top['reasons']),
            'sample_paths': top['paths'][:5],
            'interpretation': 'primary_maturity_owner_candidate_derived_from_artifact_relationships',
        }

    def _humanize_key(self, key: str) -> str:
        clean = re.sub(r'^[A-Z]-[A-Z]_?', '', key).strip('_-')
        clean = clean.replace('_', ' ').replace('-', ' ')
        if not clean:
            return key
        if clean.lower() == 'user management':
            return 'إدارة المستخدمين'
        return clean

    def _diagnostics(self, semantics: Dict[str, Any], duplicates: List[Dict[str, Any]]) -> Dict[str, Any]:
        issues: List[Dict[str, Any]] = []
        for item in semantics.get('empty_declared_targets', [])[:20]:
            issues.append({'severity': 'mature', 'category': 'truth', 'code': 'empty_declared_target_truth', 'path': item.get('path'), 'message': 'Empty artifact is a declared construction target, not completed truth.'})
        for item in semantics.get('declared_missing_artifacts', [])[:20]:
            issues.append({'severity': 'mature', 'category': 'truth', 'code': 'declared_but_missing_artifact', 'path': item.get('declared_in'), 'message': 'Declared related artifact is missing.'})
        for item in duplicates[:10]:
            issues.append({'severity': 'mature', 'category': 'duplication', 'code': 'duplicate_functional_truth', 'path': None, 'evidence': {'examples': [item]}, 'message': 'Duplicate content may be incomplete truth if functional paths differ.'})
        return {
            'mode': 'fast_value_contribution',
            'issue_count': len(issues),
            'blocking_count': 0,
            'maturity_issue_count': len([i for i in issues if i.get('severity') == 'mature']),
            'counts_by_severity': {'mature': len(issues)} if issues else {},
            'counts_by_category': {},
            'decision_hint': 'MATURE_TRUTH_OR_ACCEPT_TEMPORARY_RISK' if issues else None,
            'top_issues': issues[:12],
            'issues': issues[:50],
        }

    def _search(self, records: List[Dict[str, Any]], query: str) -> List[Dict[str, Any]]:
        terms = [x.lower() for x in re.findall(r'\w+', query or '') if len(x) > 2][:12]
        out = []
        for r in records:
            hay = (r.get('path','') + ' ' + (r.get('sample') or '')[:1000]).lower()
            score = sum(1 for t in terms if t in hay)
            if score:
                out.append({'path': r['path'], 'score': score, 'role': r.get('role'), 'surface': r.get('surface')})
        return sorted(out, key=lambda x: -x['score'])[:20]

    def _is_declared_target_path(self, path: str) -> bool:
        low = path.lower()
        return any(x in low for x in ('prd','readme','contract','standard','identity','manifest','api','schema','decision'))

    def _next_needs(self, empty: int, missing: int, duplicates: List[Dict[str, Any]], owner: Dict[str, Any] | None = None) -> List[str]:
        out = []
        if owner and owner.get('label'):
            out.append('mature_primary_owner_truth')
        if missing:
            out.append('close_or_defer_missing_declared_artifacts')
        if duplicates:
            out.append('resolve_duplicate_functional_truth_owner')
        if empty:
            out.append('mature_declared_construction_targets')
        return out or ['truth_sufficient_for_general_answer_only']
