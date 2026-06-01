from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List

from aos_core.config import AOSPaths, load_json, write_json
from aos_core.memory.identity_sync import OperationalIdentitySync
from aos_core.workspace.active_project_resolver import ActiveProjectResolver
from aos_core.entry.entry_simulator import EntrySimulator
from operations_runtime.context import make_operation_context
from operations_runtime.context_authority import ContextAuthority
from operations_runtime.operation_contract import OperationContract
from operations_runtime.scope_planner import ScopePlanner
from operations_runtime.truth_context_loader import TruthContextLoader
from operations_runtime.delivery_gate import DeliveryGroundingGate
from operations_runtime.surface_policy import SurfacePolicyResolver
from operations_runtime.performance_budget import PerformanceBudgetPlanner
from operations_runtime.layer_command import LayerCommand
from operations_runtime.quick_artifact_cockpit import QuickArtifactCockpit

from operations_runtime.operation_envelope import OperationEnvelope
from operations_runtime.layer_contribution import LayerContribution
from operations_runtime.graph_controller import RuntimeGraphController, GraphNode
from operations_runtime.trace_store import TraceStore
from operations_runtime.layer_registry import OperationsLayerRegistry
from operations_runtime.invocation_engine import MatrixInvocationEngine
from operations_runtime.contribution_bus import ContributionBus
from operations_runtime.contradiction_resolver import ContradictionResolver
from operations_runtime.truth_synthesizer import TruthSynthesizer
from operations_runtime.delivery_renderer import DeliveryRenderer


