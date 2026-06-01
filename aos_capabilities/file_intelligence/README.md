# File Intelligence Capability

Read `LAYER_IDENTITY.md` first.

This capability is the Artifact Governance & Construction Runtime. It provides the cockpit for files, text, code, routes, schemas, fingerprints, diagnostics, construction context, verification, repair plans, and receipts.

Public operations only:

- `file.health`
- `file.preflight`
- `file.build_context`
- `file.validate_plan`
- `file.diagnose`
- `file.verify_after_write`
- `file.plan_repair`
- `file.doctor`
- `file.receipt`

Internal engines are not called directly by the agent.
