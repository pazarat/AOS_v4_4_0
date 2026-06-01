from __future__ import annotations

import hashlib
from typing import Any, Dict

from aos_core.config import AOSPaths, load_json, write_json


class OperationalIdentitySync:
    """Keeps operational identity synchronized with machine-readable awareness."""

    def __init__(self, paths: AOSPaths):
        self.paths = paths
        self.identity_path = paths.operational_identity
        self.system_truth_path = paths.system_truth
        self.sync_path = paths.identity / '_aos_identity_sync.json'
        self.awareness_packet_path = paths.reports / 'operational_awareness_packet.json'

    def digest(self) -> str:
        identity = self.identity_path.read_text(encoding='utf-8') if self.identity_path.exists() else ''
        system_truth = self.system_truth_path.read_text(encoding='utf-8') if self.system_truth_path.exists() else ''
        workshop_manifest = (self.paths.workshop_system / '00_WORKSHOP_MANIFEST.md').read_text(encoding='utf-8') if (self.paths.workshop_system / '00_WORKSHOP_MANIFEST.md').exists() else ''
        agents_entry = (self.paths.root / 'AGENTS.md').read_text(encoding='utf-8') if (self.paths.root / 'AGENTS.md').exists() else ''
        silent_contract = (self.paths.identity / 'SILENT_RESPONSE_CONTRACT.md').read_text(encoding='utf-8') if (self.paths.identity / 'SILENT_RESPONSE_CONTRACT.md').exists() else ''
        payload = '\n---AGENTS---\n'.join([agents_entry, identity, system_truth, workshop_manifest, silent_contract])
        return hashlib.sha256(payload.encode('utf-8')).hexdigest()

    def sync(self) -> Dict[str, Any]:
        system_truth = load_json(self.system_truth_path, {})
        digest = self.digest()
        previous = load_json(self.sync_path, {}) or {}
        status = 'created' if not previous else ('unchanged' if previous.get('identity_digest') == digest else 'updated')
        sync_doc = {
            'system_id': 'aos',
            'system_version': system_truth.get('version'),
            'root_entrypoint': 'AGENTS.md',
            'identity_file': 'aos_identity/OPERATIONAL_IDENTITY.md',
            'silent_response_contract': 'aos_identity/SILENT_RESPONSE_CONTRACT.md',
            'system_truth_file': 'aos_identity/system_truth.json',
            'workshop_manifest': 'workshop/_workshop_system/00_WORKSHOP_MANIFEST.md',
            'identity_digest': digest,
            'status': status,
            'awareness_packet': 'reports/operational_awareness_packet.json',
            'meaning': 'Any model entering AOS must load identity, constitution, workshop role, and active-project boundaries before high-impact work.',
        }
        write_json(self.sync_path, sync_doc)
        packet = {
            'system': system_truth.get('name'),
            'version': system_truth.get('version'),
            'mission': system_truth.get('mission'),
            'must_understand': [
                'AGENTS.md is the first external model entrypoint.',
                'AOS runtime is not the project.',
                'Workshop is the general truth and standards domain, not a project.',
                'active_project is a fixed project slot and may be empty.',
                'The only current-project path is workshop/active_project/PROJECT.',
                'Empty PROJECT means no current project is loaded.',
                'AOS must discover project structure rather than impose parent/child or PRD trees.',
                'Workshop standards become executable only after local specialization and acceptance.',
                'Contradictory files are conflict candidates, not blind truth.',
                'Assumptions must not become facts without provenance.',
                'AOS may improve itself but cannot bypass its own governance.',
                'Identity questions in project context bind to the project engineer role, not generic model identity.',
            ],
            'surfaces': system_truth.get('surfaces', {}),
            'mandatory_flow': system_truth.get('mandatory_flow', []),
            'non_negotiables': system_truth.get('non_negotiables', []),
            'project_path': system_truth.get('project_path'),
            'silent_by_default': system_truth.get('silent_by_default', True),
            'identity_digest': digest,
        }
        write_json(self.awareness_packet_path, packet)
        return sync_doc
