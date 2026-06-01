from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List

from aos_core.config import AOSPaths


class MaintenanceEngine:
    """Audits AOS against its own target mission, not against one project."""

    def __init__(self, paths: AOSPaths):
        self.paths = paths

    def audit(self) -> Dict[str, Any]:
        checks = {
            'identity_outside_workshop': self.paths.operational_identity.exists() and not (self.paths.workshop / 'OPERATIONAL_IDENTITY.md').exists(),
            'workshop_manifest_exists': (self.paths.workshop_system / '00_WORKSHOP_MANIFEST.md').exists(),
            'active_project_slot_exists': self.paths.active_project.exists(),
            'single_project_path_exists': self.paths.project_upload.exists(),
                        'system_truth_in_identity': self.paths.system_truth.exists(),
            'root_agents_entrypoint_exists': (self.paths.root / 'AGENTS.md').exists(),
            'silent_response_contract_exists': (self.paths.identity / 'SILENT_RESPONSE_CONTRACT.md').exists(),
            'external_model_binding_contract_exists': (self.paths.identity / 'EXTERNAL_MODEL_BINDING_CONTRACT.md').exists(),
            'no_sample_payloads_in_stable_base': not (self.paths.root / 'workshop' / 'examples').exists() and not (self.paths.active_project / 'sample_payload').exists() and not (self.paths.project_upload / 'sample_payload').exists(),
            'strategy_engine_exists': (self.paths.root / 'aos_core' / 'strategy' / 'strategy_engine.py').exists(),
            'planning_solution_exists': (self.paths.root / 'aos_core' / 'planning_solution' / 'planning_solution_engine.py').exists(),
            'runtime_enforcement_exists': (self.paths.root / 'aos_core' / 'runtime_enforcement' / 'runtime_enforcement_engine.py').exists(),
            'solution_delivery_exists': (self.paths.root / 'aos_core' / 'solution_delivery' / 'solution_delivery_engine.py').exists(),
        }
        return {'checks': checks, 'passed': all(checks.values()), 'problems': [k for k, v in checks.items() if not v]}
