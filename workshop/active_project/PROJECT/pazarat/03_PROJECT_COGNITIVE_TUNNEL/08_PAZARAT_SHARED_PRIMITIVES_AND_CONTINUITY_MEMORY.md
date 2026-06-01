# PAZARAT SHARED PRIMITIVES AND CONTINUITY MEMORY

# Purpose

This file defines and preserves Pazarat shared primitives, reusable logic, repeated patterns, and continuity rules that affect multiple Pazarat artifacts.

It belongs to the Pazarat project-local numbered tunnel.

It is not a general project orchestration file.

It is not a cognitive runtime file.

It is not a replacement for Pazarat identity, state taxonomy, event taxonomy, structure index, UI standard, implementation standard, or hierarchical documentation protocol.

Its purpose is to prevent repeated Pazarat concepts from being redefined inconsistently across parent PRDs, child PRDs, dashboard modules, workflows, UI artifacts, and implementation notes.

Shared primitives should make Pazarat easier to document, implement, audit, and extend.


---

# 360 Central Primitive Rule / قاعدة العناصر المركزية داخل 360

Shared primitives are central extensions of the Pazarat 360-degree engineering method.

They must be consumed by documentation, implementation translation, and generated code.

A repeated role, permission, verification rule, approval behavior, audit behavior, notification behavior, table behavior, form behavior, validation pack, backend operation pattern, or UI pattern must not be redefined separately in parent PRDs, child PRDs, implementation contracts, API plans, database plans, frontend components, or tests.

When such shared logic appears, classify it as:

```txt
Existing shared primitive
Local extension of existing primitive
Proposed shared primitive candidate
Conflicting primitive
Open centralization decision
```

This rule exists so the 360 loop does not succeed at endpoint/database consistency while failing at state, event, permission, audit, UI, or validation consistency.

---

# Core Principle

If a concept, rule, flow, state, event, permission, UI behavior, or implementation assumption appears across multiple Pazarat artifacts, it should be treated as a shared primitive candidate.

If accepted, it should become a reusable project-local primitive.

The model must not redefine the same Pazarat logic differently in every child PRD.

The model must reference or inherit shared primitives where appropriate.

Shared primitives preserve project continuity.

---

# Local Tunnel Position

This file is part of the Pazarat local numbered tunnel.

The Pazarat local tunnel is discovered from the actual numbered root files directly inside the Pazarat project folder.

Any root file directly inside:

    02_MY_PROJECT/pazarat/

that starts with a numeric prefix from `00` to `99` is part of the Pazarat local tunnel unless clearly obsolete, backup, temporary, unrelated, or outside active project scope.

The model must not rely only on a hardcoded list of local tunnel files.

Numeric order determines tunnel traversal order.

File name suggests responsibility.

File content confirms actual purpose.

The list below is only a navigational snapshot for readability and review.

If additional numbered root files exist in the actual repository, they are part of the local tunnel even if not listed here yet.

If this list mentions a file that does not exist, the model must not assume it exists.

Current navigational snapshot:

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
    99_PAZARAT_PROJECT_REINFORCEMENT_MEMORY.md

---

# What This File Owns

This file owns Pazarat-specific shared primitive memory.

It defines:

- accepted shared primitive categories
- primitive candidate handling
- repeated logic detection
- shared role and actor primitive guidance
- user lifecycle primitive guidance
- verification primitive guidance
- approval primitive guidance
- permission primitive guidance
- audit primitive guidance
- notification primitive guidance
- dashboard action primitive guidance
- state and event primitive alignment
- UI primitive alignment
- implementation primitive alignment
- parent-child inheritance of shared logic
- anti-duplication behavior
- primitive update discipline

This file does not own:

- complete platform identity
- full state taxonomy
- full event taxonomy
- full UI design system
- full implementation architecture
- all module-specific PRD details
- all workflow details
- all current implementation decisions

Those remain in their dedicated Pazarat files or module artifacts.

---

# Primitive Status Model

