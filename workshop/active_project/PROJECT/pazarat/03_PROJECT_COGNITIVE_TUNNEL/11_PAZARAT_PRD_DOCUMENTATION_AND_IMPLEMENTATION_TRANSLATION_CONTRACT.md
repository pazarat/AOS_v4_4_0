# PAZARAT PRD DOCUMENTATION CONTRACT AND IMPLEMENTATION TRANSLATION STANDARD

# Purpose

This file defines the binding Pazarat documentation contract that connects scenario writing, parent/child PRD structure, cross-artifact routing, cumulative maintenance, and implementation translation.

It exists so Pazarat documentation can be written with one stable documentation identity while still adapting dynamically to each module, workflow, screen, and implementation target.

Its purpose is to ensure that every mature Pazarat artifact can support, at the correct depth:

- human understanding
- parent / child hierarchy
- cross-module traceability
- UI/UX interpretation
- ASP.NET backend implementation
- PostgreSQL database modeling
- Next.js frontend generation
- API planning
- validation, permissions, audit, events, and tests
- later cumulative maintenance without breaking hidden dependencies

This file is not a replacement for:

- `00_PRD_COGNITION_AND_TRACEABILITY_STANDARD.md`
- `05_UI_UX_DESIGN_SYSTEM_AND_VISUAL_GENERATION_STANDARD.md`
- `06_IMPLEMENTATION_ARCHITECTURE_AND_CODE_GENERATION_STANDARD.md`
- `07_PAZARAT_HIERARCHICAL_DOCUMENTATION_AND_SHARED_LOGIC_PROTOCOL.md`
- `09_PAZARAT_NARRATIVE_SEQUENCE_AND_SCENARIO_MATURITY_STANDARD.md`
- `10_PAZARAT_PARENT_CHILD_SEQUENCE_AND_CROSS_ARTIFACT_ROUTING_STANDARD.md`

It binds those standards into one operational contract for how PRDs must be written, reviewed, expanded, translated, and maintained.

---

# Core Principle

Pazarat documentation must be stable in structure and dynamic in content.

The fixed part is the documentation identity:

- clear artifact identity
- clear hierarchy
- clear narrative
- clear boundaries
- clear routing
- clear technical extraction
- clear cross-system links
- clear translation readiness
- clear maintenance impact

The dynamic part is the actual project logic:

- module-specific behavior
- local workflows
- local states and events
- local permissions
- local UI behavior
- local data implications
- local implementation complexity
- local child and sibling relationships

The model must not use a rigid fill-in template that ignores module logic.

The model must also not produce free-form documentation that cannot be translated, audited, updated, or implemented.

The correct behavior is:

```txt
raw input
→ mature scenario
→ structured PRD contract
→ routing and dependency map
→ technical extraction
→ design/code translation readiness
→ implementation artifact
→ future maintenance trace
```

---

# Raw Input To Contract Rule

User input may be raw, partial, exploratory, narrative, inconsistent, or based on intuition.

The model must not copy raw input directly into the project as final method.

The model must convert raw input into a Pazarat-fit documentation method by checking it against:

- Pazarat identity and objectives
- parent / child hierarchy
- state taxonomy
- event taxonomy
- UI/UX standard
- implementation standard
- shared primitives
- cross-artifact routing
- future maintenance needs
- design and code translation needs

When a user proposes a method, the model must treat it as intent and improve it into a professional project method unless the user explicitly asks to preserve the raw form.

If the user idea is correct but incomplete, strengthen it.

If the user idea is useful but belongs elsewhere, route it.

If the user idea conflicts with project standards, explain the conflict and propose the smallest safe correction.


---

# 0A. 360-Degree Contract Binding / ربط العقد بمنهج 360

This contract is the bridge between the documentation direction and the implementation translation direction inside the Pazarat 360-degree method:

```txt
13_PAZARAT_360_DEGREE_ENGINEERING_METHOD.md
```

It must not be used as a linear checklist detached from the engineering environment.

Every PRD output prepared for code must also remain compatible with:

```txt
06_IMPLEMENTATION_ARCHITECTURE_AND_CODE_GENERATION_STANDARD.md
14_PAZARAT_ENGINEERING_ENVIRONMENT_AND_STACK_STANDARD.md
02_PLATFORM_STATE_TAXONOMY.md
03_PLATFORM_EVENT_TAXONOMY.md
08_PAZARAT_SHARED_PRIMITIVES_AND_CONTINUITY_MEMORY.md
```

