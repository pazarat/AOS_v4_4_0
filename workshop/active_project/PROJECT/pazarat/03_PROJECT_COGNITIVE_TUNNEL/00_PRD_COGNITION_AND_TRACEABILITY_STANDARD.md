# PRD COGNITION AND TRACEABILITY STANDARD

# Purpose

This file defines the primary cognition, documentation, traceability, inheritance, and cumulative revision standard for Pazarat PRDs.

It is the first project-level standard that should be used before creating, reviewing, expanding, correcting, or generating any Pazarat documentation artifact.

This file is not only a writing guide.

It is a product cognition standard.

Its purpose is to help the model, product owner, UI/UX designer, backend developer, frontend developer, and future AI understand:

- how to think about a section
- how to mature a raw idea
- how to structure a scenario
- how to extract technical outputs
- how to preserve parent / child hierarchy
- how to detect missing relationships
- how to prevent documentation drift
- how to support UI/UX generation
- how to support backend and frontend implementation
- how to revise artifacts cumulatively without losing prior accepted logic

Pazarat documentation is not passive documentation.

It is a knowledge construction system.

---

# Standard Identity

This file defines:

```txt
PRD Cognition Standard
+ Scenario Maturity Standard
+ Technical Output Standard
+ Parent / Child Inheritance Standard
+ Cross-System Traceability Gate
+ Cumulative Revision Gate
+ UI/UX Generation Readiness Standard
+ Implementation Readiness Standard
+ Documentation Contract And Translation Readiness Standard
+ Local Numbered Tunnel Awareness Gate
+ Pazarat Hierarchical Documentation Binding
+ Pazarat Shared Primitives Binding
```

It does not replace:

- Platform identity files
- State taxonomy
- Event taxonomy
- Project structure tree
- UI/UX design and visual generation standard
- Implementation architecture and code generation standard
- Pazarat hierarchical documentation and shared logic protocol
- Pazarat PRD documentation and implementation translation contract
- Pazarat shared primitives and continuity memory
- Parent PRDs
- Child PRDs
- Workflow files
- Screen PRDs
- Backend technical specifications

It governs how those files should be understood, created, checked, connected, revised, and inherited.

This file is the first Pazarat-local standard, but it is not the only local standard.

The model must account for all actual numbered root files inside the Pazarat project folder in numeric order before producing meaningful Pazarat project work.

---

# Mandatory Project Entry Sequence

Before working on any meaningful Pazarat PRD, scenario, section, workflow, screen, technical extraction, visual generation request, implementation-aware artifact, or project audit, the model must synchronize with the Pazarat project through the local numbered tunnel and relevant dynamic context.

The Pazarat local tunnel is discovered from actual numbered root files directly inside:

    02_MY_PROJECT/pazarat/

Any root file directly inside that folder that starts with a numeric prefix from `00` to `99` is part of the Pazarat local tunnel unless clearly obsolete, backup, temporary, unrelated, or outside active project scope.

The model must not rely only on a hardcoded list of local tunnel files.

Numeric order determines traversal order.

File name suggests responsibility.

File content confirms actual purpose.

---

## Current Navigational Snapshot

The current known Pazarat local tunnel snapshot includes:

```txt
00_PRD_COGNITION_AND_TRACEABILITY_STANDARD.md
01_PAZARAT_PRD_PLATFORM_IDENTITY_AND_OBJECTIVES.md
02_PLATFORM_STATE_TAXONOMY.md
03_PLATFORM_EVENT_TAXONOMY.md
04_PROJECT_STRUCTURE_TREE_INDEX.md
05_UI_UX_DESIGN_SYSTEM_AND_VISUAL_GENERATION_STANDARD.md
06_IMPLEMENTATION_ARCHITECTURE_AND_CODE_GENERATION_STANDARD.md
07_PAZARAT_HIERARCHICAL_DOCUMENTATION_AND_SHARED_LOGIC_PROTOCOL.md
08_PAZARAT_SHARED_PRIMITIVES_AND_CONTINUITY_MEMORY.md
09_PAZARAT_NARRATIVE_SEQUENCE_AND_SCENARIO_MATURITY_STANDARD.md
10_PAZARAT_PARENT_CHILD_SEQUENCE_AND_CROSS_ARTIFACT_ROUTING_STANDARD.md
11_PAZARAT_PRD_DOCUMENTATION_AND_IMPLEMENTATION_TRANSLATION_CONTRACT.md
12_PAZARAT_PRD_AND_CODE_RUNTIME_GATES.yaml
13_PAZARAT_360_DEGREE_ENGINEERING_METHOD.md
14_PAZARAT_ENGINEERING_ENVIRONMENT_AND_STACK_STANDARD.md
15_PAZARAT_RAW_TO_PROGRAMMATIC_NARRATIVE_WEAVING_STANDARD.md
16_PAZARAT_DATA_MODEL_DATABASE_API_AND_ENDPOINT_STANDARD.md
99_PAZARAT_PROJECT_REINFORCEMENT_MEMORY.md
```

This snapshot is for navigation and review.

It is not the only source of tunnel truth.

If additional numbered root files exist in the actual repository, they must be treated as part of the local Pazarat tunnel even if this snapshot has not been updated yet.

If this snapshot lists a file that does not exist, the model must not assume it exists. It should classify the reference as missing, stale, expected, or migration-related.

If this snapshot and the actual repository structure disagree, inspect the actual repository structure first, then update the relevant index or standard.

---

## Required Synchronization Order

For meaningful Pazarat work, the model should internally apply this sequence:

```txt
1. Account for all actual numbered root files inside 02_MY_PROJECT/pazarat/ in numeric order.
2. Use the project structure tree to locate the relevant branch.
3. Inspect the relevant area, dashboard, interface, domain, parent PRD, or child PRD.
4. Check relevant local numbered files inside the target branch if they exist.
5. Inspect relevant sibling and cross-system files when required.
6. Apply parent/child sequence and cross-artifact routing when creating or expanding PRDs.
7. Apply the PRD documentation and implementation translation contract when generating, revising, auditing, or preparing PRDs for design or code.
8. Compare repository context with current conversation decisions and corrections.
8. Produce the answer or artifact from cumulative project context.
```

The sequence is mandatory in principle, but traversal depth must match the task.

Small direct questions may use compressed awareness.

