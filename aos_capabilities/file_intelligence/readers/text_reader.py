from __future__ import annotations
from pathlib import Path
from typing import Any, Dict
from aos_capabilities.file_intelligence.common import safe_read_text

class TextReader:
    def read(self, path: Path, limit: int = 1_000_000) -> Dict[str, Any]:
        text = safe_read_text(path, limit=limit)
        return {'type': 'text', 'text': text, 'chars': len(text), 'lines': text.count('\n') + (1 if text else 0)}
