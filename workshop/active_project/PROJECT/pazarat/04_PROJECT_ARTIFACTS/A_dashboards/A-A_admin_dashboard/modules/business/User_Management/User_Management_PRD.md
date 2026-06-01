# User Management Parent PRD — السيناريو الأب وخريطة المخرجات

# Artifact Identity

Artifact Type: Parent PRD  
Project: Pazarat  
Project Area: Admin Dashboard  
Dashboard: Admin Dashboard  
Domain: Business  
Module: User Management  
Canonical Parent File: User_Management_PRD.md

Primary Role:

This file defines the parent scenario, parent-level product logic, inherited rules, technical output map, design translation bridge, implementation translation bridge, child routing, and cross-system anchors for User Management.

This file is the governing parent reference for User Management child PRDs.

---

# Documentation Role

This file is not only descriptive documentation.

It is the parent knowledge map for User Management.

It should help Product, Design, Backend, Frontend, and future AI understand how the User Management area works before generating child PRDs, workflows, screens, UI references, implementation notes, or code plans.

This file does not define every child workflow, screen, API, database schema, DTO, permission matrix, final UI component, event payload contract, or final implementation detail.

Child PRDs must inherit from this file and specialize their local branch without redefining parent logic.

This file should remain stable enough to guide children, but flexible enough to receive controlled parent updates when child scenarios reveal missing parent-level logic.

---

# Project Alignment Contract

This artifact must be interpreted through the active Pazarat project tunnel before generation, review, design translation, or implementation translation.

Use the project-local numbered standards from `00` to `99` as the binding source for terminology, state families, event families, shared primitives, UI/UX translation, implementation readiness, and parent-child documentation rules.

For human readers, this document exposes only the resulting project-facing logic: scenario, boundaries, states, events, UX outputs, implementation outputs, constraints, and open decisions.
---

# Parent Scope And Boundaries

## In Scope

This Parent PRD defines the parent-level logic for User Management, including:

- `Base Account` lifecycle
- account identity root
- `UserProfile` as an aggregation surface
- `CountryContext` as an operational context
- `PolicyAgreement`
- registration paths
- seller registration path / seller onboarding signal
- `StoreOpeningRequest` before `Store` provisioning
- `Verification` and `Approval` relationship
- `AccountCapability`
- user-related operational layers
- user-related state families
- user-related event families
- user section child routing
- cross-system anchors connected to user identity and capability
- design-ready output families for User Management screens
- implementation-ready output roots for later backend, frontend, API, database, testing, and integration work

## Out Of Scope

This Parent PRD does not define final implementation details for:

- final database schema
- final API contracts
- exact DTOs
- exact backend folder structure
- exact frontend component implementation
- final screen-level UI behavior
- detailed workflow files
- final event payload contracts
- final notification templates
- final role/permission matrix
- final Store Management internals
- final Wallet implementation
- final Shipping implementation
- final Payment implementation
- final Affiliate implementation

Those details belong to child PRDs, workflow files, screen PRDs, state/event models, implementation notes, or dedicated backend/frontend specifications.

## Parent Owns

The parent owns:

- the identity philosophy
- the core user lifecycle
- the sequence from registration to account creation
- the relationship between `Account`, seller registration path, `StoreOpeningRequest`, `Verification`, `Approval`, `Capability`, and `Store`
- the parent-level entity map
- the parent-level state and event families
- the parent-level workflow families
- the child routing map
- the cross-system anchors
- the design-ready output families
- the implementation-ready roots
- the constraints that children must not violate

## Children Own

Child PRDs own:

- local workflows
- exact fields
- exact transitions
- exact validation rules
- exact actions
- exact permissions
- exact screen behavior
- exact UI components
- exact acceptance criteria
- exact implementation-ready details
- exact failure cases
- exact local state/event usage
- exact local relationships with siblings and external modules

---

# Parent Routing Control — خريطة التحكم الأبوي

This section is the living routing ledger for User Management.

It records how the parent scenario should be expanded into children, sub-children, sibling links, external routes, and reusable patterns without turning the parent into a child-level implementation file.

The parent remains the section heart and top-level map.

Children deepen local branches.

Sub-children, screen PRDs, and workflow PRDs deepen focused executable details under the correct child.

## Recommended Child Build Order

| Order | Artifact / Route | Ownership | Why This Order Exists |
|---|---|---|---|
| 0 | `Login / Registration / Account Entry` | External Web/Auth route; referenced by this parent | The journey begins before the admin module. It must be referenced here, but built in the proper Web/Auth location. |
| 1 | `verify_template` | Local User Management child | Verification templates define required documents, fields, conditions, and country/layer rules before request forms and review queues can be mature. |
| 2 | `Store Opening Request` | Future local workflow/child candidate | The request form depends on verification template logic; it should not invent requirements independently. |
| 3 | `verification` | Local User Management child | The verification center reviews submitted requirements produced by templates and requests. |
| 4 | `user_approvals` | Local User Management child | User approvals decide activation, rejection, update requests, suspension, or reactivation after verification signals are available. |
| 5 | `all_users` | Local User Management child | Base user list and account inspection should be built after lifecycle prerequisites are clear. |
| 5.1 | `all_users/create-user-form` | Sub-child / screen-workflow candidate | Creating a user is focused form logic and should not overload the all-users child. |
| 5.2 | `all_users/advanced-filter` | Existing or candidate sub-child pattern | Advanced filtering is complex and reusable across many account-capability lists. |
| 5.3 | `all_users/user-profile` | Existing related sub-child/profile artifact | User profile is the read surface for the whole account life. |
| 5.4 | `all_users/edit-user-profile` | Sub-child / screen-workflow candidate | Editing profile data has validation, audit, permissions, and side effects that need focused detail. |
| 6 | `b2c_sellers` | Local User Management child | Reuses list/table/filter/profile patterns, with B2C seller-specific columns, states, and store-capability signals. |
| 7 | `b2b_sellers` | Local User Management child | Reuses list/table/filter/profile patterns, with B2B company/commercial relationship differences. |
| 8 | `agents` | Local User Management child | Agent account capability is displayed and managed as an account layer; deeper operations stay with the owning operational domain if needed. |
| 9 | `staff` | Local User Management child | Staff account capability is displayed and managed as an account layer; exact permissions belong to Roles & Permissions. |
| 10 | `drivers` | Cross-domain child candidate / operations-linked account layer | A driver is still a base account, but driver operations are owned by Operations / Drivers. User Management shows account identity and driver capability status. |
| 11 | `user_analytics` | Local User Management child | Lifecycle analytics should read from the final event/state map after core flows and lists are clearer. |

## Child And Sub-Child Dependency Notes

- `Store Opening Request` must depend on `verify_template`; it should not invent its own document or field requirements.
- `verification` depends on request submissions and template-defined requirements.
- `user_approvals` depends on verification outcomes and approval policy.
- `all_users` is the reusable baseline for table, profile entry, account actions, advanced search, export, and account visibility patterns.
- `b2c_sellers`, `b2b_sellers`, `agents`, `staff`, and `drivers` should reuse the common list/table/filter/profile patterns unless a real local difference is documented.
- `drivers` must not own driver operations here. Driver assignment, delivery workflow, driver performance, and logistics handling belong to Operations / Drivers.

## External Artifact Routes Mentioned By This Parent

| Mentioned Artifact | Correct Owner | Relationship To This Parent |
|---|---|---|
| Login page | Web / Auth documentation branch | Entry prerequisite for any account journey; not a local User Management child. |
| Registration page / registration choice | Web / Auth or public onboarding branch | Starts the account path; this parent records how its result affects account lifecycle. |
| OTP / sessions / authentication security | Auth / Security | Required for account creation and access, but implementation is not owned by User Management. |
| Store entity after approval | Store Management / Vendors Store | User Management owns request, verification, approval, and capability signals; Store Management owns store internals. |
| Driver operations | Operations / Drivers | User Management shows account/capability state; operations owns driver workflows. |
| Roles and permissions | System / Roles & Permissions | User capability affects access, but permission matrix is owned by the system domain. |

Financial, shipping, affiliate, CRM, notifications, analytics, and other platform areas may relate to User Management at parent-to-parent level. They are not local children unless a specific User Management artifact is created for them.

## Parent-To-Parent Relationship Map

| Related Parent / Domain | Relationship Type | Parent-Level Meaning |
|---|---|---|
| Auth / Web Entry | Upstream prerequisite | No account, dashboard, seller path, or profile exists before account entry succeeds. |
| Store Management / Vendors Store | Downstream handoff | Store provisioning and store internals begin after request, verification, and approval logic. |
| System / Roles & Permissions | Cross-cutting dependency | Capabilities and account layers affect visibility and actions. |
| System / Security | Cross-cutting dependency | Identity, OTP, sessions, sensitive document handling, and audit must align with security rules. |
| System / Notifications | Downstream effect | Registration, request, verification, approval, rejection, suspension, and reactivation may notify users/admins. |
| Smart Data / Event System | Cross-cutting dependency | User lifecycle transitions must emit events for audit, automation, analytics, and debugging. |
| Marketing / CRM / Automation | Downstream effect | Abandoned onboarding, inactive accounts, seller conversion, and lifecycle signals may trigger follow-up. |
| Financial / Wallets | Downstream eligibility relationship | Wallet and payout behavior may depend on seller/account state, but financial internals are not owned here. |
| Operations / Shipping / Drivers | Cross-domain capability relationship | Country, account state, seller capability, and driver capability can affect operations, while operational workflows stay in Operations. |
| Affiliate / Marketing | Downstream eligibility relationship | Affiliate access may depend on B2C seller/store status, but affiliate program logic is not owned here. |

## Reusable Pattern Candidates

The following behavior should be treated as shared or reusable unless a child documents a real local difference:

- account list table structure,
- column visibility and saved views,
- advanced search and filters,
- pagination, sorting, export, and bulk actions,
- account/profile header pattern,
- action panel and disabled-action reasons,
- status/capability badges,
- audit timeline entry pattern.

The first deep implementation of these patterns should usually happen under `all_users` or a dedicated reusable pattern artifact, then be reused by seller, agent, staff, driver, and future account-capability lists.

---

# Parent Scenario Narrative Contract

The following scenario narrative is the parent operational story for User Management.

It should be read as a sequential product journey, not as loose prose and not as a technical checklist.

The purpose of the parent narrative is to preserve the complete journey logic from the first user action until the system knows how to route the account into verification, approval, capabilities, stores, dashboards, events, design outputs, and implementation outputs.

The narrative must preserve sequence integrity.

A strong Pazarat scenario should make each operational step clear:

```txt
What does the user see?
What does the user choose?
What information is collected?
What does the system validate?
What does the system record?
What changes after success?
What appears to the user next?
What event or notification may be produced?
What does not happen yet?
What is the next operational step?
```

This is the standard for narrative precision.

The parent scenario must not become a long fictional story.

It must not become a dry technical list.

It must describe the journey accurately enough that missing steps, missing events, missing states, missing handoffs, or wrong assumptions become visible.

English technical terms may be used inside the Arabic narrative when they preserve exact meaning.

Examples:

- `Base Account`
- `CountryContext`
- `OTP`
- `PolicyAgreement`
- `RegistrationPath`
- `SellerOnboardingSignal`
- `StoreOpeningRequest`
- `VerificationTemplate`
- `VerificationCase`
- `ApprovalCase`
- `AccountCapability`
- `SellerCapability`
- `Store`

The parent scenario should define roots and handoffs.

It should not detail every child screen, every field rule, every validation message, every API payload, or every final database structure.

From this parent scenario, future child PRDs must extract:

- Parent Inheritance
- Local Scope
- Local Workflow
- State Alignment
- Event Alignment
- Shared Primitive Usage
- Permissions And Visibility
- Audit And Notifications
- UI/UX Translation Bridge
- Implementation Translation Bridge
- Acceptance Outcomes
- Parent Update Candidates
- Open Decisions

The narrative should stay close to the original product understanding.

Refinement is allowed only when it clarifies sequence, fills a missing operational link, improves terminology, or exposes a needed boundary.

---

# Parent Scenario Narrative

## 1. Entry Page And Registration Choice — صفحة الدخول واختيار مسار التسجيل

تبدأ رحلة المستخدم من صفحة الدخول في منصة Pazarat.

هذه الصفحة تعرض مسارين رئيسيين:

- تسجيل دخول لحساب موجود.
- إنشاء حساب جديد.

عند اختيار إنشاء حساب جديد، يظهر للمستخدم اختيار واضح لمسار التسجيل:

- تسجيل حساب مستخدم عادي.
- تسجيل حساب كبائع.

