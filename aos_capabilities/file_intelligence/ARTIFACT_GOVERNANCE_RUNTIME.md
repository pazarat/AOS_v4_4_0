# Artifact Governance & Construction Runtime

This capability is the central file/artifact runtime for AOS. It is not a core layer and it does not directly own final decisions. It gives the kernel one governed API surface for artifact discovery, construction guidance, diagnostics, verification, repair planning, and receipts.

## Public API surface

- `file.health`
- `file.preflight`
- `file.build_context`
- `file.validate_plan`
- `file.diagnose`
- `file.verify_after_write`
- `file.plan_repair`
- `file.doctor`
- `file.receipt`

## Lifecycle

```text
request
→ file.preflight
→ file.build_context
→ construction gate
→ generation guidance
→ draft/write by authorized layer
→ file.verify_after_write
→ diagnostics
→ receipt
```

## Non-negotiable rule

```text
Diagnostics are read-only.
Repair planning is read-only.
Production-oriented writes require preflight, impact, diagnostics, policy, verification, and receipt.
```

## Flexible constitution decisions

- `ALLOW`: operation may continue through standard gates.
- `WARN`: operation may continue with warnings recorded.
- `MATURE`: local truth/canon/owner reference is incomplete; mature or explicitly accept temporary risk before production write.
- `BLOCK`: stop until blockers are repaired.
