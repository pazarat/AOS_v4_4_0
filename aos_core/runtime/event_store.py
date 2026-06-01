from __future__ import annotations

from pathlib import Path
from typing import Iterable, List
import json

from aos_core.contracts import Event


class EventStore:
    def __init__(self, path: Path):
        self.path = path
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.touch(exist_ok=True)

    def append(self, event: Event) -> Event:
        with self.path.open('a', encoding='utf-8') as f:
            f.write(event.to_json() + '\n')
        return event

    def read_all(self) -> List[dict]:
        events: List[dict] = []
        for line in self.path.read_text(encoding='utf-8').splitlines():
            if line.strip():
                events.append(json.loads(line))
        return events

    def count(self) -> int:
        return len(self.read_all())