A Pazarat primitive may have one of these statuses.

## Candidate

A repeated pattern has been noticed, but it is not yet accepted as canonical.

## Provisional

The primitive is useful for current documentation but still needs validation.

## Accepted

The primitive is accepted by conversation, repository standard, or project decision.

## Active

The primitive currently governs future Pazarat artifacts.

## Local

The primitive applies only to a branch, module, dashboard, or artifact family.

## Project-Wide

The primitive applies across Pazarat.

## Superseded

The primitive has been replaced by a newer definition.

## Conflicting

Multiple definitions exist and require resolution.

When status is unclear, treat the primitive as candidate or provisional, not accepted.

---

# Primitive Definition Pattern

When defining a Pazarat primitive, use enough structure to make it reusable.

A useful primitive may include:

- Primitive name
- Primitive type
- Status
- Scope
- Definition
- Applies to
- Does not apply to
- Related states
- Related events
- Related roles
- Related artifacts
- UI implications
- Implementation implications
- Audit implications
- Notification implications
- Open questions

Not every primitive needs every field.

Use the amount of detail appropriate to its importance.

---

# Primitive Types In Pazarat

Pazarat may contain these primitive types.

## Actor Primitive

Defines a role, user type, admin actor, seller type, staff type, driver, agent, or system actor.

## Entity Primitive

Defines a reusable object such as user, profile, store, product, order, payout, shipment, document, wallet, return, campaign, or notification.

## State Primitive

Defines a reusable status or condition used across modules.

## Event Primitive

Defines a trigger or occurrence that should align with the platform event taxonomy.

## Permission Primitive

Defines who can view, create, edit, approve, reject, suspend, export, assign, delete, or manage a resource.

## Workflow Primitive

Defines a recurring flow pattern such as submission, review, approval, rejection, suspension, reactivation, payout, fulfillment, or refund.

## Audit Primitive

Defines how actions should be logged and traced.

## Notification Primitive

Defines when and how users, sellers, admins, staff, drivers, or systems are notified.

## UI Primitive

Defines recurring dashboard behavior such as tables, filters, bulk actions, status badges, modals, empty states, and permission-gated actions.

## Implementation Primitive

Defines recurring technical behavior such as event emission, audit log write, validation, permission middleware, background job, service boundary, or API response pattern.

---

# Candidate Primitive Areas

The following are candidate primitive areas for Pazarat.

They are not automatically final definitions.

They should be refined and accepted through project work.

## User Lifecycle

Potentially includes registration, profile creation, verification, approval, activation, suspension, reactivation, deletion, archiving, and role assignment.

## Verification

Potentially includes document submission, identity review, business review, seller review, staff review, approval, rejection, resubmission, and audit.

## Approval

Potentially includes approval authority, approval reason, approval timestamp, reviewer identity, status transition, notification, and event emission.

## Rejection

Potentially includes rejection reason, rejected entity, reviewer identity, resubmission eligibility, notification, event emission, and audit.

## Suspension

Potentially includes reason, actor, scope, duration, affected capabilities, notification, audit, and reactivation path.

## Permission Gate

Potentially includes role, scope, action, visibility, sensitive data access, audit requirement, and UI control availability.

## Audit Log

Potentially includes actor, action, target, before state, after state, reason, timestamp, source module, and related event.

## Notification

Potentially includes recipient, trigger, channel, message type, delivery state, and relation to audit or event taxonomy.

## Dashboard Table Behavior

Potentially includes search, filters, sorting, pagination, row actions, bulk actions, export, status badges, empty state, loading state, and permission-gated controls.

## Profile Ownership

Potentially includes who owns profile data, who can edit it, who can view sensitive fields, who can approve changes, and what changes require audit.

## Event Emission

Potentially includes trigger, event name, actor, payload, downstream consumers, audit link, analytics impact, and implementation implications.

## Document Review

Potentially includes required documents, status, reviewer, rejection reason, expiry, resubmission, audit, and notification.

