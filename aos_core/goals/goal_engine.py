from __future__ import annotations

from typing import Any, Dict, List, Optional

from aos_core.contracts import Goal, GoalPlan, IntentFrame


class GoalEngine:
    """Goal realization layer.

    The user does not need to prescribe the solution. The engine derives a safe
    plan from: intent, operational surface, project condition, truth level, and
    file matrix. It must not expose AOS internals when the active project is the
    surface.
    """

    def build_plan(self, goal: Goal, file_matrix: Dict[str, Any], truth_snapshot: Dict[str, Any], intent: Optional[IntentFrame] = None) -> GoalPlan:
        condition = file_matrix.get('project_condition', 'UNKNOWN')
        facts = truth_snapshot.get('facts', [])
        assumptions = truth_snapshot.get('assumptions', [])
        steps: List[Dict[str, Any]] = []
        risks: List[str] = []
        gates = ['intent_resolved', 'policy_review', 'evaluation_required']
        surface = intent.surface if intent else 'active_project_payload'
        entrypoint = intent.entrypoint if intent else 'active_project_surface_flow'

        steps.append({'id': 'bind_intent', 'type': 'intent', 'description': 'Resolve user intent and select the correct operational surface.'})
        if surface == 'active_project_payload':
            steps.append({'id': 'respect_project_surface', 'type': 'surface', 'description': 'Compose the user-facing answer only around active-project truth and payload evidence; keep AOS internals silent.'})
        else:
            steps.append({'id': 'enter_aos_surface', 'type': 'routing', 'description': 'Use AOS environment surface because explicit AOS intent was detected.'})
        steps.append({'id': 'collect_file_evidence', 'type': 'capability', 'description': 'Use File Intelligence as silent evidence collection; it does not become the response subject.'})

        if intent and intent.intent_type == 'explain':
            steps.extend([
                {'id': 'answer_from_identity_and_truth', 'type': 'response', 'description': 'Answer from operational identity and verified truth, not from general model identity.'},
                {'id': 'avoid_unrequested_execution', 'type': 'safety', 'description': 'Do not execute or mutate files for an explanatory intent.'}
            ])
            gates = ['intent_resolved', 'truth_binding']
        elif intent and intent.intent_type == 'self_develop_aos':
            steps.extend([
                {'id': 'open_self_development_case', 'type': 'truth', 'description': 'Record the AOS change request as self-development truth.'},
                {'id': 'impact_analysis', 'type': 'architecture', 'description': 'Determine affected core contracts, schemas, policies, and tests.'},
                {'id': 'sandbox_self_patch', 'type': 'execution', 'description': 'Prepare changes as sandboxed patches; never mutate the core directly.'},
                {'id': 'run_core_regression', 'type': 'evaluation', 'description': 'Run self-check and tests before promotion.'}
            ])
            risks.extend(['self_modification_risk', 'core_contract_drift'])
            gates.extend(['architecture_contract_review', 'self_development_approval', 'core_regression_tests'])
        elif condition == 'EMPTY_NEW_PROJECT':
            steps.extend([
                {'id': 'create_truth_seed', 'type': 'truth', 'description': 'Create/complete project contract, questions, and assumptions.'},
                {'id': 'select_strategy', 'type': 'strategy', 'description': 'Select new-project strategy from workshop playbooks.'},
                {'id': 'define_acceptance', 'type': 'goal', 'description': 'Define acceptance criteria before implementation.'}
            ])
            risks.append('goal_under_specified')
            gates.append('minimum_project_truth_required')
        elif condition in {'EXISTING_UNDOCUMENTED_PROJECT', 'LEGACY_COMPLEX_PROJECT'}:
            steps.extend([
                {'id': 'recover_architecture', 'type': 'analysis', 'description': 'Build module map and dependency summary from files.'},
                {'id': 'separate_facts_assumptions', 'type': 'truth', 'description': 'Record inferred structure as assumptions until verified.'},
                {'id': 'stabilize_first', 'type': 'execution', 'description': 'Prefer stabilization and tests before feature work.'}
            ])
            risks.append('undocumented_or_legacy_payload')
        else:
            steps.extend([
                {'id': 'derive_solution_options', 'type': 'architecture', 'description': 'Generate solution options from standards and project truth.'},
                {'id': 'select_best_option', 'type': 'decision', 'description': 'Pick the option that maximizes goal satisfaction with minimal disruption.'},
                {'id': 'sandbox_patch', 'type': 'execution', 'description': 'Apply changes only through sandbox patch workflow.'},
                {'id': 'evaluate_goal', 'type': 'evaluation', 'description': 'Verify result against goal, truth, tests, and policy.'}
            ])

        if not facts and not (intent and intent.intent_type == 'explain'):
            risks.append('low_verified_truth')
            gates.append('truth_promotion_or_human_input')
        if assumptions:
            gates.append('assumption_review')
        if intent and intent.may_modify_files:
            gates.append('sandbox_required')
        if intent and intent.ambiguity_level != 'low':
            gates.append('ambiguity_resolution')
            risks.append('ambiguous_intent')

        return GoalPlan(
            goal_id=goal.id,
            condition=condition,
            steps=steps,
            gates=sorted(set(gates)),
            risks=sorted(set(risks)),
            intent_id=intent.id if intent else None,
            surface=surface,
            entrypoint=entrypoint
        )
