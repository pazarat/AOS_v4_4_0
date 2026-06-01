from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, Optional

from aos_core.config import AOSPaths
from aos_core.contracts import Fact
from aos_capabilities.truth_runtime.truth_store import TruthStore
from aos_capabilities.truth_runtime.truth_requirement.resolver import TruthRequirementResolver
from aos_capabilities.truth_runtime.truth_packet.builder import TruthPacketBuilder
from aos_capabilities.truth_runtime.truth_sufficiency.checker import TruthSufficiencyChecker
from aos_capabilities.truth_runtime.incomplete_truth.reasoner import IncompleteTruthReasoner
from aos_capabilities.truth_runtime.grounding.response_validator import ResponseGroundingValidator
from aos_capabilities.truth_runtime.grounding.execution_validator import ExecutionGroundingValidator
from aos_capabilities.truth_runtime.receipts.truth_receipt import TruthReceiptBuilder

API_SURFACE = [
    'truth.health',
    'truth.resolve_requirement',
    'truth.build_packet',
    'truth.check_sufficiency',
    'truth.detect_incomplete',
    'truth.validate_response',
    'truth.validate_execution',
    'truth.receipt',
]


class TruthRuntime:
    def __init__(self, paths: AOSPaths):
        self.paths = paths
        self.store = TruthStore(paths)

    def health(self) -> Dict[str, Any]:
        return {
            'status': 'healthy',
            'capability': 'truth_runtime',
            'api_surface': API_SURFACE,
            'truth_index_path': self.store.truth_index_path.as_posix(),
            'core_rule': 'core_uses_truth_port_only',
        }

    def snapshot(self) -> Dict[str, Any]:
        return self.store.snapshot()

    def add_fact(self, fact: Fact) -> None:
        self.store.add_fact(fact)

    def add_assumption(self, statement: str, source: str, confidence: float = 0.5) -> None:
        self.store.add_assumption(statement, source, confidence)

    def add_question(self, question: str, reason: str) -> None:
        self.store.add_question(question, reason)

    def resolve_requirement(self, request_text: str, intent: Dict[str, Any] | None = None, surface: str | None = None) -> Dict[str, Any]:
        return TruthRequirementResolver().resolve(request_text, intent=intent, surface=surface)

    def build_packet(self, request_text: str, intent: Dict[str, Any] | None = None, artifact_matrix: Dict[str, Any] | None = None, cockpit: Dict[str, Any] | None = None, surface: str | None = None) -> Dict[str, Any]:
        requirement = self.resolve_requirement(request_text, intent=intent, surface=surface)
        packet = TruthPacketBuilder().build(requirement, artifact_matrix=artifact_matrix, truth_store=self.snapshot(), cockpit=cockpit)
        suff = TruthSufficiencyChecker().check(packet)
        packet['sufficiency'] = suff
        packet['receipt'] = TruthReceiptBuilder().build('truth.build_packet', packet, suff)
        return packet

    def check_sufficiency(self, packet: Dict[str, Any]) -> Dict[str, Any]:
        return TruthSufficiencyChecker().check(packet)

    def detect_incomplete(self, requirement: Dict[str, Any], artifact_matrix: Dict[str, Any] | None = None) -> Dict[str, Any]:
        return IncompleteTruthReasoner().detect(requirement, artifact_matrix, self.snapshot())

    def validate_response(self, packet: Dict[str, Any], response_text: str | None = None) -> Dict[str, Any]:
        return ResponseGroundingValidator().validate(packet, response_text=response_text)

    def validate_execution(self, packet: Dict[str, Any], plan: Dict[str, Any] | None = None) -> Dict[str, Any]:
        return ExecutionGroundingValidator().validate(packet, plan=plan)

    def receipt(self, packet: Dict[str, Any] | None = None, operation: str = 'truth.receipt') -> Dict[str, Any]:
        return TruthReceiptBuilder().build(operation, packet or {}, (packet or {}).get('sufficiency') or {})
