# PLATFORM STATE TAXONOMY

# Purpose / الهدف

This file defines the central state taxonomy and state intelligence standard for Pazarat.

هذا الملف يعرّف فهرس الحالات المركزي ومعيار فهم الحالات داخل منصة بازارات.

It defines how states should be named, grouped, scoped, documented, transitioned, connected to events, and reused across PRDs, workflows, state/event models, screen PRDs, backend design, UI/UX design, analytics, automation, and future AI reasoning.

هو يحدد كيف تُسمى الحالات، كيف تُجمع في عائلات، كيف تُربط بالكيانات، كيف توثق، كيف تنتقل، كيف ترتبط بالأحداث، وكيف تستخدم في ملفات PRD وسير العمل والشاشات والتصميم والبرمجة والتحليل والذكاء الاصطناعي.

This file is not a full state machine for every module.

هذا الملف ليس state machine تفصيلي لكل قسم.

It is the central state alphabet and state reasoning standard.

هو أبجدية الحالات المركزية ومعيار التفكير بالحالات.

Each Parent PRD identifies state families.

كل ملف أب يحدد عائلات الحالات.

Each Child PRD deepens local states.

كل ملف ابن يفصل الحالات المحلية.

Each Workflow or State/Event Model defines exact transitions.

كل Workflow أو State/Event Model يحدد الانتقالات الدقيقة.

---

# 1. Central State Family Index / فهرس عائلات الحالات المركزي

This is the first reference index.

هذا هو الفهرس الأول الذي يجب الرجوع إليه.

It shows the main state families that may exist across Pazarat.

يوضح عائلات الحالات الأساسية التي قد تظهر في المنصة.

| State Family | Arabic Meaning | Main Use |
|---|---|---|
| `AccountStatus` | حالة الحساب | Base account lifecycle |
| `AuthenticationStatus` | حالة التحقق والدخول | OTP, sessions, login security |
| `ProfileStatus` | حالة الملف الشخصي | Profile completeness and identity data |
| `IntentStatus` | حالة النية | Seller intent, upgrade intent, abandoned intent |
| `CapabilityStatus` | حالة القدرة التشغيلية | Seller, staff, driver, affiliate, or other capability |
| `RequestStatus` | حالة الطلب التشغيلي | Store request, upgrade request, payout request, return request |
| `VerificationStatus` | حالة التحقق | Verification case lifecycle |
| `ApprovalStatus` | حالة الموافقة | Approval workflow decision lifecycle |
| `RestrictionStatus` | حالة القيد | Restriction, suspension, appeal, recovery |
| `StoreStatus` | حالة المتجر | Store lifecycle |
| `VendorStatus` | حالة البائع | Vendor operational standing |
| `CategoryStatus` | حالة التصنيف | Category lifecycle and activation |
| `ProductStatus` | حالة المنتج | Product draft, review, approval, publishing |
| `InventoryStatus` | حالة المخزون | Availability, reservation, shortage |
| `CartStatus` | حالة السلة | Active, abandoned, converted, expired |
| `CheckoutStatus` | حالة إتمام الشراء | Checkout lifecycle |
| `OrderStatus` | حالة الطلب | Order lifecycle |
| `ReturnStatus` | حالة الإرجاع | Return lifecycle |
| `RefundStatus` | حالة الاسترداد | Refund lifecycle |
| `PaymentStatus` | حالة الدفع | Payment lifecycle |
| `WalletStatus` | حالة المحفظة | Wallet lifecycle and restrictions |
| `PayoutStatus` | حالة السحب | Payout lifecycle |
| `CommissionStatus` | حالة العمولة | Commission calculation and settlement |
| `InvoiceStatus` | حالة الفاتورة | Invoice lifecycle |
| `ShipmentStatus` | حالة الشحنة | Shipment lifecycle |
| `FulfillmentStatus` | حالة التنفيذ | Packing, fulfillment, handoff |
| `WarehouseStatus` | حالة المخزن | Warehouse operational state |
| `DriverStatus` | حالة السائق | Driver lifecycle and availability |
| `AddressStatus` | حالة العنوان | Address validation and delivery eligibility |
| `AffiliateStatus` | حالة الأفلييت | Affiliate application and activity |
| `CampaignStatus` | حالة الحملة | Campaign lifecycle |
| `CouponStatus` | حالة الكوبون | Coupon lifecycle |
| `RewardStatus` | حالة المكافأة | Reward lifecycle |
| `GoalStatus` | حالة الهدف | Goal or challenge lifecycle |
| `CRMStatus` | حالة العلاقة | Lifecycle stage, engagement, reactivation |
| `NotificationStatus` | حالة الإشعار | Notification delivery lifecycle |
| `SupportTicketStatus` | حالة تذكرة الدعم | Support lifecycle |
| `ReviewStatus` | حالة التقييم | Review lifecycle and moderation |
| `SecurityStatus` | حالة الأمن | Risk, lock, fraud, access security |
| `SystemJobStatus` | حالة مهمة النظام | Background jobs and system operations |
| `IntegrationStatus` | حالة التكامل | API, webhook, external integration |
| `FileProcessingStatus` | حالة معالجة الملفات | Upload, processing, verification |
| `AIInsightStatus` | حالة مخرجات الذكاء | Insight, recommendation, anomaly lifecycle |
| `BehaviorState` | حالة سلوكية مستنتجة | Inactive, abandoned, high intent, engaged |
| `PolicyAgreementStatus` | حالة الموافقة على السياسات | Policy acceptance, expiry, and re-acceptance |
| `SubAccountStatus` | حالة الحساب الفرعي | Subaccount lifecycle and delegated access |

