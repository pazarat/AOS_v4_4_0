from __future__ import annotations
from pathlib import Path
from typing import Any, Dict

class CapabilityRegistry:
    """Discovers capability manifests without promoting them to core layers."""
    def __init__(self, root: Path):
        self.root = Path(root)

    def discover(self) -> Dict[str, Any]:
        items=[]
        for p in (self.root / 'aos_capabilities').rglob('CAPABILITY_MANIFEST.yaml') if (self.root / 'aos_capabilities').exists() else []:
            items.append({'path': p.relative_to(self.root).as_posix(), 'capability': p.parent.name})
        return {'capability_count': len(items), 'capabilities': sorted(items, key=lambda x: x['path'])}