هذا الاختيار لا يعني أن النظام ينشئ نوعين مختلفين من الحسابات من الجذر.

في الحالتين، الأصل الذي سيتم إنشاؤه هو `Base Account`.

الفرق أن مسار التسجيل كبائع يجمع منذ البداية بيانات تمهيدية مرتبطة برغبة المستخدم في فتح متجر، بينما مسار المستخدم العادي يكتفي ببيانات الحساب الأساسية.

قاعدة الأب هنا:

- المستخدم العادي يحصل على `Base Account`.
- المستخدم الذي يختار التسجيل كبائع يحصل أيضًا على `Base Account`.
- اختيار التسجيل كبائع لا ينشئ متجرًا.
- اختيار التسجيل كبائع لا يفعّل `SellerCapability`.
- اختيار التسجيل كبائع يفتح مسارًا لاحقًا لإكمال `StoreOpeningRequest` من لوحة التحكم.
- أي تفعيل فعلي للبيع يحتاج تحققًا وموافقة لاحقة.

بهذا لا يتحول مفهوم النية إلى محور زائد، بل يبقى إشارة تشغيلية داخل تسلسل التسجيل.

---

## 2. Normal User Registration Path — تسجيل حساب مستخدم عادي

إذا اختار المستخدم تسجيل حساب مستخدم عادي، يعرض النظام حقول التسجيل الأساسية.

الحقول الأساسية قد تشمل:

- الاسم.
- الكنية.
- رقم الهاتف.
- كود الدولة.
- كلمة المرور.
- تأكيد كلمة المرور.
- البريد الإلكتروني إذا كان مطلوبًا أو اختياريًا حسب السياسة.
- المحافظة.
- المنطقة التابعة للمحافظة.

اختيار كود الدولة ليس مجرد خطوة لتنسيق رقم الهاتف.

اختيار الدولة يحدد `CountryContext` الذي يعمل عليه الحساب داخل المنصة.

هذا السياق قد ينعكس لاحقًا على:

- المحافظات والمناطق المعروضة.
- متطلبات التحقق.
- الشروط والأحكام.
- السياسات التشغيلية.
- الضرائب.
- الشحن.
- المنتجات المسموحة.
- طرق الدفع.
- قيود الشراء أو البيع.
- آلية عمل الحساب داخل الدولة أو بين الدول.

مثال:

إذا اختار المستخدم سوريا، يمكن أن تظهر له قائمة المحافظات السورية، ثم المناطق المرتبطة بالمحافظة المختارة.

وإذا اختار دولة أخرى، قد تتغير القوائم أو المتطلبات أو السياسات التي يجب أن يوافق عليها.

بعد تعبئة بيانات الحساب الأساسية، يعرض النظام الشروط والأحكام والسياسات المطلوبة بحسب `CountryContext` وقالب التسجيل المعتمد.

يجب أن يسجل النظام موافقة المستخدم على السياسات كـ `PolicyAgreement`.

بعد ذلك يتم تنفيذ `OTP` على رقم الهاتف إذا كان مفروضًا في هذا المسار.

عند نجاح `OTP` واكتمال الموافقة على السياسات، ينشئ النظام `Base Account`.

بعد إنشاء الحساب، يمكن أن ينتج النظام أحداثًا مثل:

- `account_created`
- `otp_verified`
- `policy_accepted`

وقد يرسل النظام إشعارًا ترحيبيًا أو رسالة تأكيد إنشاء الحساب، مثل:

- إشعار داخل التطبيق.
- بريد إلكتروني ترحيبي إذا كان البريد متاحًا.
- رسالة SMS إذا كانت السياسة تدعم ذلك.

هذا الإشعار ليس مجرد تفصيل واجهة. هو حلقة تشغيلية تربط إنشاء الحساب بنظام الأحداث والإشعارات.

بعد إنشاء الحساب، يدخل المستخدم إلى لوحة التحكم أو الواجهة المناسبة لحساب المستخدم الأساسي.

إذا كانت الدولة أو السياسة تتطلب تحققًا إضافيًا بعد إنشاء الحساب، يمكن أن يظهر للمستخدم تنبيه لاستكمال متطلبات إضافية خلال مدة محددة أو بدون مدة حسب السياسة.

قبل استكمال هذه المتطلبات، قد تسمح المنصة ببعض الوظائف مثل:

- التصفح.
- معاينة المنتجات.
- إضافة منتجات إلى المفضلة.

وقد تمنع وظائف أخرى مثل:

- الشراء.
- مراسلة البائع.
- استخدام وسائل دفع معينة.
- تنفيذ إجراءات حساسة.

قاعدة الأب هنا:

- `Base Account` يمكن أن ينشأ قبل اكتمال كل متطلبات التحقق المتقدمة.
- بعض القدرات قد تبقى مقيدة حسب `CountryContext` و `VerificationTemplate`.
- تفاصيل واجهة التسجيل، رسائل الأخطاء، validation الدقيق، وتصميم الشاشة تخص child أو screen artifacts.
- هذا الأب يثبت الحلقة التشغيلية: بيانات أساسية → سياسات → OTP → Base Account → events/notifications → dashboard state.

---

## 3. Country Context And Platform Operation — انعكاس الدولة على التشغيل

`CountryContext` ليس تفصيلًا ثانويًا داخل التسجيل.

هو سياق تشغيلي يؤثر على الحساب والمنصة.

عندما يختار المستخدم الدولة، لا يسجل النظام كود الهاتف فقط، بل يحدد البيئة التي سيعمل الحساب ضمنها.

هذا قد ينعكس على:

- هل يستطيع المستخدم الشراء مباشرة؟
- هل يحتاج تحققًا إضافيًا؟
- هل تظهر له منتجات دولة معينة؟
- هل يمكنه الشراء من دولة أخرى؟
- هل يمكنه البيع داخل الدولة نفسها؟
- هل يحتاج وثائق محلية؟
- هل تنطبق عليه ضرائب أو شروط خاصة؟
- هل تتوفر له طرق دفع وشحن محددة؟
- هل تنطبق عليه سياسة قبول مختلفة؟

إذا كانت Pazarat تعمل كبيئة تشغيل مستقلة لكل دولة، فقد يستطيع المستخدم تصفح منتجات أو متاجر دولة أخرى، لكنه لا يستطيع الشراء منها إذا لم يكن الشحن أو التبادل التجاري بين الدول مدعومًا.

أما إذا كانت المنصة تدعم التشغيل بين دول محددة، فيمكن للمستخدمين داخل هذه الدول الشراء أو البيع وفق قواعد الشحن، التوزيع، الضرائب، الجمارك، الدفع، والسياسات المعتمدة.

وقد تسمح المنصة أيضًا بتسجيل مستخدمين من دول لا تعمل فيها كبيئة تشغيل كاملة، بحيث يمكنهم الشراء من المتاجر أو التعامل مع بائعين الجملة بحسب السياسة.

في هذه الحالة قد يكون المتجر أو البائع مسؤولًا عن الشحن والتسليم، بينما يمكن للمنصة تقديم خدمات اختيارية مثل التحقق من المنتج، مطابقة المواصفات، أو متابعة الشحن مقابل رسوم.

قاعدة الأب هنا:

- User Management لا يملك كل سياسات الدولة.
- لكنه يجب أن يثبت أن `CountryContext` يؤثر على الحساب.
- تفاصيل الضرائب والشحن والدفع والجمارك لا تفصل هنا.
- هذه التفاصيل تُحال إلى المالكين المناسبين مثل Operations, Financial, Shipping, Tax, Customs, Governance.
- الطفل الذي يعالج التسجيل أو البروفايل يجب أن يحافظ على أثر الدولة ولا يختصرها إلى كود هاتف فقط.

---

## 4. Seller Registration Path — تسجيل حساب كبائع

إذا اختار المستخدم التسجيل كبائع، لا يبدأ النظام من حساب مختلف.

النظام يعرض نفس بيانات الحساب الأساسية المطلوبة للمستخدم العادي، لأن البائع يبدأ أيضًا من `Base Account`.

لكن يضاف إلى النموذج جزء تمهيدي مرتبط بمسار فتح المتجر.

هذا الجزء قد يشمل:

- اسم المتجر المبدئي.
- وصف مختصر لطبيعة عمل المتجر.
- نوع البيع: `B2C` أو `B2B`.

إذا اختار المستخدم `B2C`، يمكن أن يحدد هل هو:

- فرد.
- شركة.

أما إذا اختار `B2B`، فيعامل المسار كمسار شركة أو كيان تجاري، لأن بيع الجملة أو التعامل التجاري بين الشركات لا يفتح كمسار فرد عادي.

هذه البيانات لا تنشئ متجرًا فعليًا.

هي تحفظ إشارة واضحة أن الحساب يريد إكمال مسار فتح متجر، وتساعد النظام لاحقًا على عرض المتطلبات المناسبة داخل لوحة التحكم.

بعد تعبئة بيانات الحساب الأساسية والبيانات التمهيدية لمسار البائع، يوافق المستخدم على الشروط والسياسات المطلوبة، ثم ينفذ `OTP` إذا كان مطلوبًا.

بعد نجاح التسجيل، النتيجة المباشرة هي:

- إنشاء `Base Account`.
- تسجيل أن الحساب بدأ مسار بائع.
- حفظ بيانات تمهيدية لطلب فتح متجر.
- إظهار تنبيه داخل لوحة التحكم مثل: “أكمل طلب فتح المتجر”.
- إنتاج حدث مركزي مناسب مثل `seller_intent_created` أو حدث محلي مقترح مثل `seller_registration_started` إذا تم اعتماده لاحقًا في Event Taxonomy.
- إرسال إشعار ترحيبي أو إرشادي يوضح أن الحساب تم إنشاؤه وأن خطوة فتح المتجر لم تكتمل بعد.

المهم هنا أن المستخدم لا يصبح بائعًا بعد التسجيل فقط.

ولا يتم إنشاء متجر فعلي بعد التسجيل فقط.

ولا يتم تفعيل صلاحية البيع بعد التسجيل فقط.

التسجيل كبائع هو تسهيل للرحلة، لأنه يجعل المستخدم يبدأ من الطريق الصحيح، لكنه لا يتجاوز التحقق والموافقة.

قاعدة الأب هنا:

- مسار التسجيل كبائع يجمع بيانات الحساب الأساسي وبيانات تمهيدية لفتح متجر.
- النتيجة المباشرة هي `Base Account` وليس `Store`.
- `SellerCapability` لا تتفعل إلا بعد `Verification` و `Approval`.
- بيانات المتجر المبدئية يمكن تعديلها لاحقًا أثناء `StoreOpeningRequest`.
- تفاصيل حقول المتجر النهائية، validation، وصياغة النموذج تخص child أو screen artifacts.
- event naming النهائي يجب أن يتوافق مع `03_PLATFORM_EVENT_TAXONOMY.md`.

---

## 5. Base Account As Stable Root — الحساب الأساسي الثابت

بعد نجاح التسجيل، سواء كان المستخدم قد اختار التسجيل كمستخدم عادي أو كبائع، يصبح لديه `Base Account`.

هذا الحساب هو الجذر الثابت لهوية المستخدم داخل Pazarat.

الحساب الأساسي يحتفظ بميزات المستخدم العادي، مثل:

- البروفايل.
- العناوين.
- الطلبات.
- المفضلة.
- الشراء.
- إعدادات الحساب.
- سجل النشاط.

إذا حصل الحساب لاحقًا على طبقة إضافية مثل بائع أو موظف أو سائق أو وكيل، لا يتم إنشاء حساب جديد.

يتم توسيع نفس الحساب بطبقة أو قدرة تشغيلية إضافية.

أمثلة:

- البائع لا يلغي حساب المستخدم العادي.
- الموظف لا يصبح حسابًا منفصلًا.
- السائق لا يحتاج هوية حساب جديدة.
- المتجر كيان مستقل مرتبط بالحساب.
- الطلبات أو المنتجات أو المحافظ لها كياناتها الخاصة، لكنها ترتبط بالحساب أو المتجر بحسب السياق.

إذن `Base Account` هو مركز الربط.

أما الطبقات مثل `SellerCapability`, `StaffCapability`, `AgentCapability`, أو غيرها، فهي توسعات تشغيلية فوق الحساب.

من ناحية العرض الإداري، هذا لا يعني أن كل الحسابات تظهر في جدول واحد.

الحساب ثابت داخليًا، لكن القوائم الإدارية تقسم الحسابات بحسب الطبقة التشغيلية التي نريد إدارتها.

فإذا أصبح المستخدم بائعًا، قد يظهر في `B2C Sellers` أو `B2B Sellers` بدل أن يبقى ضمن `All Users` كحساب عادي فقط، مع بقاء حسابه الأساسي وميزات الشراء محفوظة حسب السياسة.