This index is not a closed list.

هذا الفهرس ليس قائمة مغلقة.

If a PRD reveals a reusable state family that belongs platform-wide, this file should be updated.

إذا كشف أي PRD عائلة حالات قابلة لإعادة الاستخدام على مستوى المنصة، يجب تحديث هذا الملف.


---

# 1A. Taxonomy-First State Naming Gate / بوابة تسمية الحالات من التاكسونومي أولًا

Any Pazarat PRD, workflow, screen artifact, implementation note, or future AI-generated artifact must use this file as the first source for state family names and state terminology.

The model must not invent a new canonical state family inside a PRD.

Before writing any state family or state term, the model must check this file first.

## Allowed State Usage

A state reference is valid only if it is one of the following:

1. Existing central state family  
   The state family already exists in this taxonomy.

2. Local state under an existing central family  
   The state is local to one child or workflow, but it is explicitly mapped under an existing central family.

3. Proposed taxonomy candidate  
   The state family or state term is not yet in this taxonomy, but the artifact clearly labels it as proposed and identifies this file as the update target.

4. Conflicting or uncertain state  
   The artifact detects that the term may conflict with existing taxonomy and marks it as unresolved.

## Forbidden State Usage

The model must not:

- create a new state family name as if it were accepted
- use a synonym when a central taxonomy term already exists
- rename an existing state family inside a PRD
- hide a proposed state inside prose
- treat child-local wording as platform-wide terminology
- use state terms from general reasoning when project taxonomy already exists
- document implementation states without taxonomy alignment

## Required State Classification

When a PRD introduces or depends on a state, classify it as:

Existing central state
Local state under existing central family
Proposed state taxonomy candidate
Conflicting state term
Open state decision

---

# 2. Master State Term Catalog / فهرس مصطلحات الحالات المركزي

This catalog lists reusable state terms.

هذا الفهرس يسجل مصطلحات الحالات القابلة لإعادة الاستخدام.

A term may have different meaning depending on its state family.

قد يختلف معنى المصطلح حسب عائلة الحالة.

For example, `approved` in `ApprovalStatus` is not the same as `approved` in `ProductStatus`, even if the word is similar.

مثلاً، `approved` داخل `ApprovalStatus` ليست نفس `approved` داخل `ProductStatus` رغم تشابه الكلمة.

