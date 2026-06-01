from __future__ import annotations
import re
from pathlib import Path
from typing import Any, Dict
from aos_capabilities.file_intelligence.common import safe_read_text

class SqlReader:
    def read(self, path: Path, limit: int = 1_000_000) -> Dict[str, Any]:
        text = safe_read_text(path, limit=limit)
        tables = re.findall(r'CREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?["`\[]?([A-Za-z_][\w\.]*)(?:["`\]]?)', text, re.I)
        alters = re.findall(r'ALTER\s+TABLE\s+["`\[]?([A-Za-z_][\w\.]*)(?:["`\]]?)', text, re.I)
        return {'type': 'sql', 'text': text, 'tables': sorted(set(tables)), 'alters': sorted(set(alters))}
