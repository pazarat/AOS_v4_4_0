from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
import hashlib
import re
from typing import Any, Dict, List

from aos_core.contracts import IntentFrame


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _stable_id(prefix: str, text: str) -> str:
    return f"{prefix}_{hashlib.sha1(text.encode('utf-8')).hexdigest()[:12]}"


@dataclass
class IntentCognitionPacket:
    id: str
    created_at: str
    raw_request: str
    user_goal: str
    expressed_diagnosis: Dict[str, Any]
    initial_intent_status: str
    signal_interpretation: Dict[str, Any]
    continuity: Dict[str, Any]
    truth_grounding: Dict[str, Any]
    layer_needs: Dict[str, Any]
    forbidden_motion: List[str]
    spine_flow: List[str]
    next_runtime_step: str


class IntentCognitionRuntime:
    """Turns captured intent into operational cognition, not a route or template.

    Core law: initial intent is a hypothesis. It must be grounded by truth before
    it becomes a decision, an execution, or a project claim. User wording may be
    diagnosis, metaphor, symptom, signal, or constraint; it is not automatically
    an implementation command.
    """

    REPEATED_FAILURE_TERMS = {
        'لم ينجح', 'مازال', 'ما زال', 'لا يزال', 'لم يتحسن', 'نفس المشكلة', 'فشل', 'فشلنا',
        'عدة اصدارات', 'عدة إصدارات', 'ترقيع', 'كل مرة', 'مرة اخرى', 'مرة أخرى', 'لا يعالج',
        'غرق', 'عنق الزجاجة', 'bottleneck', 'still fails', 'not fixed', 'regression'
    }
    METAPHOR_TERMS = {
        'قمرة', 'الشريان', 'شريان', 'فتح الشرايين', 'نفق', 'الدم', 'المتاهة', 'متاهات',
        'أبجدية', 'قلب', 'عروق', 'جراحة', 'مصنع', 'خط الانتاج', 'cockpit', 'artery', 'spine'
    }
    DIAGNOSIS_HINTS = {
        'المشكلة في', 'الخلل في', 'سبب المشكلة', 'اعتقد', 'أعتقد', 'اظن', 'أظن', 'اتوقع',
        'يبدو', 'ربما', 'maybe', 'probably', 'i think', 'i suspect'
    }
    PROJECT_TERMS = {'مشروعي', 'المشروع', 'المشروع الحالي', 'project', 'active project'}
    IDENTITY_TERMS = {'من أنت', 'من انت', 'وظيفتك', 'دورك', 'مهاراتك', 'عملك', 'who are you', 'your role'}

    def build(self, request_text: str, intent: IntentFrame | Dict[str, Any], active_project_state: Dict[str, Any] | None = None, truth_requirement: Dict[str, Any] | None = None) -> Dict[str, Any]:
        frame = intent if isinstance(intent, IntentFrame) else None
        intent_data = asdict(frame) if frame else dict(intent or {})
        text = request_text or intent_data.get('raw_request', '') or ''
        lower = text.lower()
        surface = intent_data.get('surface', 'active_project_payload')
        intent_type = intent_data.get('intent_type', 'operate_project')
        active_state = (active_project_state or {}).get('state')

        repeated = self._has_any(lower, self.REPEATED_FAILURE_TERMS)
        metaphor_hits = sorted([term for term in self.METAPHOR_TERMS if term.lower() in lower])
        diagnosis_like = self._has_any(lower, self.DIAGNOSIS_HINTS)
        identity_like = self._has_any(lower, self.IDENTITY_TERMS)
        asks_project_status = bool(self._has_any(lower, self.PROJECT_TERMS) and any(t in lower for t in ['تقييم', 'قيم', 'قيّم', 'وضع', 'حالة', 'تعامل', 'كيف']))

        artifact_need = self._artifact_need(intent_type, lower, surface, identity_like, asks_project_status, repeated)
        goal_need = self._goal_need(intent_type, surface, repeated)
        truth_depth = (truth_requirement or {}).get('truth_depth')
        if truth_depth is None:
            truth_depth = self._default_truth_depth(intent_type, artifact_need, goal_need)

        user_goal = self._derive_user_goal(intent_type, surface, identity_like, asks_project_status, repeated)
        if surface == 'active_project_payload' and active_state == 'no_project_loaded':
            truth_alignment = 'intent_points_to_project_but_no_project_truth_loaded'
        else:
            truth_alignment = 'pending_truth_runtime_grounding'

        packet = IntentCognitionPacket(
            id=_stable_id('intent_cognition', text + surface + intent_type),
            created_at=_now(),
            raw_request=text,
            user_goal=user_goal,
            expressed_diagnosis={
                'present': bool(diagnosis_like or repeated),
                'status': 'user_diagnosis_is_signal_not_verified_cause',
                'law': 'the user request may describe a symptom or suspected cause; verified cause must come from truth and evidence',
            },
            initial_intent_status='hypothesis_not_decision',
            signal_interpretation={
                'metaphor_or_signal_detected': bool(metaphor_hits),
                'signals': metaphor_hits[:12],
                'law': 'user metaphors and scattered descriptions are design signals, not literal architecture instructions',
                'conversion_required': 'signal_to_standard_before_action',
            },
            continuity={
                'conversation_context_available': False,
                'repeated_failure_signal': repeated,
                'meaning': 'activate deeper goal/root-cause handling only when repeated failure or high-impact task is present',
            },
            truth_grounding={
                'required_before_decision': True,
                'truth_alignment': truth_alignment,
                'truth_depth': truth_depth,
                'law': 'intent capture must be weighed against truth before any decision, project claim, repair, or execution',
            },
            layer_needs={
                'artifact_cockpit': artifact_need,
                'goal_runtime': goal_need,
                'truth_runtime': 'required',
                'surface_runtime': 'required',
                'delivery_runtime': 'required',
            },
            forbidden_motion=[
                'convert_initial_intent_directly_to_action',
                'treat_user_diagnosis_as_verified_cause',
                'literalize_metaphor_as_file_or_layer_name',
                'open_deep_artifact_scan_for_simple_identity_or_status_without_truth_need',
                'activate_goal_runtime_for_ordinary_questions',
                'answer_project_question_when_no_project_truth_exists',
            ],
            spine_flow=[
                'entry', 'operating_identity', 'intent_cognition', 'surface_awareness',
                'truth_requirement', 'artifact_cockpit_if_needed', 'goal_runtime_if_justified', 'delivery'
            ],
            next_runtime_step='truth_requirement_then_artifact_cockpit_if_needed',
        )
        return asdict(packet)

    def validate_spine_flow(self, packet: Dict[str, Any]) -> Dict[str, Any]:
        needs = packet.get('layer_needs') or {}
        violations: List[str] = []
        if packet.get('initial_intent_status') != 'hypothesis_not_decision':
            violations.append('initial_intent_not_marked_as_hypothesis')
        if not (packet.get('truth_grounding') or {}).get('required_before_decision'):
            violations.append('truth_grounding_not_required')
        if needs.get('goal_runtime') == 'required' and not (packet.get('continuity') or {}).get('repeated_failure_signal'):
            # High-impact execution may also require goal; the runtime may set maybe_required.
            violations.append('goal_runtime_required_without_repeated_failure_signal')
        return {'passed': not violations, 'violations': violations, 'rule': 'intent_cognition_spine_flow'}

    def _artifact_need(self, intent_type: str, lower: str, surface: str, identity_like: bool, asks_project_status: bool, repeated: bool) -> str:
        if intent_type in {'inspect'} or any(t in lower for t in ['افحص الملفات', 'doctor', 'inspect', 'scan']):
            return 'explicit_diagnostic'
        if intent_type in {'implement', 'repair', 'refactor', 'self_develop_aos'}:
            return 'deep_required'
        if repeated:
            return 'focused_root_cause'
        if identity_like and not asks_project_status:
            return 'none_or_cached_identity_truth'
        if asks_project_status or intent_type in {'evaluate', 'operate_project'}:
            return 'hot_truth_packet_only'
        return 'hot_truth_packet_only'

    def _goal_need(self, intent_type: str, surface: str, repeated: bool) -> str:
        if repeated:
            return 'required_for_repeated_failure_or_root_cause'
        if intent_type in {'implement', 'repair', 'refactor', 'self_develop_aos'}:
            return 'maybe_required_for_high_impact_task'
        return 'not_required_for_normal_answer'

    def _default_truth_depth(self, intent_type: str, artifact_need: str, goal_need: str) -> int:
        if 'deep' in artifact_need or 'required' in goal_need or intent_type in {'implement', 'repair', 'refactor', 'self_develop_aos'}:
            return 5
        if artifact_need == 'focused_root_cause':
            return 4
        if artifact_need == 'hot_truth_packet_only':
            return 2
        return 1

    def _derive_user_goal(self, intent_type: str, surface: str, identity_like: bool, asks_project_status: bool, repeated: bool) -> str:
        if repeated:
            return 'resolve_repeated_failure_by_identifying_verified_cause_not_by_patching_symptoms'
        if identity_like and asks_project_status:
            return 'understand_operational_role_and_current_project_condition'
        if identity_like:
            return 'understand_operational_role'
        if intent_type in {'implement', 'repair', 'refactor'}:
            return 'change_or_repair_only_after_truth_grounding'
        if surface == 'aos_environment':
            return 'understand_or_improve_engineer_environment'
        if surface == 'workshop_general_truth':
            return 'understand_general_workshop_method_or_standard'
        return 'understand_or_operate_active_project_truthfully'

    def _has_any(self, text: str, terms: set[str]) -> bool:
        return any(term.lower() in text for term in terms)