Parent and child PRDs both belong to the documentation direction, but they do not carry the same depth:

- Parent PRDs control section identity, boundaries, child routing, high-level state/event families, relationship maps, and parent-depth implementation implications.
- Child PRDs control local scenario, local workflow, local permissions, local states/events, local data/API/UI/test implications, and parent feedback candidates.

A child PRD is expected to be more implementation-reflective than a parent PRD because it is closer to code translation.

The model must not force one generic template across parent and child artifacts when their 360 responsibilities differ.
---

# Parent PRD Documentation Contract

A Parent PRD is the section-level map.

It must make the whole section understandable from above without becoming the detailed implementation file for every child.

A mature Parent PRD must support these outputs when relevant:

1. Artifact identity.
2. Hierarchy position.
3. Section purpose.
4. Scope and boundaries.
5. High-level operational narrative.
6. Scenario segments.
7. Parent routing control.
8. Child PRD map.
9. Recommended child build order.
10. Child-to-child dependency notes.
11. Parent-to-parent relationship map.
12. External artifact routes.
13. Shared primitive candidates.
14. State family index.
15. Event family index.
16. Entity and ownership index.
17. UI/UX output index.
18. Candidate API group index.
19. Candidate database area index.
20. Governance, permission, audit, notification, and analytics implications.
21. Translation readiness notes.
22. Open decisions.
23. Maintenance and update notes.

The parent may mention candidate API groups, service boundaries, database areas, screen groups, or workflow families.

The parent must not define final endpoint contracts, complete database schema, DTO payloads, or child-local edge cases unless the project explicitly promotes that parent artifact into a technical implementation note.

A parent should answer:

- What is this section?
- Why does it exist?
- What does it own?
- What does it not own?
- What children are needed?
- What should be built first?
- What depends on what?
- What belongs outside this section?
- Which other parents does it affect?
- What must designers and developers know before they enter the children?

---

# Child PRD Documentation Contract

A Child PRD is the local execution map for one focused branch.

It inherits from the parent, then specializes.

A mature Child PRD must support these outputs when relevant:

1. Artifact identity.
2. Parent inheritance.
3. Local purpose.
4. Local scope and boundaries.
5. Local operational scenario.
6. Local workflow.
7. User/admin/system actions.
8. Command candidates.
9. Query candidates.
10. Local entities and data groups.
11. Field and validation implications.
12. State alignment and state transitions.
13. Event alignment and emitted event candidates.
14. Permission and visibility rules.
15. Audit and accountability implications.
16. Notification and analytics implications.
17. UI/UX translation bridge.
18. Backend/API translation bridge.
19. Database translation bridge.
20. Error, empty, loading, failure, and edge cases.
21. Acceptance criteria and testable outcomes.
22. Sibling and cross-system effects.
23. Parent update candidates.
24. Open decisions.

The child PRD does not need to lock every final API route name or database column unless the artifact is explicitly a technical specification.

However, it must contain enough structured logic for the implementation bridge to derive:

- endpoints or use cases
- DTO requirements
- backend commands and queries
- validation rules
- authorization policies
- persistence needs
- events and audit records
- frontend forms, tables, states, and actions
- test cases

If a child PRD does not allow these outputs to be derived without guessing, it is not implementation-ready.

---

# Sub-Child / Screen / Workflow Documentation Contract

A Child PRD may expose sub-child artifacts when the child contains more than one executable branch.

Sub-child artifacts are appropriate for:

- create or edit forms,
- advanced filters,
- profile views,
- profile edit flows,
- table interaction models,
- reusable list patterns,
- complex action panels,
- focused workflows,
- screen-level behavior that needs independent design or implementation detail.

A sub-child artifact must not restart parent logic.

It must inherit from its parent PRD and owning child PRD, then detail only its local branch.

A child PRD should identify its sub-child map when sub-children are needed.

A sub-child should expose enough detail for the next translation step: UI/UX, backend use case, validation, database impact, API planning, frontend component, test case, or reusable implementation pattern.

If a sub-child describes a reusable pattern that appears in several children, the model must mark whether that pattern should remain child-local, become a shared primitive candidate, or become a reusable UI/frontend/backend implementation pattern.

Do not duplicate a reusable pattern as independent logic across children.

Do not force a sub-child file when a concise child section is sufficient.

