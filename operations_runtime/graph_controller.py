from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, List, Any
import time

from operations_runtime.operation_envelope import OperationEnvelope
from operations_runtime.trace_store import TraceStore


@dataclass(frozen=True)
class GraphNode:
    name: str
    fn: Callable[[OperationEnvelope], OperationEnvelope]


class RuntimeGraphController:
    """Deterministic operating graph.

    The model is not the router. Runtime graph owns order, trace, retry points,
    and exit conditions. Individual nodes may use model intelligence in the
    future, but not as uncontrolled folder traversal.
    """

    def __init__(self, trace: TraceStore):
        self.trace = trace

    def run(self, envelope: OperationEnvelope, nodes: List[GraphNode]) -> OperationEnvelope:
        for node in nodes:
            started = time.perf_counter()
            self.trace.event(envelope.operation_id, node.name, 'started')
            try:
                envelope = node.fn(envelope)
                elapsed = round((time.perf_counter() - started) * 1000, 3)
                event = self.trace.event(envelope.operation_id, node.name, 'completed', elapsed_ms=elapsed)
                envelope.trace.append(event)
            except Exception as exc:  # keep failure deterministic and inspectable
                elapsed = round((time.perf_counter() - started) * 1000, 3)
                event = self.trace.event(envelope.operation_id, node.name, 'failed', elapsed_ms=elapsed, error=str(exc))
                envelope.trace.append(event)
                raise
        return envelope
