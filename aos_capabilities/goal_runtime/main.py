from __future__ import annotations

from typing import Any, Dict

from aos_core.ports.goal_runtime_port import GoalRuntimePort
from operations_runtime.context import is_valid_operations_intent


def _blocked(operation: str) -> Dict[str, Any]:
    return {
        'layer': 'goal_runtime',
        'operation': operation,
        'status': 'blocked',
        'authority': 'denied_without_operations_context',
        'reason': 'Goal Runtime can be invoked only through Operations Runtime Kernel.',
    }


class GoalRuntimeAPI:
    """Goal Runtime mini-runtime gateway behind Operations Runtime."""

    layer_id = 'goal_runtime'

    def __init__(self, paths: Any) -> None:
        self.port = GoalRuntimePort(paths)

    def describe(self) -> Dict[str, Any]:
        return {
            'layer_id': self.layer_id,
            'role': 'resolve goal memory, repeated-failure patterns, and action planning signals',
            'commands': ['goal.experience_patterns', 'goal.open'],
            'entrypoint': 'aos_capabilities.goal_runtime.main.GoalRuntimeAPI',
        }

    def healthcheck(self) -> Dict[str, Any]:
        return {'status': 'healthy', 'layer_id': self.layer_id}

    def validate_contract(self) -> Dict[str, Any]:
        return {'passed': True, 'issues': [], 'required_context': 'operations_runtime_context'}

    def execute(self, command: Any) -> Dict[str, Any]:
        data = command.to_dict() if hasattr(command, 'to_dict') else dict(command or {})
        payload = data.get('payload') or {}
        context = data.get('context') or payload.get('context')
        cmd = data.get('command')
        if cmd in {'goal.experience_patterns', 'experience_patterns'}:
            result = self.experience_patterns(request_text=payload.get('request_text', ''), intent=payload.get('intent'), context=context)
        elif cmd in {'goal.open', 'open'}:
            result = self.open(payload.get('text', ''), success_criteria=payload.get('success_criteria'), context=context)
        else:
            result = _blocked(str(cmd or 'unknown')) | {'reason': 'unsupported_command'}
        return {'operation_id': data.get('operation_id'), 'layer_id': self.layer_id, 'command': cmd, 'status': result.get('status', 'ok'), 'data': result}

    def experience_patterns(self, *, request_text: str, intent: Dict[str, Any] | None = None, context: Dict[str, Any] | None = None) -> Dict[str, Any]:
        if not is_valid_operations_intent(context):
            return _blocked('goal.experience_patterns')
        text = (request_text or '').lower()
        repeated_patch_signal = any(x in text for x in ['ترقيع', 'فشل', 'تكرر', 'دوامة', 'لم ينجح', 'not working', 'failed', 'patch loop'])
        runtime_architecture_signal = any(x in text for x in ['مركز العمليات', 'غرفة العمليات', 'kernel', 'runtime', 'microkernel', 'طبقة الحقيقة', 'طبقة الهدف'])
        patterns = []
        if repeated_patch_signal or runtime_architecture_signal:
            patterns.append({
                'pattern': 'mature_layers_but_behavior_not_improved',
                'lesson': 'افحص حاكم التشغيل والتدفق والعقود قبل إضافة قوانين سطحية أو تقوية طبقة منفردة.',
                'avoid': ['word-level patching', 'single layer patching', 'raw report dumping'],
                'prefer': 'truth-bound governance kernel + contracted layer mini-runtimes + delivery grounding gate',
            })
        patterns.append({
            'pattern': 'ordinary_project_answer',
            'lesson': 'لا تفتح هدفًا ثقيلًا لسؤال عام؛ استخدم الذاكرة كخبرة خفيفة فقط.',
            'prefer': 'answer from synthesized truth insight',
        })
        return {
            'layer': self.layer_id,
            'status': 'ok',
            'mode': 'experience_memory_lightweight',
            'value': 'تم استحضار خبرة الهدف كإرشاد نمطي خفيف لمنع تكرار الترقيع، لا كدفتر مهمة ثقيل.',
            'evidence': [{'type': 'experience_patterns', 'value': patterns}],
            'risks': [],
            'next_needs': ['open_active_goal_only_for_committed_repair_or_execution'],
            'ignored_noise': ['opening heavy goal ledger for ordinary answer'],
        }

    def open(self, text: str, *, success_criteria: list[str] | None = None, context: Dict[str, Any] | None = None) -> Dict[str, Any]:
        if not is_valid_operations_intent(context):
            return _blocked('goal.open')
        return self.port.open(text, success_criteria=success_criteria or [], context=context or {})


def create(paths: Any) -> GoalRuntimeAPI:
    return GoalRuntimeAPI(paths)
