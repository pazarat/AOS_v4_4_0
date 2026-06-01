# IMPLEMENTATION ARCHITECTURE AND CODE GENERATION STANDARD

# Purpose / الهدف

This file defines the implementation architecture and code generation standard for Pazarat.

هذا الملف يعرّف معيار الترجمة من التوثيق إلى بنية تنفيذ برمجية داخل مشروع بازارات.

Its purpose is to ensure that Pazarat PRDs, Child PRDs, Workflow PRDs, State/Event Models, Screen PRDs, and visual references can later be translated into consistent backend, database, frontend, API, testing, and integration work through the local PRD documentation and implementation translation contract.

هدفه ضمان أن ملفات التوثيق يمكن ترجمتها لاحقًا إلى كود backend وfrontend وقواعد بيانات وواجهات API واختبارات وتكاملات بدون تخمين أو فقدان لمنطق المشروع.

This file does not generate code by itself.

هذا الملف لا يولد الكود بنفسه.

It defines how documentation must be interpreted when implementation begins.

هو يحدد كيف يجب تفسير التوثيق عند بدء التنفيذ.


---

# 0A. 360-Degree Method And Environment Binding / ربط 360 وبيئة التطوير

This implementation standard operates under the Pazarat 360-degree engineering method:

```txt
13_PAZARAT_360_DEGREE_ENGINEERING_METHOD.md
```

It must also defer to the engineering environment and stack standard whenever language, framework, repository structure, tooling, migrations, testing, CI/CD, deployment, or code generation environment is involved:

```txt
14_PAZARAT_ENGINEERING_ENVIRONMENT_AND_STACK_STANDARD.md
```

This file owns translation logic: how documented product behavior becomes backend, database, API, frontend, and tests.

It does not own independent stack invention.

Code generation must use the accepted Pazarat environment unless the user explicitly requests stack reconsideration or an ADR.

All translated states, events, reusable primitives, permissions, audit patterns, and UI/backend shared behaviors must use the central project references before becoming code.
---

# 1. Target Technology Stack / التقنية المستهدفة

The current intended implementation stack is:

```txt
Backend: ASP.NET / .NET
Database: PostgreSQL
Frontend: Next.js
Language: TypeScript for frontend
API Style: HTTP APIs / REST-style resources unless otherwise documented
```

The binding details, allowed tools, forbidden deviations, local runtime, testing stack, CI/CD, and deployment readiness rules are controlled by:

```txt
14_PAZARAT_ENGINEERING_ENVIRONMENT_AND_STACK_STANDARD.md
```

This stack may evolve later only through explicit user decision or ADR-level stack migration. Documentation and implementation decisions must currently assume this direction.

يمكن تطوير التقنية لاحقًا فقط بقرار صريح أو قرار معماري، لكن قرارات التوثيق والتنفيذ الحالية يجب أن تنطلق من هذا الاتجاه.

---

# 2. Core Implementation Principle / المبدأ الأساسي للتنفيذ

Code must be derived from documented product logic.

يجب أن يُشتق الكود من منطق المنتج الموثق.

The model, developer, or implementation agent must not jump from a feature name directly to code.

لا يجوز القفز من اسم الميزة مباشرة إلى الكود.

Correct implementation sequence:

```txt
Project Standards
→ Platform Identity
→ State Taxonomy
→ Event Taxonomy
→ UI/UX Standard
→ Parent PRD
→ Child PRD
→ Workflow PRD when required
→ State/Event Model when required
→ Screen PRD when required
→ PRD Documentation And Implementation Translation Contract
→ Implementation Notes
→ Backend / Database / Frontend Code
→ Tests
→ Code Review Against PRD
```

Implementation must preserve:

- documented entities
- documented ownership
- documented states
- documented events
- documented workflows
- documented permissions
- documented validation
- documented UI behavior
- documented cross-system handoffs
- documented business rules

---

# 3. What This File Controls / ماذا يضبط هذا الملف

This standard controls how documentation maps to implementation.

هذا المعيار يضبط كيف يتحول التوثيق إلى تنفيذ.

It defines rules for:

- translating entities into backend models and database structures
- translating state families into enums, lifecycle rules, and UI indicators
- translating events into domain events, audit records, analytics signals, and automation triggers
- translating workflows into use cases, commands, queries, services, and transactions
- translating Screen PRDs into frontend routes, pages, components, forms, tables, and state displays
- translating permissions into authorization policies and UI action visibility
- translating acceptance criteria into tests
- reviewing code against PRD requirements

