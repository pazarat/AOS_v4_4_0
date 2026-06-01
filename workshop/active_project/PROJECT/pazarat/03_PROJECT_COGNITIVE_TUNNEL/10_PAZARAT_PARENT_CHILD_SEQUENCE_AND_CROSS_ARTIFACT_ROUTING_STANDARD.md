# PAZARAT PARENT / CHILD SEQUENCE AND CROSS-ARTIFACT ROUTING STANDARD

# Purpose

This file defines the Pazarat-specific standard for deciding how parent PRDs, child PRDs, sibling artifacts, external pages, cross-folder flows, shared primitives, and implementation-ready documentation should be sequenced and routed.

Its purpose is to prevent scenario documentation from becoming isolated folders that only describe themselves.

Pazarat documentation must preserve:

- parent-to-child inheritance
- child-to-parent feedback
- sibling dependency awareness
- parent-to-parent relationships
- cross-folder artifact routing
- prerequisite-before-dependent sequencing
- shared primitive continuity
- design and code translation readiness

This file does not replace:

- `00_PRD_COGNITION_AND_TRACEABILITY_STANDARD.md`
- `07_PAZARAT_HIERARCHICAL_DOCUMENTATION_AND_SHARED_LOGIC_PROTOCOL.md`
- `08_PAZARAT_SHARED_PRIMITIVES_AND_CONTINUITY_MEMORY.md`
- `09_PAZARAT_NARRATIVE_SEQUENCE_AND_SCENARIO_MATURITY_STANDARD.md`

It extends them by defining how to choose the next child or related artifact to build when a parent scenario mentions many possible branches or dependencies.

It must be applied together with:

```txt
11_PAZARAT_PRD_DOCUMENTATION_AND_IMPLEMENTATION_TRANSLATION_CONTRACT.md
```

Routing decides where logic belongs and what should be built first.

The documentation contract decides what the selected artifact must contain so later UI/UX, ASP.NET backend, PostgreSQL database, Next.js frontend, API planning, tests, and cumulative changes do not require guessing.

---

# Core Principle

A parent PRD is not only a container for child names.

A parent PRD is a routing map for future knowledge construction.

When a parent scenario mentions a page, flow, form, permission, external section, sibling module, shared primitive, or platform dependency, the model must classify the relationship before generating a child file.

The model must not assume that every mentioned item belongs under the current folder.

The correct action may be:

- create a local child PRD
- create a prerequisite child PRD first
- mark an external artifact route
- update or propose a shared primitive
- update or propose a state/event taxonomy addition
- add a parent-to-parent relationship
- mark an open decision
- defer creation because ownership is outside the current branch

---

# Parent As Routing Ledger Rule

A parent PRD is the permanent routing ledger for its section.

It must not only mention children; it must preserve the section map that lets future work continue without guessing.

When a parent PRD is created, revised, audited, or used as the source for child generation, the model must verify that the parent records, at parent level:

- local child candidates
- recommended child build order
- why the order exists
- prerequisite relationships between children
- child-to-child relationships when one child affects another
- external artifact routes mentioned by the parent
- parent-to-parent relationships
- shared primitive candidates
- state and event taxonomy candidates
- translation-readiness notes for future UI/UX, data, API, code, test, and workflow generation
- open routing decisions

The parent must explain the section from the first view.

It should give enough routing and distribution logic to show where each future child belongs, what it inherits, what it depends on, and what it must not own.

It must not expand child-local logic so deeply that the child PRD loses its purpose.

---

# Parent Routing Control Block Rule

Every mature parent PRD should include or support a concise Parent Routing Control Block when the section has children, external dependencies, or cross-parent links.

The exact heading may vary, but the block should preserve these outputs when relevant:

| Output | Purpose |
|---|---|
| Child Routing Map | Lists child candidates and their ownership. |
| Recommended Build Order | Defines which child or prerequisite should be built first and why. |
| Child Dependency Map | Shows child-to-child prerequisites, handoffs, and blocking dependencies. |
| External Artifact Routes | Records mentioned artifacts owned by another folder or branch. |
| Parent-To-Parent Links | Records relationships with other parent PRDs. |
| Shared Primitive Candidates | Marks reusable logic that may belong in shared primitives. |
| Taxonomy Candidates | Marks state/event logic that may need central alignment. |
| Translation Readiness Notes | Explains what the parent gives to future UI/UX, database, API, code, test, or visual generation. |
| Open Routing Decisions | Preserves unresolved routing or ownership questions. |

The Parent Routing Control Block is not a one-time planning note.

It is a living parent-level control surface.

When child work reveals a new dependency, external route, sibling relationship, missing prerequisite, or parent-to-parent link, the model must either update the parent through controlled patch discipline or record a parent update candidate.

---

# Sub-Child Artifact And Reusable Pattern Rule

Some children are containers for deeper local artifacts.

When a child PRD contains a complex form, advanced filter, profile view, edit flow, table behavior, saved view system, screen variant, or focused workflow that would overload the child, the model must classify that item as a sub-child artifact, screen PRD, workflow PRD, or reusable pattern candidate.

