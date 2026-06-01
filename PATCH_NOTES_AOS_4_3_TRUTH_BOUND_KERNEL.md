# AOS 4.3 Truth-Bound Kernel Patch Notes

## Purpose

This patch upgrades the agent architecture from loose layer orchestration into a truth-bound governance microkernel with contracted layer mini-runtimes.

## Implemented changes

- Added `OperationContract` as the first-class contract for every runtime operation.
- Added `ScopePlan` to bind each operation to explicit allowed roots, excluded roots, surface, and active payload role.
- Added `TruthContext` loading before layer fan-out.
- Added `TruthRuntime.produce_authoritative_packet(...)` so truth arbitration runs after contribution merge.
- Added `DeliveryGroundingGate` to validate the rendered response against truth and fixture-contamination policy.
- Added `ContextAuthority` and strengthened operation context validation so hand-made fake contexts are rejected.
- Converted major layers into gateway-style mini-runtimes with:
  - `describe()`
  - `healthcheck()`
  - `validate_contract()`
  - `execute(command)`
- Added layer manifests for the operations runtime, intent layer, truth runtime, goal runtime, and file intelligence layer.
- Replaced hardcoded project-specific project truth reading with a generic project-neutral truth reader.
- Added runtime-surface scope isolation so active project payloads are excluded from AOS runtime truth unless explicitly needed for behavior reproduction.
- Added targeted regression tests for runtime scope isolation, fake context rejection, layer gateway contracts, truth-before-layer ordering, and absence of fixture-specific names in agent runtime code.

## Key runtime flow after patch

```text
create_operation_contract
→ load_operating_identity
→ load_active_project_state
→ capture_intent_hypothesis
→ bind_operation_contract
→ plan_scope
→ load_truth_context
→ plan_layer_contributions
→ invoke_layer_matrix
→ merge_contributions
→ ground_truth_after_merge
→ resolve_contradictions
→ second_pass_if_needed
→ synthesize_operational_insight
→ render_and_validate_delivery
```

## Validation commands used

```bash
python RUN_TESTS.py
python -m unittest tests.test_truth_bound_layer_runtime_standard -v
```

Both targeted validation paths passed in this patched workspace.
