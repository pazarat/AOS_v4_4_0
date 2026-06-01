from __future__ import annotations

from typing import Dict, List


class StateTransitionError(RuntimeError):
    pass


class StateGraph:
    """Deterministic lifecycle graph.

    INTENT_INTAKE is mandatory before goals. The graph preserves a stable
    backbone: tools and providers are forbidden here.
    """

    transitions: Dict[str, List[str]] = {
        'IDLE': ['BOOTED', 'INTENT_INTAKE', 'DISCOVERY'],
        'BOOTED': ['INTENT_INTAKE', 'DISCOVERY'],
        'INTENT_INTAKE': ['DISCOVERY', 'TRUTH_BUILDING', 'GOAL_INTAKE', 'POLICY_REVIEW', 'DONE'],
        'DISCOVERY': ['INTENT_INTAKE', 'TRUTH_BUILDING', 'GOAL_INTAKE'],
        'TRUTH_BUILDING': ['INTENT_INTAKE', 'GOAL_INTAKE', 'POLICY_REVIEW'],
        'GOAL_INTAKE': ['PLANNING'],
        'PLANNING': ['POLICY_REVIEW'],
        'POLICY_REVIEW': ['SANDBOX_EXECUTION', 'HUMAN_APPROVAL', 'BLOCKED', 'EVALUATION'],
        'HUMAN_APPROVAL': ['SANDBOX_EXECUTION', 'BLOCKED'],
        'SANDBOX_EXECUTION': ['EVALUATION'],
        'EVALUATION': ['DONE', 'PLANNING', 'BLOCKED'],
        'BLOCKED': ['INTENT_INTAKE', 'GOAL_INTAKE', 'DISCOVERY'],
        'DONE': ['IDLE', 'INTENT_INTAKE']
    }

    def __init__(self, current: str = 'IDLE'):
        self.current = current

    def can_transition(self, target: str) -> bool:
        return target in self.transitions.get(self.current, [])

    def transition(self, target: str) -> str:
        if not self.can_transition(target):
            raise StateTransitionError(f'Invalid transition: {self.current} -> {target}')
        self.current = target
        return self.current
