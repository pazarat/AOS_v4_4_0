# PAZARAT RAW TO PROGRAMMATIC NARRATIVE WEAVING STANDARD

# Purpose

This file defines the Pazarat-wide method for converting any raw user explanation into a mature scenario whose prose is woven from correct product, programming, database, API, and environment semantics.

It exists because organizing a scenario into headings is not enough, and because no single scenario type may define the method for all other scenarios.

A scenario can be well-sectioned and still be wrong if the prose copies the raw order, repeats scattered examples, hides the real entity spine, or explains business ideas without showing how the system would actually record, relate, filter, and execute them.

This standard is universal for all Pazarat scenario types: governance, users, stores, products, orders, finance, shipping, dashboards, workflows, screens, APIs, database logic, and implementation contracts.

It strengthens:

- `09_PAZARAT_NARRATIVE_SEQUENCE_AND_SCENARIO_MATURITY_STANDARD.md`
- `10_PAZARAT_PARENT_CHILD_SEQUENCE_AND_CROSS_ARTIFACT_ROUTING_STANDARD.md`
- `11_PAZARAT_PRD_DOCUMENTATION_AND_IMPLEMENTATION_TRANSLATION_CONTRACT.md`
- `13_PAZARAT_360_DEGREE_ENGINEERING_METHOD.md`

It does not replace them.

---

# Universal Raw-To-Gold Rule

The model must treat raw input as project evidence, not as the final scenario structure.

The user may describe an idea with repetition, mixed order, non-technical wording, partial examples, or an inaccurate mental model of where the logic belongs.

The Expert Engineer must not simply clean the language or divide the raw text into sections.

The required transformation is:

```txt
Raw scattered intent
→ concept extraction
→ programming/database/API interpretation
→ ownership and relationship correction
→ 360 alignment
→ woven scenario
→ translation-ready artifact
```

A mature scenario is therefore not measured by headings alone.

It is measured by whether its narrative reflects how the system would actually be modeled, stored, related, filtered, executed, exposed through endpoints, rendered in UI, tested, and maintained.

## General Applicability

This rule applies to every scenario, not only country-context scenarios.

Examples:

- In User Management, the model must understand account identity, capabilities, verification records, roles, sessions, permissions, and lifecycle before writing prose.
- In Products, the model must understand catalog identity, seller/store ownership, category references, inventory, pricing, media, moderation, and visibility rules before narrating product behavior.
- In Orders, the model must understand buyer, seller, line items, payment, fulfillment, delivery address, state transitions, financial effects, and cancellation/return paths before describing the journey.
- In Finance, the model must separate calculation logic, configurable rates, transaction facts, ledger records, invoices, payouts, and audit trails before writing a financial scenario.
- In Shipping, the model must separate delivery policy, route capability, carrier responsibility, shipment records, tracking states, and handoff responsibility before describing shipping flow.

The scenario must be written after these structures are understood, not before.

---

# Core Principle

Raw input is not a scenario.

Raw input is evidence.

The model must not parrot raw explanation, raw repetition, raw order, or raw emphasis as if that were maturity.

The model must transform raw input through four gates before producing a serious scenario:

1. **Programmatic Semantics Gate** — what is the code/database meaning?
2. **Identity Spine Gate** — what stable root identity owns the chain?
3. **Variable Configuration Gate** — what is actual domain logic, and what is only a changeable value/configuration under that logic?
4. **Relational Data Gate** — how would identities, records, references, constraints, and filters exist in the database?
5. **API/Endpoint Gate** — what operations must be exposed as commands, queries, endpoints, contracts, and permission-protected transitions?
6. **Environment Fit Gate** — how does the idea fit the accepted stack and repository architecture?
7. **Narrative Weaving Gate** — how should the idea be narrated so every paragraph naturally leads to the next?

The final scenario must feel like a coherent operational journey, not a list of fragments.

---

# Programmatic Semantics Gate

Before rewriting raw project logic, the model must translate the idea into software semantics.

The model must ask:

- What is written once as domain code?
- What is instantiated many times as data records?
- What is a stable identity?
- What is a foreign-key relationship or ownership chain?
- What is a configurable value?
- What is a runtime action?
- What is a filter over existing relations?
- What is a policy matrix?
- What is only a UI surface over underlying data?

## Required Distinction

The model must distinguish between:

| Concept Type | Meaning | Example |
|---|---|---|
| Code Blueprint | Logic implemented once | Account model, tax calculation flow, shipping flow |
| Stable Identity | A root or important persisted identity | `CountryContextId`, `AccountId`, `StoreId`, `OrderId` |
| Relationship Spine | Persistent relations between identities | Account belongs to CountryContext; Store belongs to Account |
| Configurable Value | Value that differs by country, policy, or time | tax rate, commission rate, verification requirement |
| Runtime Fact | Actual operation record | order created, shipment created, payment captured |
| Filtered View | UI/search projection over existing relations | products visible when filtering by Lebanon |
| Policy Matrix | Rule table deciding allowed interactions | buyer country + store country + delivery country |

The model must not describe a filtered view as if it were a new ownership model.

---

# Relational Data And Endpoint Reflection Gate

Before final scenario prose is accepted, the model must reflect the idea against likely data and endpoint reality.

This does not mean every scenario must contain full schema or full API design.

It means the prose must not contradict the way the system would later be modeled.

The model must ask:

- Which identity would become a persisted aggregate, entity, table, or document?
- Which values are attributes of that identity, and which values belong to another owner?
- Which relations explain visibility, filtering, ownership, authorization, and lifecycle?
- Which facts are historical records rather than current settings?
- Which changes require versioning, audit, migration, or event emission?
- Which UI actions imply command endpoints?
- Which screens imply query endpoints or read models?
- Which transitions require permissions, validation, idempotency, concurrency control, or conflict handling?

The model must not wait until code generation to discover that the scenario was written against the wrong data model.

If the raw idea requires data modeling maturity, apply:

```txt
16_PAZARAT_DATA_MODEL_DATABASE_API_AND_ENDPOINT_STANDARD.md
```

A scenario may stay at parent depth, but it must still avoid false ownership, false relationships, and endpoint-impossible behavior.

---

# Identity Spine Gate

The first task is to find the root spine.

For Pazarat, common spines include:

- `CountryContext` as the stable operational identity of a country.
- `Base Account` / `Account` as the stable identity of a user.
- `AccountCapability` as an added ability over an account, not a separate account.
- `Store` as a stable commercial identity linked to an account/capability.
- `Product` as a stable catalog identity linked to a store.
- `Order` as a stable transaction identity linked to buyer account, store, products, payment, address, and fulfillment records.

## CountryContext Spine Rule

`CountryContext` is not a page setting.

It is the upper operational identity under which country-scoped platform records and configurations become addressable.

If an account is registered under Lebanon, then the account carries Lebanon as its account country context.

From there, the system can reach the account spine:

`CountryContext → Account → Capabilities → Store → Products → Orders → Financial/Shipping/Support records`

This does not mean every product must be manually documented as “inside Lebanon” in every scenario.

If the product belongs to a store, and the store belongs to an account, and the account belongs to a `CountryContext`, then many country filters can be derived through the relationship chain.

The scenario should explain the spine once and then use it intelligently.

---

# Single-Country Comparison Gate

When the user discusses multi-country behavior, the model must first run a single-country comparison.

Ask:

> If Pazarat worked in one country only, where would this logic live?

Then ask:

> When Pazarat works in many countries, what changes: the logic itself, or only the values/settings attached to each country?

## Rule

If the logic would belong to a domain in a one-country system, it usually remains in that domain in a multi-country system.

What changes is that the domain exposes country-scoped configurations instead of a single fixed form.

Examples:

| One-Country Form | Multi-Country Expression | Owner Stays |
|---|---|---|
| One verification requirements form | Verification requirements per `CountryContext` | User Management / Verification Template |
| One tax settings form | Tax settings per `CountryContext` | Financial / Tax Management |
| One commission form | Commission settings per `CountryContext` and interaction policy | Financial / Commission |
| One terms form | Terms/policy version per `CountryContext` | Legal/System/Governance according to project decision |
| One shipping settings form | Shipping settings per `CountryContext` and delivery relation | Operations / Shipping |

The model must not turn every country-scoped value into a new domain.

CountryContext provides the identity and routing context.

The owning domain still owns the form logic, validation, calculation, workflow, and implementation behavior.

---

# Variable Configuration Bundle Rule

The phrase “country operational bundle” must mean:

> the collection of country-scoped configurable values and references required by different owning domains.

It must not mean:

- a replacement for Financial logic
- a replacement for Shipping logic
- a replacement for User Management logic
- a replacement for Category/Product logic
- a new copy of every module for every country

The bundle is a coordination view over configurable values.

Each value still belongs to its owning domain.

## Correct Example

Tax logic remains in Financial / Tax Management.

When Pazarat had only Syria, the tax page could be a single form.

When Pazarat supports Syria, Lebanon, Egypt, and other countries, the same tax form logic becomes country-scoped tax settings.

The system does not create a new tax engine for Lebanon.

It creates or exposes a Lebanon tax configuration that the same tax engine reads when the transaction context requires it.

---

# Matrix Logic Rule

Cross-country interaction must not be repeated across many children.

When the question is:

- Can a buyer from one country view another country’s market?
- Can the buyer purchase?
- Can the order be delivered to the buyer country?
- Can delivery be inside the seller country?
- Does Pazarat operate the shipping or does the seller coordinate it externally?
- Is the transaction blocked, allowed, or display-only?

This belongs to one matrix concept:

`Country Interaction Matrix`

The matrix reads:

`Buyer Account Country + Market/Store Country + Delivery Country + Operation Type`

and returns an interaction decision.

Other domains consume the decision.

They do not each redefine it.

---

# Price And Cost Weaving Rule

When explaining cross-country purchase, the model must distinguish between:

- base product price set by the store
- additional cost calculated at checkout
- tax
- shipping
- customs/clearance when applicable
- commission or platform fee when applicable
- responsibility model: Pazarat-operated shipping vs seller-coordinated shipping

The base product price should not be described as changing merely because the buyer is from another country unless a separate price policy is explicitly documented.

The final payable amount may change because the checkout context changes.

Example logic:

`Product base price + country/delivery/tax/shipping/fee calculations = final checkout amount`

---

# 360 Weaving Obligation

Narrative weaving is not a writing style only.

It is the first direction of the 360 method feeding the other directions.

A woven scenario must be capable of rotating into:

- documentation hierarchy and child routing
- implementation translation
- database/entity design
- API and endpoint contracts
- frontend behavior
- environment placement
- tests and acceptance criteria
- future maintenance and refactoring

If a paragraph is beautiful but cannot rotate into these directions, it is not mature Pazarat prose.

If implementation, database design, endpoint extraction, or environment placement reveals a contradiction, the model must rotate backward and repair the scenario rather than patch the code around bad documentation.

---

# Narrative Weaving Gate

After programmatic meaning is clear, the model must weave the scenario.

A woven scenario is not just organized.

It has paragraph continuity.

Each paragraph should answer one operational idea and prepare the next idea.

The preferred paragraph chain is:

1. Establish the stable identity.
2. Explain what is generated or linked under that identity.
3. Explain which values are configurable and which logic remains in owning domains.
4. Explain what happens when an actor uses the system.
5. Explain what the system records.
6. Explain how filtering or display is derived from relationships.
7. Explain how exceptions or cross-context behavior are decided.
8. Explain what is deliberately not owned here.
9. Route the next child or external domain.

## Paragraph Test

For every important paragraph, the model must check:

- Does this paragraph introduce one clear idea?
- Does it depend on the previous paragraph naturally?
- Does it prepare the next paragraph?
- Does it reflect database/code behavior accurately?
- Does it avoid repeating the same idea in different words?
- Does it avoid copying raw explanation order when a better engineering order exists?

---

# Anti-Parrot Rule

The model must never treat raw user explanation as the final narrative structure.

Raw input may be:

- repetitive
- nonlinear
- exploratory
- example-heavy
- emotionally emphasized
- partially technically inaccurate
- correct in intention but weak in architecture

The model’s role is to preserve intent while repairing structure.

The model must not answer like a parrot that repeats raw examples.

The model must rebuild the idea as a coherent product and implementation story.

---

# Failure Signal

A scenario or explanation has failed this standard if:

- it repeats the same country permission logic in several sections
- it lists headings without explaining the spine
- it says “operational bundle” without defining what is code, value, record, or relation
- it treats country-scoped values as if they were independent domain engines
- it explains filtering without tracing the database relationship chain
- it uses the user’s examples but fails to derive the underlying architecture
- it is understandable only after the user corrects the engineering meaning
- it has correct boundaries but weak narrative weave

When this happens, the model must rebuild from programmatic semantics first, then rewrite the narrative.

---

# Acceptance Gate

Before accepting a parent or child scenario as mature, verify:

1. Is the stable identity clear?
2. Is the entity spine clear?
3. Is the single-country vs multi-country distinction clear?
4. Is the difference between domain logic and country-scoped values clear?
5. Is filtering explained through relationships, not duplicated ownership claims?
6. Is cross-country behavior centralized into a matrix when needed?
7. Are examples used to reveal architecture, not to replace architecture?
8. Does the prose flow from idea to idea without fragmentation?
9. Does every paragraph improve understanding?
10. Can a developer infer the database relationship direction without guessing?
11. Can a designer infer the screen behavior without inventing business logic?
12. Can a future PRD child inherit the idea without re-explaining the parent?

If these checks fail, the scenario is not mature enough.

---

# Project Reality Weave Requirement

The raw-to-programmatic narrative weave must use Pazarat project reality as an active source of correction and completion.

The model must not weave a scenario from the raw text alone.

It must ask how the raw idea fits the Pazarat platform that already exists:

- Which parent or module owns the root identity?
- Which existing section is naturally involved by the lifecycle?
- Which central state or event family is affected?
- Which shared primitive may already own repeated behavior?
- Which data relationship makes the behavior possible?
- Which API, command, query, or endpoint family would later express it?
- Which UI or dashboard branch would expose it?
- Which implementation environment constraint must shape it?
- Which links belong here, and which links must be routed to child or sibling artifacts?

This requirement prevents the model from producing isolated scenarios that are correct locally but disconnected from Pazarat’s full operating lifecycle.

The user does not need to explicitly list every related module in the raw scenario.

The model must infer relevant links from Pazarat reality when justified, but must classify them as confirmed truth, strong inference, recommended completion, open decision, or conflict/risk.

A scenario that ignores obvious Pazarat lifecycle links is incomplete.

A scenario that injects unrelated modules only because they exist is bloated.

The correct weave includes only the project-relevant links needed to make the scenario executable, maintainable, and traceable.