| State Term | Arabic Meaning | Common Use |
|---|---|---|
| `draft` | مسودة | Created but not submitted |
| `pending` | معلق | Waiting for next step |
| `pending_otp` | بانتظار رمز التحقق | Account or login waiting OTP |
| `pending_review` | بانتظار المراجعة | Review queue |
| `waiting_review` | بانتظار المراجعة | Approval or moderation waiting decision |
| `under_review` | قيد المراجعة | Actively being reviewed |
| `submitted` | تم الإرسال | User or system submitted request |
| `resubmitted` | أُعيد الإرسال | Submitted again after correction |
| `needs_update` | يحتاج تعديل | User must correct or complete data |
| `approved` | تمت الموافقة | Approved by owner process |
| `rejected` | مرفوض | Rejected by owner process |
| `escalated` | مصعّد | Moved to higher review level |
| `active` | فعال | Available and operational |
| `inactive` | غير نشط | Not active or dormant |
| `deactivated` | معطل | Turned off intentionally |
| `suspended` | موقوف | Temporarily blocked or restricted |
| `restricted` | مقيّد | Some actions limited |
| `locked` | مقفل | Security or financial lock |
| `blocked` | محظور | Prevented from use or visibility |
| `expired` | منتهي | Time validity ended |
| `cancelled` | ملغى | Cancelled before completion |
| `failed` | فشل | Process failed |
| `completed` | مكتمل | Process completed |
| `closed` | مغلق | Lifecycle ended |
| `archived` | مؤرشف | Retained but no longer active |
| `deleted` | محذوف | Removed from normal use |
| `restored` | مستعاد | Returned after deletion or closure |
| `available` | متاح | Available for use |
| `unavailable` | غير متاح | Not available |
| `reserved` | محجوز | Temporarily allocated |
| `released` | محرر | Reservation removed |
| `deducted` | مخصوم | Stock or balance deducted |
| `processing` | قيد المعالجة | Being processed |
| `queued` | في قائمة الانتظار | Waiting for processing |
| `sent` | مرسل | Notification/message sent |
| `delivered` | تم التسليم | Shipment or notification delivered |
| `opened` | تم الفتح | Notification/message opened |
| `clicked` | تم النقر | Link or notification clicked |
| `abandoned` | مهجور | Left without completion after time/condition |
| `converted` | تم التحويل | Intent or journey converted to next step |
| `earned` | مكتسب | Reward earned but not necessarily granted |
| `granted` | ممنوح | Reward/coupon/points granted |
| `redeemed` | مستخدم | Reward or coupon used |
| `in_transit` | في الطريق | Shipment moving |
| `out_for_delivery` | خارج للتسليم | Shipment with driver |
| `returned` | مرتجع | Shipment/order returned |
| `refunded` | مسترد | Payment/refund completed |
| `settled` | مسوى | Financial settlement complete |
| `disputed` | محل نزاع | Payment/order/review disputed |
| `healthy` | سليم | Operational condition is good |
| `at_risk` | معرض للخطر | Risk threshold detected |
| `breached` | تم تجاوز الحد | SLA or rule breached |

This catalog provides common vocabulary.

هذا الفهرس يوفر مصطلحات مشتركة.

Each PRD must still scope the term to its entity and state family.

كل PRD يجب أن يربط المصطلح بالكيان وعائلة الحالة الخاصة به.

---

# 3. State Intelligence Model / نموذج ذكاء الحالات

State reasoning must distinguish between different state layers.

يجب أن يفرّق منطق الحالات بين طبقات مختلفة.

| Layer | Meaning | Example |
|---|---|---|
| `Entity State` | Current condition of a real entity | `AccountStatus = active` |
| `Process State` | Current step in a process | `ApprovalStatus = waiting_review` |
| `Request State` | Lifecycle of a submitted request | `StoreOpeningRequestStatus = submitted` |
| `Capability State` | State of an ability attached to an account | `SellerCapabilityStatus = active` |
| `Visibility State` | Whether something is visible or published | `ProductStatus = published` |
| `Availability State` | Whether something can be used | `StockStatus = available` |
| `Financial State` | Payment, wallet, payout, invoice state | `PaymentStatus = captured` |
| `Fulfillment State` | Shipping or warehouse lifecycle state | `ShipmentStatus = in_transit` |
| `Restriction State` | Limitation or enforcement state | `RestrictionStatus = active` |
| `Behavioral State` | Derived user or actor behavior state | `UserEngagementState = inactive` |
| `Goal State` | Progress state of goal/challenge | `GoalStatus = active` |
| `System State` | Job, integration, processing state | `SystemJobStatus = failed` |

A state is always scoped.

الحالة يجب أن تكون مرتبطة بسياقها.

