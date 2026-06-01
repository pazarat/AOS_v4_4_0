# PAZARAT NARRATIVE SEQUENCE AND SCENARIO MATURITY STANDARD

# Purpose

This file defines the Pazarat-specific standard for narrative sequence, scenario maturity, raw concept transformation, missing-link detection, and documentation-to-design-to-code continuity.

It belongs to the Pazarat project-local numbered tunnel.

It is not a general writing style guide.

It is not a replacement for the PRD cognition standard.

It is not a replacement for the hierarchical documentation protocol.

It is not a replacement for state taxonomy, event taxonomy, UI/UX standards, implementation standards, or shared primitives.

Its purpose is to ensure that Pazarat scenarios are not merely formatted.

They must be understood, sequenced, matured, completed, and translated into product logic, design logic, and implementation logic.

---

# Core Principle

A Pazarat scenario is a sequential operational journey.

It should explain how something begins, what the actor sees, what the actor chooses, what the system records, what changes, what does not happen yet, what event may be produced, what appears next, and where the responsibility moves.

The goal is not long storytelling.

The goal is not technical dumping.

The goal is precise journey construction.

A mature scenario should make missing logic visible.

A mature scenario should let product, design, engineering, and future AI understand the same journey without needing to re-interpret the raw idea from zero.

---

# What This File Owns

This file owns the Pazarat standard for:

- narrative sequence integrity
- raw concept to scenario construction
- missing operational link detection
- journey continuity
- parent-level scenario narration
- child-level scenario narration
- avoiding over-inflated concepts
- avoiding generic filler
- preserving original user meaning
- refining terminology without changing meaning
- modular scenario sections
- section-level editability
- documentation-to-design continuity
- documentation-to-code continuity
- state/event awareness inside narrative
- notification and audit awareness inside narrative
- boundary discipline between parent and child artifacts

This file does not own:

- actual project identity
- actual state definitions
- actual event definitions
- actual UI components
- actual backend architecture
- actual API contracts
- actual child PRD content
- actual workflow specifications

Those belong to their dedicated Pazarat artifacts.

---

# Narrative Sequence Integrity

Narrative sequence integrity means that every scenario should preserve the real journey order.

The model must not jump between ideas only because the concepts are related.

The model must understand the path.

A strong scenario asks:

```txt
What does the user/admin/system see?
What choice is available?
What does the actor choose?
What information is collected?
What does the system validate?
What does the system record?
What changes after success?
What appears to the actor next?
What event may be produced?
What notification may be sent?
What state may change?
What does not happen yet?
What is deferred to another step?
What is the next operational step?
Who owns the next step?
```

Not every paragraph must answer every question.

But the scenario as a whole must preserve these links.

If a link is missing and it affects product logic, design, events, notifications, states, permissions, audit, or implementation, the model should identify or complete it.


---

# Central Taxonomy Synchronization Gate

Narrative precision does not mean the model may invent project terminology.

A mature scenario must be synchronized with Pazarat central terminology before it becomes accepted documentation.

When the scenario reveals states, events, permissions, primitives, workflows, UI patterns, or implementation outputs, the model must check the relevant central Pazarat files before naming them as accepted concepts.

For states, use:

    02_PLATFORM_STATE_TAXONOMY.md

For events, use:

    03_PLATFORM_EVENT_TAXONOMY.md

For shared primitives, use:

    08_PAZARAT_SHARED_PRIMITIVES_AND_CONTINUITY_MEMORY.md

For UI/UX patterns, use:

    05_UI_UX_DESIGN_SYSTEM_AND_VISUAL_GENERATION_STANDARD.md

For implementation translation, use:

    06_IMPLEMENTATION_ARCHITECTURE_AND_CODE_GENERATION_STANDARD.md

## Synchronization Rule

The model must distinguish between:

    narrative concept
    central taxonomy term
    local child term
    proposed taxonomy candidate
    open decision

A narrative concept may appear in the story before it becomes a central term.

But once it appears in technical indexes, state tables, event tables, implementation outputs, or design outputs, it must be synchronized with the central file.

## Required Behavior

When the model detects a state-like or event-like concept in raw scenario input, it must:

1. understand the narrative meaning
2. search for the closest existing central taxonomy family
3. use the existing central term if it fits
4. map the local concept under the central term if it is local
5. classify it as proposed only if no existing family fits
6. avoid presenting proposed terms as accepted truth
7. identify whether the central taxonomy needs an update

## Example

A raw scenario may say:

    مسار البائع لم يكتمل

The model should not automatically create:

    SellerOnboardingStatus

as an accepted state family.

It should first check whether this belongs under:

    IntentStatus
    RequestStatus
    BehaviorState

Only if the concept becomes reusable across the platform and cannot fit existing families should the model propose a new state family.

## Final Rule

Scenario writing and taxonomy synchronization are not separate tasks.

A scenario is mature only when its extracted state/event terminology is aligned with central Pazarat files or clearly marked as proposed.

# Scenario Is Knowledge Construction

A scenario is not only documentation.

A scenario is a way to discover system knowledge.

When the scenario is written correctly, it reveals:

- entities
- states
- events
- actors
- permissions
- workflow steps
- validations
- notifications
- audit points
- UI surfaces
- implementation use cases
- integration handoffs
- ownership boundaries
- open decisions

Therefore, the model must not treat scenario writing as wording improvement only.

It must treat scenario writing as product reasoning.

# Scenario As Collaborative Knowledge Construction
A mature Pazarat scenario is the result of guided collaboration between user intent and domain expertise.
The model should use domain knowledge to transform rough ideas into precise, complete journeys that surface all necessary details for design and implementation.

When developing a scenario, the model should:
- ask clarifying questions about scope, actors, entry points, and outcomes
- propose the operational sequence grounded in Pazarat architecture
- suggest what states, events, permissions, and UI surfaces are needed
- recommend how the scenario connects to other platform areas
- expose gaps and open decisions explicitly
- preserve the user's intent while adding depth and completeness

The result must remain within Pazarat identity and standards, never generic or disconnected from the project context.
This is the standard for scenario-driven collaboration.

---

# Raw Concept To Mature Scenario

The user may provide raw concepts, partial thoughts, rough explanations, fragments, examples, or incomplete journeys.

The model must not merely format them.

The model must transform raw input into a mature scenario by:

1. preserving the original meaning
2. identifying the intended journey
3. discovering the actor
4. discovering the entry point
5. discovering the object being created, changed, reviewed, approved, rejected, restricted, displayed, or linked
6. identifying the current step
7. identifying the previous step if implied
8. identifying the next step if implied
9. identifying what the system records
10. identifying what state changes
11. identifying what event may be emitted
12. identifying whether a notification is expected
13. identifying whether audit is required
14. identifying which part belongs to the parent
15. identifying which part belongs to a child
16. identifying which part belongs to another module
17. identifying missing but necessary operational links
18. marking uncertain additions as proposed or open when not clearly decided

The model should complete the journey intelligently, not invent unsupported business behavior.

When a missing link is obvious from the project logic, the model may add it as a proposed or inferred operational link.

When a missing link materially changes the product, the model should mark it as an open decision or ask a focused question.

---

# Missing-Link Detection

A missing link is a small or large step that makes the scenario incomplete.

A missing link may be:

- no event after an important action
- no notification after account creation
- no next screen after registration
- no state after verification
- no handoff after approval
- no owner after store creation
- no restriction target
- no distinction between account and store
- no distinction between verification and approval
- no difference between registration and activation
- no explanation of what happens when a user abandons a flow
- no clarification of whether a route is existing or proposed
- no clarity on what belongs to a child PRD
- no UI implication for an important operational moment
- no implementation implication for a state-changing operation

Missing links are not always big paragraphs.

Sometimes one sentence completes a full system chain.

Example:

A welcome notification after account creation may look small, but it connects account creation to notification logic, event logic, user feedback, and implementation outputs.

The model must be sensitive to these small operational links.

---

# Sequence With Dependency Routing

Narrative sequence must be combined with dependency routing.

The model must ask:

- what happens first in the user or system journey?
- what knowledge must exist first for the next scenario to be mature?
- which child, sibling, parent, or external artifact owns that knowledge?
- is this a local child, prerequisite, external route, shared primitive, taxonomy candidate, or open decision?

If a scenario appears earlier in prose but depends on a later-defined concept, the model should either build the prerequisite first or mark it as a blocking dependency.

Use:

    10_PAZARAT_PARENT_CHILD_SEQUENCE_AND_CROSS_ARTIFACT_ROUTING_STANDARD.md

when converting parent narrative into child build order or cross-artifact relationship maps.

---

# Sequence Before Labels

The model must not overinflate a label or concept when the real requirement is a sequence.

For example, a seller registration path should not become a large abstract concept if the actual journey is:

1. user chooses seller registration
2. system collects base account data
3. system collects preliminary store data
4. user accepts policies
5. OTP succeeds
6. system creates Base Account
7. system records seller path signal
8. user sees dashboard continuation
9. user completes Store Opening Request later
10. verification and approval decide activation

The label is useful only if it helps the sequence.

Do not let terms such as intent, capability, lifecycle, or status dominate the narrative when the journey itself is what needs to be clear.

Use technical terms to clarify meaning.

Do not let technical terms replace the journey.

---

# Narrative Granularity

Scenario detail must be balanced.

A scenario should include enough detail to preserve the journey and expose product logic.

A scenario should not include so much detail that it becomes the child PRD, screen PRD, database design, or API contract.

## Parent Scenario Granularity

A parent scenario should define:

- root journey
- major stages
- major actors
- root entities
- ownership boundaries
- state families
- event families
- child route candidates
- cross-system relationships
- design-ready output families
- implementation-ready output roots

A parent scenario should not define:

- every field rule
- every screen component
- every button behavior
- every validation message
- every API payload
- every database column
- every exact event payload
- every child acceptance criterion

## Child Scenario Granularity

A child scenario should define:

- inherited parent context
- local entry point
- local actor
- local workflow
- local states
- local events
- local permissions
- local validations
- local audit and notification implications
- local UI/UX bridge
- local implementation bridge
- local acceptance outcomes
- local open decisions

A child scenario should not redefine the full parent.

It should specialize one branch.

---

# Section-Level Modularity

A mature scenario should be organized into clear sections.

Each section should represent one operational segment.

A section should be editable without damaging the whole scenario.

This means:

- one section should have a clear purpose
- one section should describe one journey segment or one parent-level rule
- changes should be local when possible
- the section should state its boundary
- the section should not hide unrelated logic
- repeated details should move to shared primitives or child artifacts when needed

Good sectioning makes the scenario easier to revise.

Bad sectioning makes every change risky.

---

# Narrative Formula

The model may use this mental formula when constructing scenario paragraphs:

```txt
Situation
→ Choice / Trigger
→ Collected or Used Information
→ System Validation
→ System Record
→ Result
→ State / Event / Notification
→ Boundary
→ Next Step
```

This is not a rigid paragraph template.

It is a reasoning standard.

The final prose may be natural and readable, especially when the repository uses Arabic narrative with English technical terms.

But the logic behind the paragraph should preserve the formula.

---

# Arabic Narrative With English Technical Terms

Pazarat may use Arabic narrative for clarity and discussion.

Technical terms should often remain in English when they preserve exact project meaning.

Examples:

- `Base Account`
- `CountryContext`
- `OTP`
- `PolicyAgreement`
- `RegistrationPath`
- `Seller Registration Path`
- `StoreOpeningRequest`
- `VerificationTemplate`
- `VerificationCase`
- `ApprovalCase`
- `AccountCapability`
- `SellerCapability`
- `Restriction`
- `Event`
- `Notification`
- `AuditLog`
- `UserProfile`

Do not translate technical identifiers in a way that changes meaning.

Use Arabic to explain the journey.

Use English terms to stabilize concepts.

---

# Preserve Meaning While Improving Structure

When rewriting or maturing a scenario, the model must preserve the intended meaning.

The model may improve:

- order
- sectioning
- terminology
- missing links
- boundaries
- traceability
- technical extraction
- design bridge
- implementation bridge

The model must not change the core meaning without identifying the change.

The model must not remove an idea merely because it is raw.

The model must not replace a clear user journey with generic product language.

The model must not add unsupported business behavior as if it were accepted truth.

---

# Do Not Over-Polish Raw Logic

Raw user language may carry important project meaning.

The model should not over-polish it until the operational meaning is extracted.

Before rewriting raw input, identify:

- what the user is trying to explain
- what sequence is implied
- what distinction matters
- what entity is being protected
- what state or event may be hidden
- what step may be missing
- what the user fears losing
- what must be preserved in the parent or child

After extraction, the model may rewrite in cleaner project language.

But the cleaned version must remain faithful to the raw meaning.

---

# Scenario-To-Technical Extraction

Every mature scenario should allow extraction of technical outputs.

From a scenario, the model should be able to identify:

- entities
- data groups
- ownership
- states
- events
- commands
- queries
- validations
- permissions
- audit requirements
- notification triggers
- integration handoffs
- failure cases
- acceptance outcomes
- future child artifacts
- parent update candidates

If these cannot be extracted, the scenario is likely too vague.

The answer is not always to add length.

The answer may be to add one missing operational sentence.

---

# Scenario-To-Design Extraction

Every mature scenario should allow extraction of UI/UX outputs.

From a scenario, the model should be able to identify:

- entry screen
- actor role
- primary action
- form or table needs
- displayed state
- status badge needs
- empty state
- next action card
- confirmation message
- notification feedback
- review queue
- timeline
- action panel
- disabled action reason
- cross-system navigation
- visual hierarchy

If a designer cannot understand what must appear next, the sequence may be incomplete.

Design should translate documented journey logic, not invent it.

---

# Scenario-To-Code Extraction

Every mature scenario should allow extraction of implementation outputs.

From a scenario, the model should be able to identify:

- use cases
- commands
- queries
- services
- state transitions
- event emissions
- validation rules
- permission checks
- audit logging
- notification dispatch
- background jobs
- duplicate-prevention needs
- consistency boundaries
- failure handling
- acceptance tests

If a developer must guess the behavior, the scenario is not mature enough.

Implementation should translate documented product logic, not invent it.

---

# Scenario-To-Documentation-Contract Gate

A scenario is not mature merely because it is readable.

For Pazarat, the scenario must also be structured so it can feed the PRD documentation contract.

After writing or revising an important scenario, the model must check whether the scenario exposes enough signal for:

- parent or child ownership
- sequence and dependency routing
- state and event extraction
- permission and visibility extraction
- validation and edge-case extraction
- UI/UX translation
- ASP.NET / PostgreSQL / Next.js implementation translation
- cross-artifact impact tracking
- future maintenance notes

If a scenario contains a concept that affects another child, parent, workflow, screen, implementation note, or taxonomy, the relationship must be routed rather than left hidden inside prose.

This gate is governed by:

```txt
11_PAZARAT_PRD_DOCUMENTATION_AND_IMPLEMENTATION_TRANSLATION_CONTRACT.md
```

---

# Parent Scenario Standard

A Pazarat parent scenario should:

- explain the root journey
- preserve sequence integrity
- identify root entities
- explain ownership boundaries
- identify child routes
- identify state families
- identify event families
- identify shared primitives
- identify design output families
- identify implementation output roots
- avoid child-level overload
- avoid generic marketplace filler
- avoid concept inflation

The parent scenario is a map.

It should make children easier to generate, not unnecessary.

---

# Child Scenario Standard

A Pazarat child scenario should:

- inherit from parent
- explain local purpose
- preserve local sequence
- define local workflow
- align states with state taxonomy
- align events with event taxonomy
- use shared primitives
- define permissions and visibility
- define audit and notification implications
- define data/entity outputs
- define UI/UX bridge
- define implementation bridge
- define acceptance outcomes
- preserve open decisions
- report parent update candidates

The child scenario is a focused operational artifact.

It should make design and implementation possible.

---

# From Raw Ideas To Scenario

When the user provides raw ideas, the model should not wait for a perfect scenario.

The model should help build the scenario.

The model should:

1. identify the likely journey
2. group ideas by sequence
3. separate parent logic from child detail
4. detect missing steps
5. preserve the user’s terms when meaningful
6. improve terminology when needed
7. connect steps to state/event logic
8. connect steps to UI/UX implications
9. connect steps to implementation implications
10. mark assumptions
11. keep open questions
12. produce a structured scenario draft

The model should not demand that the user provide perfect sequencing.

Building sequence from raw discussion is part of the model’s role.

---

# Missing-Link Completion Rule

When a missing link is necessary for scenario maturity, the model may add it in one of three ways.

## Confirmed Link

Use when the repository or conversation already supports it.

## Inferred Link

Use when the link is strongly implied by the journey and does not materially change business policy.

## Proposed Link

Use when the link is useful but requires user or project decision.

Examples:

- welcome notification after account creation may be inferred or proposed depending on notification standards
- abandoned seller path reminder may be proposed if CRM/Automation strategy is not confirmed
- account restriction audit log may be strongly required if audit standards support it
- exact event payload must remain proposed until event taxonomy or implementation standards confirm it

Do not silently convert proposed links into accepted truth.

---

# Boundary Rule

Every scenario segment should clarify boundaries when needed.

Boundary questions:

- Does this belong to the parent or a child?
- Does this belong to another module?
- Is this a state taxonomy issue?
- Is this an event taxonomy issue?
- Is this a UI pattern issue?
- Is this an implementation detail?
- Is this a shared primitive?
- Is this an open decision?

Boundary discipline prevents parent files from becoming overloaded and prevents child files from redefining parent logic.

---

# Anti-Filler Rule

Detailed narrative is not the same as filler.

A paragraph is useful when it clarifies:

- sequence
- actor
- system behavior
- state
- event
- entity
- boundary
- ownership
- design implication
- implementation implication
- open decision

A paragraph is filler when it:

- repeats generic marketplace value
- restates broad goals without operational meaning
- explains obvious concepts without project effect
- copies parent logic into children without specialization
- adds design or code claims unsupported by scenario logic
- expands prose without improving sequence

Pazarat scenarios may be detailed.

They must not be padded.

---

# Failure Signals

Narrative sequence failures include:

- formatting a raw idea without maturing it
- losing the original user meaning
- changing sequence without reason
- skipping a step that affects state, event, design, or code
- overinflating a label such as intent into the main concept
- turning a scenario into generic marketplace prose
- turning a scenario into a dry technical checklist
- hiding event or notification implications
- failing to distinguish what happens now from what happens later
- failing to distinguish account, capability, store, request, and approval
- making the parent contain child-level details
- making the child redefine the parent
- generating design from screen name instead of scenario logic
- generating code from assumptions instead of documented behavior
- not marking inferred or proposed links

When failure occurs, rebuild the scenario from sequence, not from headings.

---

# Quality Gate

Before accepting a Pazarat scenario as mature, verify:

1. Is the journey sequence clear?
2. Is the actor clear?
3. Is the entry point clear?
4. Is the collected information clear?
5. Is the system validation clear enough for the artifact level?
6. Is the system record clear?
7. Is the result clear?
8. Are state implications visible?
9. Are event implications visible?
10. Are notification implications visible when relevant?
11. Are boundaries clear?
12. Are child responsibilities clear?
13. Are design implications extractable?
14. Are implementation implications extractable?
15. Are open decisions preserved?
16. Are inferred additions marked when needed?
17. Is the scenario detailed without filler?
18. Is the original meaning preserved?

If these are weak, improve the scenario before using it as design or code source.

---

---

# Programmatic Narrative Weaving Handoff

When raw input is conceptually rich but repetitive, nonlinear, or technically mixed, the model must not only organize it into headings.

It must first translate the raw idea into programmatic semantics: stable identity, relationship spine, configurable value, runtime fact, filtered view, or policy matrix.

For this deeper gate, use:

    15_PAZARAT_RAW_TO_PROGRAMMATIC_NARRATIVE_WEAVING_STANDARD.md

This handoff is mandatory when the scenario involves country context, user identity, account relationships, financial/shipping values, cross-country behavior, or any raw explanation where copying the user's narrative order would produce weak or repetitive prose.

A scenario that is well-sectioned but not woven from correct programming/database meaning is not mature enough for Pazarat documentation.

# Final Principle

Pazarat scenarios are not written only to be read.

They are written to build the product.

A good scenario preserves human meaning, exposes system logic, creates design clarity, supports implementation, and allows future AI to continue the project without restarting from raw conversation.

The model must build sequence from raw ideas, detect missing links, mature the journey, preserve boundaries, and translate the result into traceable product knowledge.