A parent PRD may mention sub-child families only to preserve routing, dependency order, and reuse visibility.

The parent must not expand sub-child local behavior.

A child PRD may route sub-children when its local branch needs deeper executable documentation.

A sub-child artifact must inherit from:

1. the project-local tunnel,
2. the parent PRD,
3. the owning child PRD,
4. relevant shared primitives,
5. state/event taxonomies,
6. UI/UX and implementation translation standards.

Reusable table, search, filter, pagination, export, saved-view, profile-header, action-panel, and bulk-action behavior must not be recreated as unrelated logic in every child.

When a behavior repeats across many children, classify it as:

- existing shared primitive,
- shared primitive candidate,
- reusable UI/component pattern,
- implementation utility candidate,
- child-local specialization of a shared pattern.

For example, a user list table and advanced filter pattern may be defined deeply under `all_users`, then reused by B2C sellers, B2B sellers, agents, staff, drivers, or future account-capability lists with local column and rule differences.

This prevents duplicated design/code logic while preserving each child’s local meaning.

---


# Expert Method Mediation Rule

Parent routing is not accepted because the user suggested it as a raw instruction.

It is accepted because it fits Pazarat's documentation needs: requirements hierarchy, traceability, cross-domain ownership, implementation readiness, UI/UX readiness, future change control, and platform lifecycle continuity.

When the user proposes a way to organize parent PRDs, child PRDs, cross-folder routes, or build order, the model must treat the proposal as raw intent and upgrade it into a Pazarat-fit documentation method.

The model must check the proposal against:

- Pazarat project identity
- parent-child hierarchy
- source narrative sequence
- dependency and prerequisite logic
- shared primitives
- state and event taxonomies
- UI/UX translation readiness
- database, API, code, and test readiness
- future incremental change and post-launch evolution

If the proposed method is sound, preserve the intent and express it in the correct standard.

If the proposed method is incomplete, strengthen it before codifying it.

If the proposed method would create misrouted files, duplicated ownership, weak translation, or future maintenance friction, correct the method instead of implementing it literally.

---

# Build Order Principle

Child PRDs should be built in the order that reduces guessing and preserves dependency logic.

The default ordering signals are:

1. source narrative sequence
2. prerequisite logic
3. lifecycle dependency
4. state/event dependency
5. entity and data ownership
6. permissions and access dependency
7. UI/UX dependency
8. implementation dependency
9. cross-system handoff strength
10. risk, financial, compliance, or security sensitivity

Narrative order matters, but it is not the only ordering rule.

If a later narrative item defines a prerequisite needed by an earlier screen, build the prerequisite first or mark it as a blocking dependency.

---

# Parent-To-Child Expansion Gate

Before creating or revising child PRDs from a parent PRD, the model must extract a child build map.

The map should classify each candidate as one of:

- Local Child: belongs under the current parent folder.
- Prerequisite Local Child: must be built before another local child can be mature.
- External Artifact: mentioned here but owned by another branch or interface.
- Sibling Dependency: owned by a sibling module under the same parent or dashboard.
- Parent-To-Parent Link: relationship to another parent PRD.
- Shared Primitive Candidate: reusable logic that may belong in `08_PAZARAT_SHARED_PRIMITIVES_AND_CONTINUITY_MEMORY.md`.
- Taxonomy Candidate: state or event logic that may require central taxonomy alignment.
- Open Decision: relationship exists but ownership, order, or final behavior is not yet settled.

The parent PRD should not fully define child-local logic.

It should define enough routing information for future child work to start without guessing.

---

# External Artifact Routing Rule

If a parent or child scenario mentions an artifact that is logically required but physically belongs outside the current folder, the model must not force it into the current folder.

Instead, it must document an external route.

An external route should include:

- mentioned artifact
- expected owner branch if known
- relationship type
- why it matters to the current scenario
- whether it is a prerequisite, downstream effect, handoff, or navigation target
- current maturity: existing, missing, proposed, open, or conflicting
- whether the current file may proceed without it

Example:

If User Management mentions login, authentication, or account entry, the login page is not automatically a child of the admin User Management folder.

It may belong under a web frontend, authentication, or account-access branch.

The User Management artifact should preserve the relationship as an access prerequisite or identity handoff, not invent the full login-page PRD locally.

---

# Prerequisite Before Dependent Rule

If one scenario depends on concepts that another scenario should define, build or route the prerequisite first.

Example:

A store application form may depend on verification template logic.

If the verification template defines required document types, review fields, eligibility logic, rejection reasons, evidence rules, and status behavior, it should be built before the store application form or clearly marked as a blocking dependency.

This prevents the form scenario from guessing fields that should come from verification standards.

The same rule applies to:

- permission model before permission-dependent screens
- wallet and payout logic before payout UI
- shipment status logic before delivery-tracking screens
- refund lifecycle before refund action screens
- role/access logic before dashboard visibility rules
- address/location logic before delivery forms

---

