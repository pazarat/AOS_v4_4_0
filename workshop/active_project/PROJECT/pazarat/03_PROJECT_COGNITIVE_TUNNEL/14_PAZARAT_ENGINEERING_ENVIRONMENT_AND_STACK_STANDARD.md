# PAZARAT ENGINEERING ENVIRONMENT AND STACK STANDARD

# Purpose / الهدف

This file defines the binding programming environment, stack, repository structure, development tooling, quality gates, and deployment readiness standard for Pazarat.

It is the third direction of the Pazarat 360-degree engineering loop.

It ensures that PRD-to-code translation does not produce generic code, unsupported frameworks, disconnected database schemas, or deployment-unready implementation.

هذا الملف يحدد بيئة البرمجة الشاملة التي يجب أن يلتزم بها أي توليد أو تجهيز كود في بازارات.

---

# 1. Binding Stack Decision / قرار التقنية الملزم

Current accepted Pazarat stack:

```txt
Primary editor: VS Code
Backend platform: .NET
Backend web framework: ASP.NET Core Web API
Backend language: C#
Backend architecture: Modular Monolith + DDD boundaries + Vertical Slice use cases
Database: PostgreSQL
Database access: EF Core with Npgsql provider; Dapper only for justified high-performance read paths
Frontend framework: Next.js App Router
Frontend language: TypeScript
API style: HTTP APIs / REST-style resources unless a documented contract says otherwise
API documentation: OpenAPI
Local orchestration: Docker + .NET Aspire when multi-resource local coordination is needed
CI/CD: GitHub Actions
Deployment target: AWS-ready, with final AWS service selection controlled by later deployment ADRs
```

This decision is project truth until changed by explicit user decision or an ADR-level stack migration.

---

# 2. Forbidden Stack Drift / منع الانحراف التقني

The model must not propose or generate production-oriented Pazarat backend code using NestJS, Express, Laravel, Django, FastAPI, Rails, Spring Boot, Go services, PHP services, or any non-.NET backend framework unless the user explicitly requests stack reconsideration or an ADR comparison.

The model must not replace PostgreSQL with MySQL, MongoDB, SQLite, DynamoDB, or another database unless the user explicitly requests a database decision review.

The model must not replace Next.js with another frontend framework unless the user explicitly requests a frontend stack decision review.

When discussing alternatives, classify them as alternatives, not Pazarat project truth.

---

# 3. Developer Workstation Standard / معيار جهاز المطور

Required baseline tools:

```txt
Git
.NET SDK
Node.js LTS
pnpm
Docker Desktop or Docker Engine
PostgreSQL client tools
VS Code
```

Recommended tools:

```txt
GitHub CLI
AWS CLI
Terraform CLI
DBeaver, pgAdmin, or DataGrip
```

The project should avoid undocumented machine-local assumptions.

Local setup must be reproducible through repository scripts, Docker, Aspire AppHost, `.env.example`, and documented setup steps.

---

# 4. IDE / Code Editor Standard / معيار محرر الكود

VS Code is the primary project editor because Pazarat includes backend, frontend, documentation, YAML gates, Docker, GitHub Actions, infrastructure files, and AI-readable project standards.

Recommended VS Code extensions:

```txt
C# Dev Kit
C#
ESLint
Prettier
Docker
Dev Containers
GitHub Actions
GitLens
YAML
Markdown All in One
EditorConfig
REST Client or Thunder Client
Terraform
PostgreSQL Explorer
```

Visual Studio and JetBrains Rider may be used for deep .NET work, but they do not replace VS Code as the cross-stack project reference editor.

---

# 5. Repository Strategy / استراتيجية المستودع

Pazarat should use a repository structure that supports documentation, backend, frontend, database, infrastructure, tests, and AI generation contracts.

Recommended top-level structure when code begins:

```txt
pazarat/
  docs/
  backend/
  frontend/
  database/
  infra/
  .github/
  scripts/
```

If the source code lives in the same repository as the Mind_Ai tunnel, code folders must remain clearly separated from project standards.

