from __future__ import annotations

from typing import Any, Dict, List


class DeliveryRenderer:
    """Renders final user-visible answer from OperationalInsight.

    This is not a censorship layer. It is a surface translator: project-facing
    answers keep runtime implementation silent; diagnostic answers may expose
    metrics and trace details when the user asks for them.
    """

    def wants_diagnostics(self, request_text: str) -> bool:
        text = (request_text or '').lower()
        return any(t in text for t in ['تقرير', 'تشخيص', 'أرقام', 'ارقام', 'تفاصيل', 'trace', 'audit', 'metrics', 'diagnostic', 'inspect', 'doctor'])

    def render(self, envelope: Any) -> str:
        insight = envelope.operational_insight or {}
        request = envelope.request_text or ''
        wants_diag = self.wants_diagnostics(request)
        lines: List[str] = []

        if self._is_identity_question(request):
            lines.append('داخل هذا العمل أعمل كمهندس مشروع تشغيلي: أفهم النية، أزنها بالحقيقة، أستدعي الطبقات كخدمات خلف نواة تشغيل مركزية واحدة، ثم أحوّل النتائج إلى قرار أو خطة أو تنفيذ لا يتجاوز الحقيقة المتاحة.')
            lines.append('مهامي العملية: تحليل البنية، كشف الفجوات والتعارضات، إنضاج المواصفات، ربط الصلاحيات والحالات والأحداث والبيانات، ثم تحويل الحقيقة الناضجة إلى تنفيذ قابل للاختبار.')

        state = envelope.active_project_state or {}
        if envelope.surface == 'active_project_payload':
            if state.get('state') == 'single_project_detected':
                lines.append('يوجد مشروع نشط محمّل، وأتعامل معه من حقيقته المحلية لا من اسم المجلد أو مسار الملفات.')
            elif state.get('state') == 'no_project_loaded':
                lines.append('لا توجد حقيقة مشروع محمّلة؛ لذلك يكون العمل الصحيح هو تكوين حقيقة المشروع الأولى قبل أي تقييم أو تنفيذ.')

            if insight.get('project_condition') == 'SPEC_ONLY_PROJECT':
                lines.append('وضعه الحالي: قوي كمنظومة مواصفات وحوكمة ومعرفة، لكنه لم يتحول بعد إلى حقيقة تنفيذية مغلقة تصلح للبناء الإنتاجي المباشر.')
            elif insight.get('project_condition'):
                lines.append('وضعه الحالي يحتاج قراءة بحسب النطاق المطلوب، والقرار النهائي يبقى مشروطًا بعمق الحقيقة المطلوب للنية.')

        summary = insight.get('summary') or []
        if summary:
            lines.append('قراءة الحقيقة الحالية:\n' + '\n'.join('- ' + str(x).lstrip('- ').strip() for x in summary[:5]))

        first = insight.get('first_step')
        if first:
            lines.append(first if str(first).startswith('أول خطوة') else 'أول خطوة صحيحة: ' + str(first))

        if wants_diag:
            metrics = self._metrics(envelope)
            if metrics:
                lines.append('مؤشرات تشخيص مختصرة:\n' + '\n'.join(metrics))

        return '\n\n'.join(x for x in lines if x).strip()

    def _metrics(self, envelope: Any) -> List[str]:
        fm = envelope.artifact_matrix or {}
        diag = fm.get('diagnostics') or {}
        trace = envelope.trace or []
        out: List[str] = []
        if fm.get('file_count') is not None:
            out.append(f"- عناصر النطاق المفحوصة: {fm.get('file_count')}")
        if diag.get('issue_count') is not None:
            out.append(f"- إشارات التشخيص: {diag.get('issue_count')} إجمالًا، منها {diag.get('maturity_issue_count', 0)} إنضاجية و{diag.get('blocking_count', 0)} حاسمة.")
        if trace:
            out.append(f"- عقد التشغيل المنجزة في الرسم التشغيلي: {len(trace)}")
        return out

    def validate(self, answer: str, envelope: Any) -> Dict[str, Any]:
        request = envelope.request_text or ''
        wants_diag = self.wants_diagnostics(request)
        issues: List[str] = []
        if not wants_diag:
            # Contextual surface check, not global censorship. These terms are
            # inappropriate only for ordinary project-facing answers.
            for term in ['GPT-5.5', 'ChatGPT', '.zip', 'RUN_TESTS.py', 'aos_core/', 'aos_capabilities/']:
                if term in answer:
                    issues.append(f'project_surface_runtime_leak:{term}')
        if not (envelope.operational_insight or {}).get('summary'):
            issues.append('missing_operational_insight_summary')
        if not (envelope.operational_insight or {}).get('first_step'):
            issues.append('missing_operational_first_step')
        return {'passed': not issues, 'issues': issues, 'policy': 'contextual_surface_translation', 'surface_policy': {'metrics_allowed': wants_diag, 'transform_required': ([] if wants_diag else ['summarize_metrics_as_meaning_not_counts'])}}

    def _is_identity_question(self, request_text: str) -> bool:
        text = (request_text or '').lower()
        return any(term in text for term in ['من أنت', 'من انت', 'وظيفتك', 'مهاراتك', 'دورك', 'عملك', 'عنك', 'who are you'])
