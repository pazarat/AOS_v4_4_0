from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class ConfigError(RuntimeError):
    pass


class AOSPaths:
    """Canonical path contract for AOS.

    AOS is the silent operating environment. Workshop is the general project-
    building truth domain. `workshop/active_project` is only a fixed slot.

    The current user project has exactly one canonical filesystem gate:

        workshop/active_project/PROJECT/

    The name is ASCII-only to avoid ZIP/filesystem encoding corruption. If this
    directory is empty, no current project is loaded. AOS runtime state, reports,
    examples, and workshop standards are never project payload.
    """

    def __init__(self, root: Path):
        self.root = root.resolve()
        self.identity = self.root / 'aos_identity'
        self.workshop = self.root / 'workshop'
        self.workshop_system = self.workshop / '_workshop_system'
        self.active_project = self.workshop / 'active_project'
        self.project_upload = self.active_project / 'PROJECT'
        self.project_gate = self.project_upload
        # Backward-compatible attribute only. It points to the same single gate;
        # AOS no longer creates or scans a second upload path.
        self.legacy_project_upload = self.project_upload
        self.runtime_state = self.root / 'runtime_state'
        self.project_truth = self.runtime_state / 'project_truth'
        self.event_log = self.runtime_state / 'event_log.jsonl'
        self.audit = self.root / 'audit'
        self.reports = self.root / 'reports'
        self.schemas = self.root / 'schemas'

    @property
    def operational_identity(self) -> Path:
        return self.identity / 'OPERATIONAL_IDENTITY.md'

    @property
    def bootstrap_protocol(self) -> Path:
        return self.identity / 'ENGINEER_BOOTSTRAP_PROTOCOL.md'

    @property
    def system_truth(self) -> Path:
        return self.identity / 'system_truth.json'

    def ensure(self) -> None:
        for p in [
            self.identity,
            self.workshop,
            self.workshop_system,
            self.active_project,
            self.project_upload,
            self.runtime_state,
            self.project_truth,
            self.audit,
            self.reports,
            self.schemas,
        ]:
            p.mkdir(parents=True, exist_ok=True)
        self.event_log.touch(exist_ok=True)
        (self.project_upload / '.keep').touch(exist_ok=True)


def load_json(path: Path, default: Any = None) -> Any:
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text(encoding='utf-8'))
    except json.JSONDecodeError as exc:
        raise ConfigError(f'Invalid JSON file: {path}: {exc}') from exc


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
