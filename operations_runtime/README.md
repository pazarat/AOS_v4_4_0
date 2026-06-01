# Operations Runtime Kernel

This directory is the single AOS operating kernel.

Public facade:

```text
operations_runtime/main.py
```

Layer registry:

```text
operations_runtime/layer_registry/OPERATIONS_LAYER_REGISTRY.yaml
```

All core/capability layers are services behind this kernel. They return typed `LayerContribution` objects to the runtime. The runtime synthesizes `OperationalInsight` and renders the visible answer.


## AOS v4.2 Operations Runtime Kernel

This version strengthens the runtime kernel from a unified folder into a governed execution engine:

- every major layer facade requires an OperationsContext;
- ordinary project answers invoke multiple layer services through matrix fan-out/fan-in, not a single artifact scan;
- high-value project truth is read from governing contracts, indexes, standards, memory, and owner PRDs;
- contradictions trigger a second-pass refocus before truth synthesis;
- final delivery is rendered from OperationalInsight, not from raw reports or generic model identity.
