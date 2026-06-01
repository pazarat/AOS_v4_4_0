from __future__ import annotations
import re
from pathlib import Path
from typing import Any, Dict
from aos_capabilities.file_intelligence.common import safe_read_text

class MarkdownReader:
    def read(self, path: Path, limit: int = 1_000_000) -> Dict[str, Any]:
        text = safe_read_text(path, limit=limit)
        headings = [{'level': len(m.group(1)), 'title': m.group(2).strip()} for m in re.finditer(r'^(#{1,6})\s+(.+)$', text, re.M)]
        links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', text)
        return {'type': 'markdown', 'text': text, 'headings': headings, 'links': links[:100], 'chars': len(text)}
