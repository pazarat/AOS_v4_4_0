from __future__ import annotations
from typing import Any, Dict

class ASTBridge:
    """Bundled AST bridge. Native Python AST is implemented; tree-sitter is an extension adapter."""
    def readiness(self) -> Dict[str, Any]:
        return {'python_ast': True, 'regex_fallback': True, 'tree_sitter_adapter': 'extension_point'}