It does not replace detailed backend architecture documents, database schema files, API contracts, frontend component documentation, or actual source code.

---

# 3A. PRD Contract Integration / ربط عقد التوثيق بالتنفيذ

The implementation standard must be applied together with:

```txt
11_PAZARAT_PRD_DOCUMENTATION_AND_IMPLEMENTATION_TRANSLATION_CONTRACT.md
```

That contract defines what Parent PRDs and Child PRDs must expose before implementation can safely begin.

This file defines how those exposed outputs become ASP.NET backend, PostgreSQL database structures, Next.js frontend work, API planning, validation, tests, audit, and deployment-facing implementation concerns.

If the PRD contract is incomplete, implementation must stop at diagnosis, technical extraction, or a proposed implementation spec.

It must not silently invent missing product behavior.

---

# 4. Code Readiness Gate / بوابة جاهزية التوثيق للكود

Before generating or implementing code for a module, verify that the related documentation contains enough implementation-ready logic.

قبل توليد أو كتابة الكود لأي قسم، يجب التأكد أن التوثيق يحتوي منطقًا كافيًا للتنفيذ.

## Minimum Required Inputs

For serious implementation, at least one of the following should exist:

```txt
Parent PRD + Child PRD
Parent PRD + Workflow PRD
Child PRD + Screen PRD
Child PRD + State/Event Model
```

For production-grade implementation, the preferred input is:

```txt
Parent PRD
+ Child PRD
+ Workflow PRD when the flow is complex
+ State/Event Model when lifecycle is important
+ Screen PRD for UI work
+ Visual Reference for UI direction
```

## Do Not Generate Production Code From

Do not generate production-level code from:

- feature name only
- vague conversation only
- Parent PRD only when the branch requires local details
- visual image only
- incomplete Child PRD without states, events, actions, or validation
- generic marketplace assumptions

Parent PRD may be enough for a prototype or architectural sketch, but not for final implementation.

---

# 4A. Implementation-Ready Documentation Test / اختبار جاهزية التوثيق للتنفيذ

Before generating serious code, the model must verify that the related PRD exposes enough information to derive, at the correct level:

- ASP.NET use cases, commands, queries, handlers, policies, validation, events, audit, and transaction risks
- PostgreSQL entities, relationships, constraints, indexes, state storage, event storage, and persistence decisions
- API groups, operations, request/response needs, permissions, error behavior, pagination, filters, and idempotency when relevant
- Next.js routes, screens, components, forms, tables, visible states, permission-based visibility, and error/empty/loading states
- testable acceptance criteria

If these cannot be derived without guessing, improve the PRD or create the required workflow, screen, API, database, or implementation note before production-oriented code generation.

---

# 5. Documentation To Code Translation Matrix / مصفوفة ترجمة التوثيق إلى كود

| Documentation Output | Backend Translation | Database Translation | Frontend Translation | Test Translation |
|---|---|---|---|---|
| `Entity` | Domain model / entity class | table / relation / constraint | TypeScript type / display model | entity behavior tests |
| `Entity Ownership` | module boundary / service owner | schema ownership / FK boundary | data source ownership | integration boundary tests |
| `State Family` | enum / lifecycle policy | enum / status column / transition log | badge / filter / UI condition | state transition tests |
| `Event` | domain event / integration event | event log / audit record | timeline / activity feed | event emission tests |
| `Use Case` | application service / command handler | transaction boundary | page action / workflow trigger | acceptance tests |
| `Command` | write endpoint / handler | insert/update transaction | button / form submit | command tests |
| `Query` | read endpoint / query handler | select / view / read model | table / card / detail view | query tests |
| `Business Rule` | domain rule / policy | constraint where appropriate | disabled action / validation message | rule tests |
| `Validation Rule` | DTO validator / domain validation | DB constraint when needed | form validation | validation tests |
| `Permission` | authorization policy | optional permission mapping | action visibility / route guard | permission tests |
| `Workflow` | orchestrated use case / service flow | transaction / consistency boundary | stepper / process UI | workflow tests |
| `Screen PRD` | supporting APIs | read/write models | route / page / components | UI behavior tests |
| `Cross-System Handoff` | integration service / event consumer | relationship / outbox / log | linked section / status summary | integration tests |
| `Acceptance Criteria` | behavior spec | data expectations | UI expectations | automated or manual tests |

---

# 6. Backend Architecture Standard / معيار الباك اند

The backend should be organized around business domains and use cases, not random CRUD files.

