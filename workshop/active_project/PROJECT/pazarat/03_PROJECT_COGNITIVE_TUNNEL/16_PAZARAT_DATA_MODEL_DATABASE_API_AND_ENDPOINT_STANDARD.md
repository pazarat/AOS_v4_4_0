# PAZARAT DATA MODEL, DATABASE, API, AND ENDPOINT STANDARD

# Purpose / الهدف

This file defines the Pazarat-wide standard for deriving data models, database structures, API contracts, and endpoint candidates from mature scenarios.

It exists because many documentation failures appear only when the system is forced to answer database and endpoint questions.

A scenario may sound coherent in prose but still be unsafe if it cannot explain:

- what the stable identities are
- what is stored as runtime fact
- what is only configurable value
- what relationships drive visibility and filtering
- what lifecycle states must be persisted
- what events must be emitted
- what commands and queries the UI or backend needs
- what constraints, indexes, migrations, permissions, and audit trails are implied

This file is a reinforcing 360 lens.

It does not replace:

- `11_PAZARAT_PRD_DOCUMENTATION_AND_IMPLEMENTATION_TRANSLATION_CONTRACT.md`
- `13_PAZARAT_360_DEGREE_ENGINEERING_METHOD.md`
- `14_PAZARAT_ENGINEERING_ENVIRONMENT_AND_STACK_STANDARD.md`
- `15_PAZARAT_RAW_TO_PROGRAMMATIC_NARRATIVE_WEAVING_STANDARD.md`

It makes their translation more concrete.

---

# 1. Role Inside The 360 Method

The Pazarat 360 method is not limited to three fixed files or three fixed directions.

It is a rotating engineering loop.

Database and API thinking are central reinforcing lenses because they reveal whether documentation is grounded in executable system reality.

Correct rotation:

```txt
Raw scenario
→ narrative/programmatic weave
→ entity and relationship interpretation
→ command/query/API interpretation
→ accepted stack and repository placement
→ implementation contract
→ code/migration/OpenAPI/tests
→ feedback to scenario when contradictions appear
```

The model must not postpone database/API coherence until after writing the scenario.

Scenario prose must already respect the likely entity spine, relationship model, endpoint responsibility, permissions, and persistence constraints.

---

# 2. Data Modeling Extraction Order

When a scenario, PRD, workflow, or screen implies stored behavior, derive data implications in this order:

1. **Stable identities** — aggregate roots, entities, natural platform identities, and durable references.
2. **Ownership and relationship spine** — which identity references which other identity, and why.
3. **Runtime facts** — orders, payments, shipments, approvals, verification submissions, changes, logs, and other historical records.
4. **Configurable values** — templates, rates, thresholds, policies, feature toggles, country-scoped values, role-scoped values, and versioned settings.
5. **Lifecycle states** — persisted status fields or state tables that map to the central state taxonomy.
6. **Events and audit** — event candidates, audit records, notification triggers, analytics signals, and compliance records.
7. **Read models and filters** — projections, dashboards, search views, counters, reports, and query paths.
8. **Constraints and indexes** — uniqueness, foreign keys, required fields, versioning, soft-delete rules, query performance needs, and integrity rules.
9. **Migration and seed needs** — initial records, immutable references, generated defaults, environment-safe migrations, and data backfill requirements.

The model must not start with table names from UI labels.

It must start with the domain spine and only then propose table/entity candidates.

---

# 3. Database Reality Rules

## 3.1 Identity Is Not A Label

A visible label in the UI is not automatically a database owner.

Example: a country filter does not prove that products are directly owned by `CountryContext`.

Products may appear under a country because the relationship chain is:

```txt
CountryContext → Account → Store → Product
```

or because a store, warehouse, delivery zone, market listing, or policy explicitly references the country.

The scenario must explain the correct relation chain before declaring ownership.

## 3.2 Relationship-Driven Filters

Many dashboard filters should be treated as read queries over existing relations, not as new domain concepts.

Before inventing a table or module, ask:

- Is this only a filtered view?
- Which relation produces the filter?
- Is the filter derived from account country, store country, listing country, delivery country, market country, or another explicit reference?
- Does the filter require a denormalized read model for performance, or can it be expressed from existing relations?

## 3.3 Configuration Is Not Runtime Fact

A template, rate, condition, or policy is not the same as a transaction record.

Examples:

- A verification template defines requirements. A verification submission records a user attempt.
- A tax configuration defines a calculation input. An invoice/tax line records what was charged.
- A shipping policy defines availability and cost behavior. A shipment record stores actual fulfillment.
- A commission template defines a rate. A commission entry records the amount taken from an order.

Scenarios must keep these layers separate.

## 3.4 One Logic, Many Configurations

When Pazarat expands from one country to many countries, the model must not duplicate domain engines.

The correct pattern is usually:

```txt
Single domain logic
+ country/context-scoped configuration records
+ optional cross-context policy matrix
= multi-country behavior
```

## 3.5 Historical Accuracy

If a value can change later but must preserve past transactions, the system needs snapshotting, versioning, or immutable transaction lines.

Examples:

- order price snapshot
- tax amount at time of checkout
- commission amount at time of payout
- verification requirement version used at submission time
- terms version accepted by the user

The model must flag this need at scenario or implementation-contract depth when relevant.

---

# 4. PostgreSQL And EF Core Binding

Pazarat database implementation is governed by the engineering environment standard:

```txt
PostgreSQL + EF Core with Npgsql provider
```

Therefore database implications must be compatible with:

