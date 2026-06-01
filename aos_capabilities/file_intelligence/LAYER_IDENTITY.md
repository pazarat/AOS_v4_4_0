# File Intelligence Layer Identity

File Intelligence is the Artifact Governance & Construction Runtime of AOS.

It is the artifact cockpit: the governed view over files, folders, text, code, schemas, routes, symbols, fingerprints, diagnostics, construction context, repair plans, and receipts.

## Purpose

Make file/document/code work safe, visible, fast, and evidence-grounded.

The layer must guide construction before writing, diagnose after reading, verify after writing, and prevent accumulated errors through receipts and gates.

## Not This

- Not a generic file scanner.
- Not a patch tool by itself.
- Not a replacement for Truth, Policy, or Surface.
- Not a place to hardcode a project name.
- Not a narrow scope router.

## Public interface

```text
file.health
file.preflight
file.build_context
file.validate_plan
file.diagnose
file.verify_after_write
file.plan_repair
file.doctor
file.receipt
```

The agent must not directly call internal engines such as hash, parser, AST, image, API, database, duplicate, or static-analysis engines.

## Internal responsibilities

- Discover and classify artifacts.
- Parse and structure text/code/schema/media when available.
- Build fingerprints and change maps.
- Build search and relationship evidence.
- Resolve ownership, placement, and construction context.
- Detect duplicates, weak text, broken code, contract drift, routing errors, and architecture violations.
- Run read-only doctor diagnostics.
- Plan repairs without applying them directly.
- Emit receipts and evidence.

## Governance law

```text
No direct write.
Preflight before construction.
Verify after write.
Diagnostics are read-only.
Repair requires plan + impact + gate + receipt.
```

## Relationship to AOS surfaces

The layer may inspect AOS, Workshop, or active project scopes only through the surface decision and scope intent supplied by AOS core.

It must tag evidence as:

```text
visible_to_user
silent_internal_context
project_payload_evidence
workshop_lens
aos_governance
runtime_state
cache_only
```

## Failure signals

- A claim is based only on file name.
- A write happens without preflight.
- A repair happens without plan and receipt.
- A generated/cache file is treated as source truth.
- A project-specific payload name is hardcoded into AOS identity.