Scenario generation, PRD revision, file replacement, architecture analysis, UI/UX generation, implementation-aware extraction, or technical audit requires deeper synchronization.

---

# Project Files Should Stay Locally Understandable

Pazarat project files should be understood from Pazarat local context.

They do not need to repeat exact paths to the cognitive runtime or project orchestration layers.

The upper layers are responsible for routing the model into the project.

The Pazarat project folder is responsible for preserving Pazarat-specific truth.

This file should not depend on exact upper-layer paths such as cognitive runtime or project orchestration paths.

Project-local paths such as:

    02_MY_PROJECT/pazarat/

may be used when they clarify Pazarat structure, file placement, traceability, or migration status.

This keeps Pazarat portable and prevents upper-layer architecture from polluting project-specific documentation.


---

# 360-Degree Engineering Alignment / ربط منهج 360 درجة

All Pazarat documentation work must serve the Pazarat 360-degree engineering method defined in:

```txt
13_PAZARAT_360_DEGREE_ENGINEERING_METHOD.md
```

Documentation standards are not isolated formatting templates.

They must be authored so that narrative, hierarchy, states, events, permissions, shared primitives, UI implications, backend implications, database implications, API implications, and acceptance criteria can later be translated into code through the implementation translation direction and generated inside the accepted engineering environment.

A PRD is not mature merely because it is readable.

A PRD is mature when its depth level can support the next 360 step without forcing the model to invent business logic, state terms, event terms, database structures, endpoints, or frontend behavior.

Central shared references are binding across documentation, translation, and code:

```txt
02_PLATFORM_STATE_TAXONOMY.md
03_PLATFORM_EVENT_TAXONOMY.md
08_PAZARAT_SHARED_PRIMITIVES_AND_CONTINUITY_MEMORY.md
13_PAZARAT_360_DEGREE_ENGINEERING_METHOD.md
14_PAZARAT_ENGINEERING_ENVIRONMENT_AND_STACK_STANDARD.md
15_PAZARAT_RAW_TO_PROGRAMMATIC_NARRATIVE_WEAVING_STANDARD.md
16_PAZARAT_DATA_MODEL_DATABASE_API_AND_ENDPOINT_STANDARD.md
```

The model must not define competing local names for shared states, events, primitives, permissions, reusable UI behavior, or implementation concepts when a central reference exists or should be created.
---

# Core Philosophy

A strong Pazarat PRD must do more than describe a feature.

It must construct operational understanding.

Each mature PRD should help answer:

- What is this section?
- Why does it exist?
- What lifecycle does it control?
- Who interacts with it?
- What entities appear?
- What states exist?
- What events happen?
- What workflows are implied?
- What pages or screens are needed?
- What UX outputs must exist?
- What backend boundaries are implied?
- What external systems are connected?
- What belongs to the parent?
- What belongs to children?
- What belongs to another domain?
- What must remain open for later decision?

The PRD must reduce guessing for designers, developers, product teams, and future AI.

---

# Raw Idea Maturation Principle

A raw user idea is not automatically a mature PRD.

When the user provides a raw scenario, rough explanation, partial thought, or early concept, the model must help mature it.

The model should identify:

- the section purpose
- the lifecycle controlled by the section
- the actors involved
- the operational objects involved
- the entities implied
- the states implied
- the events implied
- the workflows implied
- the pages or sections implied
- the UX outputs implied
- the backend implications
- the external dependencies
- the child branches needed
- the open decisions
- the risks if logic remains unclear

The model must not merely format the raw idea.

It must help transform the raw idea into project-grade operational knowledge.

---

# Product Knowledge Engineering Role

When building PRDs, the model should behave as a product knowledge engineer.

This means it should:

- understand the user’s intent deeply
- preserve project-specific logic
- use expert product reasoning
- detect missing flows
- detect hidden dependencies
- detect ownership conflicts
- detect state/event implications
- detect UX implications
- detect backend/API implications
- detect cross-system relationships
- propose missing branches when appropriate
- avoid replacing the user’s concept with generic marketplace logic
- separate what is confirmed from what is proposed
- help mature the section until it becomes design-ready and development-ready

The model must not behave as a passive formatter only.

---

# Documentation Levels

Pazarat documentation follows a hierarchy.

Each level has a specific role.

```txt
Platform Standard
→ Platform Identity
→ Shared Taxonomies
→ Project Structure Tree
→ Area PRD
→ Dashboard / Interface PRD
→ Domain PRD
→ Parent PRD
→ Child PRD
→ Workflow PRD
→ State/Event Model
→ Screen PRD
→ Visual Reference
→ Technical / API / Implementation Notes
```

Do not collapse all levels into one file.

Do not place child-level detail inside the parent unless it is needed to explain parent logic.

Do not allow a child file to redefine the parent logic.

Do not allow a screen PRD to invent logic that is missing from the parent or child.

---

# Scenario Narrative Standard

The scenario narrative is the operational story of the section.

It should be written as connected product logic, not as scattered bullets and not as abstract philosophy.

A good scenario narrative explains:

- entry point
- actor
- context
- action
- system behavior
- decision
- result
- state change
- event implication
- cross-system effect
- what is deferred to child PRDs or external owners

The exact sections and paragraph names may change depending on the module.

Shipping does not need to use the same paragraph titles as User Management.

Wallets do not need to use the same paragraph titles as Products.

However, every scenario must preserve the same documentation discipline:

```txt
journey
+ logic
+ boundaries
+ outputs
+ traceability
```

The story may differ.

The standard must remain stable.

---

# Scenario Paragraph Formula

When writing scenario paragraphs, use this mental formula:

```txt
Step
→ Context
→ Rule
→ Effect
→ Boundary
```

Where useful:

- Step: what happens?
- Context: what determines this step?
- Rule: what governs it?
- Effect: what changes in the system?
- Boundary: what belongs to a child or another module?

Not every paragraph needs all five parts.

But the scenario should generally preserve this reasoning structure.

---

# Scenario Narrative Quality Rules

A scenario narrative should be:

- operational
- concrete
- connected
- project-specific
- cause-and-effect based
- hierarchy-aware
- relationship-aware
- readable by product, design, development, and AI

A scenario narrative should avoid:

- vague feature descriptions
- generic marketplace statements
- excessive philosophy
- premature database detail
- UI micro-detail
- disconnected bullet dumps
- repeating the same idea in multiple sections
- hiding important decisions inside long prose

