from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Any, Dict


class TraceStore:
    """Append-only operation trace store.

    Trace is for audit/debugging. It is not visible project truth and must not be
    used as a user-facing answer source.
    """

    def __init__(self, root: Path):
        self.path = root / 'runtime_state' / 'operations_runtime_trace.jsonl'
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def event(self, operation_id: str, node: str, status: str, **data: Any) -> Dict[str, Any]:
        payload = {
            'ts': time.time(),
            'operation_id': operation_id,
            'node': node,
            'status': status,
            'data': data,
        }
        with self.path.open('a', encoding='utf-8') as f:
            f.write(json.dumps(payload, ensure_ascii=False) + '\n')
        return payload