قاعدة الأب هنا:

- `AccountId` هو root identity.
- `Capability` توسع السلوك.
- `Store` كيان مستقل مرتبط بالحساب.
- UI lists تعرض طبقات تشغيلية، لا تعيد تعريف الحساب.
- الأب يثبت القاعدة، والأبناء يفصلون سلوك كل قائمة وكل طبقة.

---

## 6. Dashboard Continuation For Seller Path — إكمال مسار البائع من لوحة التحكم

بعد تسجيل الحساب كبائع، يدخل المستخدم إلى لوحة التحكم أو الواجهة المناسبة لحسابه.

هناك يظهر له تنبيه أو بطاقة إجراء واضحة مثل:

“أكمل طلب فتح المتجر”.

هذا التنبيه ليس مجرد رسالة واجهة، بل هو استمرار للرحلة التي بدأت أثناء التسجيل.

النظام يعرف أن المستخدم سجل كمسار بائع، لكنه لا يعتبره بائعًا فعالًا بعد.

إذا ضغط المستخدم على إكمال الطلب، يبدأ `StoreOpeningRequest`.

عند هذه النقطة، يستدعي النظام المتطلبات المناسبة من `VerificationTemplate`.

المتطلبات قد تختلف بحسب:

- الدولة.
- نوع البيع: `B2C` أو `B2B`.
- فرد أو شركة.
- نوع النشاط.
- طبيعة المتجر.
- السياسات المحلية.
- المتطلبات القانونية أو التشغيلية.
- أي شروط خاصة بفئة المنتجات أو السوق.

يمكن للمستخدم أثناء الطلب تعديل بعض البيانات التي أدخلها أثناء التسجيل، مثل:

- اسم المتجر.
- وصف المتجر.
- نوع الكيان إذا كان التعديل مسموحًا.
- نوع النشاط.

إذا تغير نوع المسار، يجب أن يعيد النظام حساب المتطلبات.

مثال:

- `B2C Individual` قد يحتاج متطلبات مختلفة عن `B2C Company`.
- `B2B` يعامل ككيان شركة أو جهة تجارية.
- دولة معينة قد تطلب وثائق إضافية.
- نشاط معين قد يطلب موافقات أو شروطًا خاصة.

هنا يظهر دور `VerificationTemplate` كقلب تشغيلي.

القالب لا يحدد شكل الواجهة فقط، بل يحدد ماذا يجب أن يقدمه الحساب حتى ينتقل من مجرد حساب لديه مسار بائع إلى حساب مؤهل للمراجعة.

قاعدة الأب هنا:

- `VerificationTemplate` يحدد المتطلبات حسب السياق.
- `StoreOpeningRequest` هو الجسر بين الحساب الأساسي وتفعيل طبقة البائع.
- تفاصيل template builder, field conditions, validations, وحماية القوالب تخص `verify_template` child.
- تفاصيل شاشة إكمال الطلب تخص child أو screen PRD.

---

## 7. User Upgrade To Seller — ترقية مستخدم عادي إلى بائع

المستخدم الذي سجل في البداية كحساب عادي يمكن أن يطلب لاحقًا أن يصبح بائعًا.

داخل لوحة التحكم، قد يظهر له إجراء مثل:

“كن بائعًا على Pazarat”.

عند الضغط عليه، لا ينشئ النظام حسابًا جديدًا.

النظام يفتح نفس منطق `StoreOpeningRequest` فوق `Base Account` الحالي.

إذن يوجد طريقان للوصول إلى طلب فتح المتجر:

- اختيار التسجيل كبائع منذ البداية.
- طلب الترقية لاحقًا من حساب مستخدم عادي.

الطريقان يجب أن يلتقيا في نفس منطق الطلب والتحقق والموافقة.

الفرق أن التسجيل كبائع يبدأ المسار مبكرًا، بينما المستخدم العادي يفتح المسار لاحقًا.

إذا تم تفعيل طبقة البائع لاحقًا، لا يفقد المستخدم حسابه الأساسي ولا قدرته على الشراء.

لكن من ناحية العرض الإداري، ينتقل الحساب إلى قائمة البائعين المناسبة حسب نوع الطبقة، مثل `B2C Sellers` أو `B2B Sellers`.

قاعدة الأب هنا:

- لا يوجد حساب منفصل للبائع.
- مسار التسجيل كبائع ومسار الترقية اللاحقة يلتقيان في `StoreOpeningRequest`.
- الطفل الذي يشرح `StoreOpeningRequest` يجب أن يرث هذه القاعدة.
- يمكن للأحداث أن تفرق بين `seller_intent_created` و`upgrade_intent_created` و`intent_converted_to_request` حسب السياق.

---

## 8. Store Opening Request — طلب فتح المتجر

`StoreOpeningRequest` هو الطلب الذي يحول رغبة المستخدم في البيع إلى مسار مراجعة قابل للتحقق والموافقة.

هذا الطلب يبدأ بعد التسجيل كبائع أو بعد طلب الترقية لاحقًا.

داخل الطلب، يعرض النظام المتطلبات الناتجة عن `VerificationTemplate`.

المستخدم يراجع البيانات التمهيدية، ويكمل الوثائق أو الحقول أو الشروط المطلوبة.

قد تشمل المتطلبات:

- معلومات المتجر.
- نوع البيع.
- نوع الكيان.
- وثائق شخصية.
- وثائق تجارية.
- بيانات عنوان أو موقع.
- موافقات إضافية.
- شروط سياسة خاصة.
- متطلبات مرتبطة بالدولة أو النشاط.

بعد اكتمال الطلب وإرساله، لا يتم فتح المتجر مباشرة.

الطلب ينتقل أولًا إلى `Verification Center`.

وظيفة هذه المرحلة هي التحقق من صحة واكتمال المتطلبات.

إذا كانت البيانات ناقصة أو الوثائق غير صحيحة، يعود الطلب للمستخدم للتعديل أو إعادة الإرسال حسب السياسة.

إذا اكتمل التحقق، ينتقل الطلب إلى `Approval Center`.

عند الموافقة، يمكن للنظام تفعيل `SellerCapability` وربط أو إنشاء `Store` بحسب منطق Store Management.

بعد هذه المرحلة فقط يصبح المستخدم بائعًا فعالًا.

قاعدة الأب هنا:

- User Management يملك مرحلة ما قبل التفعيل لأنها مرتبطة بمنح الحساب قدرة بائع.
- `Verification` يراجع صحة واكتمال المتطلبات.
- `Approval` يقرر التفعيل أو الرفض.
- `Store` بعد التفعيل يصبح كيانًا عميقًا داخل Store Management.
- تفاصيل مراجعة الوثائق، rejection reasons، resubmission، approval decisions، وstore provisioning تخص children/workflow artifacts.

---

## 9. Verification Center — إرسال الطلب إلى سنتر التحقق

بعد أن يكمل المستخدم طلب فتح المتجر ويرسله، ينتقل الطلب إلى `Verification Center`.

وظيفة `Verification Center` هي مراجعة المتطلبات والوثائق، وليس اتخاذ قرار فتح المتجر.

أي أن `Verification Center` يجيب على سؤال:

هل البيانات والوثائق المطلوبة صحيحة ومكتملة بحسب `VerificationTemplate`؟

داخل `Verification Center` يمكن أن تظهر:

- طلبات مكتملة بانتظار المراجعة.
- طلبات فيها وثائق ناقصة.
- طلبات فيها وثائق مرفوضة.
- طلبات تحتاج تعديلًا من المستخدم.
- طلبات اكتمل تحققها وتنتقل إلى الموافقات.
- حسابات أظهرت مسار فتح متجر لكنها لم تكمل الطلب.

النقطة الأخيرة مهمة.

المستخدم الذي بدأ مسار فتح متجر ولم يكمل الطلب لا يجب أن يختفي من النظام.

هذه الحالة تعتبر إشارة تشغيلية يمكن ربطها بـ:

- Event System.
- CRM.
- حملات التذكير.
- Support.
- Analytics.
- Automation.
- Notifications.

مثال:

إذا سجل مستخدم كبائع ولم يكمل الطلب، يمكن إرسال تذكير بعد أسبوع.

وإذا لم يكمل بعد شهر، يمكن إرسال رسالة مختلفة أو عرض تحفيزي أو تحويله إلى متابعة دعم.

بهذا لا يكون `Verification Center` مجرد مكان لفحص الوثائق، بل نقطة قراءة لسلوك المستخدم قبل التفعيل.

قاعدة الأب هنا:

- Verification يراجع صحة واكتمال المتطلبات.
- Verification لا يساوي Approval.
- الطلب غير المكتمل أو المهجور يجب أن يبقى قابلًا للتتبع كإشارة تشغيلية.
- تفاصيل queue actions, rejection reasons, resubmission, reviewer UI تخص child PRD.

---

## 10. Approval Center — الانتقال إلى مركز الموافقات

عند اكتمال التحقق من الوثائق والمتطلبات، لا يعني ذلك أن المتجر أصبح مفتوحًا.

بعد اكتمال التحقق، ينتقل الطلب إلى `Approval Center`.

الفرق واضح:

- `Verification Center` يراجع صحة المتطلبات.
- `Approval Center` يقرر التفعيل أو الرفض أو التعليق.

`Approval Center` يعالج الحالات التي تحتاج قرارًا إداريًا، مثل:

- طلب فتح متجر جديد.
- طلب تفعيل طبقة صلاحية.
- طلب إعادة تفعيل.
- حالة معلقة.
- حالة محظورة تحتاج مراجعة.
- طلب اشتراك أو ميزة تحتاج معالجة.

عند الموافقة على فتح المتجر، يختفي الطلب من `Approval Center` كطلب معلق، لأن الغرض من المركز هو معالجة الطلبات غير المحسومة.

بعدها يظهر المتجر في قسم المتاجر، ويظهر الحساب في القسم المناسب مثل `B2C Sellers` أو `B2B Sellers` بحسب نوع الطبقة.

يجب فهم `Approval Center` هنا كآلية معالجة مرتبطة بمالك الطلب أو الكيان.

في إدارة المستخدمين، يظهر طلب فتح المتجر قبل التفعيل لأنه مرتبط بالحساب وبمنح المستخدم طبقة بائع.

لكن بعد تفعيل المتجر، يصبح المتجر كيانًا له مالك عميق داخل قسم المتاجر، وبالتالي أي تعليق أو إعادة تفعيل لاحقة للمتجر يجب أن تعالج داخل موافقات المتاجر أو مركز معالجة المتاجر.

نفس المنطق ينطبق على المنتجات والطلبات والكيانات الأخرى.

طلب الموافقة على منتج جديد لا يظهر في موافقات المستخدمين، بل في موافقات المنتجات لأن المنتج كيان يملكه قسم المنتجات.

هذا الفصل يمنع خلط مراكز الموافقات ويجعل كل كيان يعالج داخل قسمه بعد أن يصبح له مالك تشغيلي واضح.

قاعدة الأب هنا:

- Approval يملك قرار التفعيل أو الرفض.
- Approval ينتج state/event impacts.
- قرار الموافقة قد يفعّل capability أو ينقل الكيان إلى مالكه العميق.
- تفاصيل approval workflow الدقيقة تخص child/workflow PRD.

---

## 11. Affiliate Marketing Logic — منطق التسويق بالعمولة

التسويق بالعمولة في Pazarat ليس نوع حساب مستقلًا، وليس طبقة عامة متاحة لأي مستخدم مباشرة.

هو ميزة اشتراك مرتبطة بمتجر `B2C`.

إذا كان المستخدم العادي مهتمًا بخطة التسويق بالعمولة وضغط على طلب الاشتراك، فإن النظام يفهم أولًا أنه يحتاج متجرًا `B2C`.

لذلك يفتح له مسار طلب فتح متجر `B2C`.

داخل الطلب يمكن أن تظهر:

- متطلبات فتح المتجر.
- متطلبات الاشتراك بخطة التسويق بالعمولة.

إذا اكتملت شروط الاشتراك بالعمولة لكن لم تتم الموافقة بعد على فتح المتجر، تبقى ميزة التسويق معلقة حتى تتم الموافقة على المتجر.

وإذا تمت الموافقة على فتح المتجر لكن شروط الاشتراك بالعمولة لم تكتمل، فيتم فتح المتجر بشكل طبيعي كبائع `B2C`، وتبقى ميزة التسويق معلقة إلى أن يستكمل المستخدم شروط الاشتراك.

إذا كان لدى المستخدم متجر `B2C` فعال مسبقًا، يمكنه طلب الاشتراك مباشرة دون إعادة فتح متجر.

