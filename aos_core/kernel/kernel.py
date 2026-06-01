from __future__ import annotations

from dataclasses import asdict
from pathlib import Path
from typing import Any, Dict

from aos_core.config import AOSPaths, load_json, write_json
from aos_core.contracts import ActionRequest, Event, Fact, Goal
from aos_core.runtime.event_store import EventStore
from aos_core.runtime.state_graph import StateGraph
from aos_core.ports.truth_port import TruthPort
from aos_core.ports.goal_runtime_port import GoalRuntimePort
from aos_core.memory.identity_sync import OperationalIdentitySync
from aos_core.ports.file_intelligence_port import FileIntelligencePort
from aos_core.intent.intent_engine import IntentEngine
from aos_core.intent.intent_cognition import IntentCognitionRuntime
from aos_core.goals.goal_engine import GoalEngine
from aos_core.governance.policy_engine import PolicyEngine
from aos_core.tools.tool_broker import ToolBroker
from aos_core.evaluation.evaluator import Evaluator
from aos_core.observability.audit import AuditLog
from aos_core.workspace.active_project_resolver import ActiveProjectResolver
from aos_core.strategy.strategy_engine import StrategyEngine
from aos_core.planning_solution.planning_solution_engine import PlanningSolutionEngine
from aos_core.runtime_enforcement.runtime_enforcement_engine import RuntimeEnforcementEngine
from aos_core.solution_delivery.solution_delivery_engine import SolutionDeliveryEngine
from aos_core.maintenance.maintenance_engine import MaintenanceEngine
from aos_core.entry.entry_gate import EntryGate
from aos_core.entry.entry_simulator import EntrySimulator
from operations_runtime import OperationsControlRoom


