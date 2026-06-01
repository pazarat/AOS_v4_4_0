from __future__ import annotations

from aos_core.config import AOSPaths
from aos_capabilities.truth_runtime.truth_runtime import TruthRuntime


def create(paths: AOSPaths) -> TruthRuntime:
    return TruthRuntime(paths)
