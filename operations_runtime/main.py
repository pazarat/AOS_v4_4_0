from __future__ import annotations

from pathlib import Path
from operations_runtime.runtime_kernel import OperationsRuntimeKernel


class OperationsKernel(OperationsRuntimeKernel):
    """Backward-compatible name used by the CLI."""


def create(root: str | Path = '.') -> OperationsRuntimeKernel:
    return OperationsRuntimeKernel(Path(root))
