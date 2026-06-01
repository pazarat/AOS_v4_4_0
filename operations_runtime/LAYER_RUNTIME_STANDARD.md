# AOS Layer Runtime Standard v1

This standard turns every layer into a governed mini-runtime instead of a folder of callable files.

## Required layer shape

Each layer must expose one gateway file, usually `main.py`, that implements:

- `describe()`
- `healthcheck()`
- `validate_contract()`
- `execute(command)`

The gateway is the only injection surface accepted by Operations Runtime. Internal services remain private to the layer.

## Runtime law

1. No layer call without an `OperationContract`.
2. No filesystem operation without a `ScopePlan`.
3. No layer accepts a hand-made context; contexts must be issued by Operations Runtime.
4. No layer-to-layer direct calls.
5. Layer output must return typed status/data/contributions/blockers/warnings semantics.
6. Truth context is loaded before layer fan-out and truth arbitration runs after contribution merge.
7. Delivery is blocked or limited when the truth arbiter or delivery gate detects unsupported output.
8. Project payload names or fixture-specific examples are forbidden inside AOS runtime law.

## Layer gateway responsibility

The layer gateway owns command routing into its internal services. The kernel owns governance, scope, and final policy.

```text
Operations Runtime Kernel
→ OperationContract
→ ScopePlan
→ TruthContext
→ LayerGateway.execute(command)
→ LayerResult / contribution
→ TruthArbiter
→ DeliveryGroundingGate
```