أما إذا كان لديه `B2B` فقط، فلا تظهر له ميزة الاشتراك بالتسويق بالعمولة حسب السياسة الحالية، إلا إذا تغيرت السياسة لاحقًا عبر قالب تحقق أو نظام اشتراكات يسمح بذلك.

الميزة هنا لا تمنع البائع من بيع منتجاته الخاصة.

البائع يبقى قادرًا على رفع منتجاته وبيعها داخل متجره، بينما تضيف له خطة التسويق إمكانية عرض منتجات من مستودعات أو برندات أخرى مقابل عمولة.

إذا انتهى الاشتراك أو تم تعليقه، لا يعني ذلك إغلاق الحساب أو إلغاء المتجر.

يتم فقط تعطيل ميزة التسويق بالعمولة أو أدواتها بحسب سياسة الاشتراك، مع بقاء المتجر يعمل كبائع عادي إذا كانت حالته تسمح بذلك.

قاعدة الأب هنا:

- Affiliate is not an account type.
- Affiliate depends on active or pending `B2C Store` logic.
- Affiliate لا يساوي Store ولا يساوي Account.
- تفاصيل الاشتراك والعمولات تخص Affiliate / Marketing / Subscription artifacts.

---

## 12. Operational Layers — طبقات مثل الموظف والوكيل والسائق

ليست كل طبقات الصلاحية يطلبها المستخدم من نفسه.

بعض الطبقات يجب أن تبدأ من لوحة تحكم المسؤول، مثل:

- موظف.
- وكيل.
- سائق.
- ممثل منطقة.
- أي طبقة داخلية أو حساسة.

السبب أن هذه الطبقات لا يجب أن تكون مفتوحة كطلبات عامة حتى لا تغرق المنصة بطلبات غير مناسبة.

الإدارة هي التي تختار الحساب المناسب، غالبًا بعد مقابلة أو تحقق أو اتفاق مسبق.

عند إضافة هذه الطبقة من المسؤول، يظهر للمستخدم داخل حسابه طلب استكمال المتطلبات، مثل:

- أكمل طلب حساب سائق.
- أكمل طلب حساب وكيل.
- أكمل بيانات الموظف.

وهذه المتطلبات يمكن أن تعتمد أيضًا على قالب تحقق خاص بالطبقة.

بعد استكمال المتطلبات، تمر العملية بالتحقق والموافقة بحسب السياسة، ثم تظهر الطبقة في قسمها الفعال.

هذه الطبقات لا تلغي الحساب الأساسي.

لكنها تغير مكان إدارة الحساب داخل لوحة التحكم الإدارية، لأن كل طبقة لها قسمها، فلاترها، صلاحياتها، وطريقة متابعتها.

قاعدة الأب هنا:

- Operational layers extend the account.
- Sensitive layers may be admin-initiated.
- كل طبقة تحتاج owner واضح.
- تفاصيل staff / agent / driver workflows تخص children أو domains المالكة.
- السائق يبقى `Base Account` مثل أي مستخدم، ويمكنه الشراء والتفاعل كمستخدم عادي إذا كانت طبقة الحساب الأساسية فعالة.
- User Management يعرض أن الحساب لديه driver capability وحالة هذه الطبقة، بينما منطق التشغيل العميق للسائق يملكه Operations / Drivers.

---

## 13. Administrative Distribution — توزيع إدارة الحسابات على الأقسام

بعد فهم الحساب الأساسي والطبقات، يجب توزيع إدارة المستخدمين على أقسام واضحة بدل خلط كل الحالات في جدول واحد.

إدارة المستخدمين لا تعرض كل الحسابات وكل طبقاتها داخل جدول واحد.

الحساب الأساسي يبقى ثابتًا تقنيًا داخل النظام، لكن العرض الإداري يقسم الحسابات بحسب الطبقة التشغيلية التي نريد إدارتها.

هذا الفصل مهم لأن المنصة قد تضم ملايين الحسابات، وطبقات تشغيلية كثيرة مثل المستخدم العادي، البائع، الموظف، الوكيل، السائق، صاحب المتجر، أو المشترك في ميزة معينة.

لو حاولنا عرض كل هذه الطبقات في جدول واحد، سوف تصبح الفلاتر معقدة جدًا وغير قابلة للإدارة.

لذلك يتم توزيع القوائم كالتالي.

### All Users

يعرض هذا القسم حسابات طبقة المستخدم الأساسية فقط، أي المستخدمين الذين يتعاملون مع المنصة كمشترين أو حسابات عادية فعالة، ولا يعرض الحسابات التي تم تفعيل طبقة تشغيلية أعلى لها مثل بائع، موظف، وكيل، أو سائق.

الهدف من هذا الفصل هو منع تحويل جدول كل المستخدمين إلى جدول ضخم يحتوي كل طبقات الحساب وحالاتها.

فمع وجود طبقات كثيرة داخل المنصة، يصبح عرض كل شيء في جدول واحد غير عملي ويؤدي إلى فلاتر معقدة وصعبة القراءة.

يعرض جدول كل المستخدمين بيانات الحساب الأساسية اللازمة للبحث والمعاينة، مثل:

- الاسم الكامل.
- البريد الإلكتروني.
- رقم الهاتف.
- العنوان أو المنطقة.
- مؤشرات مختصرة مرتبطة بسلوك طبقة المستخدم الأساسية، مثل وجود عمليات شراء أو تقييمات أو نشاط عادي داخل المنصة.

إذا ارتقى المستخدم إلى طبقة بائع أو طبقة تشغيلية أخرى، لا يتم حذف حسابه الأساسي ولا إلغاء قدرته على الشراء، لكنه لا يبقى ضمن قسم `All Users` من ناحية العرض الإداري.

يظهر بدلًا من ذلك في القسم المناسب لطبقته، مثل `B2C Sellers` أو `B2B Sellers` أو `Staff` أو `Agents` أو `Drivers`.

ومن جدول `All Users` يمكن الوصول إلى بروفايل المستخدم لمعاينة حياة الحساب عند الحاجة، لكن هذا القسم نفسه لا يعالج طبقات البائعين أو المتاجر أو الاشتراكات أو الموافقات. كل طبقة لها قسمها وفلاترها وطريقة إدارتها.

### B2C Sellers

يعرض هذا القسم الحسابات التي لديها طبقة بائع في مسار `B2C`.

لا يعرض هذا القسم المتاجر ككيانات مستقلة، بل يعرض المستخدمين من زاوية امتلاكهم طبقة بائع مرتبطة بمتجر.

يعرض الجدول بيانات الحساب الأساسية مثل الاسم الكامل، البريد الإلكتروني، رقم الهاتف، والعنوان أو المنطقة، ثم يضيف بيانات مختصرة مرتبطة بطبقة البائع والمتجر، مثل حالة المتجر، نوع البائع فرد أو شركة، وهل لديه اشتراك في خطة تسويق بالعمولة.

يبقى هذا المستخدم قادرًا على الشراء والتفاعل كمستخدم عادي بحسب سياسة الحساب، لكن إدارته هنا تتم من زاوية طبقة البائع.

ويمكن من هذا القسم الوصول إلى بروفايل المستخدم البائع، أو الانتقال إلى المتجر المرتبط به عند الحاجة.

الفلاتر داخل هذا القسم يجب أن تخدم طبقة بائع `B2C`، مثل نوع البائع، حالة المتجر، وجود اشتراك تسويق بالعمولة، أو مؤشرات البيع المناسبة.

### B2B Sellers

يعرض هذا القسم الحسابات التي لديها طبقة بائع في مسار `B2B`.

هذا القسم يعالج الحساب من زاوية علاقته ببيع الجملة أو الشركات أو المصانع أو العلامات التجارية بحسب نموذج Pazarat.

لا يعرض القسم كل المتاجر، بل يعرض الحسابات التي لديها طبقة بائع `B2B`، مع بيانات مختصرة عن الكيان التجاري أو المتجر المرتبط بها.

الفلاتر هنا تختلف عن `B2C Sellers`، لأنها قد تحتاج معلومات مثل نوع الشركة، حجم التعامل، حالة التوثيق التجاري، مستوى الاعتماد، أو علاقة الحساب بالعلامة التجارية أو المصنع.

### Staff / Agents / Drivers

هذه الأقسام تعرض الحسابات التي حصلت على طبقات تشغيلية داخلية أو خاصة.

هذه الطبقات غالبًا لا تبدأ من طلب عام، بل من قرار إداري أو دعوة أو تعيين.

كل طبقة تحتاج ملف ابن أو فرع تفصيلي خاص بها، لأن صلاحيات الموظف تختلف عن الوكيل، والسائق يختلف عن ممثل المنطقة أو فريق الدعم.

### Verification Templates

يعرض منطق القوالب التي تحدد المتطلبات حسب الدولة، نوع الحساب، نوع الطبقة، نوع الكيان، والمسار المطلوب.

هذا الفرع لا يعالج طلبًا محددًا، بل يعالج القاعدة التي تنتج المتطلبات.

تفاصيل إنشاء القالب، تعديله، نسخه، حمايته من الحذف إذا كان مستخدمًا، وكيف تتأثر الطلبات القديمة أو الجديدة عند تغييره، يجب أن تفصل في child PRD خاص.

### Verification Center

يعرض الطلبات والمسارات والحالات التي تحتاج مراجعة متطلبات أو وثائق.

هذا المركز يراجع الاكتمال والصحة، لكنه لا يقرر التفعيل النهائي.

### Approval Center

يعرض الحالات التي تحتاج قرار تفعيل أو رفض أو تعليق أو إعادة تفعيل.

القانون العام:

الأقسام الفعالة تعرض الحسابات أو الطبقات التي اكتملت وأصبحت فعالة ضمن سياقها الإداري.

أما الطلبات والنواقص والحالات المعلقة فتذهب إلى مركز المعالجة المناسب.

### قاعدة الفصل بين قوائم الطبقات وقوائم الكيانات

القوائم الإدارية في المنصة يجب أن تفرق بين عرض الحسابات حسب الطبقات التشغيلية، وعرض الكيانات المستقلة حسب مالكها التشغيلي.

في إدارة المستخدمين، يتم عرض الحسابات من زاوية الطبقة: مستخدم عادي، بائع `B2C`، بائع `B2B`, موظف، وكيل، أو سائق.

كل قسم يعرض بيانات الحساب الأساسية، ثم يضيف فقط ما يخدم تلك الطبقة.

أما في الأقسام الأخرى مثل المتاجر أو المنتجات، فمحور الجدول يكون الكيان نفسه، وليس حساب المستخدم.

فقسم متاجر `B2C` يعرض المتاجر ككيانات، ويمكن أن يحتوي اسم صاحب المتجر أو بيانات المالك كمعلومة مساعدة.

وقسم المنتجات يعرض المنتجات ككيانات، ويمكن أن يحتوي اسم المتجر أو البائع كمعلومة مساعدة.

بهذه الطريقة يمكن البحث عن البائع من قسم البائعين عبر اسم المستخدم أو رقم الهاتف، ويمكن البحث عن المتجر من قسم المتاجر عبر اسم المتجر أو بياناته.

العلاقة بينهما تبقى متاحة عبر البروفايل والروابط، لكن كل قسم يحافظ على محور واضح للعرض والفلترة.

هذا النمط يجب أن يصبح قاعدة تشغيلية عامة في المنصة.

فالأقسام مثل `All Users` و`B2C Sellers` و`B2B Sellers` و`Stores` و`Products` تعرض السجلات الفعالة أو المستقرة حسب معنى كل قسم، بينما الحالات التي تحتاج مراجعة، موافقة، إعادة تفعيل، أو معالجة بعد حظر تظهر في مركز المعالجة الخاص بمالكها.

لذلك تظهر طلبات أو مشاكل الحساب في مراكز معالجة المستخدمين، وتظهر مشاكل المتجر في موافقات أو معالجة المتاجر، وتظهر المنتجات الجديدة أو المحظورة في موافقات أو معالجة المنتجات.

---

## 14. Blocking, Suspension, And Reactivation — الحظر والتعليق وإعادة التفعيل

يجب الفصل بين حظر الحساب، تعليق الحساب، حظر المتجر، وتعليق الطبقة.

الحظر الكامل للحساب يعني منع المستخدم من الدخول أو استخدام الحساب أساسًا.

أما التعليق التشغيلي فقد يسمح للمستخدم بالدخول، لكنه يوقف ميزات حساسة مثل:

- الشراء.
- البيع.
- المراسلة.
- السحب.
- استخدام طبقة معينة.
- إدارة متجر.
- تنفيذ إجراء حساس.

إذا تم حظر المتجر فقط:

- يبقى الحساب الأساسي فعالًا.
- يمكن للمستخدم استخدام حسابه العادي بحسب السياسة.
- قد يبقى ظاهرًا في `B2C Sellers` أو `B2B Sellers` كحساب بائع، لكن مع حالة متجر محظور أو معلق.
- تتوقف وظائف المتجر مثل البيع ورفع المنتجات وربما السحب من أموال المتجر بحسب السياسة.
- تعالج إعادة تفعيل المتجر من قسم المتاجر أو مركز الموافقات الخاص بالمتاجر، لأنه بعد التفعيل أصبح المتجر كيانًا له مالك عميق.

أما إذا تم حظر الحساب الأساسي:

- تتأثر كل الطبقات المرتبطة به.
- يتوقف المتجر لأنه مرتبط بمالك الحساب.
- يختفي الحساب من الأقسام الفعالة.
- يظهر في مركز الموافقات أو مركز معالجة الحسابات لإعادة التفعيل أو المراجعة.

إذا كان الإجراء تعليقًا وليس حظرًا كاملًا، فقد يبقى الحساب قابلًا للدخول، لكن يتم تعطيل الميزات المتأثرة فقط.

أما إذا كان الحظر شاملًا، فيجب أن تتوقف كل الطبقات والكيانات المعتمدة على الحساب إلى أن تتم إعادة التفعيل أو اتخاذ قرار نهائي.

هذا الفصل يمنع خلط حالة الحساب مع حالة المتجر أو الطبقة، ويجعل كل حالة تعالج في مركزها المناسب.

قاعدة الأب هنا:

- `Restriction` may target Account, Capability, Store, Request, or SubAccount.
- الحساب والمتجر والطبقة ليست نفس target.
- تفاصيل appeal / review / reactivation تخص child أو workflow PRD.

---

## 15. Event System Binding — ربط السيناريو بنظام الأحداث

كل خطوة مهمة في رحلة الحساب يجب أن تنتج حدثًا قابلًا للاستخدام.

أمثلة:

- فتح مسار تسجيل جديد.
- اختيار نوع التسجيل.
- تسجيل حساب.
- اختيار الدولة.
- تأكيد `OTP`.
- قبول السياسات.
- إنشاء `Base Account`.
- إرسال إشعار ترحيبي.
- اختيار مسار بائع.
- بدء طلب فتح متجر.
- عدم إكمال الطلب.
- إرسال الطلب.
- رفض وثيقة.
- قبول وثيقة.
- اكتمال التحقق.
- انتقال الطلب للموافقة.
- الموافقة على فتح المتجر.
- رفض فتح المتجر.
- تفعيل `SellerCapability`.
- ربط المتجر بالحساب.
- طلب اشتراك تسويق بالعمولة.
- تعليق الاشتراك.
- تفعيل الاشتراك.
- حظر المتجر.
- حظر الحساب.
- طلب إعادة التفعيل.

هذه الأحداث لا تستخدم فقط كسجل، بل يمكن أن تغذي:

- Analytics.
- CRM.
- Notifications.
- Automation.
- Support.
- Marketing.
- فهم سلوك المستخدم.
- قياس التحول من مستخدم إلى بائع.
- اكتشاف التوقف في رحلة التسجيل أو فتح المتجر.

`Event System` هنا لا يفصل داخل إدارة المستخدمين، لكنه يجب أن يكون حاضرًا في السيناريو لأن رحلة المستخدم تنتج إشارات مهمة للمنصة بالكامل.

قاعدة الأب هنا:

- هذا الأب يحدد event families and examples.
- event names and payloads النهائية يجب أن تتوافق مع Event Taxonomy وchild/workflow artifacts.
- أي إضافة حدث داخل child يجب أن تصنف: existing, local, proposed, conflicting, or taxonomy update candidate.

---

# Scenario Output Map — مخرجات السيناريو من الأقسام والصفحات

ينتج عن هذا السيناريو مجموعة أقسام وصفحات أبناء يجب أن تفصل لاحقًا كل فرع بحسب مستواه.

هذا القسم لا يعني أن كل عنصر أصبح ملفًا ناضجًا.

بعض العناصر موجودة كمسار حالي.

بعضها placeholder.

بعضها child candidate أو future artifact.

---

## Parent Routing Ledger And Recommended Build Sequence

The following order is the preferred routing sequence for maturing User Management children.

It may be updated later through controlled parent patches when child work reveals a better dependency order.

### 0. Login / Registration / Account Entry

Route type: external Web/Auth route reference.

This is part of the user journey but not a local User Management child.

The parent keeps it visible because account creation, seller path selection, OTP, policy agreement, and dashboard continuation all depend on entry logic.

The detailed artifact should belong to the Web/Auth or public onboarding documentation branch.

### 1. Verification Templates

Current route family: `verify_template`

This child must be built before request-form and review logic because templates define required documents, fields, conditions, country rules, layer rules, and entity-type rules.

It should explain template creation, editing, cloning, versioning, usage protection, impact on old/new requests, and how templates feed later request and verification flows.

### 2. Store Opening Request

Route type: future local workflow/child candidate.

This child should describe the formal request to open a store after seller registration path or user upgrade.

It must consume verification template logic instead of inventing its own requirements.

It should cover draft, incomplete, submitted, returned-for-update, abandoned, and completed request behavior at the proper child level.

### 3. Verification Center

Current route family: `verification`

This child reviews submitted requirements and evidence.

It checks completeness and validity, requests updates when needed, and produces verification outcomes or signals for approval.

It does not own final activation.

### 4. User Approvals

Current route family: `user_approvals`

This child owns user-related approval decisions such as activation, rejection, update request, suspension, and reactivation where those decisions belong to User Management.

It should not be confused with order approvals, store approvals, product approvals, payout approvals, or other approval centers owned by other parents.

### 5. All Users

Current route family: `all_users`

This child is the baseline list and account-reading pattern for base users.

It should explain the list/table behavior, searchable account identity, profile entry, account actions, export, saved views, and how the table remains focused on the base user layer instead of becoming a mixed table for every capability.

It should also route deeper local sub-children when needed:

- create user form,
- advanced filter / navigation filter,
- user profile admin view,
- user profile user-facing reference if relevant,
- edit user profile flow.

The advanced filter, table behavior, saved views, export, and profile header should be treated as reusable pattern candidates for other account-capability lists.

### 6. B2C Sellers

Current route family: `b2c_sellers`

This child displays accounts with B2C seller capability.

It should reuse the list/table/filter/profile patterns from `all_users` and add only B2C seller-specific columns, states, filters, and store/capability signals.

It must not duplicate generic table/filter logic as if it were a new component.

### 7. B2B Sellers

Current route family: `b2b_sellers`

This child displays accounts with B2B seller capability.

It should reuse the common account-list patterns while adding B2B-specific commercial/company fields, verification signals, and relationship indicators.

### 8. Agents

Current route family: `agents`

This child displays accounts with agent capability and the account-level signals needed by admin users.

Detailed operational workflows for agents should remain with the owning operational or business process if they exceed account-layer management.

### 9. Staff

Current route family: `staff`

This child displays internal staff accounts from the account-layer perspective.

Detailed permission matrices, internal access policy, and security enforcement belong to Roles & Permissions and Security.

### 10. Drivers

Route type: cross-domain account-layer child candidate.

Drivers are still base accounts and may also buy from the platform like any normal user.

User Management may show that the account has a driver capability, driver status, and whether the driver layer is active, blocked, or restricted.

Driver assignment, delivery workflow, proof of delivery, route performance, logistics state, and operational driver management belong to Operations / Drivers.

### 11. User Analytics

Current route family: `user_analytics`

This child analyzes registration, onboarding, seller path, abandonment, verification, approval, restriction, reactivation, and account lifecycle events.

It should be built after the main lifecycle and event families are clearer.

## Future Child / Workflow Candidates

The following are candidates, not automatically mature files:

- Registration And OTP Workflow — external Web/Auth or onboarding branch.
- Seller Registration Path Workflow — path before store activation.
- Store Opening Request Workflow — local workflow candidate after templates.
- Verification Workflow — local workflow under verification.
- User Approval Workflow — local workflow under User Approvals.
- Create User Form — sub-child under all_users.
- Advanced Filter / Saved Views — sub-child or reusable pattern under all_users.
- User Profile Full Admin View — sub-child under all_users.
- Edit User Profile Flow — sub-child under all_users/profile.
- SubAccounts PRD — future candidate.
- Suspensions And Reactivation PRD — future candidate or User Approvals branch depending on detail.
- User Events PRD — future candidate or analytics/audit bridge.

Future candidates must not be treated as existing repository files unless created or confirmed.

# Organizational Summary — الخلاصة التنظيمية

السيناريو الأب لإدارة المستخدمين يثبت هذه القواعد:

1. `Base Account` ثابت وهو أصل كل الطبقات.
2. تسجيل مستخدم عادي وتسجيل كبائع ينتجان `Base Account`.
3. التسجيل كبائع لا ينشئ متجرًا ولا يفعّل البيع.
4. التسجيل كبائع يسجل مسارًا تمهيديًا لإكمال `StoreOpeningRequest`.
5. المستخدم العادي يمكنه لاحقًا طلب فتح متجر بنفس مسار الطلب.
6. الدولة تحدد `CountryContext`، وليست كود هاتف فقط.
7. `PolicyAgreement` و `OTP` جزء من حلقة إنشاء الحساب.
8. إنشاء الحساب قد ينتج events وnotifications مثل الترحيب أو تأكيد الإنشاء.
9. `VerificationTemplate` يحدد المتطلبات حسب الدولة والمسار والطبقة.
10. `Verification Center` يراجع الوثائق والمتطلبات، ولا يوافق على التفعيل.
11. `Approval Center` يتخذ قرار التفعيل أو الرفض أو التعليق.
12. طلب فتح المتجر قبل التفعيل يعالج داخل إدارة المستخدمين لأنه مرتبط بمنح الحساب طبقة بائع.
13. بعد تفعيل المتجر، يصبح المتجر كيانًا عميقًا في قسم المتاجر.
14. قوائم إدارة المستخدمين تقسم الحسابات حسب الطبقة التشغيلية، وليس حسب كل ما يرتبط بالحساب في جدول واحد.
15. `All Users` يعرض طبقة المستخدم الأساسية فقط، وليس كل الحسابات بكل طبقاتها.
16. `B2C Sellers` و`B2B Sellers` يعرضان الحسابات من زاوية طبقة البائع، لا المتاجر ككيانات مستقلة.
17. المتجر كيان مستقل مرتبط بالحساب، وليس هو الحساب.
18. التسويق بالعمولة ميزة اشتراك مرتبطة بمتجر `B2C`.
19. بعض الطبقات يفتحها المسؤول فقط مثل `Staff`, `Agents`, `Drivers`.
20. الحظر يجب أن يفرق بين الحساب، التعليق، المتجر، والطبقة.
21. كل خطوة أو توقف أو انتقال مهم يجب أن ينتج `Event` أو event candidate.
22. كل قسم يعرض طبقته أو كيانه بوضوح، ويترك المعالجة العميقة للمالك المناسب.
23. كل Child PRD يجب أن يرث هذا المنطق ولا يعيد تعريفه.
24. كل Child PRD يجب أن يكون قابلًا للترجمة إلى تصميم وكود عند نضجه.

هذه القواعد تجعل إدارة المستخدمين نقطة تأسيس لفهم المنصة بالكامل، لأن كل قسم لاحق يعتمد على حسابات وطبقات وكيانات تبدأ من المستخدم، ثم تتفرع إلى المتاجر، المنتجات، الطلبات، الاشتراكات، الصلاحيات، الأحداث، والتحليلات.

---

# Parent Scenario Technical Output Index

## 0. Technical Index Purpose

This section is not a second explanation of the parent scenario.

It is the technical output index extracted from the parent scenario.

Its purpose is to give Backend, Frontend, UI/UX, Product, and future AI readers a clear technical map of what this parent scenario produces.

The scenario explains the operational story.

This technical index records the required technical outputs, boundaries, and references.

This section defines:

- Entities
- Entity Ownership
- Relationships
- Lifecycle / Journey
- Flow / Workflow Families
- State Families
- Event Families
- Pages / Sections
- UX Outputs
- Design-Ready Outputs
- Implementation-Ready Outputs
- Service Boundaries
- Integration Anchors
- Child PRD Directions
- Technical Constraints
- Open Technical Decisions

This is a parent-level technical index.

It must not become:

- Database Schema
- API Contract
- Full State Machine
- Full Permission Matrix
- Full Screen PRD
- Full Backend Implementation Plan
- Child Scenario Replacement