# Parent-To-Parent Relationship Map

Every mature parent PRD should include or support a parent-to-parent relationship map when meaningful.

This map should identify relationships between major parents, not only child files inside one branch.

Recommended fields:

| Field | Meaning |
|---|---|
| Related Parent | The other parent PRD or major branch. |
| Relationship Type | dependency, handoff, upstream prerequisite, downstream effect, shared primitive, navigation, compliance, data, state, event, audit, or analytics. |
| Direction | current → related, related → current, or bidirectional. |
| Why It Matters | Short reason the relationship affects scenario maturity. |
| Owner Of Logic | Which parent owns the primary logic. |
| Current Status | existing, proposed, open, missing, conflicting, or deferred. |
| Follow-Up Action | create child, update parent, add primitive, inspect sibling, defer, or mark decision. |

The relationship map should be concise.

It should not duplicate the full logic of related parents.

---

# Cross-Folder Child And Seed Rule

A child-like concept may be mentioned inside a parent scenario even when its actual file belongs elsewhere.

In that case, the current parent should create a seed reference, not a misplaced child.

A seed reference may include:

- logical name
- expected destination branch
- source sentence or scenario segment
- dependency reason
- minimum information needed later
- current maturity status

A seed reference becomes a file only when the correct owner branch is known or the user asks to create that artifact.

---

# Scenario-To-Translation Alignment Rule

Child ordering should support later translation to UI/UX, database, APIs, frontend, backend, tests, and visual generation.

A child PRD should not be built before its required vocabulary, state logic, event logic, permission model, or shared primitive is mature enough to prevent guessing.

Before finalizing a child PRD, check whether it can support:

- UI screen structure
- form field logic
- data ownership
- state transitions
- event emissions
- permission rules
- audit and notification behavior
- backend use cases
- database implications
- API grouping
- acceptance tests

If it cannot, either complete the missing bridge or mark the missing dependency clearly.

---

# Dynamic Branch Discovery Rule

The model must inspect the current project structure before choosing a path.

If a proper destination branch exists, use it.

If no clear branch exists, classify the destination as proposed and do not silently invent an accepted structure.

If the user approves the structure later, update the project tree and relevant parent maps through controlled patch discipline.

---

# No Over-Creation Rule

Not every mention creates a file.

Mentions should be classified before expansion.

A mentioned concept may be:

- explanatory context only
- local child candidate
- external dependency
- shared primitive candidate
- parent-to-parent link
- future workflow
- screen candidate
- implementation note
- open decision

Create files only when the relationship is strong enough, the owner is clear, and the current task requires it.

---

# Required Parent Routing Outputs

A mature parent PRD should support these outputs when relevant:

1. Child PRD Routing Map
2. Recommended Child Build Order
3. Prerequisite Dependency Map
4. External Artifact Relationship Map
5. Parent-To-Parent Relationship Map
6. Shared Primitive Candidate List
7. Taxonomy Alignment Candidates
8. Translation Readiness Notes
9. Open Routing Decisions

These outputs may be concise.

They exist to guide future work, not to replace detailed child PRDs.

---

# Parent Update From Routing Discovery Rule

Routing discovery is continuous.

When the model writes or reviews a child PRD, sibling PRD, screen PRD, workflow, technical extraction, or external artifact that exposes missing parent routing logic, the model must not bury that discovery inside the child only.

The model must classify the discovery as one of:

- parent update required
- parent update candidate
- child-local only
- sibling link
- external route
- shared primitive candidate
- taxonomy candidate
- parent-to-parent link
- open decision

If the parent is being revised in the current task, update the parent routing ledger directly.

If the parent is not being revised, report the parent update candidate clearly so it can be patched later.

This keeps the parent as the section heart and map while preserving child ownership of detailed logic.

---


# Lifecycle Change And Extension Rule

Pazarat documentation must remain maintainable after launch.

When a future update adds a section, child, external route, workflow, screen, state, event, permission, data object, API, or implementation behavior, the model must not patch the target file in isolation if the update affects parent routing or cross-parent meaning.

The model must classify the change impact as:

- parent routing update
- child-local update
- child-to-child dependency update
- parent-to-parent relationship update
- external artifact route update
- shared primitive update candidate
- state taxonomy update candidate
- event taxonomy update candidate
- UI/UX standard update candidate
- implementation standard update candidate
- test or acceptance-criteria update
- open decision

The parent remains the section-level map for future maintainers.

A post-launch enhancement should therefore leave a trace at the correct level: parent map, child PRD, shared primitive, taxonomy, implementation standard, UI standard, or open decision.

This allows Pazarat to evolve cumulatively without turning old documentation into disconnected legacy text.

---

# Final Rule

Pazarat documentation must be built as a connected platform map, not as isolated files.

A parent defines the route.

A child matures local logic.

A sibling or external artifact keeps its own ownership.

A shared primitive captures reusable logic.

A relationship map preserves cross-system meaning.

A build order prevents dependent scenarios from being written before their prerequisites.

The model must route before it expands.
