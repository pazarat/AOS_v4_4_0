# PAZARAT CODEBASE INTEGRATION AND DOCUMENTATION ROUTING STANDARD

# Purpose / الهدف

This file defines how Pazarat documentation, the Pazarat local tunnel, and the future software codebase must be integrated without confusing the model or the developer.

It is a Pazarat-local standard. It applies after the general structural transformation gate has already determined that a codebase integration or repository migration is required.

---

# Core Principle / المبدأ الأساسي

Pazarat must become a software project repository, not a documentation archive with code attached randomly.

However, the Pazarat local tunnel must not be confused with ordinary product documentation.

The correct distinction is:

```text
repository root
  = active project/codebase root

root tunnel files + 00_COGNITIVE_RUNTIME + 01_PROJECT_ORCHESTRATION
  = general Mind_Ai expert engine and entry route

02_MY_PROJECT/pazarat
  = Pazarat local control plane: identity, standards, registries, routing, traceability, project-local decisions

docs/
  = Pazarat product/developer documentation: dashboards, web frontend, mobile app, scenarios, API docs, database docs, architecture notes, decisions

backend/ or src/backend/
  = ASP.NET Core / .NET backend implementation

frontend/ or src/frontend/
  = Next.js frontend implementation

database/
  = PostgreSQL schemas, migrations, seeds, read models, database design artifacts

infra/
  = Docker, deployment, infrastructure, CI/CD, operations
```

---

# Required Codebase Integration Shape

When Pazarat enters codebase-integration mode, the target repository must preserve a single clear root.

Recommended target shape:

```text
pazarat/
  00_AI_REPOSITORY_BOOTSTRAP.md
  00_ENTRY_MAP.md
  ENGINEER_ENTRY_PROTOCOL.md
  00_TUNNEL_EXECUTION_COMMANDS.yaml

  00_COGNITIVE_RUNTIME/
  01_PROJECT_ORCHESTRATION/

  02_MY_PROJECT/
    pazarat/
      numbered local tunnel
      _routing/
      _registries/
      work_items/
      traceability/

  docs/
    A_dashboards/
    B_web_frontend/
    C_mobile_app/
    product/
    architecture/
    scenarios/
    api/
    database/
    decisions/

  backend/
  frontend/
  database/
  infra/
  scripts/
  tests/
  .github/
  .vscode/
```

The exact backend/frontend nesting may be refined by `14_PAZARAT_ENGINEERING_ENVIRONMENT_AND_STACK_STANDARD.md`, but the ownership distinction above is binding.

---

# Forbidden Integration Shapes

The model must not create these structures unless the user explicitly asks for them and the decision is recorded:

```text
pazarat/docs/ai_tunnel/00_COGNITIVE_RUNTIME/
pazarat/docs/ai_tunnel/01_PROJECT_ORCHESTRATION/
pazarat/docs/ai_tunnel/02_MY_PROJECT/
```

Reason: the Mind_Ai tunnel is an operating route, not ordinary documentation.

The model must not create helper folders such as `.ai/` that compete with:

```text
00_AI_REPOSITORY_BOOTSTRAP.md
00_ENTRY_MAP.md
ENGINEER_ENTRY_PROTOCOL.md
```

If a helper map is created, it must explicitly say that the root entry route is higher authority.

---

# Documentation Migration Rule

Existing Pazarat documentation branches such as:

```text
A_dashboards/
B_web_frontend/
C_mobile_app/
```

may be migrated or mirrored into:

```text
docs/A_dashboards/
docs/B_web_frontend/
docs/C_mobile_app/
```

only through a migration map.

The migration map must state:

- source path;
- target path;
- whether the content is moved, copied, mirrored, or referenced;
- which local control-plane file owns routing after migration;
- which traceability or registry file links the documentation to backend/frontend/database artifacts.

Until such migration is executed and verified, the actual repository structure remains the source of truth.

---

# Pazarat Control Plane Rule

`02_MY_PROJECT/pazarat/` remains the Pazarat control plane.

It should own:

- Pazarat identity and objectives;
- central state/event taxonomy;
- 360-degree method;
- engineering environment decisions;
- PRD-to-code translation contracts;
- routing maps;
- registries;
- work items;
- traceability;
- validation gates;
- decision memory.

It should not become the place where all product documentation and all source code are mixed.

---

# Docs Folder Rule

`docs/` is for readable product/developer documentation.

It may include:

- dashboards documentation;
- web frontend documentation;
- mobile app documentation;
- scenarios;
- API documentation;
- database documentation;
- architecture notes;
- decisions/ADRs;
- setup and operations documentation.

It must not become the owner of the general Mind_Ai runtime or orchestration layers.

---

# Code Routing Rule

When a scenario or PRD becomes implementation work, route outputs as follows:

```text
Scenario / PRD truth
  -> docs/ or existing PRD branch, depending on migration state

Project-local standards / decisions / traceability
  -> 02_MY_PROJECT/pazarat/

Backend code
  -> backend/

Frontend code
  -> frontend/

Database schemas/migrations/seeds
  -> database/

Infrastructure and CI/CD
  -> infra/ and .github/

Scripts
  -> scripts/

Tests
  -> backend tests, frontend tests, or root tests depending on test type
```

No code should be generated without a routing decision tying it back to Pazarat documentation and local standards.

---

# Required Validation Before Packaging

Before delivering a Pazarat codebase ZIP or major structural patch, verify:

1. Root entry files remain at the project root.
2. General tunnel layers remain outside ordinary `docs/`.
3. `02_MY_PROJECT/pazarat/` still exists as the local control plane.
4. Product documentation branches are either still in their original location or mapped into `docs/` through a migration map.
5. Backend, frontend, database, and infra folders are clearly separated from documentation and control-plane folders.
6. No duplicated nested route such as `docs/ai_tunnel/docs/ai_tunnel` exists.
7. Any `.ai/` or helper map is subordinate to the root entry route.
8. Traceability/routing files explain where the model writes documentation, code, database changes, and tests.

---

# Final Principle

Pazarat codebase integration must make the repository easier for both the model and a human developer to navigate.

The model must always know:

- where to enter;
- where project truth lives;
- where product documentation lives;
- where backend code lives;
- where frontend code lives;
- where database artifacts live;
- where decisions and traceability live.

If that is not clear, the structure is not ready.