If the source code lives in a separate product repository, this standard must be copied or referenced as the binding engineering environment standard.

---

## 5.1 Codebase Integration Mode / وضع دمج المشروع البرمجي

When Pazarat is transformed into a full software repository, the repository must be understood as one project root that includes documentation and implementation together.

The correct concept is:

```txt
pazarat/ = full software project repository
```

Inside it:

```txt
root Mind_Ai entry files and general layers = operating method and expert engine
02_MY_PROJECT/pazarat/ = Pazarat local control plane and traceability
/docs = Pazarat product/developer documentation
/backend = ASP.NET Core / .NET backend implementation
/frontend = Next.js frontend implementation
/database = PostgreSQL schemas, migrations, seeds, read models
/infra = infrastructure and deployment artifacts
/scripts = repeatable developer/model operations
/tests = cross-cutting tests when not owned by backend/frontend
```

`docs/` must not be used to bury the general Mind_Ai tunnel. The general tunnel is an operating layer, not ordinary project documentation.

If existing Pazarat documentation branches such as `A_dashboards`, `B_web_frontend`, or `C_mobile_app` are migrated into `docs/`, the migration must be controlled by `17_PAZARAT_CODEBASE_INTEGRATION_AND_DOCUMENTATION_ROUTING_STANDARD.md` and a before/after routing map.

Any generated ZIP or codebase scaffold must preserve this distinction before claiming that the structure is integrated.



# 6. Backend Solution Structure / هيكل الباك اند

Recommended .NET solution structure:

```txt
backend/
  Pazarat.sln

  src/
    Pazarat.Api/
    Pazarat.AppHost/
    Pazarat.ServiceDefaults/
    Pazarat.SharedKernel/

    Pazarat.Modules.Identity/
    Pazarat.Modules.Users/
    Pazarat.Modules.Merchants/
    Pazarat.Modules.Catalog/
    Pazarat.Modules.Orders/
    Pazarat.Modules.Payments/
    Pazarat.Modules.Shipping/
    Pazarat.Modules.Notifications/
    Pazarat.Modules.Admin/

  tests/
    Pazarat.Api.Tests/
    Pazarat.IntegrationTests/
    Pazarat.ArchitectureTests/
```

Each module may use:

```txt
Domain/
Application/
Infrastructure/
Presentation/
Contracts/
Tests/
```

The exact module list must be derived from accepted PRDs and the project structure tree, not invented from generic marketplace assumptions.

---

# 7. Backend Architecture Standard / معيار معمارية الباك اند

The backend should begin as a Modular Monolith, not premature microservices.

Rules:

- organize by bounded business modules
- expose use cases through vertical slices
- keep domain logic out of controllers
- keep infrastructure details out of domain logic
- keep cross-module references explicit
- use central state/event terminology
- use shared primitives instead of duplicating behavior
- isolate integration/event/outbox concerns when needed

Preferred implementation concepts:

```txt
Commands
Queries
Handlers
Validators
Authorization policies
Domain entities
Value objects
Domain events
Audit records
Repository or persistence abstractions when justified
Integration boundaries
```

Microservices, Kafka, complex event sourcing, Kubernetes, and service mesh should be deferred until the product and operational needs justify them.

---

# 8. Database Standard / معيار قاعدة البيانات

PostgreSQL is the accepted relational database.

Database design must derive from documented entities, ownership, lifecycle, relationships, implementation contracts, and `16_PAZARAT_DATA_MODEL_DATABASE_API_AND_ENDPOINT_STANDARD.md`.

Rules:

- apply `16_PAZARAT_DATA_MODEL_DATABASE_API_AND_ENDPOINT_STANDARD.md` before proposing schema, relationship, or endpoint-level implementation
- schema changes must use migrations
- no manual production schema drift
- tables must reflect business ownership
- state storage must align with the state taxonomy
- event/audit storage must align with the event taxonomy and shared primitives
- indexes must support documented queries and filters
- constraints should protect critical invariants where appropriate
- JSONB may be used for justified flexible metadata, not as a replacement for modeled core domain data