The narrative explains meaning.

The technical output index fixes outputs.

---

# Parent PRD Role

A Parent PRD is the main operational reference for a section.

It defines the complete section at parent level.

It must be deep enough to guide all children.

It must not contain every implementation detail.

A Parent PRD should define:

- section identity
- hierarchy position
- section purpose
- core philosophy
- scope and boundaries
- operational scenario narrative
- scenario segments
- key terms
- governing rules
- shared logic anchors
- technical output index
- child PRD routing
- child build order
- child-to-child dependency notes
- external relationship map
- parent-to-parent relationship map
- routing update candidates
- deferred decisions
- AI continuation summary when useful

A Parent PRD should usually give most of the conceptual understanding of the section.

Children deepen focused branches.

---

# Parent PRD Required Outputs

A mature Parent PRD should include these outputs.

The exact headings may adapt to the section, but the outputs must exist.

## 1. Artifact Identity

Identify:

- artifact name
- artifact type
- project area
- dashboard or interface
- domain
- module
- parent / child status
- related files

## 2. Hierarchy Position

Explain where the section sits in the project and why it matters.

## 3. Section Purpose

Explain the operational problem the section solves.

## 4. Parent Routing Control

For parent PRDs with children, cross-folder references, or related parents, include a parent-level routing control surface.

It should identify:

- child routing map
- recommended child build order
- child-to-child dependencies
- external artifact routes
- parent-to-parent relationships
- shared primitive candidates
- taxonomy candidates
- translation-readiness notes
- maintenance and cumulative update notes
- open routing decisions

The parent routing control surface must guide future child writing without replacing child-local detail.


## 4A. Method And Standards Alignment

When the parent introduces a routing, child sequencing, or cross-artifact organization method, the model must ensure the method is not a literal copy of raw discussion only.

It must align the method with Pazarat local standards, domain knowledge, traceability, UI/UX readiness, implementation readiness, and future change control.

The parent should preserve the user's intended direction while expressing it as a maintainable project method.

If a proposed parent structure would weaken downstream design, database modeling, API planning, code generation, testing, or later incremental updates, the model must strengthen the method before using it as the parent standard.


## 5. Core Philosophy

State the governing idea of the section in project-native language.

## 6. Scope And Boundaries

Clarify:

- In Scope
- Out of Scope
- parent-owned logic
- child-owned detail
- external-owned detail
- deep owners

## 7. Operational Scenario Narrative

Explain the main journey as connected paragraphs.

## 8. Scenario Segments

Break the journey into meaningful named segments when useful.

## 9. Key Terms

Define terms that must not be confused.

## 10. Governing Rules

List rules that protect the section from contradiction.

## 11. Shared Logic Anchors

Identify reusable concepts affecting multiple children or modules.

## 12. Parent Scenario Technical Output Index

Extract the technical and operational outputs from the scenario.

## 13. Child PRD Routing

List child branches created by the parent.

## 14. External Relationship Map

Explain relationships with other modules and deep owners.

## 15. Deferred Decisions

List unresolved decisions clearly.

## 16. AI Continuation Summary

Provide a compact summary for future AI continuation when useful.

---

# Parent Scenario Technical Output Index Standard

Every mature Parent PRD should include a technical output index.

This index is not a second explanation of the scenario.

It is a technical map extracted from the scenario.

It makes outputs explicit so developers, designers, and future AI do not need to infer everything from narrative prose.

A mature Parent Technical Output Index should include:

## 1. Technical Index Purpose

Clarify that the index is an extraction layer, not a final implementation spec.

## 2. Technical Scope

Clarify what is covered and what is out of scope.

## 3. Core Technical Principle

State the main technical rule of the section.

## 4. Core Entities Index

List major entities implied by the parent.

## 5. Entity Ownership Index

Clarify which module owns each entity or concept.

## 6. Relationship Map

Show important entity and system relationships.

## 7. Lifecycle / Journey Index

List the parent-level lifecycle sequence.

## 8. Flow Families Index

List major flow families produced by the section.

## 9. State Families Index

List required state families.

Any state logic must follow:

```txt
02_PLATFORM_STATE_TAXONOMY.md
```

## 10. Event Families Index

List required event families.

Any event logic must follow:

```txt
03_PLATFORM_EVENT_TAXONOMY.md
```

## 11. Pages / Sections Output Index

List pages, sections, or operational surfaces produced by the parent.

## 12. UX Output Index

List expected UX outputs.

Examples:

- badges
- status indicators
- timelines
- required action panels
- filters
- saved views
- contextual actions
- disabled action reasons
- review queues
- cross-system links

## 13. Service / Module Boundary Index

List conceptual service or module boundaries.

These are not final implementation names unless confirmed.

## 14. API Group Index

List candidate API groups without defining final endpoints.

## 15. Cross-System Dependency Index

List related systems and dependency meanings.

## 16. Governance Output Index

List verification, approval, permission, restriction, moderation, escalation, audit, or policy outputs.

## 17. Data Output Index

List data groups implied by the section.

## 18. Technical Constraints

List implementation rules that must not be violated.

## 19. Child PRD Routing Index

List child PRDs and what each should detail.

## 20. Parent vs Child Boundary

Clarify what the parent owns and what children own.

## 21. Open Technical Decisions

List unresolved technical decisions.

The index must be complete enough to guide designers and developers, but not so detailed that it becomes a backend specification.

---

# PRD Documentation Contract Gate

Every Parent PRD and Child PRD must satisfy the Pazarat documentation contract at its own level.

The parent-level contract makes the section understandable, routed, traceable, and ready for child expansion.

The child-level contract makes local behavior detailed enough for UI/UX, ASP.NET backend, PostgreSQL database, Next.js frontend, API planning, and tests to be derived without guessing.

The governing documentation-to-implementation contract is:

```txt
11_PAZARAT_PRD_DOCUMENTATION_AND_IMPLEMENTATION_TRANSLATION_CONTRACT.md
```

It must operate inside the full 360 loop:

```txt
13_PAZARAT_360_DEGREE_ENGINEERING_METHOD.md
14_PAZARAT_ENGINEERING_ENVIRONMENT_AND_STACK_STANDARD.md
15_PAZARAT_RAW_TO_PROGRAMMATIC_NARRATIVE_WEAVING_STANDARD.md
16_PAZARAT_DATA_MODEL_DATABASE_API_AND_ENDPOINT_STANDARD.md
```

