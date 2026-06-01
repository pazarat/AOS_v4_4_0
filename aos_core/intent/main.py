from __future__ import annotations

from typing import Any, Dict

from aos_core.intent.intent_cognition import IntentCognitionRuntime
from aos_core.intent.intent_engine import IntentEngine
from operations_runtime.context import is_valid_operations_intent


class IntentLayerAPI:
    """Intent Cognition mini-runtime gateway behind Operations Runtime."""

    layer_id = 'intent_cognition'

    def __init__(self) -> None:
        self.engine = IntentEngine()
        self.cognition = IntentCognitionRuntime()

    def describe(self) -> Dict[str, Any]:
        return {
            'layer_id': self.layer_id,
            'role': 'resolve user surface, intent hypothesis, risk, and required layer depth',
            'commands': ['intent.resolve'],
            'entrypoint': 'aos_core.intent.main.IntentLayerAPI',
        }

    def healthcheck(self) -> Dict[str, Any]:
        return {'status': 'healthy', 'layer_id': self.layer_id}

    def validate_contract(self) -> Dict[str, Any]:
        return {'passed': True, 'issues': [], 'required_context': 'operations_runtime_context'}

    def execute(self, command: Any) -> Dict[str, Any]:
        data = command.to_dict() if hasattr(command, 'to_dict') else dict(command or {})
        payload = data.get('payload') or {}
        context = data.get('context') or payload.get('operation_context')
        if data.get('command') in {'intent.resolve', 'resolve'}:
            result = self.resolve(
                payload.get('request_text', ''),
                active_project_state=payload.get('active_project_state'),
                truth_requirement=payload.get('truth_requirement'),
                operation_context=context,
            )
            return {'operation_id': data.get('operation_id'), 'layer_id': self.layer_id, 'command': data.get('command'), 'status': result.get('status'), 'data': result}
        return {'operation_id': data.get('operation_id'), 'layer_id': self.layer_id, 'command': data.get('command'), 'status': 'blocked', 'data': {'reason': 'unsupported_command'}}

    def resolve(self, request_text: str, *, active_project_state: Dict[str, Any] | None = None, truth_requirement: Dict[str, Any] | None = None, operation_context: Dict[str, Any] | None = None) -> Dict[str, Any]:
        if not is_valid_operations_intent(operation_context):
            return {
                'status': 'blocked',
                'layer': self.layer_id,
                'reason': 'Intent layer is callable only through Operations Runtime Kernel.',
                'summary': {},
                'cognition': {'validation': {'passed': False, 'issues': ['missing_or_unissued_operations_context']}},
            }
        frame = self.engine.resolve(request_text, None)
        summary = self.engine.summary(frame)
        packet = self.cognition.build(request_text, frame, active_project_state=active_project_state or {}, truth_requirement=truth_requirement or {})
        packet['operation_context'] = {'operation_id': operation_context.get('operation_id'), 'caller': operation_context.get('called_by')}
        return {'status': 'ok', 'summary': summary, 'cognition': packet, 'validation': self.cognition.validate_spine_flow(packet)}


def create() -> IntentLayerAPI:
    return IntentLayerAPI()