- EF Core migrations
- PostgreSQL constraints and indexes
- schema evolution
- explicit foreign keys where appropriate
- optimistic concurrency where needed
- transaction boundaries
- audit columns and audit tables when required
- soft delete or archival rules only when justified
- seed data for immutable or foundational platform records

Dapper may be considered only for justified high-performance read paths after the canonical domain model remains clear.

---

# 5. API And Endpoint Extraction Order

Endpoints must be derived from use cases, commands, queries, and lifecycle transitions.

Do not derive endpoints only from page names.

Extraction order:

1. **Actor intent** — who is trying to do what?
2. **Permission boundary** — who is allowed to perform or see it?
3. **Command or query** — does it change state or read state?
4. **Business rule** — what validation, policy, or lifecycle gate applies?
5. **Input contract** — required fields, optional fields, and validation.
6. **Output contract** — response shape, status, errors, and empty/blocked states.
7. **Side effects** — events, audit logs, notifications, counters, read model updates.
8. **Idempotency/concurrency** — especially for payment, order, shipment, approval, and configuration changes.
9. **OpenAPI readiness** — enough contract clarity to document the endpoint.

---

# 6. Endpoint Families

Pazarat endpoints should generally fall into these families unless a documented contract says otherwise:

| Family | Meaning | Examples |
|---|---|---|
| Command endpoint | Creates or changes state | create order, approve user, update tax configuration |
| Query endpoint | Reads data without changing state | list users, get order detail, search products |
| Transition endpoint | Applies lifecycle state change | activate country, suspend account, mark shipment delivered |
| Configuration endpoint | Changes templates/settings | update verification template, set commission policy |
| Relationship endpoint | Adds/removes/changes relations | assign agent to country, link category to market |
| Bulk endpoint | Applies controlled batch behavior | bulk approve, bulk import regions |
| Export/report endpoint | Produces reporting output | export invoices, generate sales report |
| Integration endpoint | Handles external system interaction | payment webhook, carrier status callback |

The endpoint family should be visible in the implementation contract even when the final route naming is postponed.

---

# 7. Command/Query Separation

A scenario must distinguish reads from writes.

Examples:

- “show users from Lebanon” is a query.
- “assign Lebanon to an operational agent” is a command.
- “activate Lebanon for marketplace browsing” is a transition/configuration command.
- “calculate checkout total for buyer country + store country + delivery country” may be a query/calculation operation, but placing an order is a command that persists facts.

This distinction is required before code generation.

---

# 8. Scenario Feedback Rule

If database or endpoint extraction reveals that the scenario prose is wrong, the model must repair the scenario.

Examples of mandatory feedback:

- The scenario says a module owns data that is actually derived through another relationship.
- The scenario treats a configuration as if it were a runtime record.
- The scenario describes a filter as if it were an entity.
- The scenario assumes one endpoint can safely perform multiple unrelated commands.
- The scenario ignores historical snapshots for mutable rates or terms.
- The scenario requires a cross-context matrix but spreads its decision logic across multiple children.

The model must not silently compensate in code.

Documentation must be repaired so future translation remains coherent.

---

# 9. Minimum Data/API Output By Artifact Depth

## Parent PRD

Must identify:

- major stable identities
- major relationship spines
- configuration families
- runtime fact families
- external data/API owners
- parent-depth endpoint families
- known cross-module data dependencies

Must not define all fields and routes unless the parent is intentionally acting as an implementation contract.

## Child PRD

Must identify:

- local entities or records
- local fields and validation needs
- state transitions
- event candidates
- command/query candidates
- endpoint family candidates
- database constraints or indexes when obvious
- audit, notification, or reporting effects

## Workflow / Screen / Sub-child

Must identify:

- exact user action paths
- form fields
- table/query/filter behavior
- command and query separation
- empty/loading/error/blocked states
- permission and visibility checks
- backend/API data needed by the UI

## Implementation Contract

Must identify:

- entities/tables/value objects/read models
- migrations and seed needs
- endpoint candidates and route style
- DTOs and validation
- handlers/use cases
- permissions/security
- state transitions and events
- audit/notifications
- tests and acceptance criteria

---

# 10. Anti-Patterns

The model must reject or repair these patterns:

- table design copied from UI headings
- endpoints copied from page names without commands/queries
- duplicating a domain engine for every country, role, or module
- describing filters as ownership
- treating current settings as historical facts
- writing prose that cannot identify entities or endpoints later
- adding a database table merely because a term was mentioned in raw input
- merging unrelated commands into one endpoint because the UI has one button
- ignoring permissions when extracting endpoints
- ignoring migrations and seed data for foundational records
- generating code before the data/API owner is clear

---

# 11. Required Repair Behavior

When data/API clarity is insufficient, the model must produce one of these outcomes:

```txt
accepted data/API interpretation
proposed data/API interpretation
open decision
conflict with existing project truth
missing parent/child detail
missing implementation contract
needs schema/API standard update
```

The model must explicitly distinguish accepted project truth from proposed modeling.

---

# 12. Compact Extraction Checklist

Before treating a scenario as translation-ready, check:

- [ ] What are the stable identities?
- [ ] What is the relationship spine?
- [ ] What is configurable value vs runtime fact?
- [ ] What filters are relationship-derived?
- [ ] What facts require history, versioning, or snapshots?
- [ ] What states and events are involved?
- [ ] What commands are implied?
- [ ] What queries are implied?
- [ ] What endpoint families are implied?
- [ ] What permissions protect them?
- [ ] What constraints, indexes, migrations, or seeds are likely?
- [ ] What must be routed to another parent/child/module?
- [ ] What cannot be safely generated yet?
