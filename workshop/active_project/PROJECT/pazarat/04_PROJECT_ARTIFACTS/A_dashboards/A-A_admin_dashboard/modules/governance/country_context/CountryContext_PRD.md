# CountryContext PRD — سياق الدولة

# Artifact Identity

`CountryContext` is the parent PRD for country operating context inside the Governance module.

It defines the stable country identity, the relationship between country identity and platform records, the country-scoped configurable values consumed by other domains, and the matrix that controls interaction between users, markets, stores, and delivery countries.

This file is a parent scenario.

It does not define the detailed tax engine, shipping workflow, verification form, commission calculation, catalog search algorithm, or order fulfillment implementation.

Those details remain in their owning domains.

---

# Parent Scenario Narrative

Pazarat must treat the country as a stable operating identity, not as a temporary option inside a form.

When the platform recognizes Syria, Lebanon, Egypt, or any other supported country, it is not only storing a phone code or a visible label. It is creating a durable `CountryContextId` that other platform records can reference. This identity becomes the upper context under which accounts, market views, country-scoped configurations, and cross-country policies can be understood without rewriting the logic of every module.

The system starts with Syria as the mother operating country. The expansion countries are seeded in code as known country contexts: Lebanon, Jordan, Iraq, Saudi Arabia, Qatar, UAE, Oman, Egypt, Libya, Algeria, and Tunisia. These countries exist as stable identities, but they do not all have to be public, active, or open for registration from day one. The safe default is that Syria is active and the other country contexts remain disabled or unpublished until Pazarat decides to activate them.

Creating or seeding a country context does not create a separate copy of the platform. The account model is still one account model. The order model is still one order model. The tax domain is still one financial domain. The shipping domain is still one operations domain. What changes is that some values and policies are no longer global single values; they become scoped by `CountryContextId` and are read by the same domain logic when an operation needs them.

This is the same principle as `Base Account`. The account structure is coded once, then millions of user accounts can be created as records. Each user has one stable account identity, and the rest of the user spine is related through that identity: capabilities, stores, products, orders, payments, shipping records, support records, and audit signals. `CountryContext` works as the higher country spine. When an account is registered under Lebanon, the account carries Lebanon as its account country. From that point, many views can be derived through relationships: Lebanese users, stores owned by Lebanese accounts, products under those stores, and orders made by or from that country context.

This does not mean the product scenario must manually say that every product is stored inside the Lebanon context. If a product belongs to a store, the store belongs to an account, and the account belongs to Lebanon, then a country filter can derive the product through that chain. The scenario must explain the spine, not duplicate every downstream relationship as a separate country ownership rule.

The operational bundle of a country means the set of configurable country-scoped values and references needed by different domains. It does not mean a new financial system, a new shipping system, or a new User Management system per country. If Pazarat worked only in Syria, tax might be a single form inside Financial / Tax Management. With many countries, the same tax form logic becomes tax settings per country. The tax engine remains Financial. The value it reads may be Syria tax settings, Lebanon tax settings, or Egypt tax settings depending on the transaction context.

The same rule applies to verification, commission, terms, shipping, customs, and similar configurable areas. User Management owns verification logic, but the requirements can be scoped by country. Financial owns commission logic, but the commission values can be scoped by country and by interaction policy. Operations owns shipping logic, but shipping availability and responsibility can depend on country relations and delivery destination. CountryContext gives those domains the country identity and interaction context they need; it does not replace their internal logic.

The user journey preserves a clear difference between account country and market browsing. A user registered under Lebanon remains a Lebanese account even if the user changes the market filter in the header to view Syria. Changing the market filter changes what the user is looking at; it does not rewrite the account identity. The visible categories, stores, and products may now be derived from the Syrian market context, while the buyer account still carries Lebanon as its account country.

This distinction becomes important at checkout. The store sets the base price of the product. That base price does not automatically change only because the buyer is from another country. What may change is the final payable amount after the system applies the relevant tax, shipping, customs, commission, or service rules. A product listed at 12 dollars by a Syrian store can remain 12 dollars as a base price. A Lebanese buyer shipping to Lebanon may see extra costs that make checkout 16 dollars. An Egyptian buyer shipping to Egypt may see a different final amount. A Lebanese buyer shipping to an address inside Syria may see a lower final amount because the delivery country and service context changed.

