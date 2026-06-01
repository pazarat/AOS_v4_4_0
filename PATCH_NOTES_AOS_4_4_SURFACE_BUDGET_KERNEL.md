# AOS 4.4 Surface-Budget Kernel Patch Notes

## Problem fixed

The previous patch added truth-bound contracts but still allowed slow/mixed behavior when an external model bypassed the normal answer path or when runtime-surface questions were allowed to see active project payload state too early.

## Implemented changes

- Added `operations_runtime/surface_policy.py` with deterministic pre-intent surface binding.
- Added `operations_runtime/performance_budget.py` with hot-path policies for runtime/workshop/project surfaces.
- Changed the runtime graph to resolve surface before loading active project state.
- Withheld active payload name/root for runtime and workshop surfaces.
- Preserved active-project truth loading only for active-project payload surface.
- Skipped real artifact scans and goal-runtime calls for normal runtime hot answers.
- Added lazy layer registry loading so heavy capabilities are instantiated only on first use.
- Added v4.4 regression tests for payload isolation, no active payload identity leak, no real artifact scan on runtime hot path, and bounded answer latency.
- Updated entry docs to state that runtime/agent/governance questions must never start by loading active payload truth.

## Validation performed

- `python -m unittest tests.test_operations_runtime_v44_surface_budget -v`
- `python -m unittest tests.test_truth_bound_layer_runtime_standard -v`
- Targeted runtime answer benchmark for an AOS governance/performance query: approximately 2.3-2.5 seconds in this sandbox, without active payload truth loading.

## Known limitation

The legacy v4.2 project-facing tests still exercise project truth and artifact logic and are intentionally heavier. The normal runtime hot path is now separate from those project-payload tests.
