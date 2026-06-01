from __future__ import annotations

from typing import Any, Dict

from aos_core.config import AOSPaths
from aos_core.contracts import Fact
from aos_capabilities.truth_runtime.adapter import create


class TruthPort:
    """Stable-spine port for Truth Runtime.

    Truth is a capability. The core may ask for truth requirements, packets,
    sufficiency, and grounding decisions, but must not embed truth reasoning as
    core implementation detail.
    """

    capability_id = 'truth_runtime'

    def __init__(self, paths: AOSPaths):
        self.runtime = create(paths)

    def health(self) -> Dict[str, Any]:
        return self.runtime.health()

    def snapshot(self) -> Dict[str, Any]:
        return self.runtime.snapshot()

    def add_fact(self, fact: Fact) -> None:
        self.runtime.add_fact(fact)

    def add_assumption(self, statement: str, source: str, confidence: float = 0.5) -> None:
        self.runtime.add_assumption(statement, source, confidence)

    def add_question(self, question: str, reason: str) -> None:
        self.runtime.add_question(question, reason)

    def resolve_requirement(self, request_text: str, intent: Dict[str, Any] | None = None, surface: str | None = None) -> Dict[str, Any]:
        return self.runtime.resolve_requirement(request_text, intent=intent, surface=surface)

    def build_packet(self, request_text: str, intent: Dict[str, Any] | None = None, artifact_matrix: Dict[str, Any] | None = None, cockpit: Dict[str, Any] | None = None, surface: str | None = None) -> Dict[str, Any]:
        return self.runtime.build_packet(request_text, intent=intent, artifact_matrix=artifact_matrix, cockpit=cockpit, surface=surface)

    def check_sufficiency(self, packet: Dict[str, Any]) -> Dict[str, Any]:
        return self.runtime.check_sufficiency(packet)

    def detect_incomplete(self, requirement: Dict[str, Any], artifact_matrix: Dict[str, Any] | None = None) -> Dict[str, Any]:
        return self.runtime.detect_incomplete(requirement, artifact_matrix=artifact_matrix)

    def validate_response(self, packet: Dict[str, Any], response_text: str | None = None) -> Dict[str, Any]:
        return self.runtime.validate_response(packet, response_text=response_text)

    def validate_execution(self, packet: Dict[str, Any], plan: Dict[str, Any] | None = None) -> Dict[str, Any]:
        return self.runtime.validate_execution(packet, plan=plan)

    def receipt(self, packet: Dict[str, Any] | None = None, operation: str = 'truth.receipt') -> Dict[str, Any]:
        return self.runtime.receipt(packet=packet, operation=operation)