EF Core migrations are the default migration mechanism unless an ADR changes this.

---

# 9. API Contract Standard / معيار واجهات API

Default API style:

```txt
HTTP APIs / REST-style resources
OpenAPI documentation
ProblemDetails error format
Pagination, filters, sorting, and idempotency when relevant
Authorization policies for protected operations
```

API operations must be derived from use cases, commands, queries, transitions, permissions, and the endpoint extraction rules in `16_PAZARAT_DATA_MODEL_DATABASE_API_AND_ENDPOINT_STANDARD.md`, not from frontend button names alone.

API route naming must remain stable, descriptive, and module-aware.

Public or long-lived client-facing API changes require versioning consideration.

---

# 10. Frontend Standard / معيار الفرونت اند

Frontend stack:

```txt
Next.js App Router
TypeScript
Design system aligned with Pazarat UI/UX standard
React Hook Form + Zod when form complexity requires it
Server Components first where appropriate
Client components only where interactivity requires them
```

Frontend work must derive from PRDs, screen artifacts, UI/UX standards, permissions, states, events, and API contracts.

Screens must not invent backend behavior, permissions, or state transitions.

Reusable UI patterns must synchronize with the UI/UX standard and shared primitives.

---

# 11. Local Development Runtime / بيئة التشغيل المحلية

Local development should support repeatable startup of:

```txt
ASP.NET Core API
Next.js frontend
PostgreSQL
Redis when needed
Workers when needed
Observability dashboard when needed
```

Use Docker for containerized dependencies.

Use .NET Aspire AppHost when multiple resources must be coordinated with service discovery, configuration injection, startup ordering, and local observability.

Aspire is not a replacement for ASP.NET Core, Docker, GitHub Actions, AWS, or production runtime.

It is a development-time orchestration and observability layer that helps run and inspect the local distributed application shape.

---

# 12. Testing Standard / معيار الاختبار

Backend testing tools:

```txt
xUnit
FluentAssertions
NSubstitute or Moq
WebApplicationFactory
Testcontainers for PostgreSQL integration tests
NetArchTest or ArchUnitNET for architecture rules
```

Frontend testing tools:

```txt
Vitest
React Testing Library
Playwright for E2E
```

Testing rules:

- acceptance criteria must become tests when implementation begins
- state transitions need tests
- permissions need tests
- filters and pagination need tests
- database constraints and migrations need tests where risk is high
- API behavior must be tested against documented contracts
- architecture tests should protect module boundaries

---

# 13. Code Quality Standard / معيار جودة الكود

Required quality files and practices:

```txt
.editorconfig
dotnet format
.NET analyzers
nullable enabled
TreatWarningsAsErrors for critical backend projects
ESLint
Prettier
TypeScript strict mode
```

Generated code must be readable, testable, and aligned with project naming.

The model must not generate large unreviewable files when a smaller vertical slice or implementation contract is safer.

---

# 14. Security Standard / معيار الأمن

Security must be considered from the start.

Required concerns:

- authentication approach
- policy-based authorization
- role and permission mapping
- input validation
- output shaping
- secrets outside Git
- CORS rules
- rate limiting where needed
- audit logs for sensitive actions
- PII classification where relevant
- secure error behavior

Security decisions must be documented before production exposure.

---

# 15. Observability Standard / معيار المراقبة

Pazarat implementation should support:

```txt
Structured logs
Metrics
Distributed tracing
Health checks
Audit logs
Error tracking
Performance diagnostics
```

Local observability may use Aspire Dashboard.

Production observability may use AWS CloudWatch, OpenTelemetry collectors, Grafana/Prometheus, or another ADR-approved stack.

Observability must be attached to real lifecycle and failure points, not added only as generic logging.

---

# 16. GitHub Standard / معيار GitHub

GitHub is the source control and workflow control surface.

Rules:

- no direct push to protected main when code work begins
- pull requests require CI checks
- branch protection should be configured
- issues/labels should distinguish PRD, backend, frontend, database, infra, security, and AI-generation work
- major stack decisions require ADR or explicit project decision

