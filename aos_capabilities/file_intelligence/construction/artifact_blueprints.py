from __future__ import annotations

from pathlib import Path
from typing import Any, Dict


class ArtifactBlueprints:
    """Universal construction blueprints; language-specific rules live elsewhere."""

    def blueprint_for(self, path: str, role: str | None = None) -> Dict[str, Any]:
        ext = Path(path or '').suffix.lower()
        if ext in {'.md', '.txt'}:
            kind = 'document'
            required_sections = ['purpose', 'scope', 'owner', 'rules_or_content', 'verification']
        elif ext in {'.yaml', '.yml', '.json', '.toml'}:
            kind = 'machine_contract'
            required_sections = ['id_or_name', 'version_or_schema', 'purpose', 'fields', 'validation']
        elif ext in {'.py', '.ts', '.js', '.cs', '.java', '.go', '.rs'}:
            kind = 'source_code'
            required_sections = ['public_contract', 'dependencies', 'error_handling', 'tests_or_verification']
        elif ext in {'.sql'}:
            kind = 'database_script'
            required_sections = ['purpose', 'safety', 'rollback_or_migration_policy', 'verification']
        else:
            kind = 'artifact'
            required_sections = ['purpose', 'owner', 'verification']
        return {
            'kind': kind,
            'required_construction_dimensions': required_sections,
            'universal_rules': [
                'declare owner or infer from parent artifact',
                'avoid duplicate concept ownership',
                'preserve source-of-truth hierarchy',
                'provide verification path',
            ],
        }
