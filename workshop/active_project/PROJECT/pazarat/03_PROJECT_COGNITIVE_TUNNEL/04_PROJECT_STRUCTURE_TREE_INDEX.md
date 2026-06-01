# PROJECT STRUCTURE TREE INDEX

# Purpose

This file defines the navigational structure of the Pazarat project.

Its role is to help the model locate project standards, project branches, dashboards, modules, parent PRDs, child PRDs, placeholder routes, and implementation-related documentation.

This file is a navigation index.

It is not:

- a documentation protocol
- a PRD quality standard
- a maturity report
- a replacement for dynamic inspection
- a source of truth for whether a file is complete
- a substitute for reading target files

When exact content, maturity, readiness, or current logic matters, inspect the actual file and its relevant parent, child, sibling, standard, decision, and knowledge context.

---

# Core Rules

1. Use this file to locate Pazarat project areas quickly.
2. Do not treat this tree as proof that a file is complete or mature.
3. File existence means the path exists, not that the artifact is finished.
4. Folder existence means the branch exists, not that it is fully documented or implemented.
5. Empty or weak files may be placeholders, route markers, scaffolds, or raw sources.
6. If additional files exist inside a folder, inspect them dynamically.
7. If a numbered local tunnel exists inside any branch, account for it before inspecting non-numbered content.
8. If this file and actual repository structure disagree, the actual repository structure must be inspected and this file should be updated.
9. Update this file when important paths, folders, parent PRDs, child routes, canonical names, or project branches change.
10. Do not add upper-layer behavior or orchestration paths here. This file should describe Pazarat from inside the Pazarat project.

---

# Project Root

Canonical Pazarat project root:

    02_MY_PROJECT/pazarat/

This folder is the local project folder for Pazarat.

The numbered files directly inside this folder are Pazarat project-local standards and indexes.

Non-numbered folders under this root are project content branches.

---

# Pazarat Local Numbered Tunnel

The Pazarat local tunnel is discovered from the actual numbered root files inside this folder.

Any root file directly inside:

    02_MY_PROJECT/pazarat/

that starts with a numeric prefix from `00` to `99` is part of the Pazarat local tunnel unless clearly obsolete, backup, temporary, unrelated, or outside active project scope.

The list below is a navigational snapshot.

It is useful for human readability and quick review, but it is not the only source of tunnel truth.

If additional numbered root files exist in the actual repository, they must be treated as part of the local tunnel even if this index has not been updated yet.

If this index lists a numbered file that does not exist in the actual repository, the model must not assume the file exists. It should classify the reference as missing, stale, expected, or migration-related.

If this index and the actual repository structure disagree, inspect the actual repository structure first, then update this index.

Numeric order determines tunnel traversal order.

File name suggests responsibility.

File content confirms actual purpose.

The current navigational snapshot includes:

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
    10_PAZARAT_PARENT_CHILD_SEQUENCE_AND_CROSS_ARTIFACT_ROUTING_STANDARD.md
    11_PAZARAT_PRD_DOCUMENTATION_AND_IMPLEMENTATION_TRANSLATION_CONTRACT.md
    12_PAZARAT_PRD_AND_CODE_RUNTIME_GATES.yaml
    13_PAZARAT_360_DEGREE_ENGINEERING_METHOD.md
    14_PAZARAT_ENGINEERING_ENVIRONMENT_AND_STACK_STANDARD.md
    15_PAZARAT_RAW_TO_PROGRAMMATIC_NARRATIVE_WEAVING_STANDARD.md
    16_PAZARAT_DATA_MODEL_DATABASE_API_AND_ENDPOINT_STANDARD.md
    99_PAZARAT_PROJECT_REINFORCEMENT_MEMORY.md

These files should be accounted for before producing or revising Pazarat-specific PRDs, workflows, UI artifacts, implementation notes, shared primitives, routing maps, or project decisions.

If additional numbered files are added later, they become part of the Pazarat local tunnel automatically and should be read in numeric order.

---

# Top-Level Project Content Branches