Do not treat the contract as a rigid template.

Treat it as the stable documentation identity that every PRD must satisfy dynamically according to its level and purpose.

---

# Child PRD Role

A Child PRD deepens one branch from the Parent PRD.

It inherits first, then specializes.

A Child PRD must not restart the project logic.

It must not redefine parent rules silently.

It must not ignore state, event, UX, permission, notification, analytics, or cross-system implications.

---

# Child PRD Required Outputs

A mature Child PRD should include:

## 1. Artifact Identity

Identify the child artifact, parent, domain, and related files.

## 2. Parent Inheritance

List what the child inherits from the parent:

- inherited entities
- inherited state families
- inherited event families
- inherited constraints
- inherited terminology
- inherited cross-system dependencies
- inherited governing rules

## 3. Local Purpose

Explain why this child exists.

## 4. Local Scope And Boundaries

Clarify:

- what this child owns
- what it references
- what remains parent-owned
- what belongs to siblings
- what belongs to external modules

## 5. Local Operational Scenario

Explain the local branch journey.

Do not repeat the full parent scenario.

## 6. Local Workflow

Describe local steps, decisions, outcomes, and handoffs.

## 7. Local Technical Extraction

Extract local technical outputs:

- local entities
- data groups
- states
- transitions
- events
- actions
- permissions
- notifications
- audit
- UI outputs
- API groups
- validation notes
- edge cases
- dependencies
- open questions
- maintenance and cross-artifact impact notes

## 8. Parent Alignment Check

Answer:

- Which parent rules are used here?
- Which parent states are extended here?
- Which parent events are used or expanded?
- Which parent entities are referenced?
- Does this child reveal a missing parent rule?
- Does this child contradict any parent rule?

## 9. Sibling And Cross-System Check

Identify dependencies with siblings or external modules.

## 10. Open Decisions

List unresolved child-level decisions.

---

# Workflow PRD Standard

A Workflow PRD defines execution behavior.

It should include:

- workflow purpose
- parent / child context
- trigger
- actors
- preconditions
- steps
- decision points
- state changes
- emitted events
- notifications
- audit needs
- exceptions
- outcomes
- handoffs
- ownership boundaries

A workflow must connect back to its parent or child scenario.

It must not invent unrelated product logic.

---

# State/Event Model Standard

A State/Event Model defines lifecycle traceability.

It must follow the central state and event standards.

Use:

```txt
02_PLATFORM_STATE_TAXONOMY.md
03_PLATFORM_EVENT_TAXONOMY.md
```

A State/Event Model should define:

- state families
- allowed states
- transition rules
- transition triggers
- emitted events
- side effects
- notification implications
- audit implications
- analytics implications
- automation hooks
- ownership boundaries

State and event must remain distinct.

```txt
State = current condition
Event = something that happened
```

---

# Screen PRD Standard

A Screen PRD defines UI/UX and implementation-support behavior for a specific screen.

It must inherit from its parent or child PRD.

It should include:

- screen identity
- parent / child context
- screen purpose
- user roles
- entry points
- layout zones
- displayed data
- data sources
- visible states
- actions
- permissions
- disabled action reasons
- empty states
- loading states
- error states
- filters
- saved views when needed
- navigation
- cross-system links
- events triggered
- notification / audit implications
- implementation notes
- visual reference direction

A Screen PRD must not invent logic that contradicts the parent or child.

---

# Design-Ready And Visual-Generation Outputs

A Pazarat PRD must not only explain product logic.

It must also produce enough structured design information to support consistent UI/UX design, visual reference generation, and later Figma implementation.

This does not mean that every PRD becomes a full UI specification.

It means that every mature PRD must make the design implications visible at the correct level.

---

## Design-Ready Principle

Scenario documentation must explain the meaning.

Technical output must extract the structure.

Design-ready output must clarify how the logic may appear in the interface.

A visual reference or UI/UX image should not be generated from a vague prompt when repository context exists.

Before generating UI/UX for any Pazarat section, the model must synchronize with:

- platform identity
- project structure tree
- relevant parent PRD
- relevant child PRD
- relevant workflow if available
- relevant state/event model if available
- relevant screen PRD if available
- UX outputs and screen requirements from the PRD
- shared UI/UX design system and visual generation standard
- existing visual references when available
- current conversation intent

The shared design standard must live in:

```txt
02_MY_PROJECT/pazarat/05_UI_UX_DESIGN_SYSTEM_AND_VISUAL_GENERATION_STANDARD.md
```

---

## Design-Ready Outputs

A mature Parent PRD should identify design output families, such as:

- major pages
- major sections
- operational surfaces
- dashboards
- review queues
- timelines
- profile surfaces
- tables
- filters
- status displays
- action areas
- linked entity areas
- empty / loading / error state needs

A mature Child PRD should identify local design outputs, such as:

- screen candidates
- local layout zones
- local components
- local data groups
- local actions
- local permissions
- local state displays
- local event/timeline displays
- local empty / loading / error states
- local filter and search behavior
- local visual reference requirements

A mature Screen PRD should define detailed UI behavior, including:

- screen purpose
- user roles
- entry points
- layout zones
- displayed data
- data sources
- reusable components
- state indicators
- event/timeline outputs
- actions
- permissions
- disabled action reasons
- empty states
- loading states
- error states
- filters
- saved views when needed
- navigation
- cross-system links
- implementation notes
- visual reference direction

---

## Reusable Component Awareness

When a PRD implies a UI pattern, the model must check whether the pattern should use an existing reusable component instead of inventing a new visual shape.

Examples of reusable UI patterns include:

- data table
- filter drawer
- saved views
- status badge
- capability badge
- verification panel
- approval queue
- timeline
- action bar
- profile summary card
- linked entity card
- requirement builder
- audit trail
- empty state
- error state
- loading skeleton

The model must avoid generating a new visual style for every screen when the same component pattern can serve the same purpose.

Visual consistency is part of documentation quality.

---

## Visual Generation Readiness

A mature UI/UX generation prompt should reflect:

- project identity
- target dashboard or app
- user role
- screen purpose
- parent / child context
- layout zones
- data groups
- state indicators
- actions
- permissions
- empty / loading / error states when relevant
- operational hierarchy
- reusable components
- cross-system links
- visual tone suitable for Pazarat

