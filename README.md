# AOS — Unified Operations Runtime Kernel

AOS is the silent operating environment around the user's active project. It is not the project itself.

Current version:

```text
AOS v4.4.0 — Truth-Bound Surface Budget + Lazy Layer Runtime
```

## Single Runtime Entry

For ordinary questions, do not inspect the ZIP, list files, run tests, or open layer folders. Use:

```bash
python aos.py answer "<question>"
```

The only operating kernel is:

```text
operations_runtime/
```

There is no separate operations-control-room section. The former control-room concept is unified into `operations_runtime/`.

## Runtime Flow

```text
model/request
→ operations_runtime
→ OperationEnvelope
→ RuntimeGraphController
→ registered layer main.py APIs
→ MatrixInvocationEngine
→ typed LayerContribution objects
→ ContributionBus
→ ContradictionResolver
→ TruthSynthesizer
→ DeliveryRenderer
```

## Canonical Structure

```text
operations_runtime/                 root runtime kernel, graph, registry, invocation, synthesis, delivery
aos_identity/                       operating identity and constitution
aos_core/                           core services behind registered APIs
aos_capabilities/                   capability services behind registered APIs
workshop/_workshop_system/          general workshop truth and standards
workshop/active_project/PROJECT/    current-project upload gate
runtime_state/                      runtime state and trace, never project payload truth
```

## Layer Rule

Core and capability layers are not model entrypoints. Each major layer exposes a unified `main.py` facade and is registered behind:

```text
operations_runtime/layer_registry/OPERATIONS_LAYER_REGISTRY.yaml
```

A normal response must come from `OperationalInsight`, not from raw file reports, test output, or direct folder reading.

## Diagnostic Entry

Use these only when the user explicitly asks for diagnostics or AOS internals:

```bash
python aos.py inspect --scope active_project --verbose
python aos.py doctor --scope active_project --verbose
python RUN_TESTS.py
```


## AOS v4.4 Operations Runtime Kernel

This version strengthens the runtime kernel from a unified folder into a governed execution engine:

- every major layer facade requires an OperationsContext;
- ordinary project answers invoke multiple layer services through matrix fan-out/fan-in, not a single artifact scan;
- high-value project truth is read from governing contracts, indexes, standards, memory, and owner PRDs;
- contradictions trigger a second-pass refocus before truth synthesis;
- final delivery is rendered from OperationalInsight, not from raw reports or generic model identity.


## AOS v4.4 Surface-Budget Kernel

This version adds deterministic surface binding before active payload loading and a runtime performance budget for normal answers.

- runtime/agent/governance questions are bound to `aos_environment` before project payload state is loaded;
- active payload name/root is withheld on runtime/workshop surfaces;
- ordinary runtime answers skip real artifact scans and project truth calls;
- layer registry is lazy: heavy capability gateways load only on first use;
- `RUN_TESTS.py` is a smoke runner; deep/full discovery remains available with `--full`.
