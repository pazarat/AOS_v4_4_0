# Operations Runtime Kernel — Layer Identity

## Role

`operations_runtime/` is the single root operating container of AOS. It is not an optional layer and not a compatibility wrapper. It is the runtime kernel that owns every normal operation from entry to delivery.

## Why It Exists

Previous versions split the operating brain between multiple operation sections. That made the model enter old paths, treat folders as reasoning surfaces, and bypass the intended runtime. This layer fixes the architecture by unifying all operation ownership into one kernel.

## What It Owns

- loading operational identity
- capturing intent as a hypothesis
- issuing operation context tokens
- invoking registered layer APIs
- running matrix fan-out/fan-in
- collecting typed contributions
- merging contributions
- resolving contradictions
- synthesizing OperationalInsight
- rendering contextual delivery
- producing trace and receipts

## What It Does Not Do

- It does not replace mature layers.
- It does not read raw reports into the visible answer.
- It does not censor useful details by hard word bans.
- It does not let the model navigate capability folders as reasoning paths.

## Layer Relationship

Identity, intent, truth, file intelligence, goal runtime, and delivery remain alive as services. They must be called only through this runtime kernel and their registered public facades.

## Governance Law

Every normal operation starts and ends in `operations_runtime/`. Any layer call without an operation context issued by this kernel is denied.


## v4.2 runtime identity

The runtime kernel is responsible for hard layer contracts, multi-layer matrix invocation, second-pass contradiction refocus, and OperationalInsight synthesis. It must not behave as a wrapper around a sequential scan. Layers are services; the operation envelope is the single shared state; delivery is the final renderer only after truth synthesis.
