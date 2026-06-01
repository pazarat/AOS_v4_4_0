# PAZARAT CODE PRACTICE AND IMPLEMENTATION CANON

# Purpose / الهدف

This file defines **how code must be written** inside the accepted Pazarat stack.

`14_PAZARAT_ENGINEERING_ENVIRONMENT_AND_STACK_STANDARD.md` answers:

```txt
What stack and environment does Pazarat use?
```

This file answers:

```txt
How must code be structured, persisted, integrated, tested, observed, reviewed, and evolved inside that stack?
```

Stack selection is not enough for Pazarat. Production-oriented implementation must obey this canon together with:

```txt
06_IMPLEMENTATION_ARCHITECTURE_AND_CODE_GENERATION_STANDARD.md
11_PAZARAT_PRD_DOCUMENTATION_AND_IMPLEMENTATION_TRANSLATION_CONTRACT.md
12_PAZARAT_PRD_AND_CODE_RUNTIME_GATES.yaml
13_PAZARAT_360_DEGREE_ENGINEERING_METHOD.md
14_PAZARAT_ENGINEERING_ENVIRONMENT_AND_STACK_STANDARD.md
16_PAZARAT_DATA_MODEL_DATABASE_API_AND_ENDPOINT_STANDARD.md
17_PAZARAT_CODEBASE_INTEGRATION_AND_DOCUMENTATION_ROUTING_STANDARD.md
```

---

# 1. Binding Rule

No Pazarat code, migration, API contract, realtime channel, background worker, seed, test suite, or frontend integration may be generated from a stack name alone.

The model must first derive the implementation from:

1. accepted PRD / scenario / parent-child truth;
2. state taxonomy;
3. event taxonomy;
4. shared primitives;
5. data/API contract standard;
6. engineering environment standard;
7. this code practice canon;
8. tests and acceptance criteria.

If any required owner is thin, missing, contradictory, or insufficient, classify it as **incomplete truth** and repair the owner or record an explicit decision before production-oriented implementation.

---

# 2. General Coding Rules

- Code must express accepted project truth, not generic marketplace assumptions.
- Controllers, hubs, workers, and UI handlers must not contain domain/business logic.
- Use cases and commands/queries must be derived from PRD intent, permissions, states, events, validations, and side effects.
- Generated code must preserve module boundaries and shared primitive ownership.
- Do not duplicate rules that belong to taxonomies, shared primitives, governance, or parent artifacts.
- Every significant implementation choice must be traceable back to an owner artifact or accepted decision.
- Scaffold is not product truth until it passes the relevant gates.

---

# 3. Modular Monolith Rules

Pazarat begins as a Modular Monolith.

Rules:

- organize backend by bounded business modules;
- keep cross-module calls explicit;
- avoid direct database reach-through across module boundaries unless a central contract allows it;
- keep module-owned entities, application use cases, validation, and policies inside the owning module;
- shared primitives must be central, not copied into each module;
- use domain events or integration events for lifecycle effects that cross module boundaries;
- do not split into microservices unless a recorded decision justifies it.

---

# 4. DDD And Vertical Slice Rules

- Domain language must follow Pazarat central terms.
- Aggregates must represent consistency boundaries, not UI screens.
- Commands mutate state; queries read projected information.
- Use vertical slices for feature/use-case execution while preserving module ownership.
- A slice must declare actor, permission, input contract, validation, affected aggregate/entity, state transition, events, audit, response, and tests.
- Do not create repositories or services because a generic template does so; create them only when the module/use-case needs them.

---

# 5. ASP.NET Core API Rules

- API endpoints are derived from commands/queries and resource semantics, not from page names.
- Controllers or minimal APIs should be thin orchestration edges.
- Use explicit request/response DTOs; do not expose EF entities directly.
- Use ProblemDetails-compatible error responses.
- Validation failures, permission failures, conflict failures, and not-found cases must be distinct.
- Every mutating endpoint must state required permission, idempotency expectation where relevant, audit requirement, emitted events, and tests.
- OpenAPI output must reflect accepted contracts, not generated guesses.

---

# 6. EF Core And PostgreSQL Rules

- Persistence design follows entities, relationships, invariants, and runtime facts derived from accepted PRDs.
- Use explicit entity configurations; do not hide database shape in accidental conventions when the contract matters.
- Table and column naming must be stable, consistent, and module-aware.
- Use transactions around consistency boundaries; do not open distributed behavior without a recorded design.
- Use optimistic concurrency where concurrent administrative/business changes can conflict.
- Query projections should avoid over-fetching and N+1 behavior.
- PostgreSQL features such as JSONB, indexes, constraints, generated columns, and full text search require an explicit reason.
- Sensitive or audit-relevant fields require ownership, visibility, and retention decisions.

---

# 7. Migration Rules

- Migrations are not casual code output; they are contract changes.
- Every migration must be traceable to an accepted artifact or implementation contract.
- Avoid destructive migrations without a recorded data-migration strategy.
- Prefer additive changes when business continuity matters.
- Seed data must be owned and versioned; do not hide policy decisions in seed files.
- Migration tests or database integration checks are required for important schema changes.

---

# 8. Realtime / SignalR Rules

Pazarat is a large operational platform. Realtime behavior is not a cosmetic UI enhancement when operations depend on live states, approvals, notifications, order progress, support, logistics, or administrative queues.

Rules:

- Use SignalR for realtime delivery when accepted workflows require live operational synchronization.
- Hubs must not contain business logic.
- Domain/application events drive realtime notifications; hubs deliver messages.
- SignalR groups are routing tools, not authorization boundaries.
- Authorization must be checked before group membership or data delivery.
- Reconnect/resync behavior is mandatory for state-sensitive clients.
- Clients must be able to recover missed updates from query APIs or projections.
- Redis backplane is required when SignalR scales across multiple application instances.
- Critical events must not depend only on transient websocket delivery; use outbox/event persistence where loss would break business correctness.
- Realtime message names, channels, payload shape, permissions, and tests must be documented in the implementation contract.

---

# 9. Redis Rules

- Redis is allowed for cache, distributed coordination, SignalR backplane, rate limiting, and short-lived operational state when appropriate.
- Redis must not become the source of truth for durable business facts.
- Cache keys, invalidation rules, TTLs, and fallbacks must be explicit.
- If Redis supports realtime scale-out, the fallback when Redis is unavailable must be defined.

---

# 10. Outbox And Event Dispatch Rules

- Use an outbox pattern when a database change must reliably result in an event, notification, integration call, or realtime update.
- Emit events from application/domain logic after accepted state transitions, not from controllers or UI handlers.
- Event payloads should carry stable identifiers and minimal data needed by consumers.
- Consumers must be idempotent where duplicate delivery is possible.
- Event names must align with `03_PLATFORM_EVENT_TAXONOMY.md` or be marked as proposed candidates.

---

# 11. Background Worker Rules

- Workers must have explicit ownership, retry policy, failure handling, observability, and idempotency.
- Workers must not hide core business decisions outside PRDs or implementation contracts.
- Scheduled jobs must document frequency, trigger, affected data, lock strategy, and tests.

---

# 12. Authorization And Permissions Rules

- Every sensitive command, queue, review action, export, configuration change, and data view must have a permission gate.
- Do not use role names alone as authorization logic.
- Permission names must align with shared primitives and the roles/permissions owner.
- Frontend hiding is not authorization.
- Audit and permission checks must be visible in implementation contracts.

---

# 13. Validation Rules

- Validation is layered: DTO shape, business rules, state transition rules, policy rules, and cross-module constraints are not the same.
- Do not duplicate validation rules across UI and backend without a shared owner or contract.
- Validation messages should be stable enough for frontend and localization.
- Important validation rules require tests.

---

# 14. Error Handling Rules

- Use consistent ProblemDetails-style responses.
- Separate validation, authentication, authorization, not-found, conflict, stale-state, and internal failures.
- Do not leak sensitive implementation details.
- State transition conflicts must explain safe next action where possible.

---

# 15. Audit Logging Rules

- Audit is required for sensitive administrative, financial, verification, approval, permission, policy, security, and data-export actions.
- Audit entries must include actor, action, target, before/after where appropriate, reason, correlation id, timestamp, and source.
- Audit logs must not be mutable business notes.
- Audit visibility is itself permissioned.

---

# 16. Observability Rules

- Important flows require structured logging, metrics, traces, and correlation identifiers.
- Use OpenTelemetry-compatible thinking where practical.
- Logs must not leak secrets, credentials, private documents, tokens, or sensitive personal data.
- Background jobs, integrations, realtime delivery, and critical state transitions must be observable.

---

# 17. Testing Rules

Production-oriented implementation requires tests mapped to project truth.

Test categories:

- unit tests for pure domain and validation logic;
- application/use-case tests for commands and queries;
- integration tests for EF Core/PostgreSQL, migrations, transactions, and API contracts;
- authorization tests for permission gates;
- state transition tests;
- event emission tests;
- audit tests;
- realtime reconnect/resync tests where applicable;
- architecture tests for module boundaries and forbidden dependencies;
- regression tests for repaired incomplete truth.

Testing is not an afterthought. If the implementation contract cannot produce tests, it is not mature enough for code.

---

# 18. Frontend Synchronization Rules

- Frontend state must not invent backend states, events, permissions, or lifecycle names.
- Realtime updates must reconcile with query APIs after reconnect or suspected staleness.
- UI actions must expose disabled states and failure reasons from accepted backend rules.
- Sensitive data visibility is governed by permissions, not UI convenience.

---

# 19. Naming Rules

- Use Pazarat central terminology for states, events, capabilities, approvals, verification, stores, accounts, and permissions.
- Avoid generic names such as `Manager`, `Helper`, `Service`, `Processor`, or `Handler` unless the role is precise and owned.
- Endpoint, command, event, and test names must communicate business intent and lifecycle effect.

---

# 20. Forbidden Patterns

- Code from stack name only.
- API from page name only.
- Business logic inside controllers, SignalR hubs, or frontend components.
- EF entities exposed as public API DTOs.
- Local state/event names that bypass central taxonomy.
- Authorization by UI hiding only.
- Redis as durable truth.
- Realtime without reconnect/resync strategy.
- Migration without ownership and rollback/migration discipline.
- Outbox needed but skipped for critical cross-boundary events.
- Tests as optional future work.
- Implementing a proposed repair before it becomes accepted truth.

---

# 21. Code Review Checklist

Before accepting generated or written code, verify:

1. Which artifact or decision owns this behavior?
2. Which module owns it?
3. Which actor and permission can use it?
4. Which state transition occurs?
5. Which event is emitted?
6. Which audit entry is written?
7. Which database relationship or migration is affected?
8. Which API contract exposes it?
9. Which frontend behavior consumes it?
10. Which tests prove it?
11. Which observability signals trace it?
12. Did any reference become incomplete truth that must be repaired first?

---

# 22. Relationship To Incomplete Truth

If this canon does not cover a required implementation pattern, do not invent the pattern silently.

Classify the missing pattern as:

```txt
Code Practice Canon Incomplete Truth
```

Then update this canon or record an explicit decision before production-oriented execution.