Do not use generic status without identifying the state family.

لا تستخدم status عام دون تحديد عائلة الحالة.

Bad:

```txt
status = pending
```

Better:

```txt
ApprovalStatus = waiting_review
VerificationStatus = submitted
PaymentStatus = pending_capture
ShipmentStatus = in_transit
```

---

# 4. State Scope Rule / قاعدة نطاق الحالة

A state must belong to a specific subject.

الحالة يجب أن تنتمي إلى كيان أو عملية محددة.

Correct examples:

```txt
AccountStatus
SellerCapabilityStatus
VerificationStatus
ApprovalStatus
StoreStatus
OrderStatus
ShipmentStatus
PaymentStatus
RewardStatus
NotificationStatus
```

Incorrect examples:

```txt
user_status
general_status
item_status
process_status
```

A single entity may have multiple state families.

قد يملك الكيان الواحد أكثر من عائلة حالة.

Example:

```txt
AccountStatus = active
SellerCapabilityStatus = pending_approval
VerificationStatus = submitted
ApprovalStatus = waiting_review
StoreStatus = not_created
```

Do not collapse multiple lifecycle meanings into one global state.

لا تختصر معاني متعددة في حالة واحدة عامة.

---

# 5. Master State Family Catalog / فهرس عائلات الحالات التفصيلي

This section gives common state sets for major families.

هذا القسم يعطي مجموعات حالات شائعة للعائلات الرئيسية.

These are reference sets, not mandatory final values for every PRD.

هذه مجموعات مرجعية وليست قيمًا نهائية مفروضة على كل PRD.

Each PRD must select or refine the values that match its local logic.

كل PRD يختار أو يضبط القيم التي تناسب منطقه.

---

## AccountStatus

```txt
pending_otp
active
restricted
suspended
deactivated
deleted
restored
```

---

## AuthenticationStatus

```txt
otp_requested
otp_verified
otp_failed
session_active
session_expired
session_revoked
login_blocked
```

---

## ProfileStatus

```txt
incomplete
complete
needs_update
under_review
verified
rejected
```

---

## IntentStatus

```txt
created
active
converted_to_request
abandoned
cancelled
expired
```

---

## CapabilityStatus

```txt
not_requested
requested
pending_verification
pending_approval
active
suspended
reactivated
removed
expired
```

---

## RequestStatus

```txt
draft
submitted
under_review
needs_update
approved
rejected
cancelled
expired
closed
```

---

## VerificationStatus

```txt
not_required
required
draft
submitted
resubmitted
under_review
approved
rejected
needs_update
expired
cancelled
```

---

## ApprovalStatus

```txt
not_required
waiting_review
under_review
approved
rejected
needs_update
escalated
reassigned
cancelled
expired
```

---

## RestrictionStatus

```txt
none
active
updated
expired
removed
appeal_submitted
appeal_approved
appeal_rejected
```

---

## StoreStatus

```txt
not_created
pending_activation
active
restricted
suspended
reactivated
closed
```

---

## ProductStatus

```txt
draft
submitted_for_review
under_review
approved
rejected
published
unpublished
blocked
deleted
archived
```

---

## InventoryStatus

```txt
available
reserved
low_stock
out_of_stock
replenishing
adjusted
transferred
```

---

## CartStatus

```txt
active
converted
abandoned
expired
cleared
```

---

## CheckoutStatus

```txt
started
address_selected
payment_method_selected
failed
completed
expired
```

---

## OrderStatus

```txt
created
confirmed
paid
payment_failed
cancelled
ready_for_fulfillment
fulfilled
completed
closed
```

---

## ReturnStatus

```txt
requested
under_review
approved
rejected
item_received
closed
```

---

## RefundStatus

```txt
requested
approved
rejected
processing
failed
completed
```

---

## PaymentStatus

```txt
initiated
authorized
captured
failed
cancelled
refunded
disputed
settled
```

---

## WalletStatus

```txt
not_created
active
locked
unlocked
restricted
closed
```

---

## PayoutStatus

```txt
requested
under_review
approved
rejected
processing
completed
failed
cancelled
```

---

## ShipmentStatus

```txt
created
assigned
picked_up
in_transit
out_for_delivery
delivery_attempted
delivered
failed
returned
cancelled
```