## Seller Classification

Potentially includes B2B seller, B2C seller, vendor store, verification level, commercial documents, and dashboard access.

---

# Actor And Role Primitives

Pazarat artifacts should avoid inconsistent role definitions.

Common actor primitive candidates include:

- admin
- user
- agent
- B2B seller
- B2C seller
- vendor
- staff
- driver
- support
- system
- reviewer
- finance admin
- operations admin

Before adding a role to an artifact, check whether it is already defined or implied by Pazarat standards or related artifacts.

If a role affects permissions across modules, it should become a shared primitive or be linked to roles and permissions documentation.

Do not define role behavior differently in each child PRD.

---

# User Primitive

The user primitive is central to Pazarat.

A user may appear across:

- user management
- profiles
- orders
- wallets
- verification
- notifications
- support
- analytics
- permissions
- mobile app
- web frontend
- admin dashboard

When documenting user-related artifacts, distinguish:

- account identity
- profile data
- role
- status
- verification state
- permissions
- activity
- ownership
- visibility
- audit history

Do not collapse all user concepts into one vague term.

If a child PRD introduces a new user-related concept, classify whether it is local or platform-wide.

---

# Seller Primitive

Seller-related logic may appear across B2B sellers, B2C sellers, vendors, products, stores, payouts, subscriptions, commissions, orders, returns, and support.

When documenting seller behavior, distinguish:

- seller type
- seller account
- seller profile
- seller store
- commercial documents
- verification state
- approval state
- listing permissions
- payout eligibility
- suspension status
- operational restrictions

Do not define seller categories differently across modules.

Seller classification should align with Pazarat identity, state taxonomy, and relevant business modules.

---

# Verification Primitive

Verification is likely a cross-module Pazarat primitive.

Verification may affect:

- users
- sellers
- agents
- staff
- drivers
- documents
- vendor stores
- payout eligibility
- dashboard access
- sensitive actions

A verification primitive should clarify:

- what is being verified
- who submits evidence
- who reviews it
- what documents or data are required
- what states exist
- what events are emitted
- what permissions change
- what happens on rejection
- what happens on expiry or resubmission
- what audit records are required
- what notifications occur

Do not create separate verification logic in each child PRD if the same pattern repeats.

---

# Approval Primitive

Approval may appear in many Pazarat workflows.

Approval may affect:

- user verification
- seller activation
- product publishing
- payout release
- return/refund handling
- vendor onboarding
- staff actions
- campaigns
- content publishing

An approval primitive should clarify:

- approver role
- approval target
- preconditions
- approval action
- resulting state
- emitted event
- audit requirement
- notification behavior
- reversible or irreversible nature
- required reason or comment if any

Approval logic should align with state and event taxonomy.

---

# Rejection Primitive

Rejection should not be vague.

A rejection primitive should clarify:

- rejection actor
- rejection target
- rejection reason
- resulting state
- whether resubmission is allowed
- whether evidence is required
- notification behavior
- audit requirement
- event emission
- whether rejection blocks future action

If rejection behavior differs by module, document local variation while preserving shared logic.

---

# Suspension And Reactivation Primitive

Suspension and reactivation may affect accounts, sellers, stores, drivers, products, or operational access.

A suspension primitive should clarify:

- target entity
- reason
- actor
- scope
- duration
- affected capabilities
- visibility to affected party
- audit requirement
- notification behavior
- event emission
- reactivation conditions

Do not define suspension inconsistently across user, seller, store, or driver artifacts.

---

# Permission Primitive

Permissions are critical across Pazarat dashboards and modules.

A permission primitive should clarify:

- actor role
- target resource
- action
- scope
- sensitive data access
- UI visibility
- backend enforcement
- audit requirement
- exception rules
- relationship with roles and permissions module

Permission language should be consistent.

Avoid vague phrases such as "admin can manage" without defining which actions are included.

---

# Visibility Primitive

Visibility is related to permissions but not identical.

A visibility primitive may clarify:

- who can see a record
- who can see sensitive fields
- who can see status history
- who can see audit logs
- who can see financial data
- who can see documents
- who can export data
- what is hidden or masked
- whether visibility differs by role or branch

Visibility rules should be explicit in sensitive modules.

---

# Audit Primitive

Audit is required when actions affect identity, money, permissions, status, orders, shipments, documents, compliance, or security.

An audit primitive should clarify:

- actor
- action
- target entity
- before state
- after state
- timestamp
- reason
- source module
- related event
- related notification if any
- rollback or review link if needed

Audit should not be added as generic filler.

Use it where accountability matters.

---

# Notification Primitive

Notifications may be triggered by status changes, approvals, rejections, assignments, payouts, orders, shipments, returns, support updates, verification updates, and security events.

A notification primitive should clarify:

- trigger
- recipient
- channel
- message type
- timing
- dependency on event
- relation to audit
- whether notification is required or optional
- whether notification is user-facing or internal

Do not invent final notification channels without project support.

Mark uncertain behavior as proposed.

---

# Event Primitive

Pazarat events must align with the platform event taxonomy.

An event primitive should clarify:

- event name or family
- trigger
- actor
- target entity
- payload
- state transition if any
- downstream consumers
- analytics implication
- notification implication
- audit implication
- implementation implication

Do not add new event names casually.

If a new event is needed, mark it as proposed and identify affected artifacts.

---

# State Primitive

Pazarat states must align with the platform state taxonomy.

A state primitive should clarify:

- state name
- entity affected
- meaning
- entry conditions
- exit conditions
- allowed transitions
- UI representation
- event relation
- permission impact
- implementation impact

Do not create local states that conflict with platform state taxonomy.

If a local state is necessary, classify it as local and explain its relation to platform states.

---

# Dashboard Table Primitive

Many admin modules use dashboard tables.

A dashboard table primitive may include:

- search
- filters
- sorting
- pagination
- column visibility
- row actions
- bulk actions
- status badges
- export
- empty state
- loading state
- error state
- permission-gated actions
- audit-linked actions

Do not repeat generic table behavior in every PRD unless local differences matter.

If the behavior is project-wide, place it in UI standard or shared primitives.

---

# Bulk Action Primitive

Bulk actions may affect many records and therefore require stronger control.

A bulk action primitive should clarify:

- permitted roles
- selected entity type
- allowed bulk actions
- confirmation requirement
- validation
- partial failure behavior
- audit behavior
- notification behavior
- rollback or review
- export or report impact

Bulk actions should not be added casually.

They can create operational risk.

---

# Status Badge Primitive

Status badges appear across dashboards.

A status badge primitive should align with state taxonomy.

It may define:

- label
- color category if UI standard supports it
- meaning
- entity type
- allowed actions from this state
- tooltip or explanation
- visibility rules

Do not invent status labels independently in every module.

---

# Document Review Primitive

Document review may appear in verification, seller onboarding, staff onboarding, compliance, payouts, tax, customs, and vendor workflows.

A document review primitive may include:

- document type
- submitter
- reviewer
- validation rules
- status
- rejection reason
- resubmission
- expiry
- audit
- notification
- event emission
- sensitive data handling

Document review should be consistent across modules unless local rules require variation.

---

# Profile Ownership Primitive

Profile ownership defines who controls profile data and who may edit or approve changes.

It may apply to:

- user profile
- seller profile
- staff profile
- driver profile
- agent profile
- store profile

A profile ownership primitive should clarify:

- owner
- editable fields
- admin-editable fields
- approval-required fields
- sensitive fields
- visibility rules
- audit behavior
- notification behavior
- event emission

Do not allow profile logic to diverge across modules without reason.

---

# Financial Sensitivity Primitive

Financial modules require caution.

This primitive area may apply to:

- payments
- payouts
- wallets
- invoices
- tax
- commissions
- subscriptions
- transactions
- customs clearance

Financial primitives should clarify:

- entity affected
- money movement
- approval requirement
- audit requirement
- reconciliation implication
- permissions
- export/report behavior
- compliance or jurisdiction uncertainty
- implementation risk
- open legal or tax questions

Do not produce final legal, tax, or regulated financial behavior without verification.

---

# Operational Fulfillment Primitive

Operations modules may share fulfillment and logistics patterns.

This primitive area may apply to:

- shipments
- shipping
- warehouses
- stock inventory
- fulfillment
- drivers
- supply chain
- returns

Operational primitives should clarify:

- entity lifecycle
- actor responsibilities
- state transitions
- event emission
- assignment
- failure handling
- audit
- notification
- dependency on inventory or order status

Do not define fulfillment behavior separately in each module if the same pattern repeats.

---

# Support And Escalation Primitive

Support and escalation logic may appear in support dashboard, returns, refunds, orders, security, and user management.

A support primitive should clarify:

- issue type
- submitter
- owner
- priority
- status
- escalation rule
- SLA if defined
- visibility
- audit
- notification
- resolution state

Do not invent SLA rules unless project standards define them or the user accepts them.

---

# Primitive Inheritance Rule

Child PRDs inherit relevant primitives from:

- Pazarat platform identity
- state taxonomy
- event taxonomy
- UI standard
- implementation standard
- hierarchical documentation protocol
- this shared primitives file
- parent PRD
- branch-local standards if any

A child PRD should specialize inherited primitives, not redefine them from zero.

If local behavior differs, explain the difference and whether it is intentional.

---

# Primitive Candidate Capture During PRD Generation

When generating a Pazarat PRD, the model should identify repeated logic that may need primitive capture.

The model may include a section such as:

- Shared primitive candidates
- Related shared primitives
- Parent update candidates
- State/event candidates
- Open primitive questions

Only include such sections when useful.

Do not overload small PRDs with unnecessary primitive metadata.

---

# Primitive Conflict Handling

If two Pazarat artifacts define the same primitive differently, the model must not silently merge them.

The model should identify:

- conflicting primitive
- conflicting files or branches
- likely authoritative source
- latest conversation decision
- affected artifacts
- proposed resolution
- whether user decision is needed

Conflicts should be resolved through controlled update.

---

# Primitive Update Discipline

When a shared primitive changes, identify affected artifacts.

Potentially affected artifacts include:

- parent PRDs
- child PRDs
- state taxonomy
- event taxonomy
- UI standard
- implementation standard
- decision log if present
- structure index if names or paths change
- local branch standards

Do not change project-wide primitives silently.

---

# Relationship With State Taxonomy

State primitives should not compete with state taxonomy.

The state taxonomy is the canonical map of accepted platform states.

This file may explain repeated state usage and primitive behavior, but if a new state is required, update or propose updating the state taxonomy.

Do not create conflicting state definitions here.

---

# Relationship With Event Taxonomy

Event primitives should not compete with event taxonomy.

The event taxonomy is the canonical map of accepted platform events.

This file may explain repeated event usage and primitive behavior, but if a new event is required, update or propose updating the event taxonomy.

Do not create conflicting event definitions here.

---

# Relationship With UI Standard

UI primitives that are broadly visual or interaction-based should align with the UI/UX standard.

This file may identify repeated UI primitive behavior, but the UI standard should govern detailed UI rules.

Do not duplicate full UI standards here.

---

# Relationship With Implementation Standard

Implementation primitives should align with the implementation architecture and code generation standard.

This file may identify recurring implementation concepts, but detailed implementation rules belong in the implementation standard or technical artifacts.

Do not turn this file into a code architecture document.

---

# Relationship With Parent And Child PRDs

Parent PRDs should identify major shared primitives relevant to their area.

Child PRDs should inherit and specialize relevant primitives.

If child PRDs reveal repeated logic not covered by parent or shared primitives, the model should recommend updating this file or the parent.

Do not force every primitive into every child.

Use relevance.