class AOSKernel:
    """Stable control plane for AOS.

    The kernel orchestrates contracts only. Capabilities produce evidence;
    governance decides permission; delivery is synthesized from operation packets.
    """

    def __init__(self, root: Path):
        self.paths = AOSPaths(root)
        self.paths.ensure()
        self.event_store = EventStore(self.paths.event_log)
        state_doc = load_json(self.paths.runtime_state / 'current_state.json', {'state': 'IDLE'})
        self.state = StateGraph(state_doc.get('state', 'IDLE'))
        self.truth = TruthPort(self.paths)
        self.identity_sync = OperationalIdentitySync(self.paths)
        self.intent_engine = IntentEngine()
        self.intent_cognition = IntentCognitionRuntime()
        self.policy = PolicyEngine()
        self.goal_engine = GoalEngine()
        self.goal_runtime = GoalRuntimePort(self.paths)
        self.evaluator = Evaluator()
        self.audit = AuditLog(self.paths.audit / 'audit.jsonl')
        self.tool_broker = ToolBroker(self.paths.root / 'extensions' / 'tools')
        self.file_intelligence = FileIntelligencePort()
        self.active_resolver = ActiveProjectResolver(self.paths.active_project, self.paths.project_upload)
        self.strategy = StrategyEngine(self.paths)
        self.planner = PlanningSolutionEngine()
        self.enforcement = RuntimeEnforcementEngine()
        self.delivery = SolutionDeliveryEngine()
        self.maintenance = MaintenanceEngine(self.paths)
        self.entry_gate = EntryGate(self.paths)
        self.entry_simulator = EntrySimulator(self.paths.root)
        self.operations = OperationsControlRoom(
            self.paths,
            entry_gate=self.entry_gate,
            active_resolver=self.active_resolver,
            intent_engine=self.intent_engine,
            intent_cognition=self.intent_cognition,
            truth=self.truth,
            file_intelligence=self.file_intelligence,
            goal_runtime=self.goal_runtime,
            strategy=self.strategy,
            planner=self.planner,
            enforcement=self.enforcement,
        )

    def _save_state(self) -> None:
        write_json(self.paths.runtime_state / 'current_state.json', {
            'state': self.state.current,
            'last_event_id': self.event_store.read_all()[-1]['id'] if self.event_store.count() else None,
        })

    def transition(self, target: str, reason: str) -> None:
        if self.state.current == target:
            return
        previous = self.state.current
        self.state.transition(target)
        evt = self.event_store.append(Event(type='state.transitioned', actor='kernel', subject=target, data={'from': previous, 'to': target, 'reason': reason}))
        self.audit.write('state_transition', {'event_id': evt.id, 'from': previous, 'to': target})
        self._save_state()

    def _move_to_intent_intake(self) -> None:
        if self.state.current == 'INTENT_INTAKE':
            return
        if self.state.can_transition('INTENT_INTAKE'):
            self.transition('INTENT_INTAKE', 'intent intake required')
            return
        self.state.current = 'IDLE'
        self._save_state()
        self.transition('INTENT_INTAKE', 'intent intake required after runtime reset')

    def _move_to_goal_intake(self) -> None:
        while self.state.current != 'GOAL_INTAKE':
            nxt = {
                'IDLE': 'INTENT_INTAKE',
                'BOOTED': 'INTENT_INTAKE',
                'INTENT_INTAKE': 'GOAL_INTAKE',
                'DISCOVERY': 'GOAL_INTAKE',
                'TRUTH_BUILDING': 'GOAL_INTAKE',
                'DONE': 'INTENT_INTAKE',
                'BLOCKED': 'INTENT_INTAKE',
            }.get(self.state.current)
            if not nxt:
                break
            self.transition(nxt, 'goal planning path')

    def boot(self) -> Dict[str, Any]:
        identity = self.paths.operational_identity.read_text(encoding='utf-8') if self.paths.operational_identity.exists() else ''
        system_truth = load_json(self.paths.system_truth, {})
        identity_sync = self.identity_sync.sync()
        self.event_store.append(Event(type='aos.booted', actor='kernel', subject='system', data={'version': system_truth.get('version'), 'identity_loaded': bool(identity), 'identity_sync_status': identity_sync.get('status')}))
        if self.state.current == 'IDLE':
            self.transition('BOOTED', 'boot complete')
        return {'status': 'booted', 'state': self.state.current, 'system_version': system_truth.get('version'), 'identity_loaded': bool(identity), 'identity_sync': identity_sync}

    def resolve_intent(self, request_text: str) -> Dict[str, Any]:
        self._move_to_intent_intake()
        entry = self.entry_gate.pre_intent_context(request_text, command='intent')
        # Intent must be resolved before artifact cockpit for normal entry.
        # File Intelligence is not the first awareness layer.
        frame = self.intent_engine.resolve(request_text, None)
        result = self.intent_engine.summary(frame)
        result['entry_runtime'] = entry
        active_state = self.active_resolver.state()
        truth_req = self.truth.resolve_requirement(request_text, intent=result, surface=frame.surface)
        cognition = self.intent_cognition.build(request_text, frame, active_project_state=active_state, truth_requirement=truth_req)
        result['intent_cognition'] = cognition
        result['intent_cognition_check'] = self.intent_cognition.validate_spine_flow(cognition)
        write_json(self.paths.reports / f'intent_frame_{frame.id}.json', result)
        self.event_store.append(Event(type='intent.resolved', actor='kernel', subject=frame.id, data={'intent_type': frame.intent_type, 'surface': frame.surface, 'visible_scope': frame.visible_scope, 'response_mode': frame.response_mode, 'entrypoint': frame.entrypoint, 'explicit_aos_intent': frame.explicit_aos_intent}))
        self.audit.write('intent_resolved', result)
        return result

    def inspect(self, query: str = '', changed_paths: list[str] | None = None, scope: str = 'active_project') -> Dict[str, Any]:
        if self.state.current in {'IDLE', 'BOOTED', 'INTENT_INTAKE'}:
            target = 'DISCOVERY' if self.state.can_transition('DISCOVERY') else self.state.current
            if target != self.state.current:
                self.transition(target, 'inspection started')
        matrix = self.operations.diagnostic_inspect(scope=scope, query=query, changed_paths=changed_paths or [])
        report_path = self.paths.reports / f'file_matrix_report_{scope}.json'
        write_json(report_path, matrix)
        self.event_store.append(Event(type='surface.inspected', actor='kernel', subject=scope, data={'condition': matrix['project_condition'], 'file_count': matrix['file_count'], 'query': query}))
        self.audit.write('inspection', {'report': report_path.as_posix(), 'summary': matrix.get('summary')})
        return matrix


    def _matrix_digest(self, scope: str, matrix: Dict[str, Any], visibility: str) -> Dict[str, Any]:
        diagnostics = matrix.get('diagnostics') or {}
        governance = matrix.get('artifact_governance') or {}
        decision = (governance.get('policy_decision') or {}).get('decision')
        return {
            'scope': scope,
            'visibility': visibility,
            'project_condition': matrix.get('project_condition'),
            'file_count': matrix.get('file_count'),
            'summary': matrix.get('summary'),
            'diagnostics': {
                'issue_count': diagnostics.get('issue_count', 0),
                'blocking_count': diagnostics.get('blocking_count', 0),
                'maturity_issue_count': diagnostics.get('maturity_issue_count', 0),
                'decision_hint': diagnostics.get('decision_hint'),
            },
            'governance_decision': decision,
        }

    def _compact_matrix_for_packet(self, matrix: Dict[str, Any], max_records: int = 24) -> Dict[str, Any]:
        """Return a hot packet matrix, not a verbose scan dump.

        Deep evidence remains in reports/file_matrix_report_* or the Truth Packet.
        Operation packets should be fast for models to read.
        """
        records = matrix.get('records') or []
        diagnostics = matrix.get('diagnostics') or {}
        search = matrix.get('search') or {}
        sem = matrix.get('truth_value_semantics') or {}

        def slim_record(r: Dict[str, Any]) -> Dict[str, Any]:
            return {
                'path': r.get('path'),
                'role': r.get('role'),
                'surface': r.get('surface'),
                'content_state': r.get('content_state'),
                'size_bytes': r.get('size_bytes'),
                'high_value_hint': any(x in (r.get('path') or '').lower() for x in ['contract','truth','canon','standard','identity','manifest','decision','readme']),
            }

        prioritized = []
        high_paths = {x.get('path') for x in sem.get('high_value_sources', [])}
        for r in records:
            if r.get('path') in high_paths or r.get('content_state') in {'empty','thin'}:
                prioritized.append(slim_record(r))
        for r in records:
            if len(prioritized) >= max_records:
                break
            sr = slim_record(r)
            if sr not in prioritized:
                prioritized.append(sr)

        return {
            'version': matrix.get('version'),
            'capability': matrix.get('capability'),
            'root': matrix.get('root'),
            'project_condition': matrix.get('project_condition'),
            'file_count': matrix.get('file_count'),
            'payload_file_count': matrix.get('payload_file_count'),
            'aos_surface_file_count': matrix.get('aos_surface_file_count'),
            'summary': matrix.get('summary'),
            'hot_records': prioritized[:max_records],
            'search': {'query': search.get('query'), 'lenses_used': search.get('lenses_used', []), 'results': (search.get('results') or [])[:12]},
            'truth_value_semantics': {
                'empty_declared_target_count': sem.get('empty_declared_target_count', 0),
                'declared_missing_artifact_count': sem.get('declared_missing_artifact_count', 0),
                'empty_declared_targets': (sem.get('empty_declared_targets') or [])[:12],
                'declared_missing_artifacts': (sem.get('declared_missing_artifacts') or [])[:12],
                'high_value_sources': (sem.get('high_value_sources') or [])[:12],
            },
            'diagnostics': {
                'mode': diagnostics.get('mode'),
                'issue_count': diagnostics.get('issue_count', 0),
                'blocking_count': diagnostics.get('blocking_count', 0),
                'maturity_issue_count': diagnostics.get('maturity_issue_count', 0),
                'counts_by_severity': diagnostics.get('counts_by_severity', {}),
                'counts_by_category': diagnostics.get('counts_by_category', {}),
                'decision_hint': diagnostics.get('decision_hint'),
                'top_issues': (diagnostics.get('issues') or [])[:12],
            },
            'artifact_governance': matrix.get('artifact_governance'),
            'authority': matrix.get('authority'),
            'authority_scope': matrix.get('authority_scope'),
            'packet_mode': 'hot_compact_matrix',
            'full_report_location': 'reports/file_matrix_report_<scope>.json or explicit inspect --verbose',
        }


    def _minimal_matrix_for_cognition(self, surface: str, active_state: Dict[str, Any], reason: str) -> Dict[str, Any]:
        state = active_state.get('state') if isinstance(active_state, dict) else None
        if surface == 'active_project_payload':
            if state == 'no_project_loaded':
                condition = 'EMPTY_NEW_PROJECT'
            elif state == 'single_project_detected':
                condition = 'PROJECT_PRESENT_UNSCANNED_HOT_PATH'
            else:
                condition = 'PROJECT_STATE_UNRESOLVED'
        elif surface == 'aos_environment':
            condition = 'AOS_ENVIRONMENT_HOT_IDENTITY'
        elif surface == 'workshop_general_truth':
            condition = 'WORKSHOP_HOT_IDENTITY'
        else:
            condition = 'HOT_IDENTITY_ONLY'
        return {
            'version': 'hot-minimal',
            'capability': 'file_intelligence',
            'authority': 'not_invoked_for_simple_intent',
            'authority_scope': 'identity_or_truth_hot_path_only',
            'root': None,
            'project_condition': condition,
            'file_count': 0,
            'payload_file_count': 0,
            'aos_surface_file_count': 0,
            'summary': {
                'project_condition': condition,
                'issue_count': 0,
                'diagnostic_issue_count': 0,
                'diagnostic_blocking_count': 0,
                'diagnostic_maturity_issue_count': 0,
            },
            'records': [],
            'search': {'query': '', 'lenses_used': [], 'results': []},
            'diagnostics': {'mode': 'not_run_for_simple_intent', 'issue_count': 0, 'blocking_count': 0, 'maturity_issue_count': 0, 'counts_by_severity': {}, 'counts_by_category': {}, 'decision_hint': None, 'issues': []},
            'truth_value_semantics': {'empty_declared_target_count': 0, 'declared_missing_artifact_count': 0, 'empty_declared_targets': [], 'declared_missing_artifacts': [], 'high_value_sources': []},
            'artifact_governance': {'policy_decision': {'decision': 'ALLOW', 'meaning': reason}},
            'packet_mode': 'hot_minimal_no_artifact_scan',
        }

    def _truth_hot_packet(self, truth_packet: Dict[str, Any]) -> Dict[str, Any]:
        return {
            'requirement': truth_packet.get('requirement'),
            'sufficiency': truth_packet.get('sufficiency'),
            'truth_story': truth_packet.get('truth_story'),
            'truth_value_semantics': {
                'empty_declared_target_count': (truth_packet.get('truth_value_semantics') or {}).get('empty_declared_target_count', 0),
                'declared_missing_artifact_count': (truth_packet.get('truth_value_semantics') or {}).get('declared_missing_artifact_count', 0),
            },
            'incomplete_truth': {
                'status': (truth_packet.get('incomplete_truth') or {}).get('status'),
                'issue_count': (truth_packet.get('incomplete_truth') or {}).get('issue_count', 0),
                'blocking_count': (truth_packet.get('incomplete_truth') or {}).get('blocking_count', 0),
                'maturity_issue_count': (truth_packet.get('incomplete_truth') or {}).get('maturity_issue_count', 0),
                'top_issues': ((truth_packet.get('incomplete_truth') or {}).get('issues') or [])[:12],
            },
            'identity_sync': truth_packet.get('identity_sync'),
            'receipt': truth_packet.get('receipt'),
            'packet_mode': 'hot_truth_packet',
        }

    def _build_artifact_cockpit(self, request_text: str, frame, active_gate: Path, primary_matrix: Dict[str, Any]) -> Dict[str, Any]:
        """Build a surface-aware cockpit summary without turning every answer into a verbose multi-scan.

        The cockpit keeps 360 awareness by registering allowed silent lenses and
        using the primary surface matrix. Deep scans of silent scopes are
        explicit diagnostic/implementation tools, not the normal answer path.
        """
        views = [self._matrix_digest(frame.surface, primary_matrix, 'visible_surface')]

        def register(scope: str, visibility: str, role: str) -> None:
            views.append({
                'scope': scope,
                'visibility': visibility,
                'role': role,
                'status': 'registered_not_scanned_in_hot_path',
                'meaning': 'available as a silent lens; use inspect/doctor or deep task mode for full scan',
            })

        if frame.surface == 'active_project_payload':
            register('workshop_general_truth_as_silent_lens', 'silent_internal_context', 'maturity_lens')
            register('aos_identity_as_silent_runtime_lens', 'silent_internal_context', 'operating_identity_lens')
            register('aos_surface_as_silent_runtime_lens', 'silent_internal_context', 'surface_contract_lens')
        elif frame.surface == 'workshop_general_truth':
            register('aos_identity_as_silent_runtime_lens', 'silent_internal_context', 'operating_identity_lens')
            register('active_project_when_referenced', 'conditional_context', 'project_payload_lens')
        elif frame.surface == 'aos_environment':
            register('workshop_general_truth_as_silent_lens', 'silent_internal_context', 'maturity_lens')
            register('active_project_when_referenced', 'conditional_context', 'project_payload_lens')

        return {
            'mode': 'surface_aware_artifact_cockpit',
            'hot_path': True,
            'law': 'intent_selects_visible_surface_not_blind_tunnel; cockpit_registers_allowed_scopes; deep_scans_are_explicit_tools; response_stays_focused_on_intent',
            'visible_surface': frame.surface,
            'views': views,
        }

    def operation_packet(self, request_text: str) -> Dict[str, Any]:
        self._move_to_intent_intake()
        packet = self.operations.build_answer_envelope(request_text)
        write_json(self.paths.reports / 'last_operation_packet.json', packet)
        self.event_store.append(Event(
            type='operation.packet_built',
            actor='operations_runtime',
            subject=packet.get('intent', {}).get('id', 'unknown_intent'),
            data={
                'surface': packet.get('intent', {}).get('surface'),
                'permission': (packet.get('runtime_enforcement') or {}).get('permission'),
                'operations_runtime': (packet.get('operations') or {}).get('runtime'),
            },
        ))
        return packet

    def answer(self, request_text: str) -> str:
        packet = self.operation_packet(request_text)
        answer = self.delivery.synthesize(packet)
        # Delivery may append the final response-contract check; persist the
        # completed packet after synthesis, not only before it.
        write_json(self.paths.reports / 'last_operation_packet.json', packet)
        self.audit.write('answer_synthesized', {
            'surface': packet.get('intent', {}).get('surface'),
            'response_contract_check': packet.get('response_contract_check'),
        })
        return answer

    def plan_goal(self, goal_text: str) -> Dict[str, Any]:
        self._move_to_intent_intake()
        entry_bootstrap = self.entry_gate.pre_intent_context(goal_text, command='goal')
        # Goal planning is also identity/intent/surface/truth-first.
        intent = self.intent_engine.resolve(goal_text, None)
        intent_summary = self.intent_engine.summary(intent)
        early_truth_requirement = self.truth.resolve_requirement(goal_text, intent=intent_summary, surface=intent.surface)
        intent_cognition = self.intent_cognition.build(goal_text, intent, active_project_state=self.active_resolver.state(), truth_requirement=early_truth_requirement)
        intent_cognition_check = self.intent_cognition.validate_spine_flow(intent_cognition)
        entry_state = self.entry_gate.after_intent(intent, early_truth_requirement)
        active_state_for_gate = self.active_resolver.state()
        active_gate = Path(active_state_for_gate.get('upload_gate') or self.paths.project_upload)
        if intent.surface == 'aos_environment':
            scope_root = self.paths.root
        elif intent.surface == 'workshop_general_truth':
            scope_root = self.paths.workshop_system
        else:
            scope_root = active_gate
        # Goal planning enters through the Runtime Kernel; it does not call File Intelligence directly.
        goal_packet = self.operations.build_answer_envelope(goal_text)
        matrix = goal_packet.get('file_matrix') or {}
        self.event_store.append(Event(type='intent.resolved', actor='kernel', subject=intent.id, data={'intent_type': intent.intent_type, 'surface': intent.surface, 'visible_scope': intent.visible_scope, 'response_mode': intent.response_mode, 'entrypoint': intent.entrypoint, 'explicit_aos_intent': intent.explicit_aos_intent}))
        self._move_to_goal_intake()
        goal = Goal(text=goal_text, status='planning')
        goal_trace = self.goal_runtime.open(goal_text, success_criteria=['intent resolved', 'truth requirement resolved', 'plan has gates', 'progress must be checked before repeated repairs'], context={'surface': intent.surface, 'intent_type': intent.intent_type})
        snapshot = self.truth.snapshot()
        plan = self.goal_engine.build_plan(goal, matrix, snapshot, intent=intent)
        self.transition('PLANNING', 'goal converted to plan after intent intake')
        side_effects = ['mutates_project_payload'] if intent.may_modify_files and intent.surface == 'active_project_payload' else []
        if intent.intent_type == 'self_develop_aos':
            side_effects = ['mutates_aos_core']
        action = ActionRequest(type='goal.plan', actor='goal_engine', target=plan.entrypoint, source_goal=goal.id, source_intent=intent.id, side_effects=side_effects, risk_level=intent.risk_level)
        decision = self.policy.decide(action, current_state=self.state.current, has_project_truth=bool(snapshot.get('facts') or snapshot.get('assumptions')))
        evaluation = self.evaluator.evaluate_plan(asdict(plan))
        result = {'entry_runtime': {'bootstrap': entry_bootstrap, 'sequence_state': entry_state, 'truth_requirement': early_truth_requirement}, 'intent': asdict(intent), 'intent_cognition': intent_cognition, 'intent_cognition_check': intent_cognition_check, 'goal_trace': goal_trace, 'goal': asdict(goal), 'plan': asdict(plan), 'policy_decision': asdict(decision), 'evaluation': evaluation}
        write_json(self.paths.reports / f'goal_plan_{goal.id}.json', result)
        self.event_store.append(Event(type='goal.planned', actor='kernel', subject=goal.id, data={'condition': plan.condition, 'policy': decision.status, 'evaluation_passed': evaluation['passed'], 'surface': plan.surface, 'intent_id': intent.id}))
        self.audit.write('goal_plan', result)
        return result


    def doctor(self, scope: str = 'active_project', query: str = '', changed_paths: list[str] | None = None) -> Dict[str, Any]:
        """Read-only one-touch diagnostic entrypoint backed by file intelligence.

        Scopes remain isolated: active_project, workshop, or aos. This method
        never writes project files; it only writes the report artifact under
        reports/.
        """
        result = self.operations.diagnostic_doctor(scope=scope, query=query, changed_paths=changed_paths or [])
        result['scope'] = scope
        report_path = self.paths.reports / f'doctor_report_{scope}.json'
        write_json(report_path, result)
        self.event_store.append(Event(type='file_intelligence.doctor_ran', actor='kernel', subject=scope, data={'status': result.get('status')}))
        self.audit.write('doctor', {'report': report_path.as_posix(), 'status': result.get('status')})
        return result

    def simulate_entry(self, request_text: str = '') -> Dict[str, Any]:
        result = self.entry_simulator.run(request_text)
        write_json(self.paths.reports / 'entry_simulation_report.json', result)
        self.audit.write('entry_simulation', {'passed': result.get('passed'), 'issue_count': len(result.get('issues', []))})
        return result

    def self_check(self) -> Dict[str, Any]:
        matrix = self.operations.diagnostic_inspect(scope='aos')
        tools = self.tool_broker.list_manifests()
        project_intent = self.intent_engine.resolve('ما معمارية المشروع الحالي؟', None)
        aos_intent = self.intent_engine.resolve('أريد صيانة بيئة المهندس ومعمارية AOS', None)
        workshop_intent = self.intent_engine.resolve('اشرح معايير ورشة العمل العامة', None)
        maintenance = self.maintenance.audit()
        current = {
            'state': self.state.current,
            'event_count': self.event_store.count(),
            'tool_count': len(tools),
            'root_file_count': matrix['file_count'],
            'python_issues': [i for r in matrix['records'] for i in (r.get('issues') or []) if i.startswith('python_syntax_error')],
            'identity_outside_workshop': self.paths.operational_identity.exists() and not (self.paths.workshop / 'OPERATIONAL_IDENTITY.md').exists(),
            'bootstrap_outside_workshop': self.paths.bootstrap_protocol.exists() and not (self.paths.workshop / 'ENGINEER_BOOTSTRAP_PROTOCOL.md').exists(),
            'system_truth_in_identity': self.paths.system_truth.exists(),
            'root_agents_entrypoint_exists': (self.paths.root / 'AGENTS.md').exists(),
            'silent_response_contract_exists': (self.paths.identity / 'SILENT_RESPONSE_CONTRACT.md').exists(),
            'external_model_binding_contract_exists': (self.paths.identity / 'EXTERNAL_MODEL_BINDING_CONTRACT.md').exists(),
            'truth_grounded_response_contract_exists': (self.paths.identity / 'TRUTH_GROUNDED_RESPONSE_CONTRACT.md').exists(),
            'operating_layer_map_exists': (self.paths.identity / 'OPERATING_LAYER_MAP.md').exists(),
            'surface_layer_identity_exists': (self.paths.root / 'aos_core' / 'surface' / 'LAYER_IDENTITY.md').exists(),
            'file_intelligence_layer_identity_exists': (self.paths.root / 'aos_capabilities' / 'file_intelligence' / 'LAYER_IDENTITY.md').exists(),
            'truth_runtime_capability_exists': (self.paths.root / 'aos_capabilities' / 'truth_runtime' / 'CAPABILITY_MANIFEST.yaml').exists(),
            'truth_runtime_layer_identity_exists': (self.paths.root / 'aos_capabilities' / 'truth_runtime' / 'LAYER_IDENTITY.md').exists(),
            'truth_port_exists': (self.paths.root / 'aos_core' / 'ports' / 'truth_port.py').exists(),
            'goal_runtime_capability_exists': (self.paths.root / 'aos_capabilities' / 'goal_runtime' / 'CAPABILITY_MANIFEST.yaml').exists(),
            'goal_runtime_port_exists': (self.paths.root / 'aos_core' / 'ports' / 'goal_runtime_port.py').exists(),
            'entry_runtime_exists': (self.paths.root / 'aos_core' / 'entry' / 'entry_gate.py').exists(),
            'entry_runtime_contract_exists': (self.paths.root / 'aos_core' / 'entry' / 'ENTRY_RUNTIME_CONTRACT.yaml').exists(),
            'operations_runtime_root_layer_exists': (self.paths.root / 'operations_runtime' / 'LAYER_IDENTITY.md').exists(),
            'operations_runtime_api_registry_exists': (self.paths.root / 'operations_runtime' / 'LAYER_API_REGISTRY.yaml').exists(),
            'core_has_no_operations_layer': not (self.paths.root / 'aos_core' / 'operations').exists(),
            'entry_simulation_passed': self.entry_simulator.run().get('passed') is True,
            'core_has_no_truth_layer': not (self.paths.root / 'aos_core' / 'truth').exists(),
            'no_sample_payloads_in_stable_base': not (self.paths.root / 'workshop' / 'examples').exists() and not (self.paths.active_project / 'sample_payload').exists() and not (self.paths.project_upload / 'sample_payload').exists(),
            'single_project_path_exists': self.paths.project_upload.exists(),
            'canonical_project_path_ascii': self.paths.project_upload.name == 'PROJECT',
            'workshop_manifest_exists': (self.paths.workshop_system / '00_WORKSHOP_MANIFEST.md').exists(),
            'active_project_slot_not_project': self.active_resolver.state().get('slot_is_project') is False,
            'active_project_empty_means_no_project_loaded': self.active_resolver.state().get('state') in {'no_project_loaded', 'single_project_detected', 'unformed_or_scattered_project', 'multi_project_ambiguity'},
            'intent_project_architecture_not_aos': project_intent.surface == 'active_project_payload',
            'intent_aos_surface_ok': aos_intent.surface == 'aos_environment',
            'intent_workshop_surface_ok': workshop_intent.surface == 'workshop_general_truth',
            'file_intelligence_capability': matrix.get('capability') == 'file_intelligence' and matrix.get('authority') == 'evidence_only',
            'core_has_no_file_layer': not (self.paths.root / 'aos_core' / 'files').exists(),
            'maintenance_audit_passed': maintenance['passed'],
            'python_syntax_clean': not [i for r in matrix['records'] for i in (r.get('issues') or []) if i.startswith('python_syntax_error')],
        }
        current['passed'] = all(v for k, v in current.items() if isinstance(v, bool))
        current['maintenance'] = maintenance
        self.event_store.append(Event(type='aos.self_checked', actor='kernel', subject='system', data={'passed': current['passed']}))
        write_json(self.paths.reports / 'self_check_report.json', current)
        return current