---

## FulfillmentStatus

```txt
not_started
started
packed
label_printed
handoff_ready
completed
failed
```

---

## DriverStatus

```txt
registered
pending_verification
verified
active
unavailable
assigned
suspended
deactivated
```

---

## CampaignStatus

```txt
draft
scheduled
active
paused
completed
cancelled
expired
```

---

## CouponStatus

```txt
created
active
granted
viewed
redeemed
expired
cancelled
```

---

## RewardStatus

```txt
pending
earned
granted
redeemed
expired
cancelled
revoked
```

---

## GoalStatus

```txt
assigned
active
in_progress
completed
failed
expired
cancelled
```

---

## NotificationStatus

```txt
created
queued
sent
delivered
failed
opened
clicked
dismissed
expired
```

---

## SupportTicketStatus

```txt
open
assigned
pending_customer
pending_support
resolved
reopened
closed
sla_breached
```

---

## SecurityStatus

```txt
normal
at_risk
locked
blocked
under_investigation
cleared
```

---

## SystemJobStatus

```txt
queued
running
completed
failed
cancelled
retrying
```

---

## FileProcessingStatus

```txt
uploaded
processing
processed
failed
verified
rejected
deleted
```

---

## AIInsightStatus

```txt
generated
reviewed
accepted
rejected
dismissed
applied
```

---

# 6. State To Event Mirror Rule / قاعدة انعكاس الحالة إلى الحدث

States and events are connected, but they are not the same.

الحالات والأحداث مترابطة لكنها ليست الشيء نفسه.

State means:

```txt
What is true now?
```

Event means:

```txt
What happened?
```

Use event logic from:

```txt
02_MY_PROJECT/pazarat/03_PLATFORM_EVENT_TAXONOMY.md
```

## Mirror Rules

1. Important state transitions should usually emit events.
2. Entering an important state may emit an event.
3. Leaving an important state may emit an event.
4. Staying too long in a state may create a derived signal.
5. Some behavioral events do not change state.
6. Some metrics are calculated from states and events, but are not states or events.
7. Not every minor technical state needs a central event.

---

# 7. State To Event Mirror Index / فهرس انعكاس الحالات إلى الأحداث

| State Family | Transition / Condition | Expected Event / Signal |
|---|---|---|
| `AccountStatus` | `pending_otp → active` | `otp_verified`, `account_activated` |
| `AccountStatus` | `active → suspended` | `account_suspended` |
| `AccountStatus` | `suspended → active` | `account_reactivated` |
| `IntentStatus` | `active → converted_to_request` | `intent_converted_to_request` |
| `IntentStatus` | `active` for X time with no action | `intent_abandoned` |
| `CapabilityStatus` | `pending_approval → active` | `capability_activated` |
| `CapabilityStatus` | `active → suspended` | `capability_suspended` |
| `VerificationStatus` | `draft → submitted` | `verification_submitted` |
| `VerificationStatus` | `submitted → approved` | `verification_approved` |
| `VerificationStatus` | `submitted → rejected` | `verification_rejected` |
| `VerificationStatus` | `submitted → needs_update` | `verification_needs_update` |
| `ApprovalStatus` | `waiting_review → approved` | `approval_approved` |
| `ApprovalStatus` | `waiting_review → rejected` | `approval_rejected` |
| `ApprovalStatus` | `waiting_review → escalated` | `approval_escalated` |
| `StoreStatus` | `pending_activation → active` | `store_activated` |
| `StoreStatus` | `active → suspended` | `store_suspended` |
| `ProductStatus` | `draft → submitted_for_review` | `product_submitted_for_review` |
| `ProductStatus` | `approved → published` | `product_published` |
| `InventoryStatus` | `available → reserved` | `stock_reserved` |
| `InventoryStatus` | `reserved → available` | `stock_released` |
| `InventoryStatus` | `reserved → deducted` | `stock_deducted` |
| `CartStatus` | `active → converted` | `checkout_started` or `checkout_completed` depending on logic |
| `CartStatus` | `active` for X time with items and no checkout | `cart_abandoned` |
| `OrderStatus` | `created → paid` | `order_paid` |
| `OrderStatus` | `paid → fulfilled` | `order_fulfilled` |
| `OrderStatus` | `fulfilled → completed` | `order_completed` |
| `PaymentStatus` | `initiated → captured` | `payment_captured` |
| `PaymentStatus` | `initiated → failed` | `payment_failed` |
| `ShipmentStatus` | `created → assigned` | `shipment_assigned` |
| `ShipmentStatus` | `in_transit → delivered` | `shipment_delivered` |
| `ShipmentStatus` | `out_for_delivery → failed` | `shipment_failed` |
| `WalletStatus` | `active → locked` | `wallet_locked` |
| `PayoutStatus` | `processing → completed` | `payout_completed` |
| `GoalStatus` | `active → completed` | `goal_completed` |
| `RewardStatus` | `earned → granted` | `reward_granted` |
| `NotificationStatus` | `queued → sent` | `notification_sent` |
| `SupportTicketStatus` | `open → resolved` | `support_ticket_resolved` |
| `SecurityStatus` | `normal → locked` | `account_locked` |

