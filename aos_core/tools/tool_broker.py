from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List


class ToolRegistrationError(RuntimeError):
    pass


class ToolBroker:
    """Manifest-based tool registry.

    Tools are extensions. Adding a tool must not require changing the kernel.
    """

    REQUIRED = {'id', 'name', 'version', 'risk_level', 'input_schema', 'output_schema', 'side_effects'}

    def __init__(self, registry_dir: Path):
        self.registry_dir = registry_dir
        self.registry_dir.mkdir(parents=True, exist_ok=True)

    def list_manifests(self) -> List[Dict[str, Any]]:
        tools: List[Dict[str, Any]] = []
        for path in sorted(self.registry_dir.glob('*/manifest.json')):
            data = json.loads(path.read_text(encoding='utf-8'))
            self.validate_manifest(data)
            tools.append(data)
        return tools

    def validate_manifest(self, manifest: Dict[str, Any]) -> None:
        missing = self.REQUIRED - set(manifest)
        if missing:
            raise ToolRegistrationError(f'Tool manifest missing fields: {sorted(missing)}')
        if manifest['risk_level'] not in {'read_only', 'write_project', 'execute_code', 'network', 'destructive'}:
            raise ToolRegistrationError(f'Invalid risk level: {manifest["risk_level"]}')
