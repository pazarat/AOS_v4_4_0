#!/usr/bin/env python3
"""AOS root CLI shim, not the model reasoning entrypoint.

For any model or human opening this repository first:
1. Read `00_START_HERE_FOR_ANY_MODEL.md`.
2. For normal questions, run: `python aos.py answer "<question>"`.
3. Do not inspect `aos_capabilities/file_intelligence` or reports first unless the user explicitly requested diagnostics.

This file intentionally stays tiny so code is not mistaken for first awareness. The real runtime owner is operations_runtime/.
"""
from __future__ import annotations

if __name__ == '__main__':
    from aos_core.cli import main
    raise SystemExit(main())
