from __future__ import annotations
import re
from pathlib import Path
from typing import Any, Dict
from aos_capabilities.file_intelligence.common import safe_read_text

class YamlReader:
    def read(self, path: Path, limit: int = 1_000_000) -> Dict[str, Any]:
        text = safe_read_text(path, limit=limit)
        keys = []
        for m in re.finditer(r'^\s*([A-Za-z_][A-Za-z0-9_\-]*)\s*:', text, re.M):
            if m.group(1) not in keys:
                keys.append(m.group(1))
        return {'type': 'yaml', 'text': text, 'top_keys': keys[:100], 'valid': bool(text.strip())}
