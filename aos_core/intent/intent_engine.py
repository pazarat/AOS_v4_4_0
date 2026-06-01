from __future__ import annotations

import re
from dataclasses import asdict
from typing import Any, Dict, Iterable, List

from aos_core.contracts import IntentFrame
from aos_core.surface.surface_resolver import SurfaceResolver


class IntentEngine:
    """Mandatory intent intake layer with context-aware surface detection."""

    AOS_EXPLICIT_TERMS = {
        'aos', 'agent os', 'engineer os', 'runtime', 'kernel', 'stategraph', 'event store',
        'policy engine', 'truth manager', 'operational identity', 'identity sync', 'bootstrap',
        'بيئة الوكيل', 'بيئة المهندس', 'النظام التشغيلي', 'نظام التشغيل', 'النواة',
        'الهوية التشغيلية', 'بروتوكول المهندس', 'طبقة النية', 'طبقة الهدف', 'تطوير بيئة المهندس',
        'وكيل المهندس', 'مهندس المشاريع', 'agentic operating system', 'الوكيل', 'وكيل مشاريع', 'وكيل المشاريع', 'مركز العمليات', 'غرفة العمليات', 'طبقة الحقيقة', 'طبقة الملفات', 'طبقة معالجة الملفات', 'الطبقات', 'حوكمة التشغيل', 'الحوكمة',
    }
    WORKSHOP_TERMS = {
        'workshop', 'ورشة العمل', 'الحقيقة العامة', 'معايير عامة', 'منهج عام', 'general truth',
        'global standards', 'workshop standards', 'معايير الورشة'
    }
    PROJECT_TERMS = {
        'المشروع', 'مشروعي', 'المشروع الحالي', 'active project', 'project architecture', 'معمارية المشروع',
        'بنية المشروع', 'ملفات المشروع', 'الكود', 'codebase'
    }

    SELF_DEVELOPMENT_TERMS = {
        'تطوير بيئة المهندس', 'صيانة بيئة المهندس', 'إصلاح بيئة المهندس', 'اصلاح بيئة المهندس', 'اصلاح مركز العمليات', 'إصلاح مركز العمليات', 'انضاج المعمارية', 'إنضاج المعمارية',
        'طور aos', 'تطوير aos', 'حسن aos', 'حسّن aos', 'اصلح aos', 'إصلاح aos', 'اصلاح aos', 'أصلح aos',
        'repair aos', 'fix aos', 'improve aos', 'upgrade aos', 'self development', 'self-develop',
        'stable base', 'اصدار مستقر', 'إصدار مستقر', 'النسخة القادمة'
    }

    MODIFY_TERMS = {
        'اكتب', 'عدل', 'عدّل', 'اصلح', 'أصلح', 'إصلاح', 'اصلاح', 'حسن', 'حسّن', 'نفذ', 'ابن', 'بناء',
        'generate', 'create', 'implement', 'fix', 'repair', 'refactor', 'modify', 'write', 'patch'
    }
    INSPECT_TERMS = {'افحص', 'حلل', 'راجع', 'اكتشف', 'inspect', 'analyze', 'review', 'scan'}
    EXPLAIN_TERMS = {'اشرح', 'وضح', 'ماهي', 'ما هو', 'لماذا', 'explain', 'describe'}
    DOC_TERMS = {'وثق', 'اكتب وثيقة', 'document', 'docs', 'readme'}
    EVAL_TERMS = {'قيم', 'قيّم', 'اختبر', 'test', 'evaluate', 'benchmark'}

    def __init__(self) -> None:
        self.surface_resolver = SurfaceResolver()

    def resolve(self, raw_request: str, file_matrix: Dict[str, Any] | None = None) -> IntentFrame:
        text = (raw_request or '').strip()
        lowered = text.lower()
        surface = self._resolve_surface(lowered)
        explicit_aos = surface == 'aos_environment'
        explicit_workshop = surface == 'workshop_general_truth'
        self_develop = explicit_aos and self._contains_any(lowered, self.SELF_DEVELOPMENT_TERMS)
        may_modify = self._contains_any(lowered, self.MODIFY_TERMS)
        requires_file_access = bool(file_matrix) or self._contains_any(lowered, self.INSPECT_TERMS | self.MODIFY_TERMS | self.EVAL_TERMS)

        if self_develop:
            intent_type = 'self_develop_aos'
            target = 'aos_environment'
            entrypoint = 'self_development_governed_flow'
            risk_level = 'high' if may_modify else 'medium'
        elif explicit_aos:
            intent_type = self._type_from_terms(lowered, default='runtime_architecture_or_governance')
            target = 'aos_environment'
            entrypoint = 'aos_runtime_flow'
            risk_level = 'medium' if may_modify else 'read_only'
        elif explicit_workshop:
            intent_type = self._type_from_terms(lowered, default='workshop_method_or_standard')
            target = 'workshop_general_truth'
            entrypoint = 'workshop_method_flow'
            risk_level = 'medium' if may_modify else 'read_only'
        else:
            intent_type = self._type_from_terms(lowered, default='operate_project')
            target = 'active_project'
            surface = 'active_project_payload'
            entrypoint = 'active_project_surface_flow'
            risk_level = 'medium' if may_modify else 'read_only'

        ambiguity = self._ambiguity(text, surface, file_matrix)
        truth_requirements = self._truth_requirements(intent_type, surface)
        must_not_do = [
            'present_general_model_identity_as_primary_identity',
            'promote_assumption_to_fact_without_source',
            'mutate_any_surface_without_policy_approval_validation',
            'treat_documented_content_as_execution_ready_without_maturity_check',
            'force_parent_child_or_any_single_structure_on_all_projects',
        ]
        if surface == 'active_project_payload':
            must_not_do += ['expose_aos_internal_layers_unless_requested', 'treat_workshop_standard_as_local_project_truth_without_specialization']
        if intent_type == 'self_develop_aos':
            must_not_do.append('allow_aos_to_bypass_aos_governance')

        frame = IntentFrame(
            raw_request=text,
            intent_type=intent_type,
            target=target,
            surface=surface,
            entrypoint=entrypoint,
            risk_level=risk_level,
            explicit_aos_intent=explicit_aos,
            requires_file_access=requires_file_access,
            may_modify_files=may_modify,
            ambiguity_level=ambiguity,
            truth_requirements=truth_requirements,
            must_not_do=must_not_do,
            identity_behavior='suppress_generic_identity_use_operational_context',
        )
        return self.surface_resolver.bind(frame)

    def _resolve_surface(self, text: str) -> str:
        # Explicit runtime/self-development wins only when environment terms are present.
        if self._contains_any(text, self.SELF_DEVELOPMENT_TERMS) or self._contains_any(text, self.AOS_EXPLICIT_TERMS):
            # Do not misroute project architecture questions merely because they contain "architecture".
            if any(t in text for t in ['معمارية المشروع', 'بنية المشروع', 'project architecture', 'architecture of the project']):
                return 'active_project_payload'
            return 'aos_environment'
        if self._contains_any(text, self.WORKSHOP_TERMS):
            return 'workshop_general_truth'
        return 'active_project_payload'

    def summary(self, frame: IntentFrame) -> Dict[str, Any]:
        data = asdict(frame)
        data['routing_rule'] = {
            'aos_environment': 'AOS/runtime surface selected because the request explicitly targets the engineer environment or self-development.',
            'workshop_general_truth': 'Workshop surface selected because the request explicitly targets general standards/methods.',
            'active_project_payload': 'Default active-project payload surface selected; AOS and Workshop are silent support lenses.'
        }.get(frame.surface, 'surface resolved')
        return data

    def _contains_any(self, text: str, terms: Iterable[str]) -> bool:
        return any(term.lower() in text for term in terms)

    def _type_from_terms(self, text: str, default: str) -> str:
        if self._contains_any(text, self.EXPLAIN_TERMS):
            return 'explain'
        if self._contains_any(text, self.INSPECT_TERMS):
            return 'inspect'
        if self._contains_any(text, self.EVAL_TERMS):
            return 'evaluate'
        if self._contains_any(text, self.DOC_TERMS):
            return 'document'
        if any(t in text for t in ['اصلح', 'أصلح', 'fix', 'repair']):
            return 'repair'
        if any(t in text for t in ['refactor', 'إعادة هيكلة', 'اعادة هيكلة']):
            return 'refactor'
        if any(t in text for t in ['ابن', 'بناء', 'implement', 'نفذ']):
            return 'implement'
        if any(t in text for t in ['خطة', 'خطط', 'plan']):
            return 'plan'
        return default

    def _ambiguity(self, text: str, surface: str, file_matrix: Dict[str, Any] | None) -> str:
        if not text:
            return 'high'
        if len(text.split()) < 3 and surface == 'active_project_payload':
            return 'medium'
        if file_matrix and file_matrix.get('project_condition') == 'EMPTY_NEW_PROJECT' and surface == 'active_project_payload':
            return 'medium'
        return 'low'

    def _truth_requirements(self, intent_type: str, surface: str) -> List[str]:
        base = ['operational_identity', 'system_truth']
        if surface == 'aos_environment':
            base += ['system_constitution', 'architecture_contract', 'self_development_truth']
        elif surface == 'workshop_general_truth':
            base += ['workshop_manifest', 'workshop_canons', 'applicability_rules']
        else:
            base += ['project_local_truth', 'active_project_payload_evidence', 'workshop_applicability_lens', 'file_matrix']
        if intent_type in {'implement', 'repair', 'refactor', 'self_develop_aos'}:
            base += ['policy_decision', 'approval_gate', 'patch_gate', 'evaluation_plan']
        return sorted(set(base))