---

# Workflow And Screen Artifact Contract

A Workflow PRD is required when a flow has multiple steps, approvals, external handoffs, transaction risk, state transitions, or failure paths that would overload a child PRD.

A Screen PRD is required when UI behavior, layout, table behavior, form behavior, visible states, permissions, visual hierarchy, or frontend implementation needs more detail than the child PRD should contain.

A child PRD may reference workflow and screen artifacts, but it must not bury all workflow or UI complexity in narrative prose.

Use separate workflow or screen artifacts when separation improves implementation clarity.

---

# PRD-To-Code Translation Compatibility Rule

A Pazarat PRD is mature only when its documentation level can support the next likely translation step.

The model must check:

- Can a designer understand what to design?
- Can an ASP.NET backend engineer derive use cases, handlers, policies, validation, events, and audit needs?
- Can a PostgreSQL database designer derive entities, relationships, constraints, state storage, event/audit storage, and transaction concerns?
- Can a Next.js frontend engineer derive pages, components, forms, tables, empty states, loading states, error states, and permissions?
- Can tests be written from acceptance criteria and documented behavior?

If the answer is no, the model must improve documentation before presenting the artifact as mature.

Do not jump from feature name to code.

Do not jump from parent PRD to production implementation when child-level behavior is needed.

Do not use generic CRUD as a substitute for documented product behavior.

---

# Implementation Extraction Targets

When preparing or reviewing implementation-ready documentation, the model should extract the following targets at the proper level.

## Backend / ASP.NET Targets

- domain concept or aggregate candidate
- entity or value-object candidate
- command candidate
- query candidate
- handler / service candidate
- validation rules
- authorization policy implications
- domain event candidates
- audit log requirements
- notification triggers
- background job candidates
- transaction and consistency risks
- idempotency concerns
- integration handoffs
- exception and failure paths

## PostgreSQL Targets

- table candidates
- non-table domain concepts
- relationship candidates
- ownership and foreign-key direction
- required constraints
- unique rules
- index candidates
- enum vs lookup-table candidates
- state storage requirements
- event storage requirements
- audit storage requirements
- soft delete or retention implications
- transaction boundary concerns
- reporting and analytics data needs

## API Targets

- API group candidates
- command endpoints or operations
- query endpoints or operations
- request data needs
- response data needs
- permissions per operation
- validation failure behavior
- error response implications
- pagination, filtering, sorting, and search needs
- idempotency and retry behavior when relevant

## Next.js / Frontend Targets

- route or page candidate
- screen artifact reference
- component candidates
- form fields and validation behavior
- table/list behavior
- filters and saved views
- action buttons and disabled reasons
- visible state indicators
- empty, loading, error, success, and blocked states
- permission-based visibility
- cross-linking to related sections
- notification or feedback behavior

## Test Targets

- acceptance criteria
- workflow tests
- validation tests
- authorization tests
- state transition tests
- event emission tests
- audit tests
- API tests
- UI behavior tests
- regression checks for linked artifacts

These targets are not required at full depth in every parent PRD.

They are required at the first documentation level where the logic becomes implementation-relevant.

---

# Translation Boundary Rule

Documentation and implementation must remain connected but not collapsed into one artifact.

Parent PRD:

- owns map, scope, routing, candidate groups, high-level technical output index.
- does not own final endpoint schemas or full database design.

Child PRD:

- owns local workflow, local actions, states, events, validation, permissions, and implementation bridge.
- may include candidate API groups and operation candidates.
- does not need to finalize every endpoint name unless it becomes an API specification.

API / Backend Specification:

- owns final routes, DTOs, handler names, exact validation messages, status codes, and implementation details.

Database Specification:

- owns final tables, columns, indexes, constraints, migrations, and persistence decisions.

Screen PRD / UI Specification:

- owns screen layout, component behavior, visible states, interaction details, and frontend acceptance criteria.

Code:

- implements confirmed documentation and marks unresolved items rather than inventing them.

---

# Missing Information Stop Rule

When the documentation does not contain enough information for the requested translation, the model must not silently invent final behavior.

It must classify the gap as one of:

- missing parent routing
- missing child local logic
- missing workflow detail
- missing state definition
- missing event definition
- missing validation rule
- missing permission rule
- missing entity ownership
- missing screen behavior
- missing database decision
- missing API decision
- missing testable acceptance criteria
- open business decision

Then it should provide the smallest useful next action:

- improve the PRD
- add a workflow note
- add a screen PRD
- add a technical extraction
- update taxonomy
- create an implementation specification
- ask one focused question only when necessary

---

# Cross-Artifact Impact Ledger Rule

Every meaningful addition, deletion, correction, or restructuring inside a Pazarat PRD must consider impact beyond the edited paragraph.

When a new concept, action, state, event, permission, route, screen, validation rule, database implication, API group, or external dependency appears, the model must decide whether it creates or updates:

- parent routing ledger
- child PRD map
- child build order
- sibling dependency
- parent-to-parent relationship
- external artifact route
- shared primitive candidate
- state taxonomy candidate
- event taxonomy candidate
- UI/UX translation note
- implementation translation note
- test or acceptance criterion
- open decision

This does not mean every small edit requires a large rewrite.

It means every meaningful edit must preserve traceability.

---

# Cumulative Maintenance Rule

Pazarat documentation must support future change after launch.

When adding or modifying a section later, the model must ask:

- Is this a local change only?
- Does it affect the parent map?
- Does it affect a child route?
- Does it affect a sibling?
- Does it affect another parent?
- Does it affect state taxonomy?
- Does it affect event taxonomy?
- Does it affect shared primitives?
- Does it affect UI/UX behavior?
- Does it affect backend/API/database/frontend translation?
- Does it affect tests or acceptance criteria?

If yes, the link must be recorded at the correct level.

A future maintainer, developer, or AI model should be able to inspect the document and understand what else may need review before changing the logic.

---

# Deletion And Simplification Rule

Do not delete documentation only because it looks similar to another paragraph.

Before deleting or merging content, classify it as:

- useful reinforcement
- required traceability
- harmful duplicate
- filler
- misplaced ownership
- outdated logic
- conflicting logic
- better moved elsewhere

If a weak duplicate contains a useful goal, strengthen the correct owner section first, then delete, move, or merge the weaker duplicate.

If the content is filler, remove it and report the removal.

If the content belongs in another artifact, move or route it rather than hiding it.

---

# Documentation Quality Gate

A Pazarat PRD should not be treated as mature unless it satisfies the quality gate for its level.

## Parent PRD Gate

A parent PRD is mature when it provides:

- section-level understanding
- scope and boundaries
- high-level narrative
- routing ledger
- child map
- child build order
- parent-to-parent relationships where relevant
- external routes where relevant
- technical output index
- design/code translation readiness
- open decisions
- maintenance notes

## Child PRD Gate

A child PRD is mature when it provides:

- parent inheritance
- local purpose and scope
- local scenario and workflow
- states, events, permissions, validation, and audit implications
- UI/UX bridge
- implementation bridge
- data/API/backend/frontend/test implications
- sibling and cross-system effects
- parent update candidates
- open decisions

## Implementation-Ready Gate

An artifact is implementation-ready only when the model can derive the next technical artifact without inventing hidden business behavior.

If implementation requires unresolved decisions, the artifact must say so.

---

# Standard Output Behavior

When the user provides raw scenario input for a Pazarat module, the model should normally produce or revise the artifact using this contract.

The visible output may be concise, but the artifact itself should preserve:

- narrative clarity
- technical extraction
- routing logic
- translation readiness
- maintenance trace

When the user asks for a small edit, do not rewrite the whole artifact unless necessary.

When the user asks for a new PRD or major revision, apply the full contract at the appropriate level.

When the user asks for code, verify that the PRD-to-code bridge is sufficiently mature before generating production-oriented code.

---

# Final Rule

The Pazarat documentation system exists to make the platform buildable.

A PRD that is beautiful but not traceable is weak.

A PRD that is traceable but not understandable is weak.

A PRD that is understandable but not translatable to design or code is incomplete.

A PRD that can be translated once but cannot be maintained later is not mature enough for a large platform.

The correct Pazarat standard is:

```txt
clear narrative
+ stable documentation identity
+ dynamic project logic
+ routing and dependency trace
+ UI/UX readiness
+ implementation readiness
+ cumulative maintenance safety
```


Any PRD-to-code translation must pass the code practice canon gate in `18_PAZARAT_CODE_PRACTICE_AND_IMPLEMENTATION_CANON.md`. If a PRD can yield entities/API but the implementation practice is not defined, classify the missing practice as incomplete truth before production-oriented code.
