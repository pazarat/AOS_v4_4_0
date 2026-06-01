from __future__ import annotations

from typing import Any, Dict, List

from .artifact_blueprints import ArtifactBlueprints


class GenerationGuidance:
    """Produces compact instructions for the agent before drafting content/code."""

    def build(self, targets: List[str], owner_resolution: Dict[str, Any] | None = None) -> Dict[str, Any]:
        blueprints = {p: ArtifactBlueprints().blueprint_for(p) for p in targets}
        return {
            'targets': targets,
            'blueprints': blueprints,
            'owner_resolution': owner_resolution or {},
            'agent_instruction': [
                'Do not write until preflight decision is ALLOW or WARN.',
                'If decision is MATURE, propose owner-truth repair before production write.',
                'If decision is BLOCK, stop and report blockers with evidence.',
                'After writing, run verify_after_write and record a receipt.',
            ],
        }