يجب تنظيم الباك اند حول المجالات والعمليات، وليس حول ملفات CRUD عشوائية.

## Recommended Backend Thinking

Use a modular domain-oriented structure.

استخدم تنظيمًا وحداتيًا حسب المجالات.

Each major domain should have clear ownership, such as:

```txt
UserManagement
Stores
Products
Orders
Payments
Wallets
Shipping
Marketing
Notifications
Security
System
```

Each domain may contain:

```txt
Domain Models
Enums / State Families
Commands
Queries
Handlers / Services
Validators
Events
Policies
DTOs
API Endpoints
Tests
```

The exact folder structure can be decided later, but the code must preserve domain boundaries from PRDs.

---

# 7. ASP.NET / .NET Backend Rules / قواعد ASP.NET

When translating Pazarat documentation to ASP.NET backend code:

## Entity Translation

An entity from PRD may become:

- domain entity
- aggregate root
- value object
- DTO
- read model
- database table
- external reference object

Do not assume every PRD entity is a database table.

لا تفترض أن كل كيان في PRD يجب أن يصبح جدولًا.

Before implementation, classify each entity:

| Entity Type | Meaning |
|---|---|
| `Core Entity` | Owned by this domain |
| `Referenced Entity` | Owned by another domain |
| `Value Object` | Embedded concept |
| `Read Model` | Query/display projection |
| `External Entity` | External system or integration |
| `Configuration Entity` | Settings, templates, policies |
| `Event Entity` | Recorded event or audit object |

## Command / Query Separation

Use commands for state-changing operations.

استخدم Commands للعمليات التي تغير النظام.

Examples:

```txt
CreateVerificationTemplate
SubmitVerificationCase
ApproveVerificationCase
ActivateSellerCapability
SuspendAccount
```

Use queries for read operations.

استخدم Queries لعمليات القراءة.

Examples:

```txt
GetUserProfile
ListVerificationTemplates
GetApprovalQueue
SearchUsers
GetUserTimeline
```

Commands and queries should be derived from PRD use cases, not invented from generic CRUD.

## Service / Handler Rule

A backend handler or service must map to a documented use case, command, workflow, or domain operation.

أي service أو handler يجب أن يكون مرتبطًا بعملية موثقة.

If no documented use case exists, the implementation may be premature.

---

# 8. PostgreSQL Database Standard / معيار PostgreSQL

Database structures must reflect documented ownership, lifecycle, and relationships.

يجب أن تعكس قاعدة البيانات الملكية والعلاقات ودورة الحياة الموثقة.

## Database Translation Rules

When translating documentation to PostgreSQL:

| Documentation | Database Consideration |
|---|---|
| Entity | table or embedded structure |
| State Family | enum / text with constraint / lookup table |
| Event | event table / audit log / outbox table |
| Relationship | foreign key / join table / reference |
| Permission | role mapping / policy relation |
| Workflow | state transition history / process table |
| Configuration | settings table / template table |
| Timeline | event log / audit trail |
| Metrics | materialized view / read model / aggregation |

## Naming Direction

Use consistent naming.

Preferred database naming:

```txt
snake_case
```

Examples:

```txt
user_accounts
verification_templates
verification_cases
approval_cases
account_capabilities
event_log
audit_log
```

## State Storage Rule

A state may be stored as:

- enum
- constrained text
- lookup table
- lifecycle record
- derived read model

The decision depends on stability and complexity.

Do not store multiple unrelated lifecycle states in one generic `status` column.

Bad:

```txt
users.status
```

Better:

```txt
account_status
verification_status
approval_status
seller_capability_status
store_status
```

## Event Storage Rule

Important events may require:

- event log
- audit log
- outbox table
- analytics stream
- timeline projection

The PRD should identify event families and visibility.

The implementation design decides exact storage.

---

# 9. State Implementation Rule / قاعدة تنفيذ الحالات

State families from `02_PLATFORM_STATE_TAXONOMY.md` must be translated consistently.

يجب ترجمة عائلات الحالات من ملف الحالات بشكل متسق.

A state family may become:

- backend enum
- database enum or constrained text
- state transition policy
- UI badge
- filter option
- timeline milestone
- analytics dimension
- permission condition

## State Translation Checklist

For each state family, identify:

- subject entity
- allowed values
- initial state
- terminal states
- allowed transitions
- invalid transitions
- transition triggers
- emitted events
- permissions needed to transition
- UI display
- audit needs

Do not implement a state as a simple string without understanding its lifecycle.

