# AOS Agent Entry Contract

## Mandatory Entry

Any model entering this package must treat `operations_runtime/` as the single operating kernel. Do not begin from `aos_core/`, `aos_capabilities/`, project payload files, test files, or diagnostic reports.

For ordinary user questions, use:

```bash
python aos.py answer "<user question>"
```

## Runtime Ownership

`operations_runtime/` owns:

- OperationEnvelope creation
- runtime graph sequencing
- layer API registry
- operation context tokens
- matrix fan-out/fan-in
- typed LayerContribution collection
- contradiction resolution
- truth synthesis
- surface-aware delivery rendering
- trace/receipt

## Layer Boundary

All mature layers remain preserved but operate as services behind the kernel:

- identity
- intent cognition
- truth runtime
- artifact/file intelligence
- goal runtime
- delivery/surface

Each major layer must expose a single `main.py` or equivalent API facade and must be registered in:

```text
operations_runtime/layer_registry/OPERATIONS_LAYER_REGISTRY.yaml
```

Direct model-to-layer traversal is forbidden for normal flow.

## Intent Cognition Law

Initial intent is a hypothesis, not a final decision. User language may be metaphor, symptom, scattered explanation, suspected cause, or constraint. Convert signals into operational standards, then ground them through truth.

## Truth-Grounded Response Law

Every visible answer, execution, diagnostic, and repair must be grounded in accepted truth or clearly marked as inferred, unknown, blocked, or assumed. Do not answer from memory when current file truth is required.

## Natural Surface Delivery Law

Delivery is contextual, not a word ban. Numbers, paths, reports, and traces may appear when the user asks for diagnostics or audit. Ordinary project-facing answers translate evidence into meaning and keep the runtime environment silent.

## Project Boundary Law

AOS is not the project. Workshop is not the project. The active project payload lives under the fixed project gate. The runtime must not hardcode a specific payload name as universal truth.

## Current Architecture

`AOS v4.2.0 — Hard Contracts + Multi-Layer Matrix Truth Synthesis`

The duplicate operation section has been removed. The only central operating container is `operations_runtime/`.