Suggested workflows:

```txt
ci.yml
backend.yml
frontend.yml
database.yml
security.yml
staging-deploy.yml
production-deploy.yml
```

---

# 17. CI/CD Standard / معيار النشر والتحقق

Pull request checks should include:

```txt
restore
build
lint
format check
test
typecheck
migration check
security/dependency check
```

Main branch or release workflow should prepare deployable artifacts.

Staging and production must be separated.

Production deployment should require approval and rollback awareness.

---

# 18. Deployment Readiness Standard / معيار الجاهزية للنشر

Pazarat must be AWS-ready, but it must not prematurely lock into one AWS service without an ADR.

Likely AWS mappings:

```txt
Backend: ECS Fargate or another ADR-approved compute target
Database: Amazon RDS PostgreSQL
Storage: S3
Secrets: AWS Secrets Manager or Parameter Store
Queues: SQS when needed
Email/notifications: SES/SNS when needed
Observability: CloudWatch/OpenTelemetry pipeline
```

Infrastructure should eventually be represented with Terraform or another accepted Infrastructure-as-Code approach.

---

# 19. Versioning And Release Standard / معيار الإصدارات

The project should eventually define:

- semantic versioning or release train policy
- database migration release order
- API compatibility policy
- changelog policy
- rollback policy
- environment promotion flow

Until then, code generation should avoid irreversible production assumptions.

---

# 20. AI Code Generation Guardrails / ضوابط توليد الكود بالنموذج

Before generating code, the model must verify:

- source PRD or implementation contract exists
- central state/event/primitive alignment is checked
- target stack is ASP.NET/.NET, PostgreSQL, Next.js unless explicitly changed
- file paths match the accepted structure or are clearly proposed
- migrations are included when database schema changes
- tests are included or gap-labeled
- generated output is a vertical slice when the full feature is too large
- assumptions are classified

The model must not silently invent:

- final endpoint names
- table schemas
- state names
- event names
- permission names
- module ownership
- deployment services
- package choices

---

# 21. Maintenance And Upgrade Policy / سياسة الصيانة والتحديث

Technology upgrades must be deliberate.

When a library, framework, runtime, or cloud service changes, update:

- this environment standard
- implementation standard if translation is affected
- runtime gates if enforcement is affected
- affected PRDs or implementation contracts if behavior changes
- CI/CD workflows if build/test/deploy changes

Do not let generated code drift away from the documented engineering environment.

---

# 22. Engineering Environment Alphabet / أبجدية بيئة التطوير والبرمجة

This section is the compact reference map for the accepted Pazarat engineering environment.

It does not replace the detailed standards above. It gives the model, engineer, designer, and reviewer a simple alphabet to read before any environment setup, code generation, implementation planning, or code review.

هذه الفقرة هي الخريطة المختصرة لأبجدية بيئة التطوير في بازارات. لا تستبدل التفصيل السابق، بل تختصره كمرجع سريع يمنع الانحراف ويذكّر النموذج بالبيئة التي يجب أن يولّد داخلها.

## 22.1 Core Stack Alphabet

