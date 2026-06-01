from __future__ import annotations
from typing import Any, Dict

class LSPBridge:
    """Stable extension seam for future language-server integrations."""
    def readiness(self) -> Dict[str, Any]:
        return {'lsp_bridge': 'extension_point', 'bundled_dependency': False}