Current top-level content branches:

    A_dashboards/
    B_web_frontend/
    C_mobile_app/

These branches are Pazarat project content.

They should be inspected dynamically according to the user’s request.

---

# Current Project Tree

    pazarat/
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
      10_PAZARAT_PARENT_CHILD_SEQUENCE_AND_CROSS_ARTIFACT_ROUTING_STANDARD.md
      11_PAZARAT_PRD_DOCUMENTATION_AND_IMPLEMENTATION_TRANSLATION_CONTRACT.md
      12_PAZARAT_PRD_AND_CODE_RUNTIME_GATES.yaml
      13_PAZARAT_360_DEGREE_ENGINEERING_METHOD.md
      14_PAZARAT_ENGINEERING_ENVIRONMENT_AND_STACK_STANDARD.md
      15_PAZARAT_RAW_TO_PROGRAMMATIC_NARRATIVE_WEAVING_STANDARD.md
      16_PAZARAT_DATA_MODEL_DATABASE_API_AND_ENDPOINT_STANDARD.md
      99_PAZARAT_PROJECT_REINFORCEMENT_MEMORY.md

      A_dashboards/
        A_PRD_dashboards.md

        A-A_admin_dashboard/
          modules/
            A-A_PRD_admin_dashboard.md

            dashboard/
              dashboard_PRD.md

            governance/
              governance_PRD.md

              country_context/
                CountryContext_PRD.md

            business/
              Business_PRD.md

              User_Management/
                User_Management_PRD.md

                agents/
                  00_PRD_agents.md

                all_users/
                  00_PRD_all_users.md
                  01_PRD_users_Profile_Admin_View.md
                  02_PRDUsers_Profile_User_View.md
                  03_PRD_Navigation_filter.md

                user_approvals/
                  00_PRD_user_approvals.md

                b2b_sellers/
                  00_PRD_b2b_sellers.md

                b2c_sellers/
                  00_PRD_b2c_sellers.md

                staff/
                  00_PRD_staff.md

                user_analytics/
                  00_PRD_user_analytics.md

                verification/
                  00_PRD_verification.md

                verify_template/
                  00_PRD_verify_template.md

              affiliate/
                affiliate_PRD.md

              categories/
                categories_PRD.md

              orders/
                orders_PRD.md

              products/
                products_PRD.md

              returns_refunds/
                returns_refunds_PRD.md

              vendors_store/
                vendors_store_PRD.md

            financial/
              financial_PRD.md

              commission/
                commission_PRD.md

              customs_clearance/
                customs_clearance_PRD.md

              invoices_billing/
                invoices_billing_PRD.md

              payments/
                payments_PRD.md

              payouts/
                payouts_PRD.md

              subscriptions/
                subscriptions_PRD.md

              tax_management/
                tax_management_PRD.md

              transactions/
                transactions_PRD.md

              wallets/
                wallets_PRD.md

            marketing/
              marketing_PRD.md

              automation/
                automation_PRD.md

              banner_manager/
                banner_manager_PRD.md

              campaigns/
                campaigns_PRD.md

              coupons/
                coupons_PRD.md

              crm/
                crm_PRD.md

              rewards/
                rewards_PRD.md

              support/
                support_PRD.md

            operations/
              operations_PRD.md

              address_code/
                address_code_PRD.md

              drivers/
                drivers_PRD.md

              fulfillment/
                fulfillment_PRD.md

              shipments/
                shipments_PRD.md

              shipping/
                shipping_PRD.md

              stock_inventory/
                stock_inventory_PRD.md

              supply_chain/
                supply_chain_PRD.md

              warehouses/
                warehouses_PRD.md

            smart_data/
              smart_data_PRD.md

              ai_manager/
                ai_manager_PRD.md

              analysis/
                SECTION_PRD.md

              event_system/
                event_system_PRD.md

              file_manager/
                file_manager_PRD.md

              reports/
                reports_PRD.md

              reviews/
                reviews_PRD.md

            system/
              system_PRD.md

              access_control_logs/
                access_control_logs_PRD.md

              api_integration/
                api_integration_PRD.md

              cms/
                cms_PRD.md

              notifications/
                notifications_PRD.md

              privacy_policy/
                privacy_policy_PRD.md

              roles_permissions/
                roles_permissions_PRD.md

              security/
                security_PRD.md

              settings/
                settings_PRD.md

        A-B_user_dashboard/
          A-B_user_dashboard_PRD.md

        A-C_agent_dashboard/
          A-C_agent_dashboard_PRD.md

        A-D_b2b_seller_dashboard/
          A-D_b2b_seller_dashboard_PRD.md

        A-E_b2c_seller_dashboard/
          A-E_b2c_seller_dashboard_PRD.md

        A-F_driver_dashboard/
          A-F_driver_dashboard_PRD.md

        A-G_staff_dashboard/
          A-G_staff_dashboard_PRD.md

        A-H_support_dashboard/
          A-H_support_dashboard_PRD.md

      B_web_frontend/
        B_PRD_Web.md

      C_mobile_app/
        C_PRD_mobile_app.md