```txt
Editor:
- VS Code as the primary cross-stack project editor
- Visual Studio or JetBrains Rider as optional deep .NET IDEs

Backend:
- .NET
- C#
- ASP.NET Core Web API
- Modular Monolith
- DDD boundaries
- Vertical Slice use cases

Backend support:
- EF Core
- Npgsql PostgreSQL provider
- FluentValidation
- OpenAPI / Swagger
- ProblemDetails
- Health Checks
- OpenTelemetry
- Structured logging
- Dapper only for justified high-performance read paths

Frontend:
- Next.js App Router
- TypeScript
- Pazarat UI/UX Design System
- React Hook Form when form complexity requires it
- Zod when frontend validation contracts require it
- Server Components first when appropriate
- Client Components only when interaction requires them

Database:
- PostgreSQL
- EF Core migrations
- PostgreSQL client tools
- JSONB only for justified metadata, not core domain replacement

Local development:
- Docker
- .NET Aspire AppHost when local multi-resource orchestration is needed
- .env.example
- reproducible setup scripts
- optional Dev Containers

Testing:
- xUnit
- FluentAssertions
- NSubstitute or Moq
- WebApplicationFactory
- Testcontainers for PostgreSQL integration tests
- NetArchTest or ArchUnitNET
- Vitest
- React Testing Library
- Playwright

Quality:
- .editorconfig
- dotnet format
- .NET analyzers
- nullable enabled
- TreatWarningsAsErrors for critical backend projects
- ESLint
- Prettier
- TypeScript strict mode

Source control:
- Git
- GitHub
- protected main branch when code work begins
- pull requests
- required CI checks
- explicit ADR for major stack changes

CI/CD:
- GitHub Actions
- restore
- build
- lint
- format check
- test
- typecheck
- migration check
- security/dependency check
- staging and production separation

Deployment readiness:
- AWS-ready
- Dockerized deployable services
- Amazon RDS PostgreSQL as likely database target
- S3 for storage when needed
- Secrets Manager or Parameter Store for secrets
- SQS for queues when needed
- SES/SNS for email/notifications when needed
- CloudWatch/OpenTelemetry pipeline for observability
- Terraform or another accepted IaC tool when infrastructure is formalized

Documentation and AI generation:
- Pazarat 360-degree method
- PRD cognition and traceability standard
- narrative/scenario maturity standard
- parent-child routing standard
- implementation translation contract
- implementation architecture and code generation standard
- shared primitives and continuity memory
- central state taxonomy
- central event taxonomy
- UI/UX design system standard
- engineering environment standard
- runtime YAML gates
```

## 22.2 Forbidden Alphabet Drift

The alphabet above is binding project truth.

The model must not substitute it with a different backend framework, database, frontend framework, repository pattern, deployment model, testing stack, or terminology set unless the user explicitly requests a stack review or ADR-level migration.

Examples of forbidden drift:

```txt
- Replacing ASP.NET Core with NestJS, Laravel, Django, FastAPI, Spring Boot, Rails, or Go services without an ADR.
- Replacing PostgreSQL with MongoDB, MySQL, SQLite, DynamoDB, or another database without an ADR.
- Replacing Next.js with another frontend framework without an ADR.
- Inventing state, event, permission, endpoint, module, or database terminology outside central references.
- Generating code without checking the 360-degree loop.
```

## 22.3 Reading Rule

Before any meaningful code generation or programming-environment decision, read this alphabet in this order:

```txt
1. 360 method
2. central references: states, events, shared primitives, UI/UX
3. PRD or child PRD source
4. implementation translation contract
5. engineering environment alphabet
6. target file structure
7. tests and CI/CD expectations
```

If the requested output conflicts with this alphabet, classify the conflict before generating code.



---

# Code Practice Canon Link / ربط معيار ممارسات الكود

This file selects and constrains the engineering environment. It is not sufficient by itself for production-oriented code generation.

Any backend, frontend, database, realtime, worker, migration, test, CI/CD, or implementation contract must also obey:

```txt
18_PAZARAT_CODE_PRACTICE_AND_IMPLEMENTATION_CANON.md
```

If this stack standard names a technology but the practice canon does not explain how Pazarat uses it, classify the relevant area as **Engineering Environment Incomplete Truth** and repair the owner before production-oriented execution.

---

# Realtime-First Operational Standard

Pazarat is a large operational commerce platform with administrative queues, verification, approvals, notifications, orders, logistics, support, financial workflows, audit, and cross-role coordination.

When accepted workflows require live operational synchronization, realtime is a first-class architectural concern, not a cosmetic enhancement.

Baseline direction:

```txt
SignalR for realtime delivery
Redis backplane for multi-instance scale-out
Reconnect/resync behavior for clients
Query/API recovery for missed messages
Outbox or durable event dispatch for critical state-changing effects
Permission-aware group membership and data delivery
```

This does not mean every screen must be realtime. It means any workflow that depends on live state must be evaluated through the realtime/code-practice gates before implementation.