---

# 10. Event Implementation Rule / قاعدة تنفيذ الأحداث

Events from `03_PLATFORM_EVENT_TAXONOMY.md` must be treated as platform signals.

يجب التعامل مع الأحداث كإشارات مركزية للمنصة.

An event may become:

- domain event
- integration event
- audit log entry
- notification trigger
- analytics signal
- automation trigger
- timeline item
- AI insight input

## Event Translation Checklist

For each event, identify:

- event name
- event family
- event type
- source module
- subject entity
- actor
- state before / after when relevant
- consumers
- visibility
- priority
- deduplication risk
- audit requirement
- analytics requirement

Do not confuse event with command.

Bad:

```txt
send_coupon
```

Good:

```txt
coupon_granted
```

---

# 11. Workflow Implementation Rule / قاعدة تنفيذ سير العمل

Workflows should become use cases or orchestration logic.

يجب أن تتحول التدفقات إلى use cases أو orchestration logic.

A workflow may produce:

- command sequence
- query needs
- state transitions
- emitted events
- transaction boundary
- integration calls
- notification triggers
- audit trail
- compensation logic
- acceptance tests

## When Workflow File Is Required

A separate Workflow PRD or implementation workflow note is required when the flow is:

- multi-step
- multi-system
- state-heavy
- financially sensitive
- approval-sensitive
- shipping-sensitive
- security-sensitive
- automation-sensitive
- likely to fail or retry
- important for testing

Not every child PRD needs a separate workflow file.

But every child PRD must mention important workflows.

---

# 12. API Design Standard / معيار تصميم API

API endpoints must be derived from documented use cases, commands, and queries.

يجب اشتقاق نقاط API من use cases وcommands وqueries الموثقة.

Do not generate endpoints only from database tables.

لا تولد endpoints من الجداول فقط.

## API Grouping Rule

API groups should follow domain and use-case boundaries.

Examples:

```txt
/users
/users/{id}
/users/{id}/profile
/users/{id}/capabilities
/verification/templates
/verification/cases
/approval/cases
/stores
/orders
/wallets
/shipments
```

## Command Endpoint Examples

```txt
POST /verification/templates
POST /verification/cases/{id}/submit
POST /approval/cases/{id}/approve
POST /approval/cases/{id}/reject
POST /users/{id}/suspend
POST /users/{id}/reactivate
```

## Query Endpoint Examples

```txt
GET /users
GET /users/{id}
GET /users/{id}/timeline
GET /verification/templates
GET /approval/cases
```

These are examples only.

Final endpoint names must come from detailed implementation design.

---

# 13. Frontend Architecture Standard / معيار الفرونت اند

The frontend should translate Screen PRDs and visual references into reusable Next.js UI.

يجب أن يترجم الفرونت اند ملفات Screen PRD والصور المرجعية إلى واجهات Next.js قابلة لإعادة الاستخدام.

## Next.js Frontend Rules

Frontend code should be organized around:

- app routes
- pages / screens
- reusable components
- feature modules
- API clients
- state display helpers
- form validation
- table/filter utilities
- layout shells
- design system tokens

## Frontend Translation Matrix

| Documentation | Frontend Translation |
|---|---|
| Screen PRD | route / page |
| Layout zones | page sections |
| Reusable components | component imports |
| State family | badge / status component |
| Event timeline | timeline component |
| Data group | card / table / detail block |
| Action | button / menu / form submit |
| Permission | hidden/disabled UI state |
| Validation | form validation |
| Empty state | EmptyState component |
| Loading state | skeleton |
| Error state | ErrorPanel |
| Filter behavior | FilterBar / FilterDrawer |
| Saved views | tabs or saved view selector |

## Component Reuse Rule

Do not build a new component when an existing component pattern fits.

Examples of reusable components:

```txt
AppShell
SidebarNav
Topbar
Breadcrumbs
PageHeader
SectionCard
MetricCard
StatusBadge
RoleBadge
VerificationBadge
DataTable
FilterDrawer
SavedViewsTabs
ProfileHeaderCard
Timeline
ActivityFeed
ApprovalQueue
RequirementBuilder
AuditTrail
InsightCard
QuickActionsGrid
EmptyState
LoadingSkeleton
ErrorPanel
FooterActionBar
```

The UI/UX standard lives in:

```txt
02_MY_PROJECT/pazarat/05_UI_UX_DESIGN_SYSTEM_AND_VISUAL_GENERATION_STANDARD.md
```