---

# Main Branch Responsibilities

## A_dashboards

Owns dashboard documentation for Pazarat.

It currently contains:

- dashboard overview PRD
- admin dashboard
- user dashboard
- agent dashboard
- B2B seller dashboard
- B2C seller dashboard
- driver dashboard
- staff dashboard
- support dashboard

The admin dashboard is currently the richest dashboard branch.

---

## A-A_admin_dashboard

Owns admin dashboard documentation.

The current admin dashboard content is organized under:

    A_dashboards/A-A_admin_dashboard/modules/

The modules folder contains the admin dashboard parent PRD and major functional domains.

---

## governance

Owns operational governance modules that define cross-domain platform context, especially stable country identities and country-scoped operating rules.

Current governance modules include:

- country context

Governance does not replace the owning domains such as User Management, Financial, Operations, Business, or System. It provides the stable context, identity spine, cross-country interaction matrix, and routing rules those domains consume.

---

## business

Owns business-related admin dashboard modules.

Current business modules include:

- User Management
- affiliate
- categories
- orders
- products
- returns and refunds
- vendors store

The User Management branch is currently the most important active business branch for scenario expansion.

---

## User_Management

Owns admin-side user management logic.

Canonical parent artifact:

    A_dashboards/A-A_admin_dashboard/modules/business/User_Management/User_Management_PRD.md

Current child routes include:

- agents
- all_users
- user_approvals
- b2b_sellers
- b2c_sellers
- staff
- user_analytics
- verification
- verify_template

Some child files may be placeholders, route markers, or early scaffolds.

Do not treat them as mature child PRDs without inspecting content.

When generating child scenarios under User Management, inspect:

- Pazarat local numbered standards
- User_Management_PRD.md
- target child folder
- sibling child routes when relevant
- state and event taxonomy
- project traceability standard
- current conversation decisions

---

## financial

Owns finance-related admin dashboard modules.

Current financial modules include:

- commission
- customs clearance
- invoices and billing
- payments
- payouts
- subscriptions
- tax management
- transactions
- wallets

These modules may require stronger domain knowledge, source discipline, and implementation caution because payments, tax, customs, wallets, payouts, and financial operations can be high-risk or regulation-sensitive.

---

## marketing

Owns marketing-related admin dashboard modules.

Current marketing modules include:

- automation
- banner manager
- campaigns
- coupons
- CRM
- rewards
- support

---

## operations

Owns operational and logistics-related admin dashboard modules.

Current operations modules include:

- address code
- drivers
- fulfillment
- shipments
- shipping
- stock inventory
- supply chain
- warehouses

These modules may depend on state/event modeling and operational workflow artifacts.

---

## smart_data

Owns analytics, intelligence, events, files, reports, reviews, and AI-oriented dashboard capabilities.

Current smart data modules include:

- AI manager
- analysis
- event system
- file manager
- reports
- reviews

The event system is likely connected to platform event taxonomy and should be checked against project event standards before expansion.

