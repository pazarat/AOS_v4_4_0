from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict

from aos_core.contracts import utc_now


class AuditLog:
    def __init__(self, path: Path):
        self.path = path
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.touch(exist_ok=True)

    def write(self, record_type: str, data: Dict[str, Any]) -> None:
        rec = {'timestamp': utc_now(), 'type': record_type, 'data': data}
        with self.path.open('a', encoding='utf-8') as f:
            f.write(json.dumps(rec, ensure_ascii=False) + '\n')