The goal is that a user can ask:

```txt
Generate the UI/UX image for Verification Templates.
```

and the model should know to inspect the repository path, parent logic, child logic, states, events, UX outputs, screen requirements, and design system rules before generating.

---

## Design Consistency Gate

Before accepting any visual reference or UI/UX generation output, verify:

1. Does it inherit from the relevant parent or child PRD?
2. Does it reflect the correct screen or section purpose?
3. Does it use the expected layout pattern?
4. Does it use reusable components when possible?
5. Does it show the correct state indicators?
6. Does it show the correct actions and permissions?
7. Does it avoid inventing unrelated UI logic?
8. Does it align with existing Pazarat visual references?
9. Does it support later Figma implementation?
10. Does it avoid creating a different design language for every screen?

The image is not just decoration.

It is a visual reference derived from documented product logic.

---

# Technical / API / Backend Awareness Standard

A PRD should not prematurely become a backend implementation file.

However, mature PRDs must make backend implications visible.

A PRD should identify:

- entity ownership
- service boundaries
- API groups
- data groups
- state families
- event families
- constraints
- integration points
- open technical decisions

Detailed schemas, endpoints, payloads, transactions, indexes, validations, and infrastructure choices belong in backend technical specifications or implementation notes.

The Parent PRD gives orientation.

The Child PRD gives branch depth.

Backend specs give final implementation detail.

---

---

# Implementation-Ready Documentation Outputs

A mature Pazarat PRD must be understandable by product, design, and engineering.

It does not need to become code.

It does not need to define final database schemas, endpoint payloads, infrastructure, or framework-specific implementation.

However, it must contain enough structured outputs so that a later implementation standard can translate the documentation into backend, frontend, database, API, tests, and integration work without guessing the product logic.

---

## Implementation-Ready Principle

Scenario narrative explains the operational meaning.

Technical output index extracts the project logic.

Implementation-ready outputs ensure that the extracted logic can later be converted into code architecture.

This means that a PRD should not hide important implementation logic inside prose.

If a process affects entities, states, events, permissions, integrations, financial flows, shipping flows, notifications, analytics, or external systems, the PRD must make those relationships explicit at the correct level.

---

## Implementation-Ready Outputs For Parent PRDs

A mature Parent PRD should identify, at parent level:

- major use cases
- major operations
- major entity groups
- major state families
- major event families
- major workflow families
- major cross-system handoffs
- major integration boundaries
- major permission boundaries
- major data groups
- major validation areas
- major failure areas
- major child PRDs that will detail implementation logic
- major open technical decisions

The Parent PRD does not need to define exact endpoints, database tables, DTOs, or code structure.

It must distribute the roots of implementation logic to the correct child branches.

---

## Implementation-Ready Outputs For Child PRDs

A mature Child PRD should identify, at local branch level:

- local use cases
- local operations
- local commands
- local queries
- local entities
- local data groups
- local state families
- local state transitions
- local events
- local actions
- local permissions
- local validation rules
- local failure and edge cases
- local integration handoffs
- local notification implications
- local analytics implications
- local audit implications
- local acceptance criteria
- local testable outcomes
- whether a separate workflow file is required
- whether a separate state/event model is required
- whether a screen PRD is required
- whether implementation notes are required

The Child PRD must be precise enough that implementation can later be derived from it.

It must not force future developers or AI agents to infer the local process from general parent prose.

---

## Implementation-Ready Outputs For Workflow PRDs

A Workflow PRD should identify:

- workflow name
- workflow purpose
- trigger
- actors
- preconditions
- steps
- decisions
- commands
- queries
- state transitions
- emitted events
- validation rules
- failure paths
- retries
- cancellation paths
- permissions
- transaction or consistency boundaries
- cross-system handoffs
- notifications
- audit requirements
- analytics outputs
- acceptance criteria

A Workflow PRD is required only when the flow is complex, sensitive, multi-step, multi-system, state-heavy, or implementation-critical.

Not every child PRD needs a separate workflow file.

Every child PRD must mention its important workflows.

Only complex workflows require their own files.

---

## Use Cases, Commands, And Queries

A mature PRD should help later implementation distinguish between:

| Concept | Meaning |
|---|---|
| `Use Case` | A business operation or user/system goal |
| `Command` | An operation that changes system state |
| `Query` | An operation that reads system state |
| `Business Rule` | A rule that must always be respected |
| `Validation Rule` | A rule that checks input or eligibility |
| `Policy Rule` | A rule controlled by permissions, governance, country, category, or configuration |

Examples:

| Documentation Output | Later Implementation Meaning |
|---|---|
| `Create Verification Template` | Command / API / Service Method |
| `List Verification Templates` | Query / API / Table View |
| `Activate Seller Capability` | Command / State Transition / Event |
| `Review Verification Case` | Use Case / Workflow / Permissioned Action |
| `Get User Profile Context` | Query / Aggregation / Read Model |
| `Suspend Account` | Command / Governance Action / Audit Event |

PRDs do not need to define final code names.

They must clarify the operation meaning.

---

## Business Rules And Invariants

A PRD must document rules that implementation must not violate.

Examples:

- do not activate a capability from intent alone
- do not create a store before required approval when approval is required
- do not merge verification and approval
- do not collapse multiple state families into one global status
- do not allow duplicate reward grants for the same completed goal
- do not create shipment before the order is eligible for fulfillment
- do not refund without a valid refund workflow
- do not allow unauthorized actors to change approval decisions

These are not code details.

They are implementation-critical product rules.

---

## Validation And Eligibility Rules

A mature PRD should identify validation or eligibility rules when they affect behavior.

Validation may include:

- required fields
- required documents
- country-specific requirements
- account type requirements
- seller type requirements
- category eligibility
- financial eligibility
- shipping eligibility
- permission eligibility
- duplicate prevention
- expiry rules
- time-window rules

The exact validation implementation belongs to backend specs or implementation notes.

The PRD must make the rule visible.

---

## Failure And Edge Cases

A mature PRD should not only document the happy path.

It should identify important failure and edge cases, such as:

- rejected verification
- approval needs update
- expired request
- failed payment
- insufficient stock
- shipment failed
- duplicate submission
- expired coupon
- duplicate reward
- invalid permission
- unsupported country
- abandoned cart
- inactive user
- missing required document
- integration failure

Failure cases often produce states, events, notifications, audit records, and UI messages.