This is a reference mirror.

هذا فهرس مرجعي.

Each PRD must define its own exact transitions and events.

كل PRD يجب أن يحدد انتقالاته وأحداثه الدقيقة.

---

# 8. Derived And Time-Based States / الحالات المستنتجة والزمنية

Some states are not set directly by a user action.

بعض الحالات لا تنتج من إجراء مباشر.

They are derived from time, inactivity, thresholds, repeated behavior, or missing action.

هي تُستنتج من الوقت أو عدم النشاط أو العتبات أو السلوك المتكرر أو غياب إجراء.

Examples:

| Derived State / Signal | Logic |
|---|---|
| `cart_abandoned` | Cart has items and no checkout after X time |
| `intent_abandoned` | User created intent but did not convert to request after X time |
| `user_inactive` | User had previous activity or purchase but no activity for X time |
| `seller_at_risk` | Seller performance drops below threshold |
| `shipment_sla_breached` | Shipment remains in a state longer than SLA |
| `support_sla_breached` | Ticket remains unresolved longer than SLA |
| `goal_failed` | Goal period ended without completion |
| `reward_expired` | Reward validity ended without redemption |

Derived states must define:

- source condition
- time window
- target entity
- evaluation frequency
- resulting event or signal
- deduplication rule
- owner module

Do not create derived states without evaluation logic.

لا تنشئ حالات مستنتجة دون منطق تقييم واضح.

---

# 9. State And Metric Boundary / حدود الحالة والمؤشر

Metrics are not states.

المؤشرات ليست حالات.

A metric summarizes states or events.

المؤشر يلخص حالات أو أحداث.

| Metric / Indicator | Source |
|---|---|
| `active_users_count` | Count of `AccountStatus = active` |
| `new_users_count` | Count of `account_created` |
| `pending_approvals_count` | Count of `ApprovalStatus = waiting_review` |
| `abandoned_carts_count` | Count of `CartStatus = abandoned` or `cart_abandoned` |
| `delivered_shipments_count` | Count of `ShipmentStatus = delivered` or `shipment_delivered` |
| `conversion_rate` | `checkout_started` compared with `checkout_completed` |
| `reward_redemption_rate` | `RewardStatus = redeemed` / `RewardStatus = granted` |

Dashboards display metrics.

لوحات التحكم تعرض المؤشرات.

PRDs define the state/event logic that metrics use.

ملفات PRD تحدد منطق الحالات والأحداث الذي تعتمد عليه المؤشرات.

---

# 10. Domain State Route Index / فهرس ربط الأقسام بعائلات الحالات

This is a routing guide.

هذا دليل توجيهي.

It does not define all local states for each section.

لا يحدد كل الحالات المحلية لكل قسم.

Each Parent PRD and Child PRD must define its local state families based on its scenario.

كل ملف أب وملف ابن يحدد عائلات حالاته المحلية حسب السيناريو.

