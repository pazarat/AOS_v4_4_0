from __future__ import annotations
import hashlib
from pathlib import Path
from typing import Any, Dict

class ContentFingerprinter:
    def fingerprint_file(self, path: Path) -> Dict[str, Any]:
        try:
            data = path.read_bytes()
        except Exception:
            data = b''
        return {
            'sha256': hashlib.sha256(data).hexdigest(),
            'sha1': hashlib.sha1(data).hexdigest(),
            'size_bytes': len(data),
        }
