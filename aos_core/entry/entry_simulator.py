from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List


class EntrySimulator:
    """Simulates a fresh model's first-contact behavior against the repository.

    This does not pretend to run an LLM. It audits whether likely first-opened
    files redirect the model toward operating identity instead of code/file
    intelligence tunnels.
    """

    FIRST_ENTRY = '00_START_HERE_FOR_ANY_MODEL.md'
    LEGACY_ENTRY = '00_READ_FIRST_OPERATING_ENTRY.md'
    REQUIRED_IDENTITY_FILES = [
        'AGENTS.md',
        'aos_identity/START_WORK_OPERATING_MESSAGE.md',
        'aos_identity/OPERATIONAL_IDENTITY.md',
        'aos_identity/OPERATING_LAYER_MAP.md',
        'aos_identity/SYSTEM_CONSTITUTION.md',
    ]
    LIKELY_FIRST_FILES = [
        FIRST_ENTRY,
        'aos.py',
        'README.md',
        'AGENTS.md',
        LEGACY_ENTRY,
    ]

    def __init__(self, root: Path):
        self.root = root

    def run(self, request_text: str = '') -> Dict[str, Any]:
        issues: List[Dict[str, Any]] = []
        files = {p.relative_to(self.root).as_posix(): p for p in self.root.rglob('*') if p.is_file()}

        if self.FIRST_ENTRY not in files:
            issues.append({'severity': 'block', 'code': 'entry.first_file_missing', 'message': f'{self.FIRST_ENTRY} is missing.'})
        if self.LEGACY_ENTRY not in files:
            issues.append({'severity': 'warn', 'code': 'entry.legacy_first_file_missing', 'message': f'{self.LEGACY_ENTRY} is missing.'})

        for f in self.REQUIRED_IDENTITY_FILES:
            if f not in files:
                issues.append({'severity': 'block', 'code': 'entry.identity_file_missing', 'path': f})

        for f in self.LIKELY_FIRST_FILES:
            p = files.get(f)
            if not p:
                continue
            text = p.read_text(encoding='utf-8', errors='ignore')[:5000]
            if f == 'aos.py' and self.FIRST_ENTRY not in text:
                issues.append({'severity': 'block', 'code': 'entry.aos_py_does_not_redirect', 'path': f})
            if f in {'README.md', 'AGENTS.md'} and self.FIRST_ENTRY not in text:
                issues.append({'severity': 'warn', 'code': 'entry.root_doc_does_not_reference_first_entry', 'path': f})

        # Detect dangerous guidance that suggests file intelligence is first awareness.
        dangerous_phrases = [
            'start with file intelligence',
            'begin with file intelligence',
            'file intelligence is first awareness',
            'ابدأ بطبقة معالجة الملفات',
        ]
        for f in ['AGENTS.md', 'README.md', self.FIRST_ENTRY, self.LEGACY_ENTRY]:
            p = files.get(f)
            if not p:
                continue
            text = p.read_text(encoding='utf-8', errors='ignore').lower()
            for phrase in dangerous_phrases:
                if phrase.lower() in text:
                    issues.append({'severity': 'block', 'code': 'entry.dangerous_first_awareness_phrase', 'path': f, 'phrase': phrase})

        # Release hygiene: generated diagnostic reports must not train a fresh model to start from reports.
        report_payloads = [n for n in files if n.startswith('reports/') and not n.endswith('.keep')]
        if report_payloads:
            issues.append({'severity': 'warn', 'code': 'entry.generated_reports_present', 'count': len(report_payloads), 'examples': report_payloads[:5], 'meaning': 'clean before release; allowed after runtime use'})
        runtime_logs = [n for n in files if n in {'runtime_state/event_log.jsonl', 'audit/audit.jsonl'} and files[n].stat().st_size > 0]
        if runtime_logs:
            issues.append({'severity': 'warn', 'code': 'entry.runtime_logs_bundled', 'examples': runtime_logs})

        # Root CLI shim must be small enough not to become a code rabbit hole.
        aos_py = files.get('aos.py')
        if aos_py and aos_py.stat().st_size > 1800:
            issues.append({'severity': 'block', 'code': 'entry.aos_py_too_large', 'path': 'aos.py', 'size_bytes': aos_py.stat().st_size})

        sequence = [
            '00_START_HERE_FOR_ANY_MODEL.md',
            '00_READ_FIRST_OPERATING_ENTRY.md',
            'AGENTS.md',
            'aos_identity/START_WORK_OPERATING_MESSAGE.md',
            'aos_identity/OPERATIONAL_IDENTITY.md',
            'intent_frame',
            'intent_cognition_packet',
            'surface_resolution',
            'truth_requirement',
            'artifact_cockpit_when_needed',
            'goal_runtime_when_justified',
            'truth_sufficiency',
            'response_delivery',
        ]
        return {
            'operation': 'entry.simulate_fresh_model',
            'request_text_present': bool((request_text or '').strip()),
            'expected_sequence': sequence,
            'passed': not any(i['severity'] == 'block' for i in issues),
            'issues': issues,
            'meaning': 'Fresh model entry must be identity-first. Artifact/file inspection is not first awareness unless the user explicitly asks for diagnostics.',
        }