| Domain / Module | Main State Families To Check |
|---|---|
| `User Management` | `AccountStatus`, `AuthenticationStatus`, `ProfileStatus`, `IntentStatus`, `CapabilityStatus`, `VerificationStatus`, `ApprovalStatus`, `RestrictionStatus` |
| `Store Management` | `StoreStatus`, `VendorStatus`, `VerificationStatus`, `ApprovalStatus`, `RestrictionStatus`, `CampaignStatus`, `ReviewStatus` |
| `Products / Catalog` | `ProductStatus`, `CategoryStatus`, `InventoryStatus`, `ReviewStatus`, `VisibilityState` |
| `Orders` | `CartStatus`, `CheckoutStatus`, `OrderStatus`, `PaymentStatus`, `ShipmentStatus`, `ReturnStatus`, `RefundStatus` |
| `Financial` | `PaymentStatus`, `WalletStatus`, `PayoutStatus`, `CommissionStatus`, `InvoiceStatus`, `RefundStatus`, `SecurityStatus` |
| `Shipping / Operations` | `ShipmentStatus`, `FulfillmentStatus`, `WarehouseStatus`, `DriverStatus`, `AddressStatus`, `SupportTicketStatus` |
| `Marketing / CRM / Rewards` | `CampaignStatus`, `CouponStatus`, `RewardStatus`, `GoalStatus`, `CRMStatus`, `BehaviorState`, `NotificationStatus` |
| `Support` | `SupportTicketStatus`, `NotificationStatus`, `CRMStatus`, `ReviewStatus`, `SecurityStatus` |
| `System / Security` | `SecurityStatus`, `SystemJobStatus`, `IntegrationStatus`, `NotificationStatus`, `FileProcessingStatus` |
| `Smart Data / Analytics` | `BehaviorState`, `AIInsightStatus`, metric and indicator states derived from platform activity |

---

# 11. State Naming Standard / معيار تسمية الحالات

Use clear, scoped, lowercase snake_case state values.

استخدم أسماء واضحة ومحددة وبنمط snake_case.

Good:

```txt
pending_review
waiting_review
approved
rejected
needs_update
active
suspended
completed
failed
expired
```

Avoid vague values.

تجنب القيم الغامضة.

Bad:

```txt
ok
done
new
old
normal
problem
```

Use state family names to remove ambiguity.

استخدم عائلة الحالة لإزالة الالتباس.

Example:

```txt
ApprovalStatus = approved
ProductStatus = approved
VerificationStatus = approved
```

The same word may exist in multiple families, but the state family gives it meaning.

قد تتكرر الكلمة في أكثر من عائلة، لكن عائلة الحالة تحدد معناها.

---

# 12. State Transition Documentation Standard / معيار توثيق انتقالات الحالات

A PRD that introduces state logic should document:

أي PRD يتضمن منطق حالات يجب أن يوثق:

| Item | Meaning |
|---|---|
| `State Family` | Which state family this belongs to |
| `Subject Entity` | Entity or process that owns the state |
| `Allowed States` | Valid state values |
| `Initial State` | First state in lifecycle |
| `Terminal States` | End states such as completed, cancelled, rejected |
| `Transition Trigger` | What causes movement |
| `Allowed Transitions` | Valid movements between states |
| `Blocked Transitions` | Invalid movements |
| `Emitted Events` | Events produced by transitions |
| `Permissions` | Who can cause transition |
| `Visibility` | Who can see state |
| `UI Output` | Badge, status label, alert, timeline |
| `Open Decision` | Unresolved state naming or transition issue |

Parent PRDs identify state families.

ملفات الأب تحدد عائلات الحالات.

Child PRDs define local state values and transitions.

ملفات الابن تحدد القيم والانتقالات المحلية.

State/Event Models define exact lifecycle rules.

ملفات State/Event Model تحدد قواعد دورة الحياة الدقيقة.

---

# 13. State UI Output Standard / معيار إظهار الحالة في الواجهة

States often appear in UI.

الحالات تظهر غالبًا في الواجهة.

Possible UI outputs:

- status badge
- timeline item
- disabled action reason
- required action panel
- review queue label
- warning alert
- progress stepper
- filter option
- dashboard metric
- empty state explanation

State labels must be context-aware.

تسمية الحالة يجب أن تكون مفهومة حسب السياق.

Example:

`pending` inside `B2B Sellers` may be understandable.

But `pending` inside `All Users` is ambiguous unless the layer is shown.

Better:

```txt
Seller Capability: pending approval
Verification: submitted
Store: not created
```