Detailed implementation belongs to child PRDs, workflow files, screen PRDs, state/event models, implementation notes, and technical files.

---

## 1. Technical Scope

### In Scope

This parent technical index covers the User Management system at parent level.

It defines the technical map for:

- Base Account
- User Identity
- User Profile
- Country Context
- Policy Agreement
- Registration Paths
- Seller Registration Path
- Store Opening Request
- Account Capabilities
- Verification
- Approval
- Store Linkage
- Restrictions
- User Events
- user-related pages and sections
- design-ready output families
- implementation-ready output roots
- cross-system dependencies

### Out Of Scope

This parent technical index does not define final details for:

- Database Tables
- API Payloads
- Field-Level Validation
- Screen Components
- Button Permissions
- Workflow Engine Implementation
- Event Payload Contracts
- Store Management internals
- Wallet internals
- Shipping internals
- Affiliate internals

These are handled by child PRDs or dedicated technical specifications.

---

## 2. Core Technical Principle

`AccountId` is the root identity key.

A user does not receive a new account for every role, capability, store, or operational layer.

All operational expansion must attach to the same base account.

Parent rules:

- Account is the identity root.
- Capability expands behavior.
- Seller registration path does not equal seller activation.
- Verification does not equal approval.
- Store is linked to Account but is not the Account itself.
- Restrictions may target Account, Capability, Store, Request, or SubAccount.
- Events must record meaningful transitions.
- Design outputs must reuse project-wide UI patterns.
- Implementation outputs must remain derivable from documented use cases, entities, states, events, permissions, and handoffs.

---

## 3. Core Entities Index

| Entity | Meaning | Parent-Level Role |
|---|---|---|
| `Account` | الحساب الأساسي | Root identity for all users |
| `UserProfile` | ملف عرض وتجميع | Aggregates account-related information without owning all linked data |
| `CountryContext` | سياق الدولة | Operational context affecting policies, verification, shipping, financial rules |
| `PolicyAgreement` | موافقة سياسة | Tracks policy acceptance, version, expiry, and re-acceptance when needed |
| `RegistrationPath` | مسار التسجيل | Captures whether account started as normal user or seller registration path |
| `SellerOnboardingSignal` | إشارة بدء مسار بائع | Indicates that account started or requested seller onboarding without activation |
| `AccountCapability` | قدرة تشغيلية | Adds operational ability above the account |
| `StoreOpeningRequest` | طلب فتح متجر | Request created before store provisioning |
| `Store` | متجر مستقل | Independent entity linked to account after approval |
| `VerificationTemplate` | قالب تحقق ديناميكي | Defines required verification inputs by context |
| `VerificationCase` | حالة تحقق | Tracks validation of submitted requirements |
| `ApprovalCase` | حالة موافقة | Tracks administrative or operational decision |
| `Restriction` | قيد أو تعليق | Operational limitation applied to a target |
| `UserEvent` | حدث مستخدم | Records meaningful operational transitions |
| `PermissionScope` | نطاق الصلاحية | Defines what an actor can see or do |
| `SubAccount` | حساب فرعي | Future candidate for child accounts under parent account |

`SubAccount` is a future candidate unless the project confirms or creates its detailed child artifact.

---

## 4. Entity Ownership Index

| Entity / Concept | Primary Owner | Notes |
|---|---|---|
| `Account` | User Management | Root identity |
| `UserProfile` | User Management | Display and aggregation surface |
| `CountryContext` | Governance / Country Policy / Platform Rules | Referenced by users, owned by country/policy logic |
| `PolicyAgreement` | Governance / Users | Accepted policy version and lifecycle |
| `RegistrationPath` | User Management | Registration start classification |
| `SellerOnboardingSignal` | User Management + CRM/Analytics | Indicates seller journey started before activation |
| `AccountCapability` | User Management + Roles & Permissions | Capability layer above account |
| `StoreOpeningRequest` | User Management + Approval | Request before store creation |
| `Store` | Store Management | Independent entity after provisioning |
| `VerificationTemplate` | Verification / Governance | Dynamic requirement source |
| `VerificationCase` | Verification Center | Requirement review and validation |
| `ApprovalCase` | Approval Center | Final administrative / operational decision |
| `Restriction` | Governance / Security / Owning Domain | Can target different operational objects |
| `UserEvent` | Event System | Event infrastructure |
| `Wallet Eligibility` | Financial / Wallets | Referenced by users, owned by Financial |
| `Shipping Eligibility` | Operations / Shipping | Referenced by users, owned by Operations |
| `Affiliate Access` | Affiliate / Marketing | Referenced by users, owned by Marketing / Affiliate |
| `Notifications` | Notifications System | Triggered by user-related events |

---

## 5. Identity Relationship Map

Parent-level relationship map:

- `Account` has one `UserProfile`.
- `Account` may have many `PolicyAgreement`.
- `Account` may have a `RegistrationPath`.
- `Account` may have seller onboarding signals.
- `Account` may have many `AccountCapability`.
- `Account` may create `StoreOpeningRequest`.
- `StoreOpeningRequest` may require `VerificationCase`.
- `VerificationCase` may produce or support `ApprovalCase`.
- `ApprovalCase` may activate `AccountCapability`.
- `ApprovalCase` may trigger `Store` provisioning.
- `Store` belongs to `Store Management`.
- `Store` is linked to `Account`.
- `Restriction` may target `Account`, `Capability`, `Store`, `Request`, or future `SubAccount`.
- `UserEvent` records important changes across the user lifecycle.

---

## 6. Parent Lifecycle / Journey Index

The parent scenario produces this high-level lifecycle:

1. `Entry / Login`
2. `Registration Choice`
3. `Normal User Registration` or `Seller Registration Path`
4. `Basic Account Data Collected`
5. `CountryContext Resolved`
6. `Policy Agreement Captured`
7. `OTP Verification`
8. `Base Account Created`
9. `Welcome / Confirmation Notification`
10. `Dashboard Entry`
11. `Additional Requirements Shown When Needed`
12. `Seller Path Continuation When Applicable`
13. `StoreOpeningRequest Started`
14. `Requirements Generated`
15. `VerificationCase Created`
16. `Verification Reviewed`
17. `ApprovalCase Created`
18. `Approval Decision`
19. `Capability Activated`
20. `Linked Entity Created When Needed`
21. `Operational Placement`
22. `Event Trail Continues`

This lifecycle is the parent map only.

Child PRDs define detailed transitions, edge cases, screens, and implementation behavior.

---

## 7. Workflow And Flow Families Index

The parent scenario produces workflow families.

This section does not fully define every workflow.

It identifies which flows exist, where they should be detailed, and whether a separate workflow file may be needed.

| Flow / Workflow Family | Purpose | Detailed In | Separate Workflow File Needed? |
|---|---|---|---|
| `Account Foundation Flow` | Registration, policy agreement, OTP, base identity | Auth / Users child artifacts | Only if authentication implementation is documented |
| `Country Context Flow` | Resolve operational country context | User Profile / Governance / Country rules | Maybe |
| `Policy Agreement Flow` | Accept required policies and versions | User / Governance child artifacts | Maybe |
| `Seller Registration Path Flow` | Collect seller path data without activating seller capability | User Management children | Maybe |
| `Store Opening Request Flow` | Convert seller path or upgrade into formal request | User Management / Verification / Approval children | Yes |
| `Requirements Generation Flow` | Generate required verification inputs | Verification Templates child | Yes if dynamic rule builder is implemented |
| `Verification Flow` | Submit, review, reject, request update, approve verification cases | Verification Center child | Yes |
| `Approval Flow` | Decide activation, rejection, update request, escalation | Approval-related child | Yes |
| `Capability Activation Flow` | Activate operational capability after valid requirements | Permissions / Capability / Approval artifacts | Yes if multi-system |
| `Store Provisioning Flow` | Create or link store after approval | Store Management PRD | Yes |
| `Restriction Flow` | Suspend, restrict, reactivate, appeal | Future restriction/reactivation child | Yes |
| `Event Trail Flow` | Record operational transitions and timeline events | User Analytics / Event System | Yes when payloads are defined |
| `Profile Aggregation Flow` | Assemble linked user context from multiple systems | User Profile child | Maybe |
| `Advanced Filtering Flow` | Query and save operational user views | Future filter child or screen artifact | Maybe |

Parent rule:

- Every child PRD must mention its local workflows.
- A separate Workflow PRD is required only for flows that are multi-step, state-heavy, permission-sensitive, cross-system, failure-prone, or implementation-critical.
- Workflow details must not be forced into the parent PRD unless they define parent logic.

---

## 8. State Families Index

A single `user_status` is not enough.

The parent scenario requires separate state families.

State families must align with `02_PLATFORM_STATE_TAXONOMY.md`.

| State Family | Target | Purpose | Central Alignment |
|---|---|---|---|
| `AccountStatus` | `Account` | Base account condition | Central |
| `AuthenticationStatus` | Auth context | OTP, session, login security condition | Central |
| `ProfileStatus` | `UserProfile` | Completeness or review state of profile-related data | Central |
| `PolicyAgreementStatus` | `PolicyAgreement` | Acceptance, expiry, versioning, and re-acceptance lifecycle | Central |
| `IntentStatus` | seller intent / upgrade intent | Tracks seller path or upgrade intent before formal request | Central |
| `RequestStatus` | `StoreOpeningRequest` or similar request | Operational request lifecycle | Central |
| `VerificationStatus` | `VerificationCase` | Verification progress | Central |
| `ApprovalStatus` | `ApprovalCase` | Decision progress | Central |
| `CapabilityStatus` | `AccountCapability` | Operational capability condition | Central |
| `StoreStatus` | `Store` | Store lifecycle after creation | Central |
| `RestrictionStatus` | `Restriction` | Restriction lifecycle | Central |
| `BehaviorState` | `Account` / `UserProfile` | Derived states such as inactive, at risk, high intent, or abandoned onboarding | Central |
| `SubAccountStatus` | `SubAccount` | Subaccount lifecycle and delegated access condition when subaccounts become active | Central family / future local usage |

Local modeling note:

- `RegistrationPath` is primarily a data/intent classification, not necessarily a full state family.
- `SellerOnboardingSignal` should usually map to `IntentStatus`, `RequestStatus`, or `BehaviorState` depending on whether the user is before request, inside request, or abandoned/inactive.
- Do not create `RegistrationPathStatus` or `SellerOnboardingStatus` as independent final state families unless a child workflow proves they need separate lifecycle ownership.

Example state separation:

- `AccountStatus = active`
- `IntentStatus = active`
- `IntentStatus = converted_to_request`
- `RequestStatus = submitted`
- `SellerCapabilityStatus = pending_approval`
- `StoreStatus = not_created`
- `VerificationStatus = submitted`
- `ApprovalStatus = waiting_review`
- `PolicyAgreementStatus = accepted`

State values and transitions must align with:

`02_PLATFORM_STATE_TAXONOMY.md`

or future detailed state/event model files.

---

## 9. Event Families Index

Events are not cosmetic activity logs.

They are operational signals for Notifications, CRM, Analytics, Audit, Approval, Security, Automation, Rewards, and future implementation.

User Management must align event logic with:

`03_PLATFORM_EVENT_TAXONOMY.md`

