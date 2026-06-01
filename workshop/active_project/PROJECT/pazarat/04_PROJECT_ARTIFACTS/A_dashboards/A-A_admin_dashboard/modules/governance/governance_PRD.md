# Governance PRD — الحوكمة التشغيلية

# Purpose

Governance is the admin dashboard domain that owns cross-domain operating context for Pazarat.

It does not replace Business, Financial, Operations, User Management, System, Marketing, or Smart Data.

Its role is to define the stable platform context that those domains consume when their behavior depends on country, policy, eligibility, operating scope, or cross-country interaction.

The first and most important governance child is `CountryContext`.

---

# Parent Scenario

Pazarat is not a single-page marketplace where every rule is global and fixed.

The platform may start with Syria as the mother operating country, but its structure must be able to hold Lebanon, Jordan, Iraq, Saudi Arabia, Qatar, UAE, Oman, Egypt, Libya, Algeria, and Tunisia as future operating contexts without rebuilding the system each time.

This means the platform needs a governance layer that defines the stable identity of each operating context before other domains add their own rules or values.

Governance therefore begins by establishing `CountryContext` as the stable country identity.

After this identity exists, User Management can attach accounts to it, Financial can read country-scoped tax or commission values, Operations can read shipping and serviceability values, Categories can expose country-aware market filtering, and Orders can preserve the actual buyer, market, store, delivery, and fulfillment context.

The governance domain must prevent these rules from being scattered or repeated.

When the question is about who owns account verification, the answer remains User Management.

When the question is about how tax is calculated, the answer remains Financial.

When the question is about how shipping is executed, the answer remains Operations.

When the question is about which country identity, interaction policy, and cross-country relationship the operation belongs to, the answer belongs to Governance and especially `CountryContext`.

---

# Current Children

- `country_context/` — owns the CountryContext parent scenario, stable country identity, country interaction matrix, and country-scoped operating bundle rules.

---

# Boundary Rule

Governance owns context and routing.

Owning domains own their internal workflows.

Governance must not become a duplicate Financial module, duplicate Shipping module, duplicate User Management module, or duplicate Catalog module.
