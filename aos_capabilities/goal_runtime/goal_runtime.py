from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


class GoalRuntime:
    """Trace-only goal lifecycle runtime.

    It is intentionally small: the important governance is that every hard task
    has success criteria, attempts, observations, and a close decision.
    """

    def __init__(self, store_dir: Path):
        self.store_dir = store_dir
        self.store_dir.mkdir(parents=True, exist_ok=True)

    def health(self) -> Dict[str, Any]:
        return {'capability': 'goal_runtime', 'status': 'ready', 'store': self.store_dir.as_posix()}

    def _id(self, text: str) -> str:
        return 'goal_' + hashlib.sha1(text.encode('utf-8')).hexdigest()[:12]

    def _path(self, goal_id: str) -> Path:
        return self.store_dir / f'{goal_id}.json'

    def open(self, target: str, success_criteria: List[str] | None = None, context: Dict[str, Any] | None = None) -> Dict[str, Any]:
        goal_id = self._id(target + json.dumps(context or {}, ensure_ascii=False, sort_keys=True))
        doc = {
            'goal_id': goal_id,
            'target': target,
            'status': 'open',
            'success_criteria': success_criteria or ['success criteria must be specified before closure'],
            'context': context or {},
            'observations': [],
            'attempts': [],
            'decisions': [],
            'created_at': _now(),
            'updated_at': _now(),
        }
        self._path(goal_id).write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding='utf-8')
        return doc

    def load(self, goal_id: str) -> Dict[str, Any]:
        p = self._path(goal_id)
        if not p.exists():
            return {'goal_id': goal_id, 'status': 'missing'}
        return json.loads(p.read_text(encoding='utf-8'))

    def save(self, doc: Dict[str, Any]) -> Dict[str, Any]:
        doc['updated_at'] = _now()
        self._path(doc['goal_id']).write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding='utf-8')
        return doc

    def record_observation(self, goal_id: str, observation: Dict[str, Any]) -> Dict[str, Any]:
        doc = self.load(goal_id)
        if doc.get('status') == 'missing':
            return doc
        doc.setdefault('observations', []).append({'at': _now(), **observation})
        return self.save(doc)

    def record_attempt(self, goal_id: str, attempt: Dict[str, Any]) -> Dict[str, Any]:
        doc = self.load(goal_id)
        if doc.get('status') == 'missing':
            return doc
        doc.setdefault('attempts', []).append({'at': _now(), **attempt})
        return self.save(doc)

    def check_progress(self, goal_id: str) -> Dict[str, Any]:
        doc = self.load(goal_id)
        if doc.get('status') == 'missing':
            return {'goal_id': goal_id, 'decision': 'BLOCKED', 'reasons': ['goal_missing']}
        attempts = doc.get('attempts', [])
        observations = doc.get('observations', [])
        passed = [o for o in observations if o.get('result') in {'passed', 'success'}]
        failed = [o for o in observations if o.get('result') in {'failed', 'regression', 'still_failing'}]
        reasons = []
        decision = 'CONTINUE'
        if len(attempts) >= 3 and not passed:
            decision = 'REVIEW_ROOT_CAUSE'
            reasons.append('three_or_more_attempts_without_success_evidence')
        if passed and not failed[-1:]:
            decision = 'READY_TO_CLOSE'
            reasons.append('success_evidence_present')
        if not doc.get('success_criteria'):
            decision = 'BLOCKED'
            reasons.append('missing_success_criteria')
        result = {'goal_id': goal_id, 'decision': decision, 'reasons': reasons, 'attempt_count': len(attempts), 'observation_count': len(observations)}
        doc.setdefault('decisions', []).append({'at': _now(), **result})
        self.save(doc)
        return result

    def close(self, goal_id: str, evidence: Dict[str, Any] | None = None) -> Dict[str, Any]:
        progress = self.check_progress(goal_id)
        doc = self.load(goal_id)
        if progress['decision'] != 'READY_TO_CLOSE':
            return {'goal_id': goal_id, 'closed': False, 'reason': 'not_ready_to_close', 'progress': progress}
        doc['status'] = 'closed'
        doc['closed_at'] = _now()
        doc['closure_evidence'] = evidence or {}
        self.save(doc)
        return {'goal_id': goal_id, 'closed': True, 'progress': progress}
