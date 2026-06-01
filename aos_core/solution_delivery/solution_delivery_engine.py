from __future__ import annotations

from typing import Any, Dict, List

from aos_core.solution_delivery.response_contract_enforcer import ResponseContractEnforcer


class SolutionDeliveryEngine:
    """Synthesizes visible responses from an operation packet.

    Delivery is a visible-surface translator, not a raw packet dumper. It must
    preserve the silent operating environment, avoid generic model identity, and
    express identity/status through operational truth rather than hardcoded
    prohibitions or internal paths.
    """

    def __init__(self) -> None:
        self.enforcer = ResponseContractEnforcer()

    def synthesize(self, packet: Dict[str, Any]) -> str:
        surface = packet['intent']['surface']
        active = packet['scope']['active_project_state']
        fm = packet['file_matrix']
        raw_request = (packet.get('intent', {}) or {}).get('raw_request', '')
        lines: List[str] = []

        if surface == 'aos_environment':
            lines.extend(self._aos_surface_answer(packet))
        elif surface == 'workshop_general_truth':
            lines.extend(self._workshop_surface_answer(packet))
        else:
            lines.extend(self._project_surface_answer(packet, active, fm, raw_request))

        answer = '\n\n'.join([x for x in lines if x])
        check = self.enforcer.enforce(answer, packet)
        packet['response_contract_check'] = check
        if not check['passed']:
            return 'أتعامل مع الطلب من سطحه الصحيح وبناءً على الحقيقة المتاحة. فحص عقد الاستجابة منع صياغة قد تخلط بين هوية الوكيل أو المشروع أو بيئة التشغيل.'
        return answer

    def _aos_surface_answer(self, packet: Dict[str, Any]) -> List[str]:
        return [
            'السطح هنا هو بيئة الوكيل نفسها. أتعامل معها كبيئة تشغيل صامتة لها دستور وهوية وطبقات وقدرات، لا كمشروع المستخدم.',
            'التقييم يكون على وضوح الهوية التشغيلية، سلامة الفصل بين الكور والقدرات، كفاية الحقيقة، وحوكمة التعديل والفحص.',
            'أي إصلاح للبيئة يجب أن يمر عبر فحص المالك والأثر والتعارض، ثم بوابة تعديل واختبار وإيصال تشغيل.',
        ]

    def _workshop_surface_answer(self, packet: Dict[str, Any]) -> List[str]:
        return [
            'السطح هنا هو ورشة العمل العامة. أتعامل معها كمنهاج ومعايير عامة تساعد أي مشروع على توليد حقيقته المحلية، لا كبديل عن حقيقة المشروع.',
            'أي معيار عام لا يصبح قانونًا خاصًا بمشروع معين إلا بعد تخصيصه داخل حقيقة ذلك المشروع وربطه بسياقه وقيوده.',
        ]

    def _project_surface_answer(self, packet: Dict[str, Any], active: Dict[str, Any], fm: Dict[str, Any], raw_request: str) -> List[str]:
        lines: List[str] = []
        identity_requested = self._is_identity_question(raw_request)
        insight = ((packet.get('operations') or {}).get('operational_insight') or {})
        condition = insight.get('project_condition') or fm.get('project_condition')
        cognition = packet.get('intent_cognition') or {}
        artifact_need = ((cognition.get('layer_needs') or {}).get('artifact_cockpit') or '')
        simple_identity_only = identity_requested and artifact_need == 'none_or_cached_identity_truth'

        if identity_requested:
            lines.append(
                'هويتي التشغيلية داخل هذا العمل هي مهندس مشروع يعمل من حقيقة المشروع، لا من هوية نموذج عامة. '
                'وظيفتي أن أفهم المقصد، أبني حزمة حقيقة كافية، أكشف النقص والتعارض، ثم أقدّم قرارًا أو خطة أو تنفيذًا لا يتجاوز الحقيقة المتاحة.'
            )

        if not simple_identity_only:
            if active.get('state') == 'single_project_detected':
                lines.append('يوجد مشروع نشط محمّل حاليًا، وأتعامل معه من حقيقته المحلية لا من اسم المجلد أو مساره.')
            elif active.get('state') == 'no_project_loaded':
                lines.append('لا يوجد مشروع نشط محمّل حاليًا. في هذه الحالة أعمل بوضع تكوين مشروع: نثبت الهدف، النطاق، المستخدمين، القيود، المخرجات، ومعايير النجاح قبل أي تنفيذ.')
            elif active.get('state') == 'project_path_missing':
                lines.append('بوابة المشروع النشط غير مهيأة بعد، لذلك لا أستطيع اعتبار أي محتوى مشروعًا فعليًا.')
            else:
                lines.append('مادة المشروع النشط غير محسومة بعد؛ أتعامل معها كوضع اكتشاف قبل أي حكم تنفيذي.')

            lines.append(self._condition_sentence(condition))

        identity_lines = self._identity_capabilities(raw_request)
        if identity_requested and identity_lines:
            lines.append('عملي معك عمليًا:\n' + '\n'.join(identity_lines))

        if not simple_identity_only:
            insight_summary = self._insight_summary(packet)
            if insight_summary:
                lines.append('قراءة الحقيقة الحالية:\n' + '\n'.join(insight_summary))
            else:
                truth_summary = self._natural_truth_summary(packet)
                if truth_summary:
                    lines.append('قراءة الحقيقة الحالية:\n' + '\n'.join(truth_summary))

            metric_summary = self._contextual_metric_summary(packet, raw_request)
            if metric_summary:
                lines.append('مؤشرات تشخيص مختصرة:\n' + '\n'.join(metric_summary))

            priority = self._insight_first_step(packet) or self._first_step(packet)
            if priority:
                lines.append(priority)

        return lines


    def _contextual_metric_summary(self, packet: Dict[str, Any], raw_request: str) -> List[str]:
        text = (raw_request or '').lower()
        wants_metrics = any(term in text for term in ['عدد','أرقام','ارقام','تقرير','تشخيص','إحصاء','احصاء','تفاصيل','audit','report','metrics','diagnostic'])
        if not wants_metrics:
            return []
        fm = packet.get('file_matrix') or {}
        diag = fm.get('diagnostics') or {}
        summary = fm.get('summary') or {}
        out: List[str] = []
        file_count = fm.get('file_count') or summary.get('file_count')
        if file_count is not None:
            out.append(f'- حجم مادة المشروع المفحوصة: {file_count} عنصرًا دلاليًا/ملفًا ضمن النطاق الحالي.')
        if diag.get('issue_count') is not None:
            out.append(f"- إشارات التشخيص: {diag.get('issue_count')} إجمالًا، منها {diag.get('maturity_issue_count', 0)} تحتاج إنضاجًا، و{diag.get('blocking_count', 0)} عوائق حاسمة.")
        tv = (fm.get('truth_value_semantics') or {})
        if tv.get('empty_declared_target_count'):
            out.append(f"- أهداف بناء معلنة غير مكتملة: {tv.get('empty_declared_target_count')}.")
        if tv.get('declared_missing_artifact_count'):
            out.append(f"- وعود حقيقة مذكورة ولم تُغلق: {tv.get('declared_missing_artifact_count')}.")
        return out


    def _insight_summary(self, packet: Dict[str, Any]) -> List[str]:
        insight = ((packet.get('operations') or {}).get('operational_insight') or {})
        out: List[str] = []
        for item in insight.get('summary', [])[:6]:
            if item:
                out.append('- ' + item if not str(item).strip().startswith('-') else str(item))
        return out

    def _insight_first_step(self, packet: Dict[str, Any]) -> str | None:
        insight = ((packet.get('operations') or {}).get('operational_insight') or {})
        step = insight.get('first_step')
        if step:
            return 'أول خطوة صحيحة: ' + step if not str(step).strip().startswith('أول خطوة') else str(step)
        return None

    def _condition_sentence(self, condition: str | None) -> str:
        if condition == 'SPEC_ONLY_PROJECT':
            return 'حالته الحالية: مشروع مواصفات ومعرفة منظمة، وليس بعد مشروعًا تنفيذيًا جاهزًا للكود الإنتاجي.'
        if condition == 'EMPTY_NEW_PROJECT':
            return 'حالته الحالية: مشروع جديد أو فارغ يحتاج تكوين الحقيقة الأولى قبل التقييم أو التنفيذ.'
        if condition == 'ACTIVE_ENGINEERING_PROJECT':
            return 'حالته الحالية: مشروع هندسي نشط يحتوي مادة قابلة للفحص والتنفيذ المشروط.'
        if condition == 'LEGACY_COMPLEX_PROJECT':
            return 'حالته الحالية: مشروع معقد أو موروث يحتاج فحص ترابط وأثر قبل أي تغيير.'
        return f'حالته الحالية مصنفة داخليًا كـ {condition or "غير محسومة"}.'

    def _identity_capabilities(self, raw_request: str) -> List[str]:
        return [
            '- أتعامل مع الملفات كأدلة ومعاني مترابطة، لا كأسماء أو أحجام فقط.',
            '- أميز بين الحقيقة المكتملة، الحقيقة الناقصة، هدف البناء الفارغ، والوعد المفقود.',
            '- لا أقفز إلى الكود أو السيناريو إذا كانت الحقيقة المالكة غير ناضجة.',
            '- أستخدم ورشة العمل كعدسة صامتة، وأجعل الرد الظاهر مركزًا على مشروعك وسؤالك.',
            '- عند التعارض لا أخترع بديلًا؛ أحدد مالك الحقيقة المطلوب إنضاجه أولًا.',
        ]

    def _natural_truth_summary(self, packet: Dict[str, Any]) -> List[str]:
        truth_packet = ((packet.get('truth') or {}).get('packet') or {})
        truth_value = truth_packet.get('truth_value_semantics') or {}
        incomplete = truth_packet.get('incomplete_truth') or {}
        fm = packet.get('file_matrix') or {}
        diagnostics = fm.get('diagnostics') or {}
        out: List[str] = []

        empty_count = truth_value.get('empty_declared_target_count', 0) or 0
        missing_count = truth_value.get('declared_missing_artifact_count', 0) or 0
        maturity_count = incomplete.get('maturity_issue_count', 0) or diagnostics.get('maturity_issue_count', 0) or 0
        issue_count = diagnostics.get('issue_count', 0) or 0

        if empty_count:
            out.append(f'- توجد أهداف بناء معلنة لم تُنضج بعد ({empty_count}). هذه ليست فشلًا عشوائيًا، ولا يجوز ملؤها بالتخمين.')
        if missing_count:
            out.append(f'- توجد وعود حقيقة مذكورة ولم تُغلق بملفات/أدلة مقابلة ({missing_count})، وهذا يحتاج إصلاحًا أو تأجيلًا موثقًا.')
        duplicate = self._duplicate_functional_truth(packet)
        if duplicate:
            out.append(duplicate)
        if maturity_count:
            out.append(f'- توجد حقائق ناقصة تؤثر على أي تنفيذ إنتاجي ({maturity_count})؛ المسموح الآن هو التشخيص والإنضاج لا بناء منطق نهائي فوقها.')
        if issue_count:
            out.append(f'- الفحص وجد إشارات ضعف تحتاج ترتيبًا، لكن لا توجد إشارة إلى عائق قاتل يمنع الإنضاج المرحلي.')
        if not out:
            out.append('- الحقيقة الحالية كافية للحديث العام، لكن أي تنفيذ سيحتاج فحصًا أعمق حسب النطاق.')
        return out

    def _duplicate_functional_truth(self, packet: Dict[str, Any]) -> str | None:
        diagnostics = ((packet.get('file_matrix') or {}).get('diagnostics') or {})
        top = diagnostics.get('top_issues') or []
        for issue in top:
            if issue.get('code') == 'duplication.exact_duplicates':
                examples = (issue.get('evidence') or {}).get('examples') or []
                if examples:
                    return '- توجد نسخ متطابقة أو شديدة التشابه بين مسارات يفترض أن تمثل حقائق وظيفية مختلفة؛ هذا لا يسمح بتخمين الفرق، بل يفرض إنضاج الحقيقة المالكة قبل أي تنفيذ مرتبط.'
        return None

    def _first_step(self, packet: Dict[str, Any]) -> str:
        truth_packet = ((packet.get('truth') or {}).get('packet') or {})
        truth_value = truth_packet.get('truth_value_semantics') or {}
        missing = truth_value.get('declared_missing_artifact_count', 0) or 0
        empty = truth_value.get('empty_declared_target_count', 0) or 0
        duplicate = self._duplicate_functional_truth(packet)
        if duplicate:
            return 'أول خطوة صحيحة: لا أبدأ بالكود ولا أختار ملفًا طويلًا كحقيقة نهائية. أبدأ بحسم الحقيقة المالكة للتكرار الوظيفي: هل هو هدف بناء مؤجل، نسخة مكررة، أم مسار مستقل يحتاج تعريفًا خاصًا؛ ثم فقط أتحول إلى مواصفة تنفيذية واحدة قابلة للاختبار.'
        if missing:
            return 'أول خطوة صحيحة: إغلاق الوعود المفقودة في خريطة الحقيقة، إما بإنشاء ملفاتها المالكة أو توثيق تأجيلها، قبل بناء منطق يعتمد عليها.'
        if empty:
            return 'أول خطوة صحيحة: تحويل أهداف البناء الفارغة إلى خطة إنضاج مرتبة، ثم اختيار هدف واحد وتحويله إلى حقيقة تنفيذية لا تقبل التخمين.'
        return 'أول خطوة صحيحة: تحديد نطاق صغير، بناء حزمة حقيقة كافية له، ثم الانتقال إلى خطة تنفيذ مشروطة بالتحقق.'

    def _is_identity_question(self, raw_request: str) -> bool:
        text = (raw_request or '').lower()
        return any(term in text for term in ['من أنت', 'من انت', 'ما دورك', 'مين أنت', 'who are you', 'your role', 'وظيفتك', 'مهاراتك', 'عنك', 'عملك', 'دورك'])