---

# 14. Screen PRD To Frontend Rule / قاعدة تحويل Screen PRD إلى Frontend

A Screen PRD should translate into:

- route
- page component
- layout sections
- data fetching needs
- mutation actions
- local components
- state display
- event display
- permission behavior
- form behavior
- empty/loading/error states

Before implementing a screen, verify:

1. What is the screen purpose?
2. Who can access it?
3. What data does it display?
4. What actions are available?
5. What states are shown?
6. What events or timelines are shown?
7. What components should be reused?
8. What API queries are required?
9. What API commands are required?
10. What visual reference applies?

---

# 15. Permissions And Authorization Rule / قاعدة الصلاحيات

Permissions must be documented and implemented consistently.

يجب توثيق وتنفيذ الصلاحيات بشكل متسق.

A permission may affect:

- backend endpoint access
- command execution
- query visibility
- field visibility
- action availability
- UI disabled state
- audit record
- notification recipient
- workflow assignment

A dangerous action must not be protected only in UI.

الإجراءات الحساسة لا يكفي حمايتها في الواجهة فقط.

Backend authorization is required for:

- approval decisions
- suspension / reactivation
- financial actions
- payout approval
- refund approval
- role changes
- permission changes
- security actions
- identity-sensitive updates

---

# 16. Validation Rule / قاعدة التحقق

Validation must exist at the correct layers.

يجب أن يوجد التحقق في الطبقات الصحيحة.

| Validation Type | Location |
|---|---|
| UI convenience validation | frontend |
| API input validation | backend DTO / request validator |
| business rule validation | domain/application service |
| database integrity | PostgreSQL constraints |
| permission validation | authorization layer |
| cross-system eligibility | application workflow/service |

Do not rely on frontend validation only.

لا تعتمد على تحقق الفرونت اند فقط.

---

# 17. Transactions, Consistency, And Idempotency / الاتساق ومنع التكرار

Some operations require careful consistency.

بعض العمليات تحتاج اتساقًا دقيقًا.

Examples:

- payment success and order status
- stock reservation and checkout
- order fulfillment and shipment creation
- wallet credit and reward grant
- refund approval and payment reversal
- approval decision and capability activation
- notification sent once for one event
- reward granted once for one goal

When implementation detects consistency-sensitive logic, document:

- transaction boundary
- idempotency rule
- retry behavior
- compensation behavior
- duplicate prevention
- emitted events
- audit record

PRDs identify the risk.

Implementation specs define the exact technical pattern.

---

# 18. Audit And Traceability Rule / قاعدة التدقيق والتتبع

Important actions should be auditable.

يجب أن تكون الإجراءات المهمة قابلة للتدقيق.

Audit-worthy actions include:

- approval decisions
- verification decisions
- restriction or suspension
- reactivation
- permission changes
- financial actions
- payout approval
- refund approval
- security actions
- identity-sensitive changes
- admin impersonation
- configuration changes

Audit records should identify:

- actor
- action
- subject
- previous value
- new value
- time
- reason
- source module
- related event

---

# 19. Testing And Acceptance Criteria Standard / معيار الاختبار

Tests must come from documented acceptance criteria, business rules, states, events, and permissions.

يجب أن تأتي الاختبارات من معايير القبول وقواعد العمل والحالات والأحداث والصلاحيات الموثقة.

## Test Types

| Test Type | Purpose |
|---|---|
| Unit Test | Business rule or small function |
| Domain Test | Entity behavior / state rule |
| Application Test | Use case / command / query |
| Integration Test | Database / API / external handoff |
| Authorization Test | Permission and role behavior |
| UI Test | Screen behavior and states |
| E2E Test | Complete user workflow |
| Regression Test | Prevent breaking accepted behavior |

## Testable Documentation Outputs

A PRD should produce testable statements such as:

- when OTP is verified, account becomes active
- when approval is rejected, capability must not activate
- when payment fails, order must not move to paid
- when shipment is delivered, delivery event is emitted
- when reward is already granted, duplicate grant is prevented
- when user lacks permission, action is disabled and backend rejects command

---

# 20. Code Review Against PRD / مراجعة الكود مقابل التوثيق

After code is generated or written, it must be reviewed against documentation.

بعد كتابة أو توليد الكود، يجب مراجعته مقابل التوثيق.

Review checklist:

1. Does the code implement the documented use case?
2. Are entities mapped correctly?
3. Are ownership boundaries preserved?
4. Are states implemented consistently?
5. Are transitions valid?
6. Are events emitted where documented?
7. Are permissions enforced in backend and frontend?
8. Are validations implemented?
9. Are failure cases handled?
10. Are cross-system handoffs implemented?
11. Are audit requirements covered?
12. Are UI states aligned with Screen PRD?
13. Are components reused according to UI standard?
14. Are tests derived from acceptance criteria?
15. Are open decisions still unresolved or accidentally hardcoded?

Code that passes technically but violates PRD is not acceptable.

الكود الذي يعمل تقنيًا لكنه يخالف التوثيق غير مقبول.

---

# 21. Folder And Module Structure Principle / مبدأ هيكل المجلدات

The final source code structure will be defined when the coding phase begins.

سيتم تحديد هيكل الكود النهائي عند بدء مرحلة التنفيذ.

However, it should preserve these principles:

- domain-oriented backend modules
- reusable frontend components
- clear API boundaries
- shared types where appropriate
- state/event consistency
- documented ownership
- testable use cases
- separation between UI, application logic, domain logic, database, and integrations

Possible high-level project direction:

```txt
apps/
  web-admin/
  web-customer/
  api/

packages/
  ui/
  shared-types/
  design-system/

backend/
  src/
    modules/
    shared/
    infrastructure/
    tests/
```

This is only a conceptual direction.

هذا مجرد اتجاه مفاهيمي.

The final structure must be decided when implementation starts.

---

# 22. Parent / Child Implementation Responsibility / مسؤولية الأب والابن في التنفيذ

## Parent PRD

Parent PRD should define:

- major use cases
- major entities
- major state families
- major event families
- major workflow families
- child routing
- cross-system handoffs
- implementation roots

Parent PRD should not define every endpoint or table.

## Child PRD

Child PRD should define:

- local use cases
- local operations
- local commands and queries
- local states and events
- local validation
- local edge cases
- local permissions
- local UI outputs
- local acceptance criteria

## Workflow PRD

Workflow PRD should define:

- step-by-step execution
- transitions
- decisions
- failure paths
- integration handoffs
- transaction and consistency risks

## Screen PRD

Screen PRD should define:

- UI layout
- actions
- data requirements
- visible states
- permissions
- form behavior
- frontend-ready outputs

---

# 23. Open Decisions Rule / قاعدة القرارات المفتوحة

If implementation requires a decision not documented yet, do not silently guess.

إذا احتاج التنفيذ قرارًا غير موثق، لا تخمن بصمت.

Mark it as:

```txt
Open Implementation Decision
```

Examples:

- exact database enum vs lookup table
- exact API route name
- sync vs async event handling
- transaction boundary
- idempotency key strategy
- notification deduplication rule
- frontend state management approach
- exact pagination strategy
- exact authorization policy naming

The model may propose a recommendation, but must label it as proposed unless confirmed.

---

# 24. Anti-Patterns / أخطاء يجب تجنبها

Avoid:

- generating code from screen image only
- generating code from feature name only
- building CRUD endpoints without use cases
- using one global status for many lifecycles
- ignoring events
- ignoring audit
- ignoring permissions
- hiding business rules inside UI only
- treating frontend validation as sufficient
- creating tables for every word in PRD
- ignoring cross-system handoffs
- duplicating components for the same pattern
- hardcoding unresolved decisions
- inventing behavior not documented in PRD
- changing accepted product logic to fit easy code

---

# 25. Final Rule / القاعدة النهائية

The PRD defines product truth.

ملف PRD يحدد حقيقة المنتج.

The implementation standard defines how product truth becomes code.

معيار التنفيذ يحدد كيف تتحول حقيقة المنتج إلى كود.

The backend enforces rules.

الباك اند يفرض القواعد.

The database preserves state and relationships.

قاعدة البيانات تحفظ الحالات والعلاقات.

The frontend expresses workflows and actions.

الفرونت اند يعرض التدفقات والإجراءات.

Events connect the platform.

الأحداث تربط المنصة.

Tests prove the behavior.

الاختبارات تثبت السلوك.

Implementation must not be a separate interpretation of the product.

يجب ألا يكون التنفيذ تفسيرًا منفصلًا للمنتج.

It must be a disciplined translation of the documented product logic.

Implementation generation must also obey `18_PAZARAT_CODE_PRACTICE_AND_IMPLEMENTATION_CANON.md`. Stack choice, repository structure, and API/database standards are not enough without code-practice rules for modules, persistence, migrations, realtime, authorization, validation, audit, observability, and tests.