If failure behavior is important, it must be documented.

---

## Transaction And Consistency Boundaries

A PRD should identify where consistency matters, without defining database transactions.

Examples:

- order payment success must align with order status
- stock reservation must align with checkout/order behavior
- store creation must align with approval result
- wallet credit must align with reward or refund event
- shipment creation must align with order fulfillment eligibility
- capability activation must align with approval decision
- notification should not be sent twice for the same event
- reward should not be granted twice for the same goal

These boundaries help later backend implementation decide where transactions, idempotency, locking, events, or compensating flows may be needed.

---

## Integration Handoffs

A PRD must document cross-system handoffs when a process affects another module.

Examples:

| Source Logic | Handoff |
|---|---|
| User becomes seller | User Management → Store Management → Permissions |
| Order is paid | Orders → Payments → Inventory → Shipping → Notifications |
| Refund is approved | Returns → Payments / Wallets → Notifications → Analytics |
| Shipment delivered | Shipping → Orders → Notifications → Rewards / Analytics |
| Reward granted | Rewards → Wallets / Coupons → Notifications → Analytics |
| Product published | Products → Search / Catalog → Store → Analytics |
| Verification approved | Verification → Approval / Capability / Financial Eligibility |

Cross-system handoffs must be visible in PRDs.

Otherwise later implementation will produce isolated code that does not complete the platform lifecycle.

---

## Acceptance Criteria And Testable Outcomes

A mature Child PRD, Workflow PRD, or Screen PRD should include testable outcomes when the logic is implementation-relevant.

Examples:

- when OTP is verified, account status becomes active
- when verification is rejected, the user sees rejection reason
- when approval is approved, the correct capability can be activated
- when payment fails, order must not continue to paid fulfillment
- when shipment is delivered, the order can move toward completion
- when a reward is granted, it must not be granted again for the same goal
- when a restricted account tries an action, the action is disabled with a reason

Acceptance criteria help convert documentation into tests later.

They also help AI coding agents validate whether generated code matches the PRD.

---

## Code Translation Readiness Gate

Before treating a PRD as ready for later code translation, verify:

1. Are the main use cases clear?
2. Are commands and queries distinguishable?
3. Are core entities identified?
4. Are entity ownership boundaries clear?
5. Are state families identified?
6. Are important state transitions documented?
7. Are related events documented?
8. Are actions and permissions identified?
9. Are validation rules visible?
10. Are failure and edge cases identified?
11. Are cross-system handoffs documented?
12. Are business rules and invariants explicit?
13. Are data groups identified?
14. Are UX outputs identified?
15. Are acceptance criteria or testable outcomes available where needed?
16. Are open implementation decisions listed instead of hidden?
17. Does the PRD avoid becoming a framework-specific implementation file?
18. Does the PRD provide enough structure for a later implementation standard to translate it into code?

This gate does not mean that the PRD writes the code.

It means that the PRD contains the logic needed for code to be generated or implemented later without guessing.

---

# Traceability Rule

Every important concept introduced in a PRD must be traceable.

If an entity appears in the scenario, it should appear in the Entities Index.

If a state is implied, it should appear in State Families or State Transitions.

If an event happens, it should appear in Event Families.

If a page or screen is produced, it should appear in Pages / Sections or Screen Outputs.

If another system is affected, it should appear in Cross-System Dependencies.

If a child must detail it later, it should appear in Child PRD Routing.

If implementation must not violate it, it should appear in Technical Constraints.

Important logic must not remain hidden only inside prose.

---

# Cross-System Consistency Gate

Any PRD that mentions or affects another system must document the relationship at the correct level.

Examples:

- User Management affects Wallet eligibility.
- Shipping depends on Country Context.
- Store activation depends on Approval.
- Notifications depend on Events.
- Analytics depends on lifecycle events.
- CRM depends on drop-off and reactivation events.
- Permissions affect who can perform actions.
- Orders affect Financial, Shipping, Inventory, Notifications, and Events.
- Returns affect Orders, Wallets, Shipping, Support, and Analytics.

If the relationship is important, document it in one of:

- External Relationship Map
- Cross-System Dependencies
- Integration Anchors
- Technical Constraints
- Child PRD Routing
- Workflow handoffs

depending on the correct artifact level.

---

# Parent To Child Inheritance Gate

Before generating or revising any Child PRD, the model must identify:

- parent purpose
- parent scenario
- parent entities
- parent state families
- parent event families
- parent constraints
- parent child-routing intent
- parent cross-system dependencies
- relevant shared taxonomies
- current conversation decisions

The child must not be generated from the child name alone.

The child must clearly state what it inherits.

---

# Child To Parent Feedback Gate

A Child PRD may reveal missing parent logic.

When this happens, classify the discovery:

## Local Child Logic

Belongs only in the child.

Do not move to parent.

## Parent-Level Logic

Affects multiple children or defines section-wide behavior.

Recommend adding it to the parent.

## Platform-Level Logic

Affects multiple domains or shared primitives.

Recommend adding it to a central reference.

## Cross-System Logic

Affects another module or domain.

Recommend updating or referencing the related PRD.

The model must not silently bury parent-level discoveries inside a child.

---

# Central Reference Binding

Some standards are defined in Pazarat local numbered files and must not be redefined locally inside ordinary PRDs.

The model must account for the actual numbered Pazarat local tunnel before producing or revising important artifacts.

The files below are central references by current navigational snapshot, but the actual numbered root files in the repository remain the operational source of tunnel discovery.

## State Logic

Any PRD that introduces, changes, or depends on states must follow:

```txt
02_PLATFORM_STATE_TAXONOMY.md
```

The PRD may define local state families, but it must not contradict the central state logic.

If a PRD introduces a new state, classify it as existing, local, proposed, conflicting, or requiring taxonomy update.

## Event Logic

Any PRD that emits, consumes, displays, audits, notifies, analyzes, or automates events must follow:

```txt
03_PLATFORM_EVENT_TAXONOMY.md
```

The PRD may define local event families, but it must not contradict the central event logic.

If a PRD introduces a new event, classify it as existing, local, proposed, conflicting, or requiring event taxonomy update.

## Project Structure

Any file location, branch route, parent-child relationship, or project navigation claim must follow:

```txt
04_PROJECT_STRUCTURE_TREE_INDEX.md
```

