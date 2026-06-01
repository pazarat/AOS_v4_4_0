from __future__ import annotations

from typing import Any, Dict, List

from aos_core.ports.truth_port import TruthPort
from operations_runtime.context import is_valid_operations_intent


def _blocked(operation: str) -> Dict[str, Any]:
    return {
        'layer': 'truth_runtime',
        'operation': operation,
        'status': 'blocked',
        'authority': 'denied_without_operations_context',
        'reason': 'Truth Runtime can be invoked only through Operations Runtime Kernel.',
        'sufficiency': {'decision': 'BLOCKED_DIRECT_ACCESS'},
        'truth_value_semantics': {},
        'incomplete_truth': {'maturity_issue_count': 0, 'issues': []},
    }


class TruthRuntimeAPI:
    """Truth Runtime mini-runtime gateway behind Operations Runtime."""

    layer_id = 'truth_runtime'

    def __init__(self, paths: Any) -> None:
        self.port = TruthPort(paths)

    def describe(self) -> Dict[str, Any]:
        return {
            'layer_id': self.layer_id,
            'role': 'truth requirement, truth packet, sufficiency, claim grounding, and arbiter decision',
            'commands': ['truth.resolve_requirement', 'truth.build_packet', 'truth.produce_authoritative_packet', 'truth.validate_response'],
            'entrypoint': 'aos_capabilities.truth_runtime.main.TruthRuntimeAPI',
        }

    def healthcheck(self) -> Dict[str, Any]:
        try:
            return self.port.health() | {'layer_id': self.layer_id}
        except Exception as exc:
            return {'status': 'degraded', 'layer_id': self.layer_id, 'error': str(exc)}

    def validate_contract(self) -> Dict[str, Any]:
        return {'passed': True, 'issues': [], 'required_context': 'operations_runtime_context'}

    def execute(self, command: Any) -> Dict[str, Any]:
        data = command.to_dict() if hasattr(command, 'to_dict') else dict(command or {})
        payload = data.get('payload') or {}
        context = data.get('context') or payload.get('intent')
        cmd = data.get('command')
        if cmd in {'truth.resolve_requirement', 'resolve_requirement'}:
            result = self.resolve_requirement(payload.get('request_text', ''), intent=context or {}, surface=payload.get('surface', 'active_project_payload'))
        elif cmd in {'truth.build_packet', 'build_packet'}:
            result = self.build_packet(payload.get('request_text', ''), intent=context or {}, artifact_matrix=payload.get('artifact_matrix') or {}, cockpit=payload.get('cockpit') or {}, surface=payload.get('surface', 'active_project_payload'))
        elif cmd in {'truth.produce_authoritative_packet', 'produce_authoritative_packet'}:
            result = self.produce_authoritative_packet(
                payload.get('request_text', ''),
                intent=context or {},
                artifact_matrix=payload.get('artifact_matrix') or {},
                cockpit=payload.get('cockpit') or {},
                surface=payload.get('surface', 'active_project_payload'),
                contributions=payload.get('contributions') or [],
                truth_context=payload.get('truth_context') or {},
                scope_plan=payload.get('scope_plan') or {},
            )
        else:
            result = _blocked(str(cmd or 'unknown')) | {'reason': 'unsupported_command'}
        return {'operation_id': data.get('operation_id'), 'layer_id': self.layer_id, 'command': cmd, 'status': result.get('status', 'ok'), 'data': result}

    def resolve_requirement(self, request_text: str, *, intent: Dict[str, Any], surface: str) -> Dict[str, Any]:
        if not is_valid_operations_intent(intent):
            return _blocked('truth.resolve_requirement')
        out = self.port.resolve_requirement(request_text, intent=intent, surface=surface)
        out['called_through'] = 'operations_runtime'
        return out

    def build_packet(self, request_text: str, *, intent: Dict[str, Any], artifact_matrix: Dict[str, Any], cockpit: Dict[str, Any], surface: str) -> Dict[str, Any]:
        if not is_valid_operations_intent(intent):
            return _blocked('truth.build_packet')
        out = self.port.build_packet(request_text, intent=intent, artifact_matrix=artifact_matrix, cockpit=cockpit, surface=surface)
        out['called_through'] = 'operations_runtime'
        return out

    def produce_authoritative_packet(self, request_text: str, *, intent: Dict[str, Any], artifact_matrix: Dict[str, Any], cockpit: Dict[str, Any], surface: str, contributions: List[Dict[str, Any]], truth_context: Dict[str, Any], scope_plan: Dict[str, Any]) -> Dict[str, Any]:
        if not is_valid_operations_intent(intent):
            return _blocked('truth.produce_authoritative_packet')
        packet = self.build_packet(request_text, intent=intent, artifact_matrix=artifact_matrix, cockpit=cockpit, surface=surface)
        packet['truth_context'] = truth_context
        packet['scope_plan'] = scope_plan
        packet['contribution_count'] = len(contributions or [])
        packet['arbiter'] = self._arbiter_decision(packet, contributions or [], truth_context, scope_plan, surface)
        return packet

    def validate_response(self, packet: Dict[str, Any], response_text: str | None = None, *, intent: Dict[str, Any] | None = None) -> Dict[str, Any]:
        if not is_valid_operations_intent(intent):
            return _blocked('truth.validate_response')
        return self.port.validate_response(packet, response_text=response_text)

    def _arbiter_decision(self, packet: Dict[str, Any], contributions: List[Dict[str, Any]], truth_context: Dict[str, Any], scope_plan: Dict[str, Any], surface: str) -> Dict[str, Any]:
        blockers = []
        warnings = []
        for c in contributions:
            if c.get('status') == 'blocked':
                blockers.append({'code': 'required_layer_blocked', 'layer': c.get('layer')})
            for risk in c.get('risks') or []:
                if isinstance(risk, dict) and risk.get('severity') == 'block':
                    blockers.append(risk)
        if truth_context.get('missing_required_truth'):
            warnings.append({'code': 'truth_context_partial', 'missing': truth_context.get('missing_required_truth')})
        if surface == 'aos_environment' and scope_plan.get('active_project_role') == 'fixture_only_excluded_from_runtime_truth':
            warnings.append({'code': 'fixture_excluded_from_runtime_truth', 'policy': scope_plan.get('fixture_policy')})
        suff = packet.get('sufficiency') or {}
        if blockers:
            decision = 'BLOCK'
        elif suff.get('decision') in {'INSUFFICIENT', 'MATURE'} or warnings:
            decision = 'ANSWER_WITH_LIMITS'
        else:
            decision = 'ALLOW'
        return {
            'decision': decision,
            'blockers': blockers,
            'warnings': warnings,
            'supported_claim_policy': 'claims must be sourced from truth_context, layer contributions, or explicitly marked as inference/unknown',
        }


def create(paths: Any) -> TruthRuntimeAPI:
    return TruthRuntimeAPI(paths)
