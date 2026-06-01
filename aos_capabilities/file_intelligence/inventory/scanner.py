from __future__ import annotations
from pathlib import Path
from typing import Any, Dict, List
from aos_capabilities.file_intelligence.common import IGNORE_DIRS, TEXT_EXTS, CODE_EXTS, LANG_BY_EXT, AOS_DEFAULT_DIRS, rel, is_binary_sample, path_role

class InventoryScanner:
    """Project-neutral filesystem scanner.

    It separates AOS default surfaces from the actual project payload and never
    treats generated indexes as final truth.
    """
    def __init__(self, root: Path):
        self.root = Path(root).resolve()

    def iter_files(self) -> List[Path]:
        if not self.root.exists():
            return []
        files: List[Path] = []
        for path in self.root.rglob('*'):
            if any(part in IGNORE_DIRS for part in path.parts):
                continue
            if path.is_file():
                if path.name == '.keep':
                    continue
                files.append(path)
        return sorted(files, key=lambda p: p.as_posix())

    def scan(self) -> List[Dict[str, Any]]:
        records: List[Dict[str, Any]] = []
        for path in self.iter_files():
            r = rel(path, self.root)
            ext = path.suffix.lower()
            try:
                size = path.stat().st_size
                sample = path.read_bytes()[:4096]
            except Exception:
                size = 0
                sample = b''
            parts = Path(r).parts
            first = parts[0] if parts else ''
            if len(parts) >= 3 and parts[0] == 'workshop' and parts[1] == 'active_project' and parts[2] == 'PROJECT':
                surface = 'active_project_payload'
            elif first in AOS_DEFAULT_DIRS:
                surface = 'aos_default_surface'
            else:
                surface = 'project_payload'
            binary = is_binary_sample(sample)
            records.append({
                'path': r,
                'name': path.name,
                'extension': ext,
                'language': LANG_BY_EXT.get(ext, 'unknown'),
                'size_bytes': size,
                'is_text': (ext in TEXT_EXTS) and not binary,
                'is_code': (ext in CODE_EXTS) and not binary,
                'is_binary': binary,
                'surface': surface,
                'role': path_role(r),
            })
        return records
