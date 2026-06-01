from __future__ import annotations

from aos_core.contracts import IntentFrame, SurfaceDecision


class SurfaceResolver:
    """Enforces separation between runtime, workshop, and active project."""

    PROJECT_RESPONSE_RULES = [
        'answer_about_active_project_payload_by_default',
        'use_aos_internally_without_exposing_it',
        'use_workshop_as_silent_maturity_lens',
        'start_from_project_truth_and_PROJECT_payload_evidence',
        'do_not_describe_aos_or_workshop_as_the_project',
        'do_not_open_with_generic_model_identity',
        'empty_PROJECT_means_no_current_project_loaded',
        'mark_missing_project_truth_as_unknown_question_or_assumption',
        'do_not_force_parent_child_or_single_template',
    ]
    WORKSHOP_RESPONSE_RULES = [
        'answer_about_general_methods_standards_and_maturity_lenses',
        'do_not_treat_workshop_as_active_project',
        'explain_applicability_to_project_types_when_relevant',
        'local_truth_is_required_before_execution',
    ]
    AOS_RESPONSE_RULES = [
        'answer_about_aos_environment_because_intent_is_explicit',
        'separate_aos_core_from_workshop_and_active_project_payload',
        'do_not_apply_project_payload_claims_to_aos_core',
        'do_not_modify_aos_without_self_governance',
        'mature_the_environment_against_its_mission_not_against_one_project',
    ]

    def resolve(self, frame: IntentFrame) -> SurfaceDecision:
        if frame.surface == 'aos_environment' or frame.explicit_aos_intent:
            return SurfaceDecision(
                surface='aos_environment',
                visible_scope='aos_environment',
                user_facing_subject='aos_environment',
                internal_scopes_allowed=['aos_environment', 'workshop_general_truth', 'active_project_when_referenced'],
                hidden_scopes=[],
                truth_priority=['system_truth', 'system_constitution', 'operational_identity', 'architecture_contract', 'self_development_truth'],
                response_mode='aos_surface_visible',
                response_rules=list(self.AOS_RESPONSE_RULES),
                forbidden_exposure=['treat_active_project_payload_as_aos_core', 'treat_workshop_as_runtime_identity'],
                reason='Explicit AOS/environment intent detected.',
            )
        if frame.surface == 'workshop_general_truth':
            return SurfaceDecision(
                surface='workshop_general_truth',
                visible_scope='workshop_general_truth',
                user_facing_subject='workshop_general_truth',
                internal_scopes_allowed=['aos_environment_as_silent_runtime', 'active_project_when_referenced'],
                hidden_scopes=['aos_core', 'aos_capabilities', 'engineer_protocol'],
                truth_priority=['workshop_manifest', 'workshop_canons', 'applicable_standards', 'project_local_truth_when_specializing'],
                response_mode='workshop_surface_visible',
                response_rules=list(self.WORKSHOP_RESPONSE_RULES),
                forbidden_exposure=['treat_workshop_as_active_project', 'execute_workshop_standard_without_local_specialization'],
                reason='Explicit Workshop/general standards intent detected.',
            )
        return SurfaceDecision(
            surface='active_project_payload',
            visible_scope='active_project_payload',
            user_facing_subject='active_project_payload',
            internal_scopes_allowed=['aos_environment_as_silent_runtime', 'workshop_general_truth_as_silent_lens'],
            hidden_scopes=['aos_environment', 'aos_core', 'aos_capabilities', 'workshop_internals', 'engineer_protocol'],
            truth_priority=['project_local_truth', 'upload_gate_payload_evidence', 'workshop_applicability_lens', 'runtime_state'],
            response_mode='project_surface_only',
            response_rules=list(self.PROJECT_RESPONSE_RULES),
            forbidden_exposure=['present_aos_as_project', 'present_workshop_as_project', 'explain_stable_spine_in_project_answer', 'describe_file_intelligence_or_intent_layer_unless_requested', 'show_generic_model_identity_first'],
            reason='Default project surface selected.',
        )

    def bind(self, frame: IntentFrame) -> IntentFrame:
        decision = self.resolve(frame)
        frame.surface = decision.surface
        frame.visible_scope = decision.visible_scope
        frame.user_facing_subject = decision.user_facing_subject
        frame.hidden_scopes = list(decision.hidden_scopes)
        frame.response_mode = decision.response_mode
        frame.response_contract = {
            'subject': decision.user_facing_subject,
            'visible_scope': decision.visible_scope,
            'internal_scopes_allowed': decision.internal_scopes_allowed,
            'hidden_scopes': decision.hidden_scopes,
            'truth_priority': decision.truth_priority,
            'rules': decision.response_rules,
            'forbidden_exposure': decision.forbidden_exposure,
            'reason': decision.reason,
        }
        return frame
