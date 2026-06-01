from __future__ import annotations

import re
from pathlib import Path
from typing import Any, Dict, List

from operations_runtime.context import is_valid_operations_intent


class ProjectTruthReaderAPI:
    """Generic project truth gateway behind Operations Runtime.

    The reader is payload-neutral. It discovers local project markers and high-value
    artifacts from the active project root without embedding any project name,
    module name, or fixture-specific path into the agent runtime.
    """

    MARKERS = ['00_PROJECT_ENTRYPOINT.md', '01_PROJECT_CONTRACT.yaml', '02_PROJECT_TRUTH_INDEX.yaml']
    GOVERNING_NAME_HINTS = ('contract', 'truth', 'index', 'memory', 'standard', 'architecture', 'implementation', 'runtime', 'gate', 'api', 'schema', 'identity', 'decision')
    TEXT_EXTS = {'.md', '.yaml', '.yml', '.json', '.txt'}

    layer_id = 'project_truth'

    def describe(self) -> Dict[str, Any]:
        return {
            'layer_id': self.layer_id,
            'role': 'generic active-project truth discovery and high-value project evidence contribution',
            'commands': ['project_truth.contribute'],
            'entrypoint': 'operations_runtime.project_truth_reader.ProjectTruthReaderAPI',
        }

    def healthcheck(self) -> Dict[str, Any]:
        return {'status': 'healthy', 'layer_id': self.layer_id}

    def validate_contract(self) -> Dict[str, Any]:
        return {'passed': True, 'issues': [], 'project_specific_names_allowed': False}

    def execute(self, command: Any) -> Dict[str, Any]:
        data = command.to_dict() if hasattr(command, 'to_dict') else dict(command or {})
        payload = data.get('payload') or {}
        context = data.get('context') or payload.get('intent')
        if data.get('command') in {'project_truth.contribute', 'contribute'}:
            result = self.contribute(payload.get('project_root', '.'), request_text=payload.get('request_text', ''), intent=context)
            return {'operation_id': data.get('operation_id'), 'layer_id': self.layer_id, 'command': data.get('command'), 'status': result.get('status', 'ok'), 'data': result, 'contributions': [result] if result.get('layer') else []}
        return {'operation_id': data.get('operation_id'), 'layer_id': self.layer_id, 'command': data.get('command'), 'status': 'blocked', 'data': {'reason': 'unsupported_command'}}

    def contribute(self, project_root: str | Path, *, request_text: str, intent: Dict[str, Any] | None = None) -> Dict[str, Any]:
        if not is_valid_operations_intent(intent):
            return self._blocked()
        root = self._resolve_project_root(Path(project_root))
        if not root.exists():
            return {
                'layer': self.layer_id,
                'mode': 'no_project_truth_loaded',
                'value': 'لا توجد حمولة مشروع قابلة للقراءة؛ لا يجوز تقييم مشروع غير موجود.',
                'evidence': [{'type': 'project_truth_state', 'value': 'missing'}],
                'risks': [{'severity': 'block', 'code': 'project_truth_missing', 'message': 'Project root is missing'}],
                'next_needs': ['load_or_create_project_truth'],
                'ignored_noise': ['guessing project identity from folder name'],
            }
        docs = self._read_governing_docs(root)
        contract = docs.get('01_PROJECT_CONTRACT.yaml', '')
        project_name = self._yaml_scalar(contract, 'project_name') or self._yaml_scalar(contract, 'name') or root.name
        project_type = self._yaml_scalar(contract, 'project_type') or self._yaml_scalar(contract, 'type') or 'unknown_project_type'
        stack = self._stack_signal('\n'.join(docs.values()))
        readiness = self._readiness_signal(docs)
        owner = self._owner_signal(root, docs)
        high_value_nodes = [
            {'role': self._role(rel), 'name': Path(rel).name.replace('_', ' '), 'reason': 'governing_or_owner_truth'}
            for rel, text in docs.items() if text.strip()
        ]
        value = (
            'تمت قراءة حقيقة المشروع من ملفاته المحلية الحاكمة بطريقة عامة ومحايدة. '
            'قيمة الحقيقة الحالية تُستمد من العقود والفهارس والمعايير وذاكرة المشروع، لا من اسم الحمولة أو حجم الملفات. '
            'أي توصية تنفيذية تبقى مشروطة بإغلاق الترجمة من الحقيقة إلى حدود/حالات/أحداث/صلاحيات/بيانات/اختبارات قبول.'
        )
        evidence = [
            {'type': 'project_identity', 'value': {'name': project_name, 'type': project_type}},
            {'type': 'stack_signal', 'value': stack},
            {'type': 'readiness_signal', 'value': readiness},
            {'type': 'primary_owner_candidate', 'value': owner},
            {'type': 'high_value_truth_nodes', 'value': high_value_nodes[:12]},
        ]
        next_needs = ['mature_selected_owner_execution_baseline', 'derive_state_event_permission_data_acceptance']
        risks = []
        if not readiness.get('implementation_target_ready'):
            risks.append({'severity': 'mature', 'code': 'implementation_target_not_ready', 'message': 'Implementation target or translation gates are not fully ready.'})
        if not owner.get('label'):
            risks.append({'severity': 'mature', 'code': 'primary_owner_not_identified', 'message': 'No clear project-local owner node was identified.'})
        return {
            'layer': self.layer_id,
            'mode': 'generic_high_value_truth_contribution',
            'value': value,
            'evidence': evidence,
            'risks': risks,
            'next_needs': next_needs,
            'ignored_noise': ['payload name as project truth', 'file count as maturity', 'runtime fixture assumptions'],
        }

    def _blocked(self) -> Dict[str, Any]:
        return {
            'layer': self.layer_id,
            'mode': 'blocked_direct_access',
            'value': '',
            'evidence': [{'type': 'blocked', 'value': 'missing_operations_context'}],
            'risks': [{'severity': 'block', 'code': 'direct_project_truth_access'}],
            'next_needs': ['invoke_project_truth_through_operations_runtime'],
            'ignored_noise': [],
            'status': 'blocked',
        }

    def _resolve_project_root(self, root: Path) -> Path:
        if all((root / m).exists() for m in self.MARKERS):
            return root
        if root.exists():
            candidates = [p for p in root.iterdir() if p.is_dir() and all((p / m).exists() for m in self.MARKERS)]
            if len(candidates) == 1:
                return candidates[0]
        return root

    def _read_governing_docs(self, root: Path) -> Dict[str, str]:
        rels: List[str] = []
        for marker in self.MARKERS + ['99_PROJECT_MEMORY.yaml']:
            if (root / marker).exists():
                rels.append(marker)
        for p in sorted(root.rglob('*'), key=lambda x: x.as_posix()):
            if not p.is_file() or p.suffix.lower() not in self.TEXT_EXTS:
                continue
            rel = p.relative_to(root).as_posix()
            low = rel.lower()
            if rel in rels:
                continue
            if any(h in low for h in self.GOVERNING_NAME_HINTS) or re.search(r'(^|/)\d{2}[_-]', rel):
                rels.append(rel)
            if len(rels) >= 24:
                break
        out: Dict[str, str] = {}
        for rel in rels[:24]:
            p = root / rel
            try:
                out[rel] = p.read_text(encoding='utf-8', errors='ignore')[:20000] if p.exists() else ''
            except Exception:
                out[rel] = ''
        return out

    def _yaml_scalar(self, text: str, key: str) -> str | None:
        m = re.search(rf'^\s*{re.escape(key)}\s*:\s*(.+?)\s*$', text, flags=re.MULTILINE)
        if not m:
            return None
        return m.group(1).strip().strip('"\'')

    def _stack_signal(self, text: str) -> Dict[str, Any]:
        low = text.lower()
        return {
            'backend': self._first_match(low, ['asp.net', '.net', 'laravel', 'django', 'fastapi', 'spring', 'nestjs', 'express']),
            'database': self._first_match(low, ['postgresql', 'mysql', 'sql server', 'mongodb', 'sqlite', 'redis']),
            'frontend': self._first_match(low, ['next.js', 'react', 'vue', 'angular', 'svelte']),
            'translation_required_before_code': 'do not generate production code' in low or 'do not generate' in low or 'translation' in low and 'gate' in low,
        }

    def _first_match(self, text: str, choices: List[str]) -> str | None:
        for c in choices:
            if c in text:
                return self._canonical_stack_name(c)
        return None

    def _canonical_stack_name(self, name: str) -> str:
        names = {
            'asp.net': 'ASP.NET',
            '.net': '.NET',
            'postgresql': 'PostgreSQL',
            'next.js': 'Next.js',
            'fastapi': 'FastAPI',
            'nestjs': 'NestJS',
            'mysql': 'MySQL',
            'sql server': 'SQL Server',
            'mongodb': 'MongoDB',
            'sqlite': 'SQLite',
            'redis': 'Redis',
            'react': 'React',
            'vue': 'Vue',
            'angular': 'Angular',
            'svelte': 'Svelte',
            'laravel': 'Laravel',
            'django': 'Django',
            'spring': 'Spring',
            'express': 'Express',
        }
        return names.get(name, name)

    def _readiness_signal(self, docs: Dict[str, str]) -> Dict[str, Any]:
        combined = '\n'.join(docs.values()).lower()
        return {
            'has_contract': bool(docs.get('01_PROJECT_CONTRACT.yaml')),
            'has_truth_index': bool(docs.get('02_PROJECT_TRUTH_INDEX.yaml')),
            'has_memory': bool(docs.get('99_PROJECT_MEMORY.yaml')),
            'implementation_target_ready': 'placeholder' not in combined and 'reserved for future' not in combined,
            'has_translation_gates': 'translation' in combined and 'gate' in combined,
            'has_data_api_lens': ('database' in combined or 'data model' in combined) and ('endpoint' in combined or 'api' in combined),
        }

    def _owner_signal(self, root: Path, docs: Dict[str, str]) -> Dict[str, Any]:
        candidates: Dict[str, Dict[str, Any]] = {}
        for rel, text in docs.items():
            low = (rel + '\n' + text[:3000]).lower()
            score = 0
            if any(x in low for x in ['parent', 'owner', 'module', 'capability', 'workflow', 'permission', 'state', 'event', 'acceptance criteria']):
                score += 3
            if any(x in low for x in ['prd', 'spec', 'requirements', 'contract']):
                score += 2
            if not score:
                continue
            parts = [p for p in Path(rel).parts[:-1] if p and not p.startswith(('00_', '01_', '02_', '03_', '04_', '05_', '06_', '99_'))]
            key = parts[-1] if parts else Path(rel).stem
            item = candidates.setdefault(key, {'key': key, 'label': key.replace('_', ' '), 'score': 0, 'paths': []})
            item['score'] += score
            item['paths'].append(rel)
        if not candidates:
            return {}
        best = sorted(candidates.values(), key=lambda x: (-x['score'], x['key']))[0]
        best['why_primary'] = 'أعلى مرشح عام مشتق من إشارات المالك/المتطلبات/الحالات/الأحداث داخل الحقيقة المحلية.'
        return best

    def _role(self, rel: str) -> str:
        low = rel.lower()
        if 'contract' in low or low.endswith(('.yaml', '.yml', '.json')):
            return 'contract_or_gate'
        if 'implementation' in low or 'architecture' in low or 'api' in low or 'schema' in low:
            return 'implementation_translation_standard'
        if 'memory' in low:
            return 'project_memory'
        if 'identity' in low or 'truth' in low or 'standard' in low:
            return 'governing_project_truth'
        return 'project_truth_artifact'


def create() -> ProjectTruthReaderAPI:
    return ProjectTruthReaderAPI()