| Event Family | Example Events | Notes |
|---|---|---|
| `AccountEvents` | `account_created`, `account_updated`, `account_activated`, `account_restricted`, `account_suspended`, `account_reactivated`, `account_country_context_resolved`, `account_country_context_changed` | Base identity and account context |
| `AuthenticationEvents` | `otp_requested`, `otp_verified`, `otp_failed`, `login_succeeded`, `login_failed`, `session_created`, `session_revoked` | Authentication and access |
| `ProfileEvents` | `profile_created`, `profile_updated`, `identity_data_updated`, `contact_email_updated`, `contact_phone_updated` | Profile and contact changes |
| `IntentEvents` | `seller_intent_created`, `upgrade_intent_created`, `intent_converted_to_request`, `intent_abandoned`, `seller_intent_cancelled`, `upgrade_intent_cancelled` | Seller path and upgrade intent should prefer this family before creating new event families |
| `VerificationEvents` | `verification_case_created`, `verification_submitted`, `verification_resubmitted`, `verification_review_started`, `verification_approved`, `verification_rejected`, `verification_needs_update` | Verification lifecycle |
| `ApprovalEvents` | `approval_case_created`, `approval_review_started`, `approval_approved`, `approval_rejected`, `approval_needs_update`, `approval_escalated` | Administrative decision lifecycle |
| `CapabilityEvents` | `capability_requested`, `capability_activated`, `capability_suspended`, `capability_reactivated`, `capability_removed` | Operational layer lifecycle |
| `StoreEvents` | `store_opening_request_created`, `store_opening_request_submitted`, `store_created`, `store_activated`, `store_linked_to_account` | Store-related user expansion and handoff |
| `RestrictionEvents` | `restriction_applied`, `restriction_updated`, `restriction_removed`, `appeal_submitted`, `appeal_approved`, `appeal_rejected` | Restrictions and recovery |
| `SecurityEvents` | `permission_changed`, `role_assigned`, `role_removed`, `access_denied`, `security_alert_created` | Permission and security-sensitive actions |
| `CRMEngagementEvents` | `user_segment_entered`, `user_segment_exited`, `retention_offer_sent`, `reactivation_message_sent`, `user_reactivated` | Engagement and retention signals |
| `NotificationEvents` | `notification_created`, `notification_queued`, `notification_sent`, `notification_delivered`, `notification_failed`, `notification_opened`, `notification_clicked` | Communication lifecycle; welcome/reminder messages should usually be context on notification events |
| `BehaviorAnalyticsEvents` | `page_viewed`, `search_performed`, `filter_applied`, `store_viewed`, `banner_clicked` | Behavioral analytics when relevant to user journeys |
| `PolicyAgreementEvents` | `policy_agreement_required`, `policy_accepted`, `policy_rejected`, `policy_expired`, `policy_reacceptance_requested`, `policy_reaccepted`, `policy_version_changed` | Central event family for policy acceptance, expiry, versioning, and re-acceptance |
| `Local Extension Candidate: RegistrationEvents` | `registration_started`, `registration_completed` | Use only if registration path requires separate event ownership beyond `AccountEvents` and `AuthenticationEvents` |
| `Local Extension Candidate: SellerOnboardingEvents` | `seller_onboarding_started`, `seller_onboarding_abandoned` | Prefer `seller_intent_created` / `intent_abandoned` unless child workflow proves a separate family is needed |

Parent event rules:

- `State` means current condition.
- `Event` means something happened.
- `Metric` means a calculated number from events or states.
- `Automation` decides what to do after events, signals, or conditions.
- New event names should be treated as proposed unless already accepted in the event taxonomy.
- Child PRDs must not invent final event payloads casually.
- Event payload contracts belong to event/system or implementation artifacts.
- If a child needs a non-central event, classify it as: existing, local extension, proposed taxonomy update, conflicting, or open decision.

Examples:

- `ApprovalStatus = approved`
- `approval_approved` is an event.
- `IntentStatus = active` for a long time with no request may produce derived signal `intent_abandoned`.
- A welcome message should usually be modeled as `notification_sent` with welcome context, not as a new global event unless needed.

---

## 10. Pages / Sections Output Index

Parent scenario produces these page or section families.

| Page / Section | Parent-Level Purpose | Status |
|---|---|---|
| `Login / Registration / Account Entry` | External upstream journey reference | External Web/Auth route |
| `Verification Templates` | Requirement rules by country, account type, layer, entity, and path | Current route family |
| `Store Opening Request` | Formal request completion after seller path or upgrade | Future workflow/child candidate |
| `Verification Center` | Review submitted requirements and documents | Current route family |
| `User Approvals` | User-related activation, rejection, update request, suspension, and reactivation decisions | Current route family |
| `All Users` | Base user-layer list, reusable list pattern, and access to profiles | Current route family |
| `Create User Form` | Focused user creation form behavior | Sub-child candidate under all_users |
| `Advanced Filters / Saved Views` | Reusable scalable filtering, saved views, table navigation | Existing/candidate sub-child or reusable pattern under all_users |
| `User Profile` | Aggregated account life view | Current related placeholder/candidate under all_users |
| `Edit User Profile` | Focused profile editing behavior | Sub-child candidate under all_users/profile |
| `B2C Sellers` | Manage accounts with B2C seller capability | Current route family; should reuse common list patterns |
| `B2B Sellers` | Manage accounts with B2B seller capability | Current route family; should reuse common list patterns |
| `Agents` | Manage agent account capability | Current route family |
| `Staff` | Manage internal staff account layer | Current route family |
| `Drivers` | Account-layer visibility for driver capability | Cross-domain candidate; operations owns driver workflows |
| `User Analytics` | Lifecycle metrics, drop-off, conversion, and event insights | Current route family |

---

## 11. UX Output Index

Parent-level UX output families:

| UX Output | Meaning |
|---|---|
| `Registration Choice Pattern` | Normal user vs seller path selection |
| `Country-Aware Registration Form` | Country, province, region, policy, and requirement influence |
| `Policy Agreement Block` | Required acceptance before account creation |
| `OTP Verification Step` | Phone verification during registration |
| `Welcome / Confirmation Notification` | Account creation feedback |
| `Seller Completion Card` | Dashboard continuation card for completing store opening |
| `Account Identity Header` | Shows base identity, country, status, and main account signals |
| `Capability Badges` | Shows active or pending layers such as B2C seller, B2B seller, staff, agent |
| `State Badges` | Shows contextual state labels with target meaning |
| `Verification Panels` | Shows required documents, submitted evidence, missing items, review status |
| `Approval Queues` | Shows pending administrative decisions |
| `Event Timeline` | Shows account lifecycle and key transitions |
| `Linked Entity Cards` | Shows linked store, wallet, orders, shipping, affiliate, support context |
| `Action Panels` | Shows available actions according to state and permissions |
| `Advanced Filters` | Supports large operational lists |
| `Reusable Account List Pattern` | Table, columns, saved views, sorting, pagination, export, and bulk actions reused across account-capability lists |
| `Profile Read/Edit Pattern` | Separates account profile reading from focused edit flows with permissions, validation, and audit |
| `Empty / Loading / Error States` | Required for scalable admin screens |
| `Disabled Action Reasons` | Explains why restricted actions are blocked |

UX outputs must align with:

`05_UI_UX_DESIGN_SYSTEM_AND_VISUAL_GENERATION_STANDARD.md`

---

## 12. Service / Module Boundary Index

Conceptual boundaries:

| Boundary | Meaning |
|---|---|
| `Users` | Account identity, profile, registration path, capability root |
| `Auth` | Login, OTP, sessions, authentication security |
| `Verification` | Requirements and evidence validation |
| `Approval` | Administrative decisions and activation |
| `Roles & Permissions` | What actors can see and do |
| `Store Management` | Store entity after provisioning |
| `Notifications` | User/admin/system notifications |
| `Event System` | Operational event capture and downstream usage |
| `CRM / Automation` | Follow-up and behavior-triggered campaigns |
| `Analytics` | User lifecycle metrics |
| `Financial / Wallets` | Wallet and financial eligibility |
| `Operations / Shipping` | Shipping and country-dependent operations |
| `Affiliate / Marketing` | Affiliate subscription and marketing capability |
| `Governance / Country Policy` | Country context, policy, category, and platform rules |

This parent defines the anchors.

Each owning domain defines its own internal details.

---

## 13. API Group Index

This parent does not define final endpoints.

It identifies candidate API groups for later implementation.

| API Group Candidate | Parent-Level Meaning |
|---|---|
| `Accounts` | Create, update, search, inspect base account |
| `Registration` | Registration choice, country context, policy agreement, OTP completion |
| `Profiles` | Get profile aggregation and linked context |
| `SellerOnboarding` | Track seller registration path and completion state |
| `StoreOpeningRequests` | Create and update store opening request |
| `Capabilities` | Query or activate operational capability |
| `VerificationTemplates` | Manage requirement templates |
| `VerificationCases` | Submit and review verification cases |
| `ApprovalCases` | Review and decide activation cases |
| `Restrictions` | Apply, remove, and inspect restrictions |
| `UserEvents` | Read timeline and emit user lifecycle events |
| `UserLists` | Search, filter, and export user-related lists |

Final API names, routes, payloads, and contracts belong to implementation artifacts.

---

## 14. Cross-System Dependency Index

| Dependency | Meaning |
|---|---|
| User Management → Auth | Registration, login, OTP, sessions |
| User Management → Store Management | Store is created or activated after approval |
| User Management → Roles & Permissions | Capabilities affect access and admin actions |
| User Management → Verification | Requirements are reviewed before approval |
| User Management → Approval | Activation requires decision |
| User Management → Notifications | Lifecycle transitions may notify users/admins |
| User Management → Event System | Important transitions must emit events |
| User Management → CRM / Automation | Onboarding abandonment and lifecycle signals support follow-up |
| User Management → Analytics | Conversion, drop-off, activation, restriction metrics |
| User Management → Financial / Wallets | Wallet eligibility and seller financial behavior |
| User Management → Shipping / Operations | Country and seller state may affect shipping eligibility |
| User Management → Affiliate / Marketing | Affiliate access depends on B2C store logic |
| User Management → Governance / Country Policy | Country context affects requirements and policies |

---

## 15. Governance Output Index

Governance outputs include:

- `PolicyAgreement`
- `VerificationTemplate`
- `VerificationCase`
- `ApprovalCase`
- `PermissionScope`
- `Restriction`
- `AuditLog`
- `UserEvent`
- `CountryPolicy`
- `CategoryPolicy`
- `CapabilityActivationRule`

Governance rule:

Verification, Approval, Restriction, Moderation, Permission, and Suspension must remain distinct concepts.

---

## 16. Data Output Index

| Data Group | Parent-Level Meaning |
|---|---|
| `Account Data` | Root identity data |
| `Registration Data` | Registration choice, country, phone, policy, OTP result |
| `Profile Data` | Display and aggregation data |
| `Country Context Data` | Operational country context |
| `Policy Agreement Data` | Accepted policies and versions |
| `Seller Onboarding Data` | Seller registration path and completion signals |
| `Requirement Data` | Required verification inputs |
| `Verification Data` | Submitted documents or fields |
| `Approval Data` | Decisions, reasons, reviewers |
| `Capability Data` | Activated or pending account capabilities |
| `Store Opening Request Data` | Request before store provisioning |
| `Store Link Data` | Linked store references |
| `Restriction Data` | Restrictions and recovery status |
| `Event Data` | Timeline, audit, and operational events |
| `Notification Data` | Welcome, reminders, decision, or lifecycle notices |
| `Linked Context Data` | Wallet, orders, store, affiliate, shipping summaries |
| `SubAccount Data` | Future candidate data group if subaccounts are adopted |

---

## 17. Technical Constraints

1. `AccountId` must remain the root identity.
2. Do not create separate accounts for each role.
3. Do not treat `Seller` as a separate identity root.
4. Do not treat `Store` as a field inside `Account`.
5. Do not create a store from seller registration alone.
6. Do not activate seller capability from seller registration alone.
7. Do not merge `Verification` and `Approval`.
8. Do not use one global `user_status` for all user-related conditions.
9. Do not activate capability from registration path alone.
10. Do not create store before approval when approval is required.
11. Do not apply all restrictions only at account level.
12. Do not hide country-based rules behind phone number logic.
13. Do not make badges ambiguous in mixed-context lists.
14. Do not place child-level details inside the parent scenario.
15. Do not let child PRDs redefine parent rules.
16. Do not treat events as optional cosmetic logs.
17. Do not duplicate ownership of Store, Wallet, Shipping, or Affiliate inside Users.
18. Do not generate UI/UX visuals from the screen name only.
19. Do not generate implementation from the parent PRD alone when child-level logic is required.
20. Do not treat future child candidates as existing files unless repository evidence confirms them.
21. Do not bury parent-level discoveries inside a child without marking parent update candidates.
22. Do not repeat generic marketplace explanations that do not affect User Management logic.
23. Do not overinflate seller registration path into a separate account type.
24. Do not skip small sequence links such as welcome notification, event emission, or dashboard continuation when they affect system behavior.
25. Do not introduce final state families or event families that conflict with `02_PLATFORM_STATE_TAXONOMY.md` or `03_PLATFORM_EVENT_TAXONOMY.md`.

---

## 18. Design-Ready Output Notes

This Parent PRD must support future UI/UX generation, Figma direction, and frontend planning.

At parent level, User Management requires these design-ready output families:

| Design Output | Parent-Level Meaning |
|---|---|
| `Registration Choice Screen` | Normal user vs seller path decision |
| `Country-Aware Registration Form` | Country, province, region, policies, OTP, and dynamic requirements |
| `Seller Registration Extension` | Store name, store description, B2C/B2B, individual/company where relevant |
| `Post-Registration Dashboard Continuation` | Continue store opening request card or alert |
| `User Management App Shell` | Admin dashboard context for user operations |
| `All Users List Pattern` | Base user-layer list, filters, columns, saved views, batch actions |
| `User Profile Pattern` | Identity header, linked entities, states, timeline, actions |
| `Verification Template Builder Pattern` | Dynamic requirements, conditions, account type rules |
| `Verification Review Queue Pattern` | Submitted cases, status, reviewer actions, reasons |
| `Approval Queue Pattern` | Approval, rejection, update requests, escalation |
| `Capability Badge System` | Displays active or pending operational layers |
| `State Badge System` | Shows account, verification, approval, capability, restriction states |
| `Event Timeline Pattern` | Shows account lifecycle, verification, approval, store, restriction events |
| `Cross-System Summary Cards` | Store, wallet, orders, shipping, affiliate, support context |
| `Advanced Filter Pattern` | Large-scale filtering and saved views |
| `Smart Insight Cards` | Inactivity, abandoned seller path, campaign eligibility, risk signals |

Design rules:

1. User Management screens must use reusable components from the UI/UX standard.
2. Profile, list, review queue, and form screens should not invent separate visual languages.
3. State badges must be contextual and must not show ambiguous labels such as `Pending` without layer meaning.
4. Admin screens may be denser and more operational than customer-facing screens.
5. Visual references must align with the Pazarat UI/UX standard.
6. This parent does not define exact screen layouts.
7. Child PRDs and Screen PRDs define exact UI behavior.
8. Design output must translate the documented journey, not invent a generic marketplace screen.

---

## 19. Implementation-Ready Output Notes

This Parent PRD must support future translation into ASP.NET backend, PostgreSQL database design, Next.js frontend, APIs, tests, and implementation notes.

At parent level, User Management identifies the roots of implementation logic.

| Implementation Output | Parent-Level Meaning |
|---|---|
| `Use Cases` | Register account, verify OTP, accept policy, create base account, start seller path, continue store opening request, submit verification, review approval, activate capability, link store, restrict/reactivate account |
| `Commands` | Create account, verify OTP, accept policy, record seller path, start store opening request, submit verification, approve case, reject case, request update, activate capability, suspend account, reactivate account |
| `Queries` | Get user profile, list users, search users, get registration state, get seller completion state, get verification cases, get approval queue, get user timeline, get linked context |
| `Business Rules` | Account is root identity, capability expands behavior, seller registration is not activation, verification is not approval, store is linked but separate, restrictions may target multiple layers |
| `Validation Areas` | OTP, required account fields, country rules, policy acceptance, seller path fields, required documents, seller type requirements, duplicate submission, permission eligibility |
| `Failure Cases` | OTP failed, policy not accepted, verification rejected, approval rejected, request expired, needs update, duplicate request, unsupported country, permission denied |
| `Consistency Boundaries` | Account creation must align with OTP/policy; approval must align with capability activation; store creation must align with approval; restriction must align with affected target; event trail must align with lifecycle transitions |
| `Integration Handoffs` | User Management → Auth, Store Management, Roles & Permissions, Verification, Approval, Notifications, Events, CRM, Analytics, Wallets, Shipping |
| `Acceptance Criteria Roots` | Each child must define testable outcomes for its local workflow, states, events, permissions, UI behavior, and implementation behavior |

Implementation rules:

1. This parent does not define final database tables.
2. This parent does not define final API endpoints.
3. This parent does not define final DTOs.
4. This parent does not define exact frontend routes.
5. Child PRDs and workflow files must provide local implementation-ready detail.
6. Future implementation must align with the Pazarat implementation architecture and code generation standard.
7. Code generation must translate documented product logic and must not invent missing business behavior silently.

This section ensures that User Management documentation can later be translated into code without forcing the parent PRD to become a backend specification.

---

# Child PRD Routing Index

This routing index separates current repository routes from proposed future candidates.

It should be updated after child generation reveals better naming, missing routes, or parent-level discoveries.

## Current Or Existing Route Families

| Route / Artifact Family | Current Status | Should Detail |
|---|---|---|
| `verify_template` | Existing route family | Template builder, fields, rules, country/layer/entity conditions, versioning, protection |
| `verification` | Existing route family | Review queue, submitted evidence, missing requirements, update requests, verification outcomes |
| `user_approvals` | Current route family | User-related activation, rejection, update request, suspension, and reactivation decisions |
| `all_users` | Existing route family / placeholders | Base user list, shared account-list pattern, filters, columns, actions, export, saved views |
| `all_users/profile` | Existing related placeholders under all_users | Profile layout, linked context, lifecycle timeline, actions, read surface |
| `all_users/navigation_filter` | Existing related placeholder under all_users | Advanced filter/search/saved-view pattern; candidate for reusable account-list filtering |
| `b2c_sellers` | Existing route family | B2C seller account layer; reuse common list patterns with B2C-specific fields |
| `b2b_sellers` | Existing route family | B2B seller account layer; reuse common list patterns with commercial/company fields |
| `agents` | Existing route family | Agent account capability and admin visibility |
| `staff` | Existing route family | Internal staff account layer and admin visibility |
| `user_analytics` | Existing route family | Conversion, drop-off, lifecycle metrics |

## Sub-Child / Screen / Workflow Candidates

| Candidate | Owner | Reason |
|---|---|---|
| `Login / Registration / Account Entry` | External Web/Auth branch | Upstream route mentioned by the parent; not local User Management child |
| `Store Opening Request Workflow` | Future User Management child/workflow | Should follow verification template logic and seller path completion |
| `Create User Form` | Sub-child under all_users | Focused form with validation, permissions, audit, and account creation effects |
| `Advanced Filter / Saved Views` | Sub-child or reusable pattern under all_users | Reusable filter/table/navigation logic for many account-capability lists |
| `User Profile Full Admin View` | Sub-child under all_users | Read surface for account lifecycle, linked entities, timeline, and actions |
| `Edit User Profile Flow` | Sub-child under all_users/profile | Focused edit flow with validation, permissions, audit, and side effects |
| `User Approval Workflow` | Workflow under user_approvals | Approval decisions, escalation, update requests, reactivation, rejection |
| `Verification Workflow` | Workflow under verification | Submission, review, rejection, resubmission, completion |
| `Drivers Account Capability View` | Cross-domain candidate | User Management displays account/capability state; Operations owns driver workflows |
| `SubAccounts PRD` | Future candidate | Parent-child accounts and delegated permissions |
| `Suspensions And Reactivation PRD` | Future candidate or user_approvals branch | Restriction targets, recovery, appeals |
| `User Events PRD` | Future candidate or analytics/audit bridge | Timeline, audit, event visibility |
| `Policy Agreement Workflow` | External / Auth or governance candidate | Policy versioning, expiry, and re-acceptance |
| `Seller Registration Path Workflow` | Future onboarding workflow | Seller data before store activation |

Future candidates must not be treated as existing repository files unless created or confirmed.

---

# Parent vs Child Boundary

## Parent Owns

- General identity philosophy
- System-wide user lifecycle
- Account as identity root
- Registration path sequence
- Country context as operating context
- Policy/OTP/account creation loop
- Seller registration path vs seller activation distinction
- Verification vs approval distinction
- Entity map
- State families
- Event families
- Workflow families
- Page / section map
- Design-ready output families
- Implementation-ready output roots
- Cross-system anchors
- Technical constraints
- Child routing map

## Child Owns

- Detailed screen behavior
- Exact fields
- Exact state transitions
- Exact API contracts
- Exact validation rules
- Exact permissions
- Exact workflows
- Exact edge cases
- Exact UI components
- Exact event payloads
- Exact acceptance criteria
- Exact implementation-ready details

---

# Child Scenario Output Contract For This Parent

Any mature child PRD under User Management must include or account for the following dimensions when relevant:

1. Artifact Identity
2. Parent Inheritance
3. Local Purpose
4. Local Scope And Boundaries
5. Source Scenario Signal if based on raw input or placeholder
6. Local Scenario Narrative
7. Local Workflow
8. Local States And Events
9. Shared Primitives And Reusable Logic
10. Permissions And Visibility
11. Audit And Notifications
12. Data And Entity Outputs
13. UI/UX Translation Bridge
14. Implementation Translation Bridge
15. Acceptance And Testable Outcomes
16. Parent Update Candidates
17. Sibling And Cross-System Effects
18. Open Decisions

A child scenario that cannot guide design is not fully mature.

A child scenario that cannot guide implementation is not fully mature.

A child scenario that redefines this parent instead of inheriting from it is not valid.

---

# Shared Primitive Anchors

User Management depends on shared primitives that may be reused across many children.

Relevant primitive anchors include:

- `Base Account`
- `Registration Path`
- `Seller Registration Path`
- `Country Context`
- `Policy Agreement`
- `OTP Verification`
- `Account Capability`
- `User Lifecycle`
- `Verification`
- `Approval`
- `Rejection`
- `Suspension`
- `Reactivation`
- `Profile Ownership`
- `Permission Gate`
- `Visibility`
- `Audit Log`
- `Notification`
- `Event Emission`
- `Dashboard Table Behavior`
- `Bulk Action Behavior`
- `Document Review`
- `Seller Classification`
- `Store Linkage`
- `Reusable Account List Pattern`
- `Advanced Filter Pattern`
- `Saved View Pattern`
- `Account Table Pattern`
- `Profile Read Pattern`
- `Profile Edit Pattern`
- `Action Panel Pattern`

Child PRDs must use these anchors consistently.

If a child reveals repeated logic not defined yet, classify it as a primitive candidate and propose the correct update location.

---

# Open Technical Decisions

These decisions should not be forced inside the parent scenario.

They must be resolved in child or technical files.

| Decision | Notes |
|---|---|
| `Capability Model` | Separate table, polymorphic model, or hybrid |
| `Workflow Engine` | Shared engine or domain-specific workflow logic |
| `Restriction Targeting` | Unified target model or separate restriction tables |
| `Event Payload Standard` | Shared taxonomy and payload contract |
| `Approval Ownership` | User Approvals owns user-related decisions; other domains may own order, store, product, payout, or domain-specific approval queues |
| `Verification Template Engine` | Rule builder model and condition system |
| `SubAccount Permissions` | Inherited vs explicit permission scopes |
| `Policy Agreement Model` | Policy versioning, expiry, and re-acceptance rules |
| `Country Policy Resolution` | Runtime resolution strategy |
| `Advanced Filter Architecture` | Query builder, saved collections, indexing |
| `Profile Aggregation Strategy` | Read model, projection, or live aggregation |
| `Registration Path Modeling` | Whether registration path is stored as entity, event, or derived onboarding state |
| `Seller Onboarding Signal Modeling` | How abandoned seller registration or incomplete store request is tracked |
| `Welcome Notification Policy` | Which channels are used and whether notification is required or configurable |
| `Visual Reference Strategy` | Which child screens need visual references first |
| `Implementation Phasing` | Which child branch becomes first executable module |
| `User Approvals Boundary` | Clarify which user-related approval decisions belong under `user_approvals` and which approval decisions belong to Store, Product, Order, Payout, or other domain-specific approval queues |
| `RegistrationEvents Centralization` | Whether registration events deserve a central family or should remain derived from account/auth/intent events |

---

# Parent Update Loop

This parent is stable enough to generate children, but it is not frozen.

After creating one or more child PRDs, compare child discoveries against this parent.

If children reveal missing parent-level logic, classify it as:

- local child logic
- parent-level update candidate
- shared primitive candidate
- state taxonomy update candidate
- event taxonomy update candidate
- structure index update candidate
- UI standard update candidate
- implementation standard update candidate
- decision log candidate

Do not rewrite the parent casually.

Use patch-first updates unless the parent becomes structurally obsolete.

This reciprocal loop is part of the Pazarat documentation maturity process.

---

# Technical Index Final Rule

This file is the parent technical and narrative map.

Designers and developers should not need to re-analyze the full scenario to discover:

- what the registration sequence means
- what entities exist
- what state families are needed
- what event families are expected
- what pages and sections come from the parent
- what UX outputs are required
- what design-ready patterns are implied
- what implementation-ready roots exist
- what systems are connected
- what belongs to child PRDs
- what constraints must not be violated

The scenario explains the meaning.

The technical index fixes the outputs.

Child PRDs, Workflow PRDs, Screen PRDs, State/Event Models, Design Standards, and Implementation Standards complete the details.

---

# Final Parent Rule

User Management is a root operational area in Pazarat.

It must explain how a human account becomes a stable platform identity, how registration creates a base account, how country context affects operation, how policy agreement and OTP participate in account creation, how seller registration differs from seller activation, how verification differs from approval, how capability differs from identity, how store ownership is linked but not collapsed into account identity, and how user-related events become signals for the whole platform.

This parent should make children easier to generate, not unnecessary.

Every child must deepen one branch without breaking the parent.

Every design output must translate documented product logic.

Every implementation output must translate documented product logic.

This parent is the governing map for that process.