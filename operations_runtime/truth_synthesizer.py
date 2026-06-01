from __future__ import annotations

from typing import Any, Dict, List


class TruthSynthesizer:
    """Builds final OperationalInsight from governed contributions.

    The synthesizer is not a truth source. It only compresses already loaded
    operation contract, scope plan, truth context, and layer contributions into a
    response-ready insight.
    """

    def synthesize(self, envelope: Any, merged: Dict[str, Any], contradictions: List[Dict[str, Any]]) -> Dict[str, Any]:
        by = merged.get('by_layer') or {}
        intent = envelope.intent or {}
        surface = envelope.surface
        artifact = by.get('artifact_cockpit') or by.get('artifact_matrix') or {}
        project_truth = by.get('project_truth') or {}
        truth_context = getattr(envelope, 'truth_context', {}) or {}
        scope_plan = getattr(envelope, 'scope_plan', {}) or {}
        truth_packet = getattr(envelope, 'truth_packet', {}) or {}

        project_identity = self._extract_evidence(project_truth, 'project_identity') or {}
        stack_signal = self._extract_evidence(project_truth, 'stack_signal') or {}
        readiness_signal = self._extract_evidence(project_truth, 'readiness_signal') or {}
        owner_from_project = self._extract_evidence(project_truth, 'primary_owner_candidate') or {}
        owner_from_artifact = self._extract_evidence(artifact, 'owner_signal') or {}
        owner = owner_from_artifact or owner_from_project or {}
        value_map = self._extract_evidence(artifact, 'value_map') or {}
        condition = self._extract_evidence(artifact, 'condition') or (envelope.artifact_matrix or {}).get('project_condition')

        summary: List[str] = []
        if surface == 'aos_environment':
            summary.extend(self._aos_summary(scope_plan, truth_context, truth_packet, by))
            owner = {}
            project_identity = {}
            stack_signal = {}
            readiness_signal = {}
            condition = condition or 'AOS_RUNTIME_SCOPE'
        elif surface == 'active_project_payload':
            summary.extend(self._project_summary(envelope, project_identity, stack_signal, readiness_signal))
        else:
            summary.append('السطح ليس مشروعًا مباشرًا؛ يتم التعامل معه كمنهج أو بيئة معرفة عامة حسب النية وسياق الحقيقة.')

        if surface == 'active_project_payload' and owner.get('label'):
            summary.append(f"العقدة العملية المرشحة الآن هي {owner['label']}؛ لأنها ظهرت كمالك محتمل من الأدلة المحلية لا من افتراض ثابت.")
        if surface == 'active_project_payload' and value_map.get('interpretation') == 'governing_truth_strong_but_execution_truth_not_closed':
            summary.append('قراءة القيمة تقول إن قوة المشروع في المنهج الحاكم، بينما الضعف في إغلاق طبقة الترجمة التنفيذية القابلة للاختبار.')
        if contradictions:
            summary.append('لا يجوز تحويل إشارات النقص أو التشابه إلى منطق مخترع؛ يجب إنضاج مالك الحقيقة أو توثيق التأجيل قبل التنفيذ.')

        first_step = self._first_step(surface, owner, contradictions, condition, truth_context)
        return {
            'type': 'operational_insight',
            'surface': surface,
            'intent_type': intent.get('intent_type'),
            'project_condition': condition,
            'project_identity': project_identity,
            'stack_signal': stack_signal,
            'readiness_signal': readiness_signal,
            'primary_owner': owner,
            'summary': summary[:7],
            'contradictions': contradictions,
            'decision': self._decision(envelope, contradictions, condition, owner, truth_context),
            'first_step': first_step,
            'evidence_mode': 'synthesized_from_layer_contributions',
            'grounding_mode': 'operation_contract_scope_truth_context_and_layer_contributions',
            'source_layers': sorted([k for k in by.keys() if k]),
            'law': 'visible response must be rendered from OperationalInsight after truth arbiter and delivery gate, not raw reports or folder traversal',
        }

    def _aos_summary(self, scope_plan: Dict[str, Any], truth_context: Dict[str, Any], truth_packet: Dict[str, Any], by: Dict[str, Any]) -> List[str]:
        arbiter = (truth_packet.get('arbiter') or {}).get('decision') or 'UNKNOWN'
        sources = truth_context.get('governing_sources') or []
        missing = truth_context.get('missing_required_truth') or []
        registered = sorted([k for k in by.keys() if k])
        out = [
            'الطلب موجّه إلى بنية الوكيل ومركز العمليات؛ لذلك حمولة المشروع النشطة ليست حقيقة رئيسية في هذا المسار.',
            'مركز العمليات يجب أن يعمل كـ microkernel حاكم: ينشئ عقد العملية، يخطط النطاق، يحمّل سياق الحقيقة، يستدعي الطبقات عبر واجهات مركزية، ثم يمنع التسليم غير المؤسس.',
            f"سياق الحقيقة المحمّل هو {truth_context.get('profile') or 'غير محدد'} بعدد مصادر حاكمة {len(sources)}؛ قرار Arbiter الحالي: {arbiter}.",
            f"الطبقات المشاركة عبر السجل التشغيلي: {', '.join(registered) if registered else 'لا توجد مساهمات كافية'}.",
        ]
        if scope_plan.get('active_project_role'):
            out.append(f"دور حمولة المشروع في هذا النطاق: {scope_plan.get('active_project_role')}؛ لا يسمح لها بتوجيه تشخيص الوكيل.")
        if missing:
            out.append('توجد مصادر حوكمة مفقودة أو غير مغلقة؛ يجب إعلان النقص بدل تعويضه بتخمين.')
        return out

    def _project_summary(self, envelope: Any, project_identity: Dict[str, Any], stack_signal: Dict[str, Any], readiness_signal: Dict[str, Any]) -> List[str]:
        summary: List[str] = []
        if envelope.active_project_state.get('state') == 'no_project_loaded':
            summary.append('لا توجد حقيقة مشروع محملة؛ القرار الصحيح هو تكوين حقيقة المشروع الأولى لا تقييم مشروع غير موجود.')
            return summary
        if project_identity.get('name'):
            ptype = project_identity.get('type') or 'مشروع غير مصنف'
            summary.append(f"المشروع المحمّل هو {project_identity.get('name')}، وتصنيفه المحلي: {ptype}.")
        else:
            summary.append('المشروع يملك طبقة حقيقة محلية يمكن الاستناد إليها، لكن لا يجوز افتراض هويته أو جاهزيته دون مصادر حاكمة.')
        stack_parts = [v for v in [stack_signal.get('backend'), stack_signal.get('database'), stack_signal.get('frontend')] if v]
        if stack_parts:
            summary.append('الاتجاه التنفيذي المثبت محليًا: ' + ' / '.join(stack_parts) + '؛ ولا يسمح بتغييره دون قرار معماري.')
        if readiness_signal:
            summary.append('جاهزية التنفيذ مشروطة بإغلاق عقود الترجمة والبوابات والاختبارات، لا بمجرد وجود مواصفات.')
        summary.append('الفجوة الأساسية هي تحويل الحقيقة العليا إلى مواصفات تنفيذية مغلقة: مالك، حدود، حالات، أحداث، صلاحيات، بيانات، واختبارات قبول.')
        return summary

    def _extract_evidence(self, contribution: Dict[str, Any], evidence_type: str) -> Any:
        for ev in contribution.get('evidence') or []:
            if ev.get('type') == evidence_type:
                return ev.get('value')
        return None

    def _decision(self, envelope: Any, contradictions: List[Dict[str, Any]], condition: str | None, owner: Dict[str, Any], truth_context: Dict[str, Any]) -> str:
        if envelope.surface == 'aos_environment':
            if truth_context.get('missing_required_truth'):
                return 'AOS_RUNTIME_ANSWER_WITH_LIMITS_UNTIL_GOVERNING_TRUTH_COMPLETE'
            return 'AOS_RUNTIME_GOVERNANCE_REFACTOR_ALLOWED_FROM_CURRENT_TRUTH'
        if envelope.active_project_state.get('state') == 'no_project_loaded':
            return 'PROJECT_TRUTH_MISSING_FORMATION_MODE'
        if contradictions:
            return 'MATURE_CONFLICTING_OR_INCOMPLETE_TRUTH_BEFORE_EXECUTION'
        if owner.get('label'):
            return 'MATURE_PRIMARY_OWNER_TRUTH_BEFORE_EXECUTION'
        if condition == 'SPEC_ONLY_PROJECT':
            return 'SPECIFICATION_MATURITY_REQUIRED_BEFORE_CODE'
        return 'ANSWER_ALLOWED_FROM_CURRENT_INSIGHT'

    def _first_step(self, surface: str, owner: Dict[str, Any], contradictions: List[Dict[str, Any]], condition: str | None, truth_context: Dict[str, Any]) -> str:
        if surface == 'aos_environment':
            if truth_context.get('missing_required_truth'):
                return 'أول خطوة صحيحة: أغلق مصادر الحوكمة المفقودة في سياق الحقيقة ثم ثبّت معيار تشغيل الطبقات قبل أي إنضاج منفرد للطبقات.'
            return 'أول خطوة صحيحة: ثبّت AOS Layer Runtime Standard داخل مركز العمليات: OperationContract، ScopePlan، TruthContext، LayerGateway، LayerResult، TruthArbiter، وDeliveryGroundingGate.'
        if owner.get('label'):
            return f"ابدأ بإنضاج عقدة {owner['label']} كحقيقة مالكة: ثبّت الحدود، الفروع التابعة، الحالات، الصلاحيات، الأحداث، البيانات، وقواعد القبول قبل أي كود."
        if contradictions:
            return 'ابدأ بإغلاق التناقض أو الوعد المفقود الذي يمنع بناء قرار تنفيذي آمن.'
        if condition == 'SPEC_ONLY_PROJECT':
            return 'اختر عقدة مالكة واحدة وحوّلها من مواصفة عامة إلى مواصفة تنفيذية قابلة للاختبار.'
        return 'ابنِ حزمة حقيقة محددة للنطاق المطلوب ثم انتقل إلى التنفيذ المشروط بالتحقق.'
