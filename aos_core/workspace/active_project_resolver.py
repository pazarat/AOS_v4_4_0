from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List

TRUTH_MARKERS = ['00_PROJECT_ENTRYPOINT.md', '01_PROJECT_CONTRACT.yaml', '02_PROJECT_TRUTH_INDEX.yaml']
IGNORED_PROJECT_FILES = {'.keep', '.gitkeep', '.DS_Store'}
CANONICAL_PROJECT_DIR = 'PROJECT'


def _display_project_name(root: Path) -> str:
    contract = root / '01_PROJECT_CONTRACT.yaml'
    if contract.exists():
        try:
            for line in contract.read_text(encoding='utf-8').splitlines():
                stripped = line.strip()
                if stripped.startswith('project_name:'):
                    value = stripped.split(':', 1)[1].strip().strip('\"\'')
                    if value:
                        return value
        except Exception:
            pass
    return root.name


class ActiveProjectResolver:
    """Resolves the real current project from one stable ASCII path.

    `workshop/active_project` is a slot, not a project. The only current-project
    payload path is `workshop/active_project/PROJECT`. If PROJECT is empty, no
    current project is loaded. No samples, aliases, runtime state, or workshop
    material are scanned as the user project.
    """

    def __init__(self, slot: Path, upload_gate: Path | None = None, legacy_gates: List[Path] | None = None):
        self.slot = Path(slot)
        self.upload_gate = Path(upload_gate) if upload_gate is not None else self.slot / CANONICAL_PROJECT_DIR
        self.legacy_gates: List[Path] = []

    def state(self) -> Dict[str, Any]:
        gate = self.upload_gate
        base = {
            'slot': self.slot.as_posix(),
            'project_path': gate.as_posix(),
            'upload_gate': gate.as_posix(),
            'upload_gate_display_name': CANONICAL_PROJECT_DIR,
            'canonical_project_path': (self.slot / CANONICAL_PROJECT_DIR).as_posix(),
            'canonical_upload_gate': (self.slot / CANONICAL_PROJECT_DIR).as_posix(),
            'legacy_upload_gate_aliases': [],
            'legacy_alias_used': False,
            'legacy_alias_candidates': [],
            'slot_is_project': False,
            'project_path_is_only_payload_gate': True,
            'reserved_dirs': [CANONICAL_PROJECT_DIR],
            'local_truth_slot': None,
            'local_truth_exists': False,
        }
        if not self.slot.exists():
            return {**base, 'state': 'slot_missing', 'project_root': None, 'project_name': None, 'candidates': [], 'meaning': 'AOS active-project slot missing'}
        if not gate.exists():
            return {**base, 'state': 'project_path_missing', 'project_root': None, 'project_name': None, 'candidates': [], 'meaning': 'canonical PROJECT path missing'}

        entries = [p for p in gate.iterdir() if p.name not in IGNORED_PROJECT_FILES and not p.name.startswith('.')]
        dirs = [p for p in entries if p.is_dir()]
        files = [p for p in entries if p.is_file()]
        marker_roots = [d for d in dirs if all((d / m).exists() for m in TRUTH_MARKERS)]
        gate_has_markers = all((gate / m).exists() for m in TRUTH_MARKERS)

        if not entries:
            return {**base, 'state': 'no_project_loaded', 'project_root': None, 'project_name': None, 'candidates': [], 'meaning': 'PROJECT is empty; no current project is loaded'}
        if gate_has_markers:
            return {**base, 'state': 'single_project_detected', 'project_root': gate.as_posix(), 'project_name': _display_project_name(gate), 'candidates': [gate.as_posix()], 'meaning': 'project payload root is PROJECT itself'}
        if len(marker_roots) == 1 and not files:
            root = marker_roots[0]
            return {**base, 'state': 'single_project_detected', 'project_root': root.as_posix(), 'project_name': _display_project_name(root), 'candidates': [root.as_posix()], 'meaning': 'one truth-marker project root detected under PROJECT'}
        if len(marker_roots) > 1:
            return {**base, 'state': 'multi_project_ambiguity', 'project_root': None, 'project_name': None, 'candidates': [p.as_posix() for p in marker_roots], 'meaning': 'multiple project roots detected under PROJECT'}
        return {**base, 'state': 'unformed_or_scattered_project', 'project_root': None, 'project_name': None, 'candidates': [p.as_posix() for p in entries], 'meaning': 'PROJECT contains payload but no truth-marker project root is resolved'}
