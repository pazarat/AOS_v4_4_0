from __future__ import annotations

from typing import Any, Dict, List

from aos_core.config import AOSPaths
from aos_capabilities.goal_runtime import GoalRuntime


class GoalRuntimePort:
    def __init__(self, paths: AOSPaths):
        self.runtime = GoalRuntime(paths.runtime_state / 'goals')

    def health(self) -> Dict[str, Any]:
        return self.runtime.health()

    def open(self, target: str, success_criteria: List[str] | None = None, context: Dict[str, Any] | None = None) -> Dict[str, Any]:
        return self.runtime.open(target, success_criteria, context)

    def record_observation(self, goal_id: str, observation: Dict[str, Any]) -> Dict[str, Any]:
        return self.runtime.record_observation(goal_id, observation)

    def record_attempt(self, goal_id: str, attempt: Dict[str, Any]) -> Dict[str, Any]:
        return self.runtime.record_attempt(goal_id, attempt)

    def check_progress(self, goal_id: str) -> Dict[str, Any]:
        return self.runtime.check_progress(goal_id)

    def close(self, goal_id: str, evidence: Dict[str, Any] | None = None) -> Dict[str, Any]:
        return self.runtime.close(goal_id, evidence)
