from __future__ import annotations

from dataclasses import asdict
from pathlib import Path
from typing import Any, Dict

from aos_core.contracts import IntentFrame


class EntryGate:
    """First-touch gate for normal AOS work.

    This gate deliberately does not inspect files. It loads operating identity
    facts and builds a bootstrap packet so the kernel can resolve intent/surface
    before invoking the artifact cockpit. Direct artifact entry is reserved for
    explicit diagnostic commands such as inspect/doctor.
    """

    DIRECT_ARTIFACT_COMMANDS = {'inspect', 'doctor', 'file.diagnose', 'file.inspect', 'file.doctor'}

    def __init__(self, paths: Any):
        self.paths = paths

    def bootstrap(self, request_text: str, command: str = 'answer') -> Dict[str, Any]:
        identity_loaded = self.paths.operational_identity.exists()
        system_truth_exists = self.paths.system_truth.exists()
        return {
            'mode': 'entry_bootstrap',
            'command': command,
            'request_text_present': bool((request_text or '').strip()),
            'identity_loaded': identity_loaded,
            'system_truth_exists': system_truth_exists,
            'normal_answer_sequence': [
                'operating_identity',
                'intent_frame',
                'surface_resolution',
                'truth_requirement',
                'artifact_cockpit',
                'truth_sufficiency',
                'response_delivery',
            ],
            'direct_artifact_entry_allowed': command in self.DIRECT_ARTIFACT_COMMANDS,
            'law': 'identity_intent_surface_truth_before_artifact_cockpit',
        }

    def pre_intent_context(self, request_text: str, command: str = 'answer') -> Dict[str, Any]:
        boot = self.bootstrap(request_text, command)
        return {
            'entry_bootstrap': boot,
            'artifact_scan_allowed_now': boot['direct_artifact_entry_allowed'],
            'artifact_scan_reason': 'explicit_artifact_diagnostic_command' if boot['direct_artifact_entry_allowed'] else 'normal_answer_must_resolve_identity_intent_surface_truth_first',
        }

    def after_intent(self, frame: IntentFrame, truth_requirement: Dict[str, Any] | None = None) -> Dict[str, Any]:
        return {
            'mode': 'entry_sequence_state',
            'identity_loaded': self.paths.operational_identity.exists(),
            'intent_resolved': True,
            'surface_resolved': bool(frame.surface),
            'truth_requirement_resolved': bool(truth_requirement),
            'artifact_cockpit_allowed': True,
            'visible_surface': frame.surface,
            'response_mode': frame.response_mode,
            'frame': asdict(frame),
        }

    def validate_sequence(self, packet: Dict[str, Any]) -> Dict[str, Any]:
        entry = packet.get('entry_runtime') or {}
        intent = packet.get('intent') or {}
        truth = packet.get('truth') or {}
        file_matrix = packet.get('file_matrix') or {}
        violations = []
        if not (entry.get('bootstrap') or {}).get('identity_loaded'):
            violations.append('identity_not_loaded')
        if not intent.get('surface'):
            violations.append('surface_not_resolved')
        if not (truth.get('requirement') or (truth.get('packet') or {}).get('requirement')):
            violations.append('truth_requirement_missing')
        if file_matrix.get('packet_mode') != 'hot_compact_matrix':
            violations.append('normal_answer_not_using_hot_matrix')
        return {
            'passed': not violations,
            'violations': violations,
            'rule': 'normal_answer_must_enter_identity_intent_surface_truth_then_artifact_cockpit',
        }
