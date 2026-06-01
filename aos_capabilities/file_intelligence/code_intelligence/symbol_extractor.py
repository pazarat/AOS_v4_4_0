from __future__ import annotations
import ast, re
from pathlib import Path
from typing import Any, Dict, List

class SymbolExtractor:
    def extract(self, path: Path, text: str, language: str) -> Dict[str, Any]:
        if language == 'python':
            return self.extract_python(path, text)
        return self.extract_regex(path, text, language)

    def extract_python(self, path: Path, text: str) -> Dict[str, Any]:
        symbols: List[Dict[str, Any]] = []
        imports: List[Dict[str, Any]] = []
        calls: List[Dict[str, Any]] = []
        issues: List[str] = []
        try:
            tree = ast.parse(text or '')
            for node in ast.walk(tree):
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    symbols.append({'kind': 'function', 'name': node.name, 'line': node.lineno})
                elif isinstance(node, ast.ClassDef):
                    symbols.append({'kind': 'class', 'name': node.name, 'line': node.lineno})
                elif isinstance(node, ast.Import):
                    for alias in node.names:
                        imports.append({'module': alias.name, 'line': node.lineno, 'kind': 'import'})
                elif isinstance(node, ast.ImportFrom):
                    imports.append({'module': node.module or '', 'line': node.lineno, 'kind': 'from_import'})
                elif isinstance(node, ast.Call):
                    name = self.call_name(node.func)
                    if name:
                        calls.append({'name': name, 'line': getattr(node, 'lineno', None)})
        except SyntaxError as exc:
            issues.append(f'python_syntax_error:{exc.lineno}:{exc.msg}')
        except Exception as exc:
            issues.append(f'python_ast_error:{type(exc).__name__}:{exc}')
        return {'symbols': symbols, 'imports': imports, 'calls': calls[:500], 'issues': issues}

    def call_name(self, node: ast.AST) -> str | None:
        if isinstance(node, ast.Name):
            return node.id
        if isinstance(node, ast.Attribute):
            root = self.call_name(node.value)
            return f'{root}.{node.attr}' if root else node.attr
        return None

    def extract_regex(self, path: Path, text: str, language: str) -> Dict[str, Any]:
        symbols: List[Dict[str, Any]] = []
        imports: List[Dict[str, Any]] = []
        patterns = [
            ('class', r'\bclass\s+([A-Za-z_][A-Za-z0-9_]*)'),
            ('function', r'\bfunction\s+([A-Za-z_][A-Za-z0-9_]*)\s*\('),
            ('function', r'\b(?:def|fn)\s+([A-Za-z_][A-Za-z0-9_]*)\s*\('),
            ('interface', r'\binterface\s+([A-Za-z_][A-Za-z0-9_]*)'),
            ('method', r'\b(?:public|private|protected|static|async|export|internal|virtual|override|sealed|partial|final|suspend|fun)\s+[\w<>\[\],\s]+\s+([A-Za-z_][A-Za-z0-9_]*)\s*\('),
            ('const', r'\b(?:const|let|var)\s+([A-Za-z_][A-Za-z0-9_]*)\s*=')
        ]
        lines = text.splitlines()
        for kind, pat in patterns:
            for m in re.finditer(pat, text):
                line = text[:m.start()].count('\n') + 1
                symbols.append({'kind': kind, 'name': m.group(1), 'line': line})
        for i, line in enumerate(lines, start=1):
            m = re.search(r'^\s*(?:import\s+(?:.+?\s+from\s+)?["\']([^"\']+)["\']|using\s+([A-Za-z0-9_.]+)\s*;|require\(["\']([^"\']+)["\']\))', line)
            if m:
                imports.append({'module': next(g for g in m.groups() if g), 'line': i, 'kind': 'import'})
        return {'symbols': symbols[:500], 'imports': imports[:500], 'calls': [], 'issues': []}
