from __future__ import annotations

from pathlib import Path
from typing import Optional
import shutil


class SandboxWorkspace:
    """Ephemeral workspace copy.

    This implementation is filesystem-only and safe for local tests. Docker/K8s
    can be added later as a provider behind this interface.
    """

    def __init__(self, sandbox_root: Path):
        self.sandbox_root = sandbox_root
        self.sandbox_root.mkdir(parents=True, exist_ok=True)

    def create_copy(self, source: Path, name: str = 'active_project_copy') -> Path:
        target = self.sandbox_root / name
        if target.exists():
            shutil.rmtree(target)
        ignore = shutil.ignore_patterns('_aos_runtime_project_state')
        shutil.copytree(source, target, ignore=ignore)
        return target
