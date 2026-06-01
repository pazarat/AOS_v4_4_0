# PAZARAT 360-DEGREE ENGINEERING METHOD

# Purpose / الهدف


# 0A. 360 Logical Measurement Secret / سر القياس المنطقي داخل 360

360 is not only cross-direction awareness.

It is a measurement discipline.

Before authoring any Pazarat scenario, PRD, translation rule, environment standard, database contract, API contract, UI brief, or code output, the model must measure the candidate result against:

```txt
Upstream truth: what source owns this logic?
Downstream consumer: what layer must consume it next?
Environment fit: what stack, architecture, repository structure, scale, and delivery path must run it?
Extractable logic: what actors, roles, permissions, entities, fields, states, events, workflows, data, APIs, UI behavior, and tests must be derivable?
Contradiction: where does one direction make another weak, impossible, or unsafe?
Repair owner: which parent, child, taxonomy, primitive, standard, environment decision, or project decision must be strengthened?
```

A readable scenario that cannot be translated into implementation logic is not mature.

A translation standard that does not understand the documentation shape and engineering environment is not mature.

An engineering environment standard chosen without measuring Pazarat scale, modular boundaries, domain complexity, and delivery reality is not mature.

This is why Pazarat documentation templates must have stable identity and variable content: the stable identity comes from downstream measurement, while the variable content comes from the specific module truth.


This file defines the highest project-local engineering method for Pazarat.

It makes the whole Pazarat tunnel serve one operating loop:

```txt
Documentation Standards
↔ Implementation Translation Standards
↔ Data / Database / API Contract Standards
↔ Engineering Environment Standards
↔ Code Practice / Implementation Canon
↔ Testing / Quality Gates
↔ Pazarat Platform Objective
```

منهج 360 درجة هو القاعدة الحاكمة التي تجعل كل معايير التوثيق، والترجمة إلى كود، وبيئة التطوير تعمل كحلقة واحدة لخدمة مشروع بازارات الضخم، لا كملفات منفصلة.

This method is not an optional explanation.

It is a binding project-local operating method for any meaningful Pazarat PRD, child PRD, workflow, screen, implementation contract, code generation, database design, API design, frontend output, test plan, or environment setup.

---

# 1. Highest 360 Rule / القاعدة العليا

No Pazarat artifact may be treated as complete because it satisfies only one side of the work.

A Pazarat artifact is mature only when it is checked through the full 360 loop:

```txt
1. Documentation Direction
   Does the artifact capture the scenario, hierarchy, ownership, lifecycle, relationships, states, events, permissions, validations, and testable behavior?

2. Implementation Translation Direction
   Can the documented logic be translated into use cases, commands, queries, APIs, database structures, frontend behavior, events, audit records, and tests without guessing?

3. Data / Database / API Contract Direction
   Does the artifact expose stable identities, relationship spines, configurable values, runtime facts, persistence implications, endpoint families, command/query separation, and contract boundaries without contradicting later implementation?

4. Engineering Environment Direction
   Will the translated outputs be generated inside the accepted Pazarat stack, repository structure, code architecture, database migration model, CI/CD gates, and deployment pathway?

5. Code Practice Canon Direction
   Does the output obey the accepted implementation practice rules for DDD, modular monolith structure, EF Core/PostgreSQL, migrations, SignalR/realtime, Redis, outbox, validation, authorization, errors, audit, observability, and tests instead of generating code from a stack name only?

6. Pazarat Platform Direction
   Does the result preserve large-scale platform coherence, cross-module consistency, shared primitives, lifecycle dependencies, and future maintainability?
```

If any direction is weak, incomplete, contradictory, or disconnected, the model must classify the gap and repair the owning artifact or standard before producing production-oriented code.

---

# 2. 360 Is A Rotating System, Not A Linear Checklist / 360 حلقة دوران وليس قائمة خطية

The active 360 directions and reinforcing engineering lenses must be written to reflect each other.

Documentation standards must not be generic templates.

They must be designed so that implementation translation can extract logic from them.

Implementation translation standards must not invent code structure independently.

They must use the documented scenario logic and the accepted engineering environment.

Engineering environment standards must not be isolated tool lists.

They must define the real stack, structure, testing, migration, and delivery rules that code generation must obey.

Correct flow:

```txt
Raw Input
→ Scenario Maturity
→ Parent/Child Documentation
→ Central Taxonomy / Primitive Alignment
→ Translation Contract
→ Engineering Environment Alignment
→ Code / Database / API / Frontend / Tests
→ Validation Against Documentation
→ Feedback To Parent, Child, Taxonomy, Primitive, Or Environment Standards
```

The loop may rotate backward when implementation exposes missing documentation, missing shared primitives, missing state/event terms, or missing environment standards.

---

# 2.1 360 Is Expandable By Engineering Lens / 360 قابل للتعزيز بعدسات هندسية

The 360 method is not limited to a fixed count of directions.

Its essence is rotational coherence.

When Pazarat reveals that a missing engineering lens repeatedly causes weak scenarios, bad translation, or unsafe code generation, that lens must be added as a central reinforcing standard instead of being treated as an afterthought.

Current reinforcing lenses include:

```txt
15_PAZARAT_RAW_TO_PROGRAMMATIC_NARRATIVE_WEAVING_STANDARD.md
16_PAZARAT_DATA_MODEL_DATABASE_API_AND_ENDPOINT_STANDARD.md
18_PAZARAT_CODE_PRACTICE_AND_IMPLEMENTATION_CANON.md
```

These lenses do not fragment the method.

They strengthen the rotation by forcing each artifact to answer deeper questions before it reaches code.

A raw scenario must therefore be checked not only for prose quality, but also for:

- programmatic backbone
- database relationship reality
- API/endpoint extractability
- environment fit
- platform-wide consistency

If any lens exposes a contradiction, the model must rotate backward and repair the owning scenario, PRD, standard, or implementation contract.

---

# 3. Project-Wide Central Reference Rule / قاعدة المرجع المركزي المشترك

The 360 method depends on central project files for shared concepts.

No direction may independently define shared states, events, primitives, roles, permissions, UI patterns, implementation patterns, lifecycle terms, or reusable names when a central file exists or should exist.

Central files act as project-wide extensions consumed by all three directions.

Current central files include:

```txt
02_PLATFORM_STATE_TAXONOMY.md
03_PLATFORM_EVENT_TAXONOMY.md
05_UI_UX_DESIGN_SYSTEM_AND_VISUAL_GENERATION_STANDARD.md
08_PAZARAT_SHARED_PRIMITIVES_AND_CONTINUITY_MEMORY.md
13_PAZARAT_360_DEGREE_ENGINEERING_METHOD.md
14_PAZARAT_ENGINEERING_ENVIRONMENT_AND_STACK_STANDARD.md
15_PAZARAT_RAW_TO_PROGRAMMATIC_NARRATIVE_WEAVING_STANDARD.md
16_PAZARAT_DATA_MODEL_DATABASE_API_AND_ENDPOINT_STANDARD.md
18_PAZARAT_CODE_PRACTICE_AND_IMPLEMENTATION_CANON.md
```

When a PRD introduces a state, event, shared behavior, permission pattern, audit behavior, table behavior, form pattern, validation pattern, or implementation convention, the model must first check the central owner.

If no central owner exists, classify the item as one of:

```txt
Existing central reference
Local extension under existing central reference
Proposed central reference candidate
Conflicting term
Open centralization decision
```

The model must not create multiple names for the same state, event, primitive, permission, endpoint style, database pattern, or UI behavior across different directions.

---

# 4. Central Taxonomy Binding / ربط الحالات والأحداث مركزياً

State and event terms are never owned separately by documentation, translation, and code.

They are shared project language.

## State Binding

All PRDs, workflow artifacts, screen artifacts, implementation contracts, database models, APIs, frontend displays, tests, and generated code must use `02_PLATFORM_STATE_TAXONOMY.md` as the first source for state family and state terminology.

A Child PRD may deepen local states, but it must map them to an existing state family or mark a proposed taxonomy candidate.

## Event Binding

All triggers, lifecycle events, audit actions, notifications, analytics signals, automation hooks, integration effects, and generated event names must use `03_PLATFORM_EVENT_TAXONOMY.md` as the first source for event family and event terminology.

A Child PRD may introduce local event candidates, but it must classify them under an existing event family or mark a proposed event taxonomy candidate.

## Shared Primitive Binding

All repeated roles, permissions, verification logic, approval logic, audit patterns, notification patterns, table behavior, form patterns, validation packs, UI patterns, or backend operation patterns must synchronize with `08_PAZARAT_SHARED_PRIMITIVES_AND_CONTINUITY_MEMORY.md` before being duplicated.

---

# 5. Parent And Child Documentation Difference / فرق توثيق الأب والابن

The documentation direction contains multiple artifact depths.

A Parent PRD and a Child PRD both belong to the documentation direction, but they do not use the same depth or the same template responsibility.

## Parent PRD Responsibility

A Parent PRD defines:

- section identity
- platform role
- scope and boundaries
- parent-level scenario
- child map
- child build order
- parent-to-parent relationships
- high-level state/event families
- shared primitive candidates
- routing ledger
- implementation-readiness notes at parent depth

A Parent PRD must guide all children but must not absorb child-local detail.

## Child PRD Responsibility

A Child PRD defines:

- inherited parent context
- local scenario
- local actors and permissions
- local fields and validation
- local state usage and transitions
- local events emitted or consumed
- local UI behavior
- backend/API implications
- database implications
- frontend implications
- acceptance criteria and tests
- sibling and parent feedback candidates

A Child PRD is more detailed because it is closer to implementation translation.

## Sub-Child / Workflow / Screen Responsibility

When child logic is still too complex, the child must route distinct forms, screens, advanced filters, workflows, modals, table behavior, or reusable local patterns to sub-child, workflow, or screen artifacts instead of burying complexity in prose.

---

# 6. Direction One: Documentation Standard Obligations / الاتجاه الأول

Documentation standards must be authored so that they can feed translation.

They must preserve:

- hierarchy and ownership
- narrative scenario sequence
- actors and permissions
- entities and data implications
- states and state transitions
- events and event triggers
- shared primitive candidates
- cross-artifact relationships
- parent/child inheritance
- child-to-child dependencies
- UI and UX implications
- API and backend implications
- database implications
- acceptance criteria
- testing implications
- open decisions and uncertainty classification

A documentation standard fails the 360 method if it produces readable prose that cannot later support code extraction.

---

# 7. Direction Two: Implementation Translation Obligations / الاتجاه الثاني

Implementation translation must consume the documented scenario and central references.

It must derive only what the documentation supports, including:

- use cases
- commands
- queries
- handlers
- policies
- validators
- domain entities
- value objects
- state transition rules
- domain events
- audit records
- notification effects
- API operations
- DTOs
- database tables
- relationships
- constraints
- indexes
- migrations
- frontend routes
- pages
- components
- forms
- tables
- empty/loading/error/blocked states
- tests

It must not invent missing behavior from general marketplace assumptions, UI labels, or raw feature names.

When translation discovers a missing parent rule, child rule, state family, event family, shared primitive, or environment rule, it must report the missing owner and produce the smallest sufficient repair.

---

# 8. Direction Three: Data / Database / API Contract Obligations / اتجاه قواعد البيانات والعقود

Data/database/API contract standards make the scenario testable against system reality before code generation.

They must govern:

- stable identities and aggregate/entity candidates
- relationship spines and foreign-key implications
- configurable values versus runtime facts
- historical snapshots and versioning needs
- query/read-model behavior and filters
- commands, queries, endpoint families, DTOs, and OpenAPI implications
- persistence constraints, indexes, migrations, and seed data
- permissions, audit, events, and side effects attached to endpoints

The accepted Pazarat data/API extraction standard is owned by:

```txt
16_PAZARAT_DATA_MODEL_DATABASE_API_AND_ENDPOINT_STANDARD.md
18_PAZARAT_CODE_PRACTICE_AND_IMPLEMENTATION_CANON.md
```

This direction is activated whenever scenario wording implies entities, storage, relationships, dashboard filters, forms, endpoint operations, commands, queries, migrations, or OpenAPI contracts.

It must feed back into documentation if the prose describes false ownership, false relationships, impossible endpoints, or missing historical records.

---

# 9. Direction Four: Engineering Environment Obligations / الاتجاه الرابع

Engineering environment standards define the actual code world into which translated outputs are generated.

They must govern:

- editor and workstation setup
- repository and solution structure
- backend platform and framework
- frontend platform and framework
- database platform
- migration model
- API contract model
- testing tools
- code quality gates
- security standards
- observability
- GitHub workflow
- CI/CD
- deployment readiness
- versioning
- maintenance and upgrade policy
- forbidden deviations

The accepted Pazarat engineering environment is owned by:

```txt
14_PAZARAT_ENGINEERING_ENVIRONMENT_AND_STACK_STANDARD.md
```

Code generation must not use any framework, language, package structure, database pattern, or deployment model that conflicts with that file unless the user explicitly requests a stack reconsideration or ADR.

---

# 10. Direction Five: Pazarat Platform Objective / الاتجاه الخامس

The fifth direction is the actual project target: Pazarat as a large, complex, interconnected platform.

The 360 method must preserve platform-scale consistency.

It must prevent:

- isolated endpoints that ignore lifecycle logic
- database tables derived only from UI labels
- frontend screens that expose unauthorized actions
- PRD children that redefine parent logic
- duplicate state or event naming
- duplicated shared components
- untracked cross-module dependencies
- code generated outside the accepted stack
- tests disconnected from acceptance criteria
- deployment paths not aligned with the environment standard

Every local artifact should make the next layer safer, not merely longer.

---

# 11. 360 Stop And Repair Rule / قاعدة الإيقاف والإصلاح

When the model detects that one side of the loop cannot safely continue, it must not hide the weakness.

It must stop the unsafe action and classify the gap:

```txt
Documentation gap
Parent/child routing gap
Central taxonomy gap
Shared primitive gap
Translation gap
Engineering environment gap
Implementation contract gap
Testing gap
Maintenance impact gap
Conflict with accepted project truth
```

Then it must choose the smallest useful repair:

- update the owning PRD
- add a child/sub-child/workflow/screen artifact
- update the state taxonomy
- update the event taxonomy
- update shared primitives
- update the implementation translation contract
- update the engineering environment standard
- update the runtime gates
- produce an implementation contract instead of code
- classify the issue as open when a decision is required

---

# 12. 360 Code Generation Rule / قاعدة توليد الكود

No production-oriented Pazarat code may be generated from a raw feature name, isolated UI description, incomplete child PRD, or undocumented assumption.

Any serious code generation must pass through:

```txt
Relevant Pazarat Standards
→ Central State/Event/Primitive Alignment
→ Parent PRD
→ Child PRD or Workflow/Screen Artifact when needed
→ PRD Documentation And Implementation Translation Contract
→ Implementation Architecture Standard
→ Engineering Environment Standard
→ Generated Code / Database / API / Frontend / Tests
→ Validation Against Source Documentation
```

Prototype or exploratory code must be clearly labeled as prototype and must not be presented as production-ready project implementation.

---

# 13. 360 Validation Checklist / قائمة تحقق 360

Before delivering a major Pazarat artifact, implementation contract, or code-oriented output, verify:

- [ ] Does the artifact inherit from the correct parent or owner?
- [ ] Does it use central state taxonomy terms or classify new state candidates?
- [ ] Does it use central event taxonomy terms or classify new event candidates?
- [ ] Does it check shared primitives before duplicating behavior?
- [ ] Does it distinguish parent, child, sub-child, workflow, screen, and implementation depth?
- [ ] Can implementation translation derive use cases, data, API, UI, and tests without guessing?
- [ ] Does it pass the raw-to-programmatic narrative weaving standard instead of merely copying raw order?
- [ ] Does it identify stable identities, relationship spines, configurable values, runtime facts, command/query needs, and endpoint families at the appropriate artifact depth?
- [ ] Is the output aligned with ASP.NET/.NET, PostgreSQL, Next.js, and the accepted engineering environment?
- [ ] Are cross-artifact dependencies and feedback candidates recorded?
- [ ] Are unsupported assumptions classified as proposed or open?
- [ ] Does the result serve Pazarat platform coherence, not a generic marketplace pattern?

If the answer is no, repair before treating the output as complete.

---

# 14. Method Evolution Rule / قاعدة تطوير المنهج

The 360 method may evolve when Pazarat reveals new shared logic.

When repeated logic appears across multiple branches, the model must decide whether it belongs to:

- state taxonomy
- event taxonomy
- shared primitives
- UI/UX standard
- implementation architecture standard
- engineering environment standard
- runtime gates
- a new central standard
- local child ownership only

Useful repetition must be preserved until the shared objective is safely centralized.

Harmful duplication must be consolidated only after the central owner is strengthened.

---

# 12. Pazarat Reality Calibration Lens / عدسة القياس على واقع بازارات

The Pazarat 360 method must measure every raw scenario, PRD, repair, translation, and implementation decision against the current Pazarat project reality.

Pazarat reality includes:

- platform objective and marketplace operating model;
- admin dashboard structure;
- business, user management, financial, operations, governance, marketing, smart data, and system modules;
- state and event taxonomies;
- shared primitives;
- local numbered standards;
- current parent/child PRD hierarchy;
- accepted implementation stack and environment;
- data, database, API, and endpoint standards;
- lifecycle dependencies between users, stores, products, orders, payments, shipping, notifications, invoices, returns, reports, permissions, and audit behavior.

The model must not require the user to restate every Pazarat capability inside every raw scenario.

If a scenario naturally reaches delivery completion, approval, payment, refund, verification, publication, suspension, or another lifecycle transition, the model must consider the relevant Pazarat sections that already exist.

For example:

- order delivery completion may imply order status, shipment status, notification events, invoice or receipt visibility, settlement or wallet implications, analytics/reporting signals, and audit logs;
- seller approval may imply account capability, verification state, store status, role/permission updates, notification, audit, and dashboard visibility;
- country activation may imply registration visibility, market visibility, verification templates, tax/commission/shipping configurations, geo structure, interaction matrix, agency context, and downstream child routing.

The model must include the link when it is lifecycle-critical at the current artifact depth.

The model must route it to a child, sibling, central primitive, taxonomy, or implementation contract when it would bloat the current artifact.

The model must not invent final Pazarat business policy from inference alone.

It must classify additions as:

```txt
confirmed Pazarat truth
strong Pazarat inference
recommended lifecycle completion
open Pazarat decision
conflict or risk
```

This lens binds the local Pazarat method to the general orchestration rule:

```txt
01_PROJECT_ORCHESTRATION/21_PROJECT_REALITY_CALIBRATION_AND_GOLDEN_SYNTHESIS_METHOD.md
```

A Pazarat scenario is not mature because it is well divided into headings.

It is mature when its narrative, ownership, lifecycle, data model, API implications, environment fit, and project-wide module reality all converge.


---

# Incomplete Truth Maturity Lens / عدسة إنضاج الحقيقة الناقصة

A documented Pazarat source can be authoritative and still incomplete for a requested operation.

This is different from a normal gap.

- A gap may mean that no source exists.
- Incomplete truth means that a source exists, has authority, but lacks enough maturity, detail, consistency, downstream extractability, or project-scale fit to safely support production-oriented execution.

The model must not ignore incomplete truth. It must not obey it blindly when higher Pazarat truth requires more. It must not invent over it.

Required behavior:

```txt
1. Locate the owner file or decision.
2. Compare it to higher Pazarat truth and the active 360 direction.
3. Classify the source: accepted truth / incomplete truth / missing truth / conflicting truth / proposed repair.
4. Identify missing dimensions.
5. Propose owner repair or explicit decision.
6. Block production-oriented execution until the repair is accepted or the risk is explicitly recorded.
```

Discovery may propose repairs. Execution must obey accepted Pazarat truth only.

---

# Code Practice Canon Lens / عدسة ممارسات الكود

Engineering environment defines the stack. It does not fully define how code must be written.

Any Pazarat production-oriented code, API contract, database migration, realtime channel, background worker, authorization rule, validation strategy, test plan, or observability output must rotate through:

```txt
18_PAZARAT_CODE_PRACTICE_AND_IMPLEMENTATION_CANON.md
```

If the stack standard says what tool is used but the code practice canon does not yet define how to use it for the requested operation, classify the code practice area as incomplete truth and repair the canon before production-oriented execution.