---

## system

Owns system, permissions, security, settings, CMS, integration, and governance modules.

Current system modules include:

- access control logs
- API integration
- CMS
- notifications
- privacy policy
- roles and permissions
- security
- settings

These modules may affect platform-wide shared primitives and should not be documented in isolation when they influence permissions, audit, identity, events, or notifications across Pazarat.

---

## B_web_frontend

Owns web frontend project documentation.

Current parent artifact:

    B_web_frontend/B_PRD_Web.md

This branch should not be expanded from admin dashboard assumptions alone.

Inspect project identity, frontend-specific scope, and relevant user-facing standards before generating web frontend artifacts.

---

## C_mobile_app

Owns mobile application project documentation.

Current parent artifact:

    C_mobile_app/C_PRD_mobile_app.md

This branch should not be expanded from web or admin dashboard assumptions alone.

Inspect mobile-specific scope and relevant user-facing standards before generating mobile app artifacts.

---

# Placeholder And Route Marker Handling

Many child files may be empty, very short, or structurally present before they are mature.

Possible meanings:

- placeholder
- route marker
- scaffold
- raw future artifact
- child artifact waiting for parent maturity
- child artifact waiting for user discussion
- child artifact waiting for domain knowledge
- intentionally minimal local tunnel file

Do not judge these files as failures automatically.

Do not treat them as final PRDs automatically.

Classify intent before generating, replacing, or auditing.

---

# Local Tunnel Handling

Any folder may contain numbered files.

When a folder contains numbered files, those files form a local tunnel for that folder.

Examples in current Pazarat include multiple User Management child folders with `00_PRD_...` files.

When working inside a child folder, inspect numbered files in numeric order before producing or judging local content.

If future folders add files such as:

    00_LOCAL_STANDARD.md
    01_LOCAL_STRUCTURE.md
    99_LOCAL_REINFORCEMENT.md

they must be treated as local governing context.

---

# Parent And Child Guidance

Parent PRDs should define high-level scope, purpose, structure, and child roadmap.

Child PRDs should define focused details under a parent.

Do not generate a child PRD without accounting for its parent.

Do not overload a parent PRD with every child detail.

For User Management, the parent is:

    A_dashboards/A-A_admin_dashboard/modules/business/User_Management/User_Management_PRD.md

The children are the child folders under:

    A_dashboards/A-A_admin_dashboard/modules/business/User_Management/

---

# Dynamic Inspection Guidance

For focused work, inspect only the relevant branch and its governing context.

For example, when working on User Management child scenarios, inspect:

- Pazarat numbered standards
- User_Management_PRD.md
- target child file
- related siblings when relevant
- platform state taxonomy
- platform event taxonomy
- structure tree
- current conversation decisions

For full audits, inspect more broadly.

Do not scan every Pazarat file for every small response.

Do not answer from the target file alone when standards and parent context exist.

---

# Known Naming Notes

Canonical current name:

    User_Management/

Do not use:

    User_management/

Canonical current dashboard PRD name after cleanup:

    dashboard_PRD.md

Do not use:

    dashboard_PRD_.md

If the old names appear in any file, update references.

---

# Update Policy

Update this file when:

- a top-level branch is added, removed, or renamed
- a module folder is added, removed, or renamed
- a parent PRD is renamed
- a canonical child route changes
- a placeholder becomes a mature artifact and needs clearer classification
- a local tunnel is added inside a branch
- a project-specific standard changes navigation expectations
- actual repository structure differs from this file

This file should remain concise enough to navigate, but detailed enough to prevent wrong project discovery.

---

# Final Principle

This file helps the model locate Pazarat context.

It must not replace reading actual files.

The correct workflow is:

1. Use this file to find the likely path.
2. Inspect relevant Pazarat numbered standards.
3. Inspect the target branch, parent artifact, local numbered files, and related context.
4. Classify artifact intent and maturity.
5. Produce project-native answers or artifacts from cumulative context.

Pazarat should be understood from its own local standards, structure, artifacts, and conversation updates.