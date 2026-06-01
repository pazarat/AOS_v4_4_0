from __future__ import annotations
import json
from pathlib import Path
from typing import Any, Dict
from aos_capabilities.file_intelligence.common import safe_read_text

class JsonReader:
    def read(self, path: Path, limit: int = 1_000_000) -> Dict[str, Any]:
        text = safe_read_text(path, limit=limit)
        try:
            data = json.loads(text) if text.strip() else None
            keys = list(data.keys())[:50] if isinstance(data, dict) else []
            return {'type': 'json', 'text': text, 'valid': True, 'top_keys': keys, 'data_type': type(data).__name__}
        except Exception as exc:
            return {'type': 'json', 'text': text, 'valid': False, 'error': str(exc)}
