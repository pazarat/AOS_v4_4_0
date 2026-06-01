from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Any, Callable, Dict
import time


class MatrixInvocationEngine:
    """Small fan-out/fan-in executor for independent layer requests."""

    def invoke(self, calls: Dict[str, Callable[[], Any]], *, max_workers: int = 4) -> Dict[str, Any]:
        started = time.perf_counter()
        results: Dict[str, Any] = {}
        errors: Dict[str, str] = {}
        if not calls:
            return {'mode': 'no_calls', 'results': results, 'errors': errors, 'elapsed_ms': 0}
        with ThreadPoolExecutor(max_workers=min(max_workers, max(1, len(calls)))) as pool:
            future_map = {pool.submit(fn): name for name, fn in calls.items()}
            for fut in as_completed(future_map):
                name = future_map[fut]
                try:
                    results[name] = fut.result()
                except Exception as exc:
                    errors[name] = str(exc)
        return {
            'mode': 'matrix_fanout_fanin',
            'results': results,
            'errors': errors,
            'elapsed_ms': round((time.perf_counter() - started) * 1000, 3),
            'call_count': len(calls),
        }