class OperationsRuntimeKernel:
    """AOS v4 root operating kernel.

    This is the single runtime owner. It keeps the model inside one runtime kernel
    and invokes layer APIs as services. Existing identity, intent, truth,
    artifact, and goal layers are preserved behind this kernel.
    """

    VERSION = '4.4.0-surface-budget-lazy-runtime-governance'

    def __init__(self, root: Path):
        self.paths = AOSPaths(root)
        self.paths.ensure()
        self.trace_store = TraceStore(self.paths.root)
        self.graph = RuntimeGraphController(self.trace_store)
        self.registry = OperationsLayerRegistry(self.paths.root, self.paths)
        self.invoker = MatrixInvocationEngine()
        self.bus = ContributionBus()
        self.resolver = ContradictionResolver()
        self.synthesizer = TruthSynthesizer()
        self.renderer = DeliveryRenderer()
        self.delivery_gate = DeliveryGroundingGate()
        self.context_authority = ContextAuthority()
        self.scope_planner = ScopePlanner(self.paths)
        self.surface_policy = SurfacePolicyResolver()
        self.performance_budget = PerformanceBudgetPlanner()
        self.truth_context_loader = TruthContextLoader(self.paths)
        self.identity_sync = OperationalIdentitySync(self.paths)
        self.active_resolver = ActiveProjectResolver(self.paths.active_project, self.paths.project_upload)
        self.entry_simulator = EntrySimulator(self.paths.root)
        self.quick_artifacts = QuickArtifactCockpit()

    # Public API ---------------------------------------------------------
    def boot(self) -> Dict[str, Any]:
        self.identity_sync.sync()
        return {
            'status': 'booted',
            'system_version': self.VERSION,
            'entry_owner': 'operations_runtime',
            'layer_registry': self.registry.describe(),
            'law': 'operations_runtime is the single graph/state runtime owner; layers are typed services behind it',
        }

    def self_check(self) -> Dict[str, Any]:
        checks = {
            'operations_runtime_exists': (self.paths.root / 'operations_runtime' / 'main.py').exists(),
            'registered_layer_api_facades': all((self.paths.root / p).exists() for p in [
                'aos_core/intent/main.py',
                'aos_capabilities/file_intelligence/main.py',
                'aos_capabilities/truth_runtime/main.py',
                'aos_capabilities/goal_runtime/main.py',
            ]),
            'runtime_trace_store': True,
        }
        return {'passed': all(checks.values()), 'checks': checks, 'entry_owner': 'operations_runtime'}

    def simulate_entry(self, _: str = '') -> Dict[str, Any]:
        sim = self.entry_simulator.run()
        issues = list(sim.get('issues') or [])
        start = self.paths.root / '00_START_HERE_FOR_ANY_MODEL.md'
        text = start.read_text(encoding='utf-8') if start.exists() else ''
        if 'operations_runtime' not in text:
            issues.append('start_file_does_not_name_operations_runtime')
        return {'passed': not issues, 'issues': issues, 'entry_owner': 'operations_runtime', 'simulation': sim}

    def resolve_intent(self, request_text: str) -> Dict[str, Any]:
        env = OperationEnvelope(request_text=request_text)
        env = self._create_operation_contract(env)
        env = self._resolve_surface_policy(env)
        env = self._load_active_state(env)
        env = self._capture_intent(env)
        return {'operations_runtime': {'operation_id': env.operation_id, 'entry_owner': 'operations_runtime'}, 'intent': env.intent, 'truth_requirement': env.truth_requirement, 'intent_cognition': env.intent.get('cognition'), 'intent_cognition_check': (env.intent.get('cognition') or {}).get('validation')}

    def operation_packet(self, request_text: str) -> Dict[str, Any]:
        env = self._run_graph(request_text, include_delivery=False)
        packet = self._packet(env)
        write_json(self.paths.reports / 'last_operation_packet.json', packet)
        return packet

    def answer(self, request_text: str) -> str:
        env = self._run_graph(request_text, include_delivery=True)
        packet = self._packet(env)
        write_json(self.paths.reports / 'last_operation_packet.json', packet)
        return env.delivery.get('answer', '')

    def inspect(self, query: str = '', changed_paths: List[str] | None = None, scope: str = 'active_project') -> Dict[str, Any]:
        root = self._scope_root(scope)
        context = make_operation_context('diagnostic_inspect', 'explicit_diagnostic', scope_plan={'allowed_roots': [root.resolve().as_posix()]}, layer_id='artifact_matrix')
        api = self.registry.get('artifact_matrix')
        result = api.inspect(root, query=query, changed_paths=changed_paths or [], intent=context.to_intent(surface=scope, artifact_need='explicit_diagnostic'))
        result['operations_entry'] = 'operations_runtime.inspect'
        write_json(self.paths.reports / f'file_matrix_report_{scope}.json', result)
        return result

    def doctor(self, scope: str = 'active_project', query: str = '', changed_paths: List[str] | None = None) -> Dict[str, Any]:
        root = self._scope_root(scope)
        context = make_operation_context('diagnostic_doctor', 'explicit_diagnostic', scope_plan={'allowed_roots': [root.resolve().as_posix()]}, layer_id='artifact_matrix')
        api = self.registry.get('artifact_matrix')
        result = api.doctor(root, query=query, changed_paths=changed_paths or [], intent=context.to_intent(surface=scope, artifact_need='explicit_diagnostic'))
        result['operations_entry'] = 'operations_runtime.doctor'
        write_json(self.paths.reports / f'doctor_report_{scope}.json', result)
        return result

    def plan_goal(self, goal_text: str) -> Dict[str, Any]:
        env = self._run_graph(goal_text, include_delivery=False)
        context = make_operation_context(env.operation_id, 'goal_open', scope_plan=env.scope_plan, layer_id='goal_runtime')
        goal = self.registry.get('goal_runtime').open(goal_text, success_criteria=['truth-grounded plan', 'no patch loop'], context=context.to_intent(surface=env.surface, insight=env.operational_insight))
        packet = self._packet(env)
        packet['goal_runtime'] = goal
        return packet

    # Graph --------------------------------------------------------------
    def _run_graph(self, request_text: str, *, include_delivery: bool) -> OperationEnvelope:
        env = OperationEnvelope(request_text=request_text)
        nodes = [
            GraphNode('create_operation_contract', self._create_operation_contract),
            GraphNode('resolve_surface_policy', self._resolve_surface_policy),
            GraphNode('load_operating_identity', self._load_identity),
            GraphNode('load_active_project_state', self._load_active_state),
            GraphNode('capture_intent_hypothesis', self._capture_intent),
            GraphNode('bind_operation_contract', self._bind_operation_contract),
            GraphNode('plan_scope', self._plan_scope),
            GraphNode('load_truth_context', self._load_truth_context),
            GraphNode('plan_layer_contributions', self._plan_layer_contributions),
            GraphNode('invoke_layer_matrix', self._invoke_layer_matrix),
            GraphNode('merge_contributions', self._merge_contributions),
            GraphNode('ground_truth_after_merge', self._ground_truth),
            GraphNode('resolve_contradictions', self._resolve_contradictions),
            GraphNode('second_pass_if_needed', self._second_pass_if_needed),
            GraphNode('synthesize_operational_insight', self._synthesize_insight),
        ]
        if include_delivery:
            nodes.append(GraphNode('render_and_validate_delivery', self._render_delivery))
        return self.graph.run(env, nodes)

    def _create_operation_contract(self, env: OperationEnvelope) -> OperationEnvelope:
        env.operation_contract = OperationContract.from_envelope(env).to_dict()
        return env

    def _resolve_surface_policy(self, env: OperationEnvelope) -> OperationEnvelope:
        decision = self.surface_policy.resolve(env.request_text)
        env.surface = decision.surface
        env.intent['surface_policy'] = decision.to_dict()
        budget = self.performance_budget.plan(env.surface, env.request_text)
        env.intent['performance_budget'] = budget.to_dict()
        env.add_contribution(LayerContribution(
            layer='surface_policy',
            mode='deterministic_pre_intent_guard',
            value='تم تحديد السطح قبل تحميل حمولة المشروع أو استدعاء الطبقات؛ هذا يمنع خلط سؤال الوكيل بحقيقة مشروع نشط.',
            evidence=[{'type': 'surface_policy', 'value': decision.to_dict()}, {'type': 'performance_budget', 'value': budget.to_dict()}],
            ignored_noise=['payload-first routing', 'manual zip inspection as normal answer path'],
        ).to_dict())
        return env

    def _bind_operation_contract(self, env: OperationEnvelope) -> OperationEnvelope:
        env.operation_contract = OperationContract.from_envelope(env).to_dict()
        return env

    def _plan_scope(self, env: OperationEnvelope) -> OperationEnvelope:
        plan = self.scope_planner.plan(env)
        env.scope_plan = plan.to_dict()
        env.add_contribution(LayerContribution(
            layer='scope_planner',
            mode='governed_scope_plan',
            value='تم تثبيت نطاق التشغيل قبل استدعاء الطبقات؛ النطاق يحدد ما يُقرأ وما يُستبعد وما دور حمولة المشروع.',
            evidence=[{'type': 'scope_plan', 'value': env.scope_plan}],
            ignored_noise=['folder traversal as truth', 'active project fixture as runtime truth'],
        ).to_dict())
        return env

    def _load_truth_context(self, env: OperationEnvelope) -> OperationEnvelope:
        plan = self.scope_planner.plan(env)
        ctx = self.truth_context_loader.load(plan)
        env.truth_context = ctx.to_dict()
        env.add_contribution(LayerContribution(
            layer='truth_context',
            mode='loaded_before_layer_fanout',
            value='تم تحميل سياق الحقيقة الحاكم قبل تشغيل الطبقات؛ أي نقص يبقى معلنًا ولا يتحول إلى تخمين.',
            evidence=[{'type': 'truth_context', 'value': {'profile': ctx.profile, 'status': ctx.status, 'sources': [x.get('id') for x in ctx.governing_sources], 'missing': ctx.missing_required_truth}}],
            risks=[{'severity': 'mature', 'code': 'truth_context_partial', 'missing': ctx.missing_required_truth}] if ctx.missing_required_truth else [],
            next_needs=['close_missing_governing_truth'] if ctx.missing_required_truth else [],
            ignored_noise=['raw file count as truth'],
        ).to_dict())
        return env

    def _load_identity(self, env: OperationEnvelope) -> OperationEnvelope:
        identity_text = self.paths.operational_identity.read_text(encoding='utf-8') if self.paths.operational_identity.exists() else ''
        contribution = LayerContribution(
            layer='operating_identity',
            mode='loaded_by_runtime_graph',
            value='الهوية التشغيلية الظاهرة هي مهندس مشروع يعمل من الحقيقة؛ هوية النموذج العامة ليست سطح المشروع.',
            evidence=[{'type': 'identity_loaded', 'value': bool(identity_text)}],
            ignored_noise=['generic model identity', 'runtime package names as visible identity'],
        ).to_dict()
        env.add_contribution(contribution)
        return env

    def _load_active_state(self, env: OperationEnvelope) -> OperationEnvelope:
        policy = (env.intent.get('surface_policy') or {})
        if policy and not policy.get('allow_active_payload_state', True):
            env.active_project_state = {
                'state': 'intentionally_not_loaded_for_surface',
                'project_root': None,
                'project_name': None,
                'meaning': 'active payload state withheld because this operation targets runtime/workshop truth',
                'visibility': policy.get('active_payload_visibility'),
            }
            return env
        env.active_project_state = self.active_resolver.state()
        return env

    def _capture_intent(self, env: OperationEnvelope) -> OperationEnvelope:
        truth_req_seed = {'mode': 'preliminary'}
        api = self.registry.get('intent_cognition')
        context = make_operation_context(env.operation_id, 'intent_cognition', layer_id='intent_cognition')
        resolved_packet = api.execute(LayerCommand(
            operation_id=env.operation_id,
            layer_id='intent_cognition',
            command='intent.resolve',
            payload={'request_text': env.request_text, 'active_project_state': env.active_project_state, 'truth_requirement': truth_req_seed},
            context=context.to_intent(surface=env.surface or 'intent', pre_resolved_surface=env.surface),
        ))
        resolved = resolved_packet.get('data') or {}
        previous_policy = env.intent.get('surface_policy') or {}
        previous_budget = env.intent.get('performance_budget') or {}
        env.intent = resolved.get('summary') or {}
        env.intent['raw_request'] = env.request_text
        if previous_policy.get('surface') in {'aos_environment', 'workshop_general_truth'}:
            env.surface = previous_policy['surface']
            env.intent['surface'] = env.surface
            env.intent['target'] = env.surface
            env.intent['entrypoint'] = 'operations_runtime_surface_policy_flow'
        else:
            env.surface = env.intent.get('surface') or 'active_project_payload'
        env.intent['surface_policy'] = previous_policy
        env.intent['performance_budget'] = previous_budget
        cognition = resolved.get('cognition') or {}
        env.intent['cognition'] = cognition
        env.truth_requirement = {'surface': env.surface, 'intent_type': env.intent.get('intent_type'), 'mode': 'derive_after_artifacts'}
        env.add_contribution(LayerContribution(
            layer='intent_cognition',
            mode='intent_hypothesis_not_decision',
            value='النية الأولى فرضية تشغيلية؛ لا تصبح قرارًا أو تنفيذًا إلا بعد وزنها بالحقيقة ومساهمات الطبقات.',
            evidence=[{'type': 'intent_type', 'value': env.intent.get('intent_type')}, {'type': 'surface', 'value': env.surface}],
            next_needs=self._intent_next_needs(cognition),
            ignored_noise=['treating user wording as final diagnosis'],
        ).to_dict())
        return env

    def _plan_layer_contributions(self, env: OperationEnvelope) -> OperationEnvelope:
        # Plan is stored in intent for traceability; it is not visible by default.
        text = (env.request_text or '').lower()
        explicit_diag = any(t in text for t in ['تقرير', 'تشخيص', 'أرقام', 'ارقام', 'تفاصيل', 'audit', 'metrics', 'diagnostic', 'inspect', 'doctor', 'trace'])
        budget = env.intent.get('performance_budget') or {}
        cognition = env.intent.get('cognition') or {}
        artifact_need = ((cognition.get('layer_needs') or {}).get('artifact_cockpit') or '')
        identity_only = artifact_need == 'none_or_cached_identity_truth'
        if env.surface in {'aos_environment', 'workshop_general_truth'} and budget.get('artifact_policy') in {'skip_artifact_scan_use_truth_context', 'skip_or_scoped_workshop_only'}:
            artifact_depth = 'none'
        elif identity_only:
            artifact_depth = 'none'
        else:
            artifact_depth = 'deep_diagnostic' if explicit_diag else 'fast_value'
        env.intent['contribution_plan'] = {
            'artifact_depth': artifact_depth,
            'goal_runtime': ('not_required' if env.surface == 'aos_environment' and budget.get('profile') == 'runtime_hot_answer' else ('consult_experience_only' if env.surface == 'active_project_payload' or self._goal_needed(env.intent.get('cognition') or {}) else 'not_required')),
            'delivery_surface': 'diagnostic' if explicit_diag else ('runtime_natural' if env.surface == 'aos_environment' else 'project_natural'),
            'performance_budget': budget,
        }
        return env

    def _invoke_layer_matrix(self, env: OperationEnvelope) -> OperationEnvelope:
        plan = env.intent.get('contribution_plan') or {}
        scope_plan = env.scope_plan or {}
        root = Path(scope_plan.get('primary_root') or self._scope_root('active_project_payload'))
        context = make_operation_context(env.operation_id, 'multi_layer_matrix', scope_plan=scope_plan)

        calls = {
            'truth_requirement_preview': lambda: self._truth_requirement_preview(env, context),
        }
        if plan.get('goal_runtime') != 'not_required':
            calls['goal_runtime'] = lambda: self._goal_memory_contribution(env, context)

        if env.surface == 'active_project_payload' and (env.intent.get('performance_budget') or {}).get('project_truth_policy') != 'forbidden':
            calls['project_truth'] = lambda: self._project_truth_contribution(env, root, context)

        if plan.get('artifact_depth') == 'none':
            calls['artifact_matrix'] = lambda: {
                'artifact_matrix': self._minimal_artifact_matrix(env.surface, 'identity-only request does not require artifact scan'),
                'contribution': LayerContribution(
                    layer='artifact_cockpit',
                    mode='not_invoked_for_simple_intent',
                    value='لم يتم تشغيل فحص الملفات لأن النية لا تحتاجه؛ تم الاكتفاء بالهوية والنية وسياق الحقيقة المتاح.',
                    evidence=[{'type': 'condition', 'value': 'HOT_IDENTITY_ONLY'}],
                    ignored_noise=['unneeded file scan'],
                ).to_dict(),
            }
        else:
            calls['artifact_matrix'] = lambda: self._artifact_contribution(env, root, plan, context)

        result = self.invoker.invoke(calls, max_workers=5)
        env.intent['matrix_invocation'] = {k: v for k, v in result.items() if k != 'results'}
        env.intent['matrix_invocation']['call_names'] = sorted(calls.keys())
        if result.get('errors'):
            env.add_contribution(LayerContribution(
                layer='layer_invocation',
                mode='fanout_errors',
                value='بعض استدعاءات الطبقات فشلت؛ يجب إعلان ذلك أو خفض الثقة بدل إنتاج رد طبيعي.',
                risks=[{'severity': 'block', 'code': 'required_layer_error', 'errors': result.get('errors')}],
                ignored_noise=[],
            ).to_dict())
        for name, item in (result.get('results') or {}).items():
            if isinstance(item, dict) and item.get('layer'):
                env.add_contribution(item)
            elif isinstance(item, dict) and item.get('artifact_matrix'):
                env.artifact_matrix = item['artifact_matrix']
                env.add_contribution(item['contribution'])
        return env

    def _ground_truth(self, env: OperationEnvelope) -> OperationEnvelope:
        truth_api = self.registry.get('truth_runtime')
        context = make_operation_context(env.operation_id, 'truth_grounding_after_merge', scope_plan=env.scope_plan, layer_id='truth_runtime')
        intent = dict(env.intent)
        intent.update(context.to_intent(surface=env.surface, truth_need='authoritative_packet'))
        req_result = truth_api.execute(LayerCommand(
            operation_id=env.operation_id,
            layer_id='truth_runtime',
            command='truth.resolve_requirement',
            payload={'request_text': env.request_text, 'surface': env.surface},
            context=intent,
        ))
        env.truth_requirement = req_result.get('data') or {}
        cockpit = {'mode': 'operations_runtime_graph_cockpit', 'surface': env.surface, 'scope_plan': env.scope_plan}
        packet_result = truth_api.execute(LayerCommand(
            operation_id=env.operation_id,
            layer_id='truth_runtime',
            command='truth.produce_authoritative_packet',
            payload={
                'request_text': env.request_text,
                'artifact_matrix': env.artifact_matrix,
                'cockpit': cockpit,
                'surface': env.surface,
                'contributions': env.contributions,
                'truth_context': env.truth_context,
                'scope_plan': env.scope_plan,
            },
            context=intent,
        ))
        env.truth_packet = packet_result.get('data') or {}
        env.add_contribution(self._truth_contribution(env.truth_packet))
        return env

    def _merge_contributions(self, env: OperationEnvelope) -> OperationEnvelope:
        env.intent['merged_contributions'] = self.bus.merge([self.bus.normalize(c) for c in env.contributions])
        return env

    def _resolve_contradictions(self, env: OperationEnvelope) -> OperationEnvelope:
        env.contradictions = self.resolver.resolve(env.intent.get('merged_contributions') or {})
        return env

    def _second_pass_if_needed(self, env: OperationEnvelope) -> OperationEnvelope:
        if not env.contradictions:
            return env
        if env.surface in {'aos_environment', 'workshop_general_truth'}:
            env.intent['second_pass_invocation'] = {
                'mode': 'skipped_by_surface_budget',
                'reason': 'runtime/workshop surfaces do not refocus through active payload scans',
                'call_count': 0,
                'call_names': [],
            }
            return env
        root = Path((env.scope_plan or {}).get('primary_root') or self._scope_root('active_project' if env.surface == 'active_project_payload' else ('workshop' if env.surface == 'workshop_general_truth' else 'aos')))
        context = make_operation_context(env.operation_id, 'second_pass_contradiction_resolution', scope_plan=env.scope_plan)
        focus = ' '.join([c.get('type', '') for c in env.contradictions]) + ' ' + (env.request_text or '')
        calls = {
            'artifact_refocus': lambda: self._artifact_contribution(env, root, {'artifact_depth': 'fast_value'}, context, query_override=focus),
        }
        if env.surface == 'active_project_payload':
            calls['project_truth_refocus'] = lambda: self._project_truth_contribution(env, root, context, refocus=True)
        result = self.invoker.invoke(calls, max_workers=2)
        env.intent['second_pass_invocation'] = {k: v for k, v in result.items() if k != 'results'}
        env.intent['second_pass_invocation']['call_names'] = sorted(calls.keys())
        for item in (result.get('results') or {}).values():
            if isinstance(item, dict) and item.get('layer'):
                item['mode'] = str(item.get('mode') or '') + '_second_pass'
                env.add_contribution(item)
            elif isinstance(item, dict) and item.get('artifact_matrix'):
                env.artifact_matrix = item['artifact_matrix']
                contrib = item['contribution']
                contrib['mode'] = str(contrib.get('mode') or '') + '_second_pass'
                env.add_contribution(contrib)
        env.intent['merged_contributions'] = self.bus.merge([self.bus.normalize(c) for c in env.contributions])
        env.contradictions = self.resolver.resolve(env.intent.get('merged_contributions') or {})
        return env

    def _synthesize_insight(self, env: OperationEnvelope) -> OperationEnvelope:
        env.operational_insight = self.synthesizer.synthesize(env, env.intent.get('merged_contributions') or {}, env.contradictions)
        return env

    def _render_delivery(self, env: OperationEnvelope) -> OperationEnvelope:
        answer = self.renderer.render(env)
        validation = self.renderer.validate(answer, env)
        grounding = self.delivery_gate.validate(answer, env)
        if not validation['passed'] or not grounding['passed']:
            answer = self._safe_insight_answer(env)
            validation = self.renderer.validate(answer, env)
            grounding = self.delivery_gate.validate(answer, env)
        env.delivery = {'answer': answer, 'validation': validation, 'grounding_gate': grounding}
        return env

    # Contribution helpers ---------------------------------------------
    def _project_truth_contribution(self, env: OperationEnvelope, root: Path, context: Any, *, refocus: bool = False) -> Dict[str, Any]:
        api = self.registry.get('project_truth')
        result = api.execute(LayerCommand(
            operation_id=env.operation_id,
            layer_id='project_truth',
            command='project_truth.contribute',
            payload={'project_root': root.as_posix(), 'request_text': env.request_text},
            context=context.to_intent(surface=env.surface, refocus=refocus, layer_id='project_truth'),
        ))
        c = result.get('data') or {}
        if refocus:
            c['mode'] = str(c.get('mode') or '') + '_refocus'
            c.setdefault('evidence', []).append({'type': 'refocus_reason', 'value': [x.get('type') for x in env.contradictions]})
        return c

    def _truth_requirement_preview(self, env: OperationEnvelope, context: Any) -> Dict[str, Any]:
        truth_api = self.registry.get('truth_runtime')
        intent = dict(env.intent)
        intent.update(context.to_intent(surface=env.surface, truth_need='preview', layer_id='truth_runtime'))
        req_result = truth_api.execute(LayerCommand(
            operation_id=env.operation_id,
            layer_id='truth_runtime',
            command='truth.resolve_requirement',
            payload={'request_text': env.request_text, 'surface': env.surface},
            context=intent,
        ))
        req = req_result.get('data') or {}
        return LayerContribution(
            layer='truth_requirement',
            mode='preview_before_full_grounding',
            value='تم تحديد عمق الحقيقة المطلوب مبكرًا قبل التسليم؛ النية لا تتحول إلى قرار دون وزن الحقيقة.',
            evidence=[{'type': 'truth_requirement_preview', 'value': req}],
            next_needs=['ground_truth_after_layer_contributions'],
            ignored_noise=['treating initial intent as final action'],
        ).to_dict()

    def _artifact_contribution(self, env: OperationEnvelope, root: Path, plan: Dict[str, Any], context: Any, query_override: str | None = None) -> Dict[str, Any]:
        query = query_override or env.request_text
        if plan.get('artifact_depth') == 'deep_diagnostic':
            raw_result = self.registry.get('artifact_matrix').execute(LayerCommand(
                operation_id=env.operation_id,
                layer_id='artifact_matrix',
                command='artifact.inspect',
                payload={'root': root.as_posix(), 'query': query, 'changed_paths': []},
                context=context.to_intent(surface=env.surface, artifact_need='deep_diagnostic', layer_id='artifact_matrix'),
            ))
            raw = raw_result.get('data') or {}
            env_matrix = self._compact_matrix(raw)
            return {'artifact_matrix': env_matrix, 'contribution': self._contribution_from_matrix(env_matrix, mode='deep_diagnostic_compacted')}
        matrix = self.quick_artifacts.scan(root, query=query, surface=env.surface)
        return {'artifact_matrix': matrix, 'contribution': self.quick_artifacts.contribution(matrix)}

    def _goal_memory_contribution(self, env: OperationEnvelope, context: Any) -> Dict[str, Any]:
        api = self.registry.get('goal_runtime')
        result = api.execute(LayerCommand(
            operation_id=env.operation_id,
            layer_id='goal_runtime',
            command='goal.experience_patterns',
            payload={'request_text': env.request_text, 'intent': env.intent},
            context=context.to_intent(surface=env.surface, goal_need=(env.intent.get('contribution_plan') or {}).get('goal_runtime'), layer_id='goal_runtime'),
        ))
        return result.get('data') or {}

    def _truth_contribution(self, truth_packet: Dict[str, Any]) -> Dict[str, Any]:
        sem = truth_packet.get('truth_value_semantics') or {}
        incomplete = truth_packet.get('incomplete_truth') or {}
        value = 'الحقيقة موزونة بالقيمة والسياق والعلاقة والنية؛ لا تُختزل في حجم الملف أو حالة ملف واحد.'
        if sem.get('empty_declared_target_count'):
            value += ' توجد أهداف بناء فارغة يجب إنضاجها لا تجاهلها.'
        if sem.get('declared_missing_artifact_count'):
            value += ' توجد وعود حقيقة معلنة تحتاج إغلاقًا أو تأجيلًا موثقًا.'
        return LayerContribution(
            layer='truth_runtime',
            mode='truth_value_grounding',
            value=value,
            evidence=[{'type': 'truth_value_semantics', 'value': sem}, {'type': 'sufficiency', 'value': truth_packet.get('sufficiency')}],
            risks=(incomplete.get('issues') or [])[:10],
            next_needs=['mature_incomplete_truth'] if incomplete.get('maturity_issue_count') else [],
            ignored_noise=['raw file count as truth', 'single artifact as final truth'],
        ).to_dict()

    def _contribution_from_matrix(self, matrix: Dict[str, Any], *, mode: str) -> Dict[str, Any]:
        sem = matrix.get('truth_value_semantics') or {}
        owner = matrix.get('owner_signal') or {}
        next_needs: List[str] = []
        if sem.get('empty_declared_target_count'):
            next_needs.append('mature_declared_construction_targets')
        if sem.get('declared_missing_artifact_count'):
            next_needs.append('close_or_defer_missing_declared_artifacts')
        if sem.get('duplicate_functional_truth_count'):
            next_needs.append('resolve_duplicate_functional_truth_owner')
        if owner.get('label'):
            next_needs.append('mature_primary_owner_truth')
        return LayerContribution(
            layer='artifact_cockpit',
            mode=mode,
            value='تم تحويل الفحص التشخيصي إلى مساهمة قيمة مختصرة بدل تقرير خام.',
            evidence=[{'type': 'condition', 'value': matrix.get('project_condition')}, {'type': 'owner_signal', 'value': owner}, {'type': 'value_map', 'value': matrix.get('value_map')}, {'type': 'high_value_sources', 'value': (sem.get('high_value_sources') or [])[:8]}],
            risks=((matrix.get('diagnostics') or {}).get('top_issues') or [])[:12],
            next_needs=next_needs,
            ignored_noise=['raw file matrix', 'diagnostic dump as answer'],
        ).to_dict()

    def _compact_matrix(self, raw: Dict[str, Any]) -> Dict[str, Any]:
        out = dict(raw)
        if isinstance(out.get('records'), list):
            out['records'] = out['records'][:40]
        out['packet_mode'] = 'operations_runtime_deep_compacted'
        return out

    def _intent_next_needs(self, cognition: Dict[str, Any]) -> List[str]:
        needs = cognition.get('layer_needs') or {}
        out: List[str] = []
        if needs.get('artifact_cockpit'):
            out.append(f"artifact:{needs.get('artifact_cockpit')}")
        if needs.get('goal_runtime') and needs.get('goal_runtime') != 'not_required_for_normal_answer':
            out.append(f"goal:{needs.get('goal_runtime')}")
        return out

    def _goal_needed(self, cognition: Dict[str, Any]) -> bool:
        need = ((cognition.get('layer_needs') or {}).get('goal_runtime') or '')
        return need not in {'', 'not_required_for_normal_answer'}


    def _minimal_artifact_matrix(self, surface: str, reason: str) -> Dict[str, Any]:
        condition = 'HOT_IDENTITY_ONLY' if surface == 'active_project_payload' else 'RUNTIME_HOT_IDENTITY'
        return {
            'version': 'operations-runtime-minimal',
            'capability': 'operations_runtime',
            'authority': 'not_invoked_for_simple_intent',
            'authority_scope': 'identity_truth_only',
            'project_condition': condition,
            'file_count': 0,
            'summary': {'project_condition': condition},
            'records': [],
            'diagnostics': {'mode': 'not_run_for_simple_intent', 'issue_count': 0, 'blocking_count': 0, 'maturity_issue_count': 0},
            'truth_value_semantics': {},
            'packet_mode': 'operations_identity_minimal_no_artifact_scan',
            'reason': reason,
        }

    def _scope_root(self, scope: str) -> Path:
        if scope == 'aos':
            return self.paths.root
        if scope == 'workshop':
            return self.paths.workshop_system
        return self.paths.project_upload

    def _safe_insight_answer(self, env: OperationEnvelope) -> str:
        insight = env.operational_insight or {}
        summary = insight.get('summary') or ['أتعامل مع المشروع من الحقيقة المتاحة ولا أستخدم بيئة التشغيل كسطح ظاهر.']
        first = insight.get('first_step') or 'ابنِ حزمة حقيقة مغلقة للنطاق المطلوب قبل أي تنفيذ.'
        return '\n\n'.join(['أعمل هنا كمهندس مشروع تشغيلي يستند إلى الحقيقة والسياق.', 'قراءة الحقيقة الحالية:\n' + '\n'.join('- ' + str(x).lstrip('- ').strip() for x in summary[:4]), first if str(first).startswith('أول خطوة') else 'أول خطوة صحيحة: ' + str(first)])

    def _packet(self, env: OperationEnvelope) -> Dict[str, Any]:
        return {
            'operations_runtime': {
                'version': self.VERSION,
                'entry_owner': 'operations_runtime',
                'operation_id': env.operation_id,
                'graph_trace': env.trace,
                'layer_registry': self.registry.describe(),
            },
            'intent': env.intent,
            'scope': {'active_project_state': env.active_project_state, 'operation_contract': env.operation_contract, 'scope_plan': env.scope_plan, 'truth_context': env.truth_context},
            'file_matrix': env.artifact_matrix,
            'truth': {'requirement': env.truth_requirement, 'packet': env.truth_packet},
            'intent_cognition': env.intent.get('cognition'),
            'contributions': env.contributions,
            'contradictions': env.contradictions,
            'operations': {'operational_insight': env.operational_insight, 'matrix_invocation': env.intent.get('matrix_invocation')},
            'delivery': env.delivery,
            'operations_delivery_gate': (env.delivery or {}).get('validation'),
            'delivery_grounding_gate': (env.delivery or {}).get('grounding_gate'),
        }
