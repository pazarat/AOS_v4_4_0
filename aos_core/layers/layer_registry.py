from __future__ import annotations
from pathlib import Path
from typing import Any, Dict, List

class LayerRegistry:
    """Discovers core layer contracts only. Capabilities use CAPABILITY_MANIFEST and are not promoted to core."""
    def __init__(self, root: Path):
        self.root = Path(root)

    def discover(self) -> Dict[str, Any]:
        cores=[]
        for p in self.root.rglob('LAYER_CORE.yaml'):
            if 'aos_capabilities' in p.parts:
                continue
            cores.append({'path': p.relative_to(self.root).as_posix(), 'layer': p.parent.name})
        return {'layer_core_count': len(cores), 'layer_cores': sorted(cores, key=lambda x: x['path'])}