Do not make a badge carry all meaning alone.

لا تجعل الشارة وحدها تحمل كل المعنى.

---

# 14. State Quality Gate / بوابة جودة الحالة

Before accepting state documentation, verify:

قبل اعتماد توثيق أي حالة، تحقق من:

1. Is the state scoped to a clear entity or process?
2. Is the state family named?
3. Are allowed values clear?
4. Is the initial state clear?
5. Are terminal states clear?
6. Are transitions clear?
7. Are invalid transitions considered?
8. Are emitted events identified?
9. Are permissions considered?
10. Is UI visibility considered?
11. Is the state not replacing several different state families?
12. Is the state not actually a metric?
13. Is the state not actually an automation command?
14. If time-based, is evaluation logic clear?
15. Does it align with the event taxonomy?

---

# 15. State Feedback Loop / حلقة تغذية الحالات

The central state taxonomy and PRDs must improve each other.

يجب أن يطوّر ملف الحالات وملفات PRD بعضهما.

If a PRD reveals a meaningful local state:

إذا كشف PRD حالة محلية مهمة:

- document it inside the PRD
- classify its state family
- decide if it is reusable platform-wide
- update this file only if it becomes central

If this taxonomy suggests a state family a PRD forgot:

إذا اقترح هذا الفهرس عائلة حالات قد تكون مفقودة في PRD:

- review the PRD
- decide whether the state family applies
- add it if it reflects real section logic
- do not force it if it does not apply

The PRD owns local truth.

ملف PRD يملك الحقيقة المحلية.

This taxonomy guides discovery and consistency.

هذا الملف يوجه الاكتشاف والاتساق.

---

# 16. State Anti-Patterns / أخطاء شائعة

| Anti-Pattern | Bad | Better |
|---|---|---|
| Global status | `user_status` for everything | `AccountStatus`, `CapabilityStatus`, `VerificationStatus` |
| Vague state | `ok`, `done`, `problem` | `active`, `completed`, `failed`, `needs_update` |
| Metric as state | `new_users_count` | metric from `account_created` or account records |
| Event as state | `approval_approved` | `ApprovalStatus = approved` |
| Command as state | `send_coupon` | automation action, not state |
| Mixed ownership | wallet state inside user state | `WalletStatus` owned by Financial |
| UI-only state | badge text without lifecycle | define actual state family |
| Missing event mirror | transition with no event | add event if transition is meaningful |
| Overloaded pending | one `pending` for all contexts | scoped pending: `pending_review`, `pending_approval`, `pending_payment` |

---

# 17. Applying This Taxonomy / طريقة تطبيق الملف

When building or reviewing any PRD:

عند بناء أو مراجعة أي PRD:

1. Identify the entities.
2. Identify the state families.
3. Identify allowed states.
4. Identify transitions.
5. Identify events produced by transitions.
6. Identify UI outputs.
7. Identify permissions.
8. Identify cross-system effects.
9. Identify metrics that depend on states.
10. Identify derived or time-based states.
11. Decide what belongs in parent.
12. Decide what belongs in child.
13. Decide what belongs in workflow or state/event model.

---

# 18. Final Rule / القاعدة النهائية

States describe what is true now.

الحالات تصف ما هو صحيح الآن.

Events describe what happened.

الأحداث تصف ما حدث.

Transitions explain how states change.

الانتقالات تشرح كيف تتغير الحالات.

Derived states explain what the system infers from time, inactivity, thresholds, or behavior.

الحالات المستنتجة تشرح ما يستنتجه النظام من الوقت أو عدم النشاط أو العتبات أو السلوك.

Metrics summarize states and events.

المؤشرات تلخص الحالات والأحداث.

Automation reacts to states, events, signals, and conditions.

الأتمتة تتفاعل مع الحالات والأحداث والإشارات والشروط.

Every mature Pazarat PRD must identify its state families, document state logic at the correct level, connect important transitions to events, and avoid hiding lifecycle logic inside vague prose.

كل PRD ناضج في بازارات يجب أن يحدد عائلات حالاته، ويوثق منطق الحالات في المستوى الصحيح، ويربط الانتقالات المهمة بالأحداث، ويتجنب إخفاء دورة الحياة داخل نصوص عامة.