If the repository differs from the tree, current repository evidence takes priority and the tree should be updated later.

The structure tree is a navigation index, not proof of maturity.

## Platform Identity

Any major product interpretation must align with:

```txt
01_PAZARAT_PRD_PLATFORM_IDENTITY_AND_OBJECTIVES.md
```

Pazarat must not be reduced to a generic marketplace.

## UI And Visual Generation

Any PRD, screen artifact, or visual generation request that affects interface behavior, layout, components, visual reference, design direction, reusable UI pattern, or Figma-readiness must align with:

```txt
05_UI_UX_DESIGN_SYSTEM_AND_VISUAL_GENERATION_STANDARD.md
```

PRDs should expose design implications at the correct level, but they should not invent a separate design language for every screen.

## Implementation And Code Generation Readiness

Any PRD, workflow, state/event model, or technical extraction that affects backend, frontend, API, database, service boundaries, validation, permissions, audit, event emission, or implementation planning must align with:

```txt
06_IMPLEMENTATION_ARCHITECTURE_AND_CODE_GENERATION_STANDARD.md
```

PRDs should make implementation implications visible without becoming framework-specific code files.

## Hierarchical Documentation And Shared Logic

Any parent PRD, child PRD, workflow, scenario expansion, placeholder expansion, scaffold replacement, or parent-child revision must align with:

```txt
07_PAZARAT_HIERARCHICAL_DOCUMENTATION_AND_SHARED_LOGIC_PROTOCOL.md
```

This file governs Pazarat-specific parent-child hierarchy, source scenario preservation, coverage mapping, segment discussion, anti-filler behavior, shared logic extraction, and controlled PRD evolution.

A child PRD must not be generated from the child name alone.

## Shared Primitives And Continuity Memory

Any repeated role, state, event, workflow, permission, audit, notification, table behavior, verification pattern, approval pattern, profile ownership rule, or implementation behavior that appears across multiple artifacts must align with:

```txt
08_PAZARAT_SHARED_PRIMITIVES_AND_CONTINUITY_MEMORY.md
```

If a repeated concept is not yet defined there, classify it as a shared primitive candidate.

Do not redefine shared logic differently inside every child PRD.

## Parent / Child Sequence And Cross-Artifact Routing

Any parent PRD expansion, child PRD sequencing, prerequisite ordering, cross-folder artifact reference, parent-to-parent relationship, external seed route, or child build map must align with:

```txt
10_PAZARAT_PARENT_CHILD_SEQUENCE_AND_CROSS_ARTIFACT_ROUTING_STANDARD.md
```

This file governs how to decide whether a mentioned concept becomes a local child, prerequisite child, external artifact, sibling dependency, parent-to-parent link, shared primitive candidate, taxonomy candidate, or open routing decision.

---


# Documentation Method Evolution Rule

Pazarat documentation standards must support initial construction and later evolution.

When a new feature, section, flow, child PRD, screen, integration, or post-launch enhancement is added later, the model must determine whether the change affects only the local artifact or also requires updates to parent routing, parent-to-parent relationships, shared primitives, state/event taxonomies, UI/UX standards, implementation standards, tests, or open decisions.

A change is mature only when it leaves the correct trace at the correct level.

Do not bury platform-level or parent-level changes inside a child file.

Do not promote one-time local details into global standards.

This keeps Pazarat flexible without letting future growth break the documentation architecture.

---

# Central Reference Update Rule

If a PRD reveals a missing platform-level state, event, primitive, structure route, UI pattern, implementation rule, or hierarchy rule, the model should not silently bury that discovery inside the PRD.

Classify the discovery as:

- local artifact logic
- parent-level logic
- Pazarat shared primitive candidate
- state taxonomy update candidate
- event taxonomy update candidate
- structure index update candidate
- UI standard update candidate
- implementation standard update candidate
- decision or roadmap update candidate

Then recommend or apply the correct controlled update when requested.

Do not turn every local detail into a central standard.

Do centralize repeated or governing logic that affects multiple artifacts.

---

# Entity And Ownership Standard

Not every entity needs a central taxonomy file.

Many entities are discovered from the scenario.

When documenting entities, identify:

- entity name
- meaning
- parent-level or child-level relevance
- owning module
- referenced modules
- lifecycle relationship
- state families
- events
- whether it is independent or linked
- whether ownership is local or external

Entity ownership prevents modules from swallowing each other.

Example:

A User Management PRD may reference Wallet eligibility.

But Wallet remains owned by the Financial domain.

---

# Governance Standard

When a PRD includes verification, approval, restriction, moderation, roles, policies, escalation, or security, the model must clarify:

- who owns the decision
- who can perform the action
- what state changes
- what event is emitted
- what UI must show
- what child PRD will detail it
- whether the rule is local, parent-level, platform-level, or cross-system

Governance must not remain implicit.

Verification, Approval, Restriction, Moderation, Permission, and Suspension must not be treated as the same concept.

---

# Notification And Audit Check

Whenever a PRD introduces an event, decision, approval, rejection, restriction, suspension, verification, payment, shipment, return, refund, or important lifecycle transition, the model must consider:

- Should this trigger a notification?
- Should this appear in an event timeline?
- Should this be auditable?
- Should analytics consume it?
- Should CRM consume it?
- Should support see it?
- Should permissions restrict who can see or act on it?

Not every event needs all outputs.

But every important event must be checked.

---

# UX Output Standard

When a PRD produces operational behavior, the model must consider how it appears in UX.

Possible UX outputs include:

- badges
- status indicators
- timelines
- required action panels
- filters
- saved views
- contextual actions
- disabled action reasons
- alerts
- review queues
- dashboards
- cross-system links
- empty states
- loading states
- error states

Parent PRDs record UX output families.

Child PRDs deepen local UX behavior.

Screen PRDs define exact UI.

---

# Cumulative Documentation Revision Gate

Pazarat scenarios and PRDs mature through many iterations.

The model must treat accepted or reviewed artifacts as controlled knowledge assets.

When the user adds a new idea, correction, or refinement, the model must:

- preserve previous accepted logic
- preserve accepted terminology
- preserve accepted structure
- add the new logic in the correct location
- modify only what the user requested
- avoid rewriting unrelated sections
- avoid removing earlier corrections
- avoid treating the latest note as the only instruction
- avoid generating a new unrelated version unless requested

Documentation improvement is cumulative.

It is not free-form regeneration.

---

# Patch-First Rule

For mature or reviewed artifacts, patch-first behavior is preferred.

Use patch-first behavior when:

- adding a paragraph
- adding a technical index
- correcting terminology
- adding a relationship
- adding a child route
- modifying one section
- reducing filler
- improving one explanation
- adding a missing state/event implication

A full rewrite is allowed only when:

- the user explicitly asks for a full rewrite
- the current file is raw or structurally broken
- the user approves restructuring
- patching would create confusion
- the model clearly explains why replacement is safer

---

# Revision Quality Gate

Before outputting a revised PRD, verify:

1. What is the current baseline?
2. What did the user accept?
3. What did the user reject?
4. What terminology is locked?
5. What structure is locked?
6. What new change is requested?
7. Does the change affect parent, child, sibling, or shared references?
8. Did any accepted idea disappear?
9. Did any meaning change silently?
10. Did any new logic enter without being identified?
11. Did the revision preserve traceability?
12. Did the revision reduce review burden?

If the model cannot access the current baseline, it must ask for the current file or state the limitation.

---

# Maturity Classification Rule

Before judging or rewriting a file, classify its maturity.

Possible states:

- Authentic Artifact
- Mature Draft
- Raw Reference
- Placeholder
- Duplicated Scaffold
- Empty Structural Node
- Outdated Artifact
- Conflicting Artifact

Do not treat placeholder or empty child files as failures.

Use maturity classification to decide whether to preserve, patch, expand, replace, or ask for confirmation.

---

# Parent PRD Quality Gate

Before considering a Parent PRD mature, verify:

1. Does it identify artifact identity?
2. Does it explain hierarchy position?
3. Does it explain section purpose?
4. Does it define core philosophy?
5. Does it define scope and boundaries?
6. Does it define parent-owned logic?
7. Does it identify child-owned detail?
8. Does it identify external-owned detail?
9. Does it provide operational scenario narrative?
10. Does it identify scenario segments when useful?
11. Does it define key terms?
12. Does it define governing rules?
13. Does it identify shared logic anchors?
14. Does it include a technical output index?
15. Does it identify core entities?
16. Does it define entity ownership?
17. Does it identify relationships?
18. Does it define lifecycle / journey index?
19. Does it identify flow families?
20. Does it identify state families?
21. Does it identify event families?
22. Does it identify pages / sections?
23. Does it identify UX outputs?
24. Does it identify service / module boundaries?
25. Does it identify API groups at high level?
26. Does it identify cross-system dependencies?
27. Does it identify governance outputs?
28. Does it identify data outputs?
29. Does it define technical constraints?
30. Does it route child PRDs?
31. Does it recommend child build order when meaningful?
32. Does it identify child-to-child dependencies and prerequisites?
33. Does it identify external artifact routes when mentioned concepts belong elsewhere?
34. Does it identify parent-to-parent relationships when this section affects another parent?
35. Does it separate parent from child responsibility?
36. Does it list open decisions?
37. Does it avoid becoming a technical dump?
38. Does it avoid leaving technical outputs hidden in prose?
39. Does it support future UI/UX generation?
40. Does it support future backend and frontend planning?

---

# Child PRD Quality Gate

Before considering a Child PRD mature, verify:

1. Does it identify artifact identity?
2. Does it declare parent inheritance?
3. Does it explain local purpose?
4. Does it define local scope?
5. Does it preserve parent rules?
6. Does it avoid repeating the full parent?
7. Does it identify local entities?
8. Does it identify local states?
9. Does it identify local events?
10. Does it identify actions and permissions?
11. Does it identify screens or UX outputs?
12. Does it identify data groups?
13. Does it identify API groups?
14. Does it identify dependencies?
15. Does it identify edge cases?
16. Does it identify validation notes?
17. Does it identify notifications or audit needs?
18. Does it check parent alignment?
19. Does it check sibling and cross-system relationships?
20. Does it flag missing parent-level logic when discovered?
21. Does it avoid redefining parent logic?
22. Does it avoid becoming disconnected from the parent?
23. Does it support screen PRD generation?
24. Does it support UI/UX visual generation?

---

# Screen PRD Quality Gate

Before considering a Screen PRD mature, verify:

1. Does it identify inherited parent or child logic?
2. Does it define screen purpose?
3. Does it define users / roles?
4. Does it define entry points?
5. Does it define layout zones?
6. Does it define displayed data?
7. Does it define data sources?
8. Does it define visible states?
9. Does it define actions?
10. Does it define permissions?
11. Does it define disabled action reasons?
12. Does it define empty states?
13. Does it define loading states?
14. Does it define error states?
15. Does it define filters?
16. Does it define navigation?
17. Does it define cross-system links?
18. Does it define events triggered by actions?
19. Does it define notifications or audit implications?
20. Does it define implementation notes without becoming a full backend spec?
21. Does it provide enough detail for UI/UX generation?

---

# Documentation Consistency Rule

The same documentation discipline must apply across all domains.

User Management, Shipping, Orders, Wallets, Products, Marketing, Smart Data, and System modules may have different content and different scenario segment names.

But they must share:

- scenario-first thinking
- technical output extraction
- parent / child hierarchy
- traceability
- state/event awareness
- cross-system dependency awareness
- ownership clarity
- child routing
- open decision tracking
- cumulative revision behavior

Consistency does not mean identical wording.

Consistency means complete and traceable reasoning.

---

# Anti-Generic Output Rule

The model must not produce generic PRDs that could apply to any marketplace.

Pazarat PRDs must reflect:

- multi-vendor marketplace complexity
- B2B and B2C logic
- multi-role identity
- governance-aware operations
- workflow-driven architecture
- event-aware reasoning
- state-aware systems
- operational UX
- platform scalability
- cross-system relationships
- AI-oriented documentation continuity

If the output feels generic, it is not mature.

---

# Final Rule

The model must not ask future designers, developers, product teams, or AI systems to infer critical outputs from long scenario prose.

The PRD must make important outputs explicit.

The scenario explains meaning.

The technical output index fixes outputs.

The child PRDs explain branch detail.

The workflows explain execution.

The state/event models explain lifecycle.

The screen PRDs explain interaction.

The visual references support design generation.

The implementation notes support development.

Traceability connects them all.

Pazarat documentation must become a living cognitive system for building the product, not a static document archive.