---

# Placeholder And Scaffold Handling

Placeholders and scaffolds may reveal primitive needs.

If many placeholder child routes depend on the same logic, define or propose the primitive before expanding all children.

If a scaffold repeats generic logic, do not treat it as primitive truth.

Extract useful signal, discard filler, and align with accepted primitives.

---

# Primitive Review Checklist

Before finalizing a major Pazarat PRD, internally check:

1. Does this artifact reuse existing primitives correctly?
2. Does it redefine a shared primitive unnecessarily?
3. Does it introduce a new primitive candidate?
4. Does it conflict with state taxonomy?
5. Does it conflict with event taxonomy?
6. Does it conflict with UI or implementation standards?
7. Does it need audit, notification, permission, or visibility primitives?
8. Does it expose a parent update need?
9. Does it create a project-wide rule from local detail by mistake?
10. Does it duplicate logic that belongs here?

Expose this checklist only when useful.

---

# User Management Primitive Focus

User Management is currently an important active branch for scenario expansion.

Likely primitive candidates include:

- user lifecycle
- profile ownership
- verification
- approval
- rejection
- suspension
- reactivation
- role assignment
- sensitive data visibility
- audit log
- user notification
- dashboard table behavior
- bulk action behavior
- document review

Before generating User Management child PRDs, account for these candidate primitives and align with parent context.

---

# Financial Primitive Focus

Financial modules require stronger discipline.

Likely primitive candidates include:

- payment state
- payout state
- wallet balance
- transaction record
- invoice
- tax record
- commission rule
- refund movement
- reconciliation
- audit trail
- financial permission gate
- export/reporting behavior

Do not finalize regulated financial behavior without sufficient evidence and project decision.

---

# Operations Primitive Focus

Operations modules may require shared lifecycle primitives.

Likely primitive candidates include:

- shipment state
- fulfillment state
- inventory adjustment
- warehouse movement
- driver assignment
- delivery event
- return lifecycle
- exception handling
- operational audit
- customer or seller notification

Align these with state and event taxonomy.

---

# System And Security Primitive Focus

System modules may define project-wide governance primitives.

Likely primitive candidates include:

- role
- permission
- access control
- audit log
- security event
- notification template
- system setting
- privacy rule
- integration event
- API access rule

Changes here may affect the whole project.

Use controlled updates.

---

# Marketing Primitive Focus

Marketing modules may share campaign, coupon, reward, CRM, support, and automation primitives.

Likely primitive candidates include:

- campaign lifecycle
- coupon state
- reward rule
- CRM segment
- automation trigger
- banner placement
- support escalation
- marketing notification

Do not define marketing triggers inconsistently with platform event taxonomy.

---

# Smart Data Primitive Focus

Smart Data modules may share analytics and event intelligence primitives.

Likely primitive candidates include:

- event stream
- report
- dashboard metric
- AI recommendation
- review analysis
- file asset
- data export
- analytics permission
- data freshness

These should align strongly with event taxonomy and implementation standards.

---

# Failure Signals

Shared primitive failures include:

- same concept defined differently in multiple PRDs
- child PRD redefines parent concept incorrectly
- module invents a state that conflicts with taxonomy
- module invents an event that conflicts with event taxonomy
- permissions are vague or inconsistent
- audit behavior is repeated differently across modules
- notifications are invented without shared rule
- UI table behavior differs without reason
- implementation notes contradict PRD primitives
- local rule is promoted to project-wide without evidence
- project-wide rule is ignored in a local child
- scaffold logic is treated as canonical
- raw notes are over-polished into false primitive truth

When failure occurs, classify the primitive issue and correct the canonical location.

---

# Final Principle

Pazarat shared primitives are the continuity memory of repeated project logic.

They should prevent contradiction, reduce duplicate explanations, and make future PRDs stronger.

A strong Pazarat artifact should either use existing primitives or reveal new primitive candidates clearly.

Every repeated rule should become clearer over time, not more fragmented.