The logic that decides whether this cross-country operation is allowed must not be repeated inside every domain. CountryContext owns a central `Country Interaction Matrix`. This matrix evaluates the buyer account country, the market or store country, the delivery country, and the operation type. It can decide whether viewing is allowed, whether purchasing is allowed, whether delivery is allowed, whether Pazarat operates shipping, whether the seller coordinates shipping externally, or whether the operation is blocked. Financial, Shipping, Orders, and Catalog consume this decision instead of redefining it.

When Pazarat does not operate shipping for a certain country interaction, the order does not disappear from the platform. The platform may choose not to provide the physical shipping service, but it still records the order, the buyer, the seller, the market country, the delivery country, the shipping responsibility model, the invoice, and the order status. The difference is between owning the logistics service and preserving the transaction record. Pazarat may leave shipping coordination to the seller for a certain relation, while still showing the order and its status to the buyer and seller.

Agents also become clearer through CountryContext. In User Management, an agent is still an account with an added capability. In Governance, that agent may be linked to a specific country context as an operating representative or branch. This gives the agent a country-scoped dashboard and country-scoped responsibilities according to Pazarat policy and contract. The agent does not own the country identity and does not change Pazarat’s global rules. The agent receives delegated operational authority inside a defined country context.

CountryContext must support activation and suspension without destructive deletion. A country identity should not be deleted once it can be referenced by accounts, configurations, orders, or logs. A country can be disabled, hidden from registration, hidden from market filtering, paused for new purchases, blocked for cross-country interaction, or placed under internal-only configuration. These runtime controls protect data continuity while giving Pazarat the ability to stop an unsafe or unfinished context.

The parent purpose of CountryContext is therefore to make country behavior understandable as a spine and matrix. The spine explains how records inherit or derive country relation through stable identities. The matrix explains how interactions between countries are allowed, blocked, priced, routed, or handed to another responsibility model. The configurable bundle explains how each domain keeps its own logic while reading the values that belong to the relevant country context.

---

# Seeded Country Contexts

Initial seeded country contexts:

- Syria — mother operating country, active by default.
- Lebanon — expansion country, disabled/unpublished by default.
- Jordan — expansion country, disabled/unpublished by default.
- Iraq — expansion country, disabled/unpublished by default.
- Saudi Arabia — expansion country, disabled/unpublished by default.
- Qatar — expansion country, disabled/unpublished by default.
- UAE — expansion country, disabled/unpublished by default.
- Oman — expansion country, disabled/unpublished by default.
- Egypt — expansion country, disabled/unpublished by default.
- Libya — expansion country, disabled/unpublished by default.
- Algeria — expansion country, disabled/unpublished by default.
- Tunisia — expansion country, disabled/unpublished by default.

These contexts should be seeded from code/migration rather than created casually from a normal dashboard action.

---

# Core Ownership

CountryContext owns:

- stable country identity
- seeded country list
- country activation/publication controls
- account-country context reference rules
- country-scoped configuration coordination
- Country Interaction Matrix
- relationship between account country, market/store country, and delivery country
- agent-to-country operating context
- non-destructive country runtime controls

CountryContext does not own:

- verification template internals
- tax calculation internals
- commission calculation internals
- shipping execution internals
- product catalog internals
- category management internals
- order lifecycle internals
- payment execution internals
- legal drafting internals

---

# Child Map Candidate

## Country Registry

Displays seeded country contexts, their identity, visibility, activation state, and protected metadata. It prevents destructive deletion and country-code mutation.

## Country Operational Bundle

Shows the country-scoped configurable values and links to their owning domains. It is a coordination view, not the owner of every domain’s internal logic.

## Country Interaction Matrix

Defines allowed and blocked interactions between account country, market/store country, delivery country, and operation type.

## Country Runtime Controls

Controls activation, suspension, public visibility, registration availability, market visibility, purchasing availability, and safe operational pauses.

## Country Agency Context

Links a qualified agent account to a country context and defines the delegated operating scope.

## Country Geo Structure

Defines country-level administrative areas needed by address, delivery, serviceability, and filtering domains without owning shipping execution.

## Country Change Impact Rules

Defines how country-scoped value changes affect new operations, pending operations, existing users, existing orders, policy re-acceptance, and operational continuity.

---

# Scenario Maturity Notes

This parent scenario intentionally explains the database and programming meaning before detailed screens.

The next child should not repeat the whole CountryContext philosophy.

Each child should inherit these rules and then focus on its own local journey.
