from __future__ import annotations

from typing import Any, Dict, List


class TruthStoryPacketBuilder:
    """Builds a concise narrative of why evidence means what it means."""

    def build(self, requirement: Dict[str, Any], matrix: Dict[str, Any], semantics: Dict[str, Any], incomplete: Dict[str, Any]) -> Dict[str, Any]:
        summary = matrix.get('summary') or {}
        project_condition = matrix.get('project_condition')
        story: List[Dict[str, Any]] = []

        if project_condition:
            story.append({
                'claim': f'Artifact surface condition is {project_condition}',
                'grade': 'verified',
                'meaning': 'The current answer/execution must respect this project condition; it is not permission to execute blindly.',
            })
        if semantics.get('empty_declared_target_count'):
            story.append({
                'claim': 'Empty governed artifacts exist as declared construction targets.',
                'grade': 'verified',
                'meaning': 'They are planned truth targets to mature. They are not completed truth and must not be filled by guessing.',
                'count': semantics.get('empty_declared_target_count'),
            })
        if semantics.get('declared_missing_artifact_count'):
            story.append({
                'claim': 'Some artifacts declare child/related files that are missing.',
                'grade': 'verified',
                'meaning': 'A missing declared artifact is a broken truth promise and should be repaired or explicitly deferred.',
                'count': semantics.get('declared_missing_artifact_count'),
            })
        if incomplete.get('maturity_issue_count'):
            story.append({
                'claim': 'Incomplete truth exists and requires maturity before production-oriented execution.',
                'grade': 'verified',
                'meaning': 'The agent may diagnose and plan, but must not invent final logic from incomplete truth.',
                'count': incomplete.get('maturity_issue_count'),
            })
        if summary.get('diagnostic_issue_count'):
            story.append({
                'claim': 'Diagnostics found issues that shape the safe response posture.',
                'grade': 'derived',
                'meaning': 'The answer should name the type of weakness, not merely say the project is weak.',
                'count': summary.get('diagnostic_issue_count'),
            })
        return {
            'type': 'truth_story_packet',
            'requirement_depth': requirement.get('truth_depth'),
            'depth_label': requirement.get('depth_label'),
            'story': story,
            'response_law': 'answer_from_truth_story_not_isolated_file_or_largest_document',
        }
