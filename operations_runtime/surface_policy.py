from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Dict, Iterable


@dataclass(frozen=True)
class SurfacePolicyDecision:
    surface: str
    reason: str
    confidence: str
    active_payload_visibility: str
    allow_active_payload_state: bool
    allow_active_payload_truth: bool

    def to_dict(self) -> Dict[str, object]:
        return asdict(self)


class SurfacePolicyResolver:
    """Deterministic pre-intent surface guard owned by Operations Runtime.

    This resolver runs before active payload loading and before layer fan-out. It
    is deliberately small and conservative: runtime/agent/governance language
    wins early so the kernel does not leak into active-project truth by default.
    """

    AOS_TERMS = {
        'aos', 'runtime', 'kernel', 'microkernel', 'agent', 'agentic',
        'operations runtime', 'operation center', 'control room', 'truth layer',
        'layer runtime', 'layer gateway', 'governance kernel',
        'الوكيل', 'وكيل', 'وكيل المشاريع', 'وكيل مشاريع', 'مركز العمليات',
        'غرفة العمليات', 'النواة', 'القلب والعقل', 'طبقة الحقيقة', 'طبقة الهدف',
        'طبقة الملفات', 'طبقة معالجة الملفات', 'طبقات', 'الطبقات', 'بيئة التشغيل',
        'الحوكمة', 'حوكمة التشغيل', 'الدستور التشغيلي', 'الرد عبر حقيقة',
        'طبقة الوكيل', 'معمارية الوكيل', 'هوية البيئة', 'الأداء', 'الاداء',
    }
    WORKSHOP_TERMS = {'workshop', 'ورشة العمل', 'الحقيقة العامة', 'معايير الورشة', 'منهج عام'}

    PROJECT_TERMS = {
        'مشروعي', 'المشروع الحالي', 'active project', 'project payload',
        'ملفات المشروع', 'بنية المشروع', 'معمارية المشروع', 'كود المشروع',
    }

    def resolve(self, request_text: str) -> SurfacePolicyDecision:
        text = (request_text or '').lower()
        if self._contains_any(text, self.AOS_TERMS):
            return SurfacePolicyDecision(
                surface='aos_environment',
                reason='runtime_or_agent_terms_detected_before_payload_loading',
                confidence='high',
                active_payload_visibility='metadata_only_no_name_no_root',
                allow_active_payload_state=False,
                allow_active_payload_truth=False,
            )
        if self._contains_any(text, self.WORKSHOP_TERMS):
            return SurfacePolicyDecision(
                surface='workshop_general_truth',
                reason='workshop_or_general_method_terms_detected',
                confidence='high',
                active_payload_visibility='excluded_unless_application_requested',
                allow_active_payload_state=False,
                allow_active_payload_truth=False,
            )
        return SurfacePolicyDecision(
            surface='active_project_payload',
            reason='no_runtime_or_workshop_terms_detected; default project surface',
            confidence='medium' if self._contains_any(text, self.PROJECT_TERMS) else 'low_default',
            active_payload_visibility='primary_truth_when_loaded',
            allow_active_payload_state=True,
            allow_active_payload_truth=True,
        )

    def _contains_any(self, text: str, terms: Iterable[str]) -> bool:
        return any(term.lower() in text for term in terms)
