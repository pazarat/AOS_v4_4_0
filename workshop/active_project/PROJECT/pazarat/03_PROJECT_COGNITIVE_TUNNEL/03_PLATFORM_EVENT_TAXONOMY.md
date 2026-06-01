# PLATFORM EVENT TAXONOMY

# Purpose / الهدف

This file defines the central event taxonomy and event intelligence standard for Pazarat.

هذا الملف يعرّف فهرس الأحداث المركزي ومعيار فهم الأحداث داخل منصة بازارات.

It defines the event alphabet of the platform.

هو يحدد أبجدية الأحداث في المنصة.

Each PRD, workflow, state model, screen PRD, automation system, reward system, CRM system, analytics system, notification system, and future AI reasoning process must use this file to understand:

- what an event is
- what is not an event
- how events are named
- how events relate to states
- how events become triggers
- how events feed metrics and analytics
- how events power automation and rewards
- how events are documented inside PRDs
- how events are inherited from parent PRDs to child PRDs
- how new reusable events are discovered and promoted to this central file

هذا الملف ليس ملف حملات، وليس ملف أتمتة، وليس ملف قوالب إشعارات، وليس مواصفة payload نهائية.

هو مرجع مركزي يساعدنا على بناء الأحداث داخل كل قسم بدقة وبدون عشوائية.

---

# 1. Central Event Family Index / فهرس عائلات الأحداث المركزي

This is the first reference index.

هذا هو الفهرس الأول الذي يجب الرجوع إليه.

It shows the main event families that may exist across Pazarat.

يوضح عائلات الأحداث الأساسية التي قد تظهر في كل المنصة.

| Event Family | Arabic Meaning | Main Use |
|---|---|---|
| `AccountEvents` | أحداث الحساب | Account lifecycle and identity |
| `AuthenticationEvents` | أحداث الدخول والتحقق | Login, OTP, sessions, password |
| `ProfileEvents` | أحداث الملف الشخصي | Profile, contact, address, identity data |
| `IntentEvents` | أحداث النية | Seller intent, upgrade intent, abandoned intent |
| `CapabilityEvents` | أحداث القدرات | Activation, suspension, reactivation of account capabilities |
| `VerificationEvents` | أحداث التحقق | Verification cases, submissions, approvals, rejections |
| `ApprovalEvents` | أحداث الموافقات | Approval workflow and decisions |
| `RestrictionEvents` | أحداث القيود | Restrictions, suspensions, appeals |
| `StoreEvents` | أحداث المتاجر | Store requests, activation, suspension, linkage |
| `CategoryEvents` | أحداث التصنيفات | Category lifecycle and rules |
| `ProductEvents` | أحداث المنتجات | Product lifecycle, publishing, blocking, views |
| `InventoryEvents` | أحداث المخزون | Stock reservation, deduction, replenishment |
| `CartCheckoutEvents` | أحداث السلة والدفع المبدئي | Cart behavior and checkout journey |
| `OrderEvents` | أحداث الطلبات | Order lifecycle |
| `ReturnRefundEvents` | أحداث الإرجاع والاسترداد | Return and refund lifecycle |
| `PaymentEvents` | أحداث الدفع | Payment lifecycle |
| `WalletEvents` | أحداث المحافظ | Wallet and balance lifecycle |
| `PayoutCommissionEvents` | أحداث العمولات والسحوبات | Commission, payout, invoices |
| `ShippingEvents` | أحداث الشحن | Shipment lifecycle |
| `FulfillmentWarehouseEvents` | أحداث التنفيذ والمخازن | Packing, barcode, warehouse operations |
| `DriverEvents` | أحداث السائقين | Driver lifecycle and delivery behavior |
| `AddressEvents` | أحداث العناوين | Address verification and eligibility |
| `AffiliateEvents` | أحداث الأفلييت | Affiliate links, conversions, commissions |
| `CampaignEvents` | أحداث الحملات | Campaigns, offers, coupons |
| `RewardEvents` | أحداث المكافآت | Rewards, points, cashback, draw entries |
| `GoalChallengeEvents` | أحداث الأهداف والتحديات | Goals, challenges, streaks, progress |
| `CRMEngagementEvents` | أحداث العلاقة والتفاعل | Segments, retention, reactivation |
| `NotificationEvents` | أحداث الإشعارات | Notification lifecycle |
| `SupportEvents` | أحداث الدعم | Tickets, messages, SLA |
| `ReviewRatingEvents` | أحداث التقييمات | Reviews, ratings, reputation |
| `SecurityEvents` | أحداث الأمن | Fraud, permissions, access, alerts |
| `SystemEvents` | أحداث النظام | Settings, integrations, jobs, webhooks |
| `FileMediaEvents` | أحداث الملفات والوسائط | Uploads, processing, document handling |
| `AIInsightEvents` | أحداث الذكاء والتحليل | AI insights, recommendations, anomalies |
| `BehaviorAnalyticsEvents` | أحداث السلوك والتحليل | Views, searches, clicks, behavior tracking |
| `PolicyAgreementEvents` | أحداث الموافقة على السياسات | Terms, policies, versions, re-acceptance |
| `SubscriptionEvents` | أحداث الاشتراكات | Plans, renewals, expiry, cancellation |
| `RequestEvents` | أحداث الطلبات التشغيلية | Generic request lifecycle before domain-specific ownership |
| `CountryContextEvents` | أحداث سياق الدولة | Country context resolution, changes, eligibility impact |

This index is not a closed list.

هذا الفهرس ليس قائمة مغلقة.

If a PRD reveals a reusable event family that belongs platform-wide, this file should be updated.

إذا كشف أي PRD عائلة أحداث قابلة لإعادة الاستخدام على مستوى المنصة، يجب تحديث هذا الملف.

---

# 1A. Taxonomy-First Event Naming Gate / بوابة تسمية الأحداث من التاكسونومي أولًا

Any Pazarat PRD, workflow, screen artifact, automation note, analytics note, notification note, implementation note, or future AI-generated artifact must use this file as the first source for event family names and event terminology.

The model must not invent a new canonical event family inside a PRD.

Before writing any event family or event name, the model must check this file first.

## Allowed Event Usage

An event reference is valid only if it is one of the following:

1. Existing central event family  
   The event family already exists in this taxonomy.

2. Local event under an existing central family  
   The event is local to one child, workflow, or module, but it is explicitly mapped under an existing central event family.

3. Proposed event taxonomy candidate  
   The event family or event name is not yet in this taxonomy, but the artifact clearly labels it as proposed and identifies this file as the update target.

4. Conflicting or uncertain event  
   The artifact detects that the term may conflict with existing taxonomy and marks it as unresolved.

## Forbidden Event Usage

The model must not:

- create a new event family name as if it were accepted
- use a synonym when a central taxonomy event family already exists
- rename an existing event family inside a PRD
- hide a proposed event inside prose
- treat child-local event wording as platform-wide terminology
- use event names from general reasoning when project taxonomy already exists
- document analytics, notifications, automations, or audit triggers without event taxonomy alignment

## Required Event Classification

When a PRD introduces or depends on an event, classify it as:

    Existing central event
    Local event under existing central family
    Proposed event taxonomy candidate
    Conflicting event term
    Open event decision

If the term is proposed, the PRD must not treat it as accepted project truth.

## Event Naming Priority

Use this priority:

    1. Exact existing event family in 03_PLATFORM_EVENT_TAXONOMY.md
    2. Existing central event family with local child-specific event underneath
    3. Proposed event taxonomy candidate with explicit label
    4. Open decision

Do not reverse this order.

## Example

Incorrect:

    SellerOnboardingEvents

if it is not defined as a central event family.

Correct alternatives:

    IntentEvents — if describing seller path or upgrade intent
    RequestEvents — if describing formal store-opening request lifecycle
    AccountEvents — if describing account creation or account lifecycle
    NotificationEvents — if describing notification delivery
    BehaviorAnalyticsEvents — if describing derived abandonment or engagement signals
    Proposed event taxonomy candidate: SellerOnboardingEvents

The model must choose the closest existing central family unless the project truly needs a new reusable family.

---

# 2. Master Event Catalog / الفهرس المركزي للأحداث

This catalog lists core reusable events.

هذا الفهرس يسجل الأحداث الأساسية القابلة لإعادة الاستخدام.

It does not replace local PRD event documentation.

لا يستبدل توثيق الأحداث داخل كل PRD.

Each module must still document the exact local events that apply to its own scenario.

كل قسم يجب أن يوثق الأحداث الدقيقة التي تنطبق على سيناريوهاته.

| Event Family | Core Events |
|---|---|
| `AccountEvents` | `account_created`, `account_updated`, `account_activated`, `account_deactivated`, `account_restricted`, `account_suspended`, `account_reactivated`, `account_deleted`, `account_restored`, `account_country_context_resolved`, `account_country_context_changed` |
| `AuthenticationEvents` | `login_succeeded`, `login_failed`, `logout_completed`, `otp_requested`, `otp_verified`, `otp_failed`, `password_changed`, `password_reset_requested`, `password_reset_completed`, `two_factor_enabled`, `two_factor_disabled`, `session_created`, `session_revoked` |
| `ProfileEvents` | `profile_created`, `profile_updated`, `profile_photo_updated`, `contact_email_updated`, `contact_phone_updated`, `identity_data_updated`, `address_added`, `address_updated`, `address_removed` |
| `IntentEvents` | `seller_intent_created`, `seller_intent_cancelled`, `seller_intent_abandoned`, `upgrade_intent_created`, `upgrade_intent_cancelled`, `intent_converted_to_request`, `intent_abandoned` |
| `CapabilityEvents` | `capability_requested`, `capability_activated`, `capability_suspended`, `capability_reactivated`, `capability_removed`, `capability_expired` |
| `VerificationEvents` | `verification_case_created`, `verification_requirement_generated`, `verification_submitted`, `verification_resubmitted`, `verification_review_started`, `verification_approved`, `verification_rejected`, `verification_needs_update`, `verification_expired`, `verification_cancelled` |
| `ApprovalEvents` | `approval_case_created`, `approval_review_started`, `approval_approved`, `approval_rejected`, `approval_needs_update`, `approval_escalated`, `approval_reassigned`, `approval_cancelled`, `approval_expired` |
| `RestrictionEvents` | `restriction_applied`, `restriction_updated`, `restriction_removed`, `restriction_expired`, `appeal_submitted`, `appeal_approved`, `appeal_rejected` |
| `StoreEvents` | `store_opening_request_created`, `store_opening_request_submitted`, `store_created`, `store_activated`, `store_updated`, `store_suspended`, `store_reactivated`, `store_closed`, `store_linked_to_account`, `vendor_plan_changed`, `vendor_rating_updated` |
| `CategoryEvents` | `category_created`, `category_updated`, `category_activated`, `category_deactivated`, `category_policy_updated`, `category_attribute_updated` |
| `ProductEvents` | `product_created`, `product_updated`, `product_submitted_for_review`, `product_approved`, `product_rejected`, `product_published`, `product_unpublished`, `product_blocked`, `product_unblocked`, `product_deleted`, `product_price_changed`, `product_stock_changed`, `product_viewed`, `product_added_to_wishlist` |
| `InventoryEvents` | `stock_reserved`, `stock_released`, `stock_deducted`, `stock_replenished`, `stock_adjusted`, `stock_below_threshold`, `inventory_count_started`, `inventory_count_completed`, `warehouse_stock_transferred` |
| `CartCheckoutEvents` | `cart_created`, `cart_item_added`, `cart_item_removed`, `cart_abandoned`, `checkout_started`, `checkout_address_selected`, `checkout_payment_method_selected`, `checkout_failed`, `checkout_completed` |
| `OrderEvents` | `order_created`, `order_confirmed`, `order_paid`, `order_payment_failed`, `order_cancelled`, `order_updated`, `order_ready_for_fulfillment`, `order_fulfilled`, `order_completed`, `order_closed` |
| `ReturnRefundEvents` | `return_requested`, `return_approved`, `return_rejected`, `return_item_received`, `refund_requested`, `refund_approved`, `refund_rejected`, `refund_processed`, `refund_failed`, `refund_completed` |
| `PaymentEvents` | `payment_initiated`, `payment_authorized`, `payment_captured`, `payment_failed`, `payment_cancelled`, `payment_refunded`, `payment_disputed`, `payment_settled` |
| `WalletEvents` | `wallet_created`, `wallet_activated`, `wallet_credit_added`, `wallet_debit_added`, `wallet_balance_updated`, `wallet_locked`, `wallet_unlocked`, `wallet_transaction_created`, `wallet_transaction_reversed` |
| `PayoutCommissionEvents` | `commission_calculated`, `commission_adjusted`, `payout_requested`, `payout_approved`, `payout_rejected`, `payout_processing_started`, `payout_completed`, `payout_failed`, `invoice_generated`, `invoice_paid` |
| `ShippingEvents` | `shipment_created`, `shipment_assigned`, `shipment_picked_up`, `shipment_in_transit`, `shipment_out_for_delivery`, `shipment_delivery_attempted`, `shipment_delivered`, `shipment_failed`, `shipment_returned`, `shipment_cancelled`, `tracking_updated` |
| `FulfillmentWarehouseEvents` | `fulfillment_started`, `fulfillment_completed`, `package_packed`, `package_label_printed`, `barcode_scanned`, `warehouse_receiving_started`, `warehouse_receiving_completed`, `warehouse_transfer_created`, `warehouse_transfer_completed`, `item_damaged_reported` |
| `DriverEvents` | `driver_registered`, `driver_verified`, `driver_activated`, `driver_suspended`, `driver_assigned_to_shipment`, `driver_location_updated`, `delivery_started`, `delivery_completed`, `delivery_failed`, `driver_rating_updated` |
| `AddressEvents` | `address_created`, `address_updated`, `address_deleted`, `address_verified`, `address_geocoded`, `address_delivery_eligibility_checked` |
| `AffiliateEvents` | `affiliate_application_submitted`, `affiliate_approved`, `affiliate_rejected`, `affiliate_link_created`, `affiliate_link_clicked`, `affiliate_conversion_recorded`, `affiliate_commission_calculated`, `affiliate_payout_created` |
| `CampaignEvents` | `campaign_created`, `campaign_started`, `campaign_paused`, `campaign_completed`, `offer_sent`, `offer_viewed`, `offer_clicked`, `coupon_created`, `coupon_granted`, `coupon_viewed`, `coupon_redeemed`, `coupon_expired` |
| `RewardEvents` | `reward_earned`, `reward_granted`, `reward_redeemed`, `reward_expired`, `points_granted`, `points_redeemed`, `cashback_granted`, `draw_entry_earned`, `draw_entry_used`, `raffle_draw_completed`, `winner_selected` |
| `GoalChallengeEvents` | `goal_assigned`, `goal_started`, `goal_progress_updated`, `goal_completed`, `goal_failed`, `challenge_joined`, `challenge_completed`, `challenge_failed`, `streak_started`, `streak_progress_updated`, `streak_completed`, `streak_broken` |
| `CRMEngagementEvents` | `user_segment_entered`, `user_segment_exited`, `retention_offer_sent`, `reactivation_message_sent`, `user_reactivated`, `customer_lifecycle_stage_changed`, `crm_task_created`, `crm_task_completed` |
| `NotificationEvents` | `notification_created`, `notification_queued`, `notification_sent`, `notification_delivered`, `notification_failed`, `notification_opened`, `notification_clicked`, `notification_dismissed` |
| `SupportEvents` | `support_ticket_created`, `support_ticket_assigned`, `support_ticket_updated`, `support_ticket_resolved`, `support_ticket_reopened`, `support_message_sent`, `support_sla_breached` |
| `ReviewRatingEvents` | `review_submitted`, `review_approved`, `review_rejected`, `review_updated`, `rating_submitted`, `rating_updated`, `seller_rating_changed`, `product_rating_changed`, `driver_rating_changed` |
| `SecurityEvents` | `suspicious_login_detected`, `fraud_check_started`, `fraud_check_passed`, `fraud_check_failed`, `account_lock_requested`, `account_locked`, `permission_changed`, `role_assigned`, `role_removed`, `access_denied`, `security_alert_created` |
| `SystemEvents` | `setting_updated`, `policy_updated`, `integration_connected`, `integration_disconnected`, `api_key_created`, `api_key_revoked`, `webhook_created`, `webhook_failed`, `system_job_started`, `system_job_completed`, `system_job_failed` |
| `FileMediaEvents` | `file_uploaded`, `file_processed`, `file_processing_failed`, `file_deleted`, `image_uploaded`, `image_optimized`, `document_uploaded`, `document_verified`, `document_rejected` |
| `AIInsightEvents` | `ai_insight_generated`, `ai_recommendation_generated`, `ai_anomaly_detected`, `ai_classification_completed`, `ai_summary_generated`, `ai_action_suggested`, `ai_action_accepted`, `ai_action_rejected` |
| `BehaviorAnalyticsEvents` | `page_viewed`, `search_performed`, `filter_applied`, `product_viewed`, `store_viewed`, `banner_clicked`, `wishlist_item_added`, `cart_item_added`, `checkout_started`, `checkout_abandoned` |
| `PolicyAgreementEvents` | `policy_agreement_required`, `policy_accepted`, `policy_rejected`, `policy_expired`, `policy_reacceptance_requested`, `policy_reaccepted`, `policy_version_changed` |
| `SubscriptionEvents` | `subscription_requested`, `subscription_started`, `subscription_renewed`, `subscription_upgraded`, `subscription_downgraded`, `subscription_cancelled`, `subscription_expired`, `subscription_suspended`, `subscription_reactivated`, `subscription_payment_failed` |
| `RequestEvents` | `request_created`, `request_updated`, `request_submitted`, `request_cancelled`, `request_expired`, `request_needs_update`, `request_resubmitted`, `request_converted_to_case`, `request_closed` |
| `CountryContextEvents` | `country_context_resolved`, `country_context_changed`, `country_policy_applied`, `country_policy_changed`, `country_eligibility_checked`, `country_requirement_generated`, `country_operation_blocked` |

---

# 3. Event Intelligence Model / نموذج ذكاء الأحداث

Pazarat event reasoning must distinguish between different signal layers.

يجب أن يفرّق منطق الأحداث في بازارات بين طبقات مختلفة.

| Layer | Meaning | Example |
|---|---|---|
| `State` | Current condition of an entity | `CartStatus = active` |
| `Fact Event` | Something actually happened | `account_created` |
| `Behavior Event` | User or actor behavior worth tracking | `product_viewed` |
| `Derived Signal` | Signal inferred from time, absence, threshold, or pattern | `cart_abandoned`, `user_inactive_for_30_days` |
| `Metric / Indicator` | Aggregated number calculated from events | `new_users_count`, `orders_today` |
| `Automation Rule` | Rule that decides what to do | if new user and campaign active, grant coupon |
| `Action Result Event` | Event produced after action succeeds | `coupon_granted` |
| `Notification Event` | Lifecycle of a sent notification | `notification_sent`, `notification_opened` |
| `Reward Event` | Reward lifecycle event | `reward_granted`, `reward_redeemed` |
| `Audit Event` | Event preserved for traceability | `permission_changed` |

The event is the alphabet.

الحدث هو الأبجدية.

Domain PRDs compose meaning from this alphabet.

ملفات الأقسام تؤلف المعنى من هذه الأبجدية حسب سيناريو كل قسم.

---

# 4. Master Terms Index / فهرس المصطلحات الأساسية

| Term | Definition | الشرح العربي |
|---|---|---|
| `State` | Current condition of an entity | الحالة الحالية لكيان |
| `Event` | Recorded fact that something happened | تسجيل أن شيئًا حدث |
| `Fact Event` | Operational event from a real system action or transition | حدث تشغيلي حقيقي |
| `Behavior Event` | Event describing user or actor behavior | حدث سلوكي للتحليل |
| `Derived Signal` | Signal inferred from time, inactivity, threshold, or pattern | إشارة مستنتجة من زمن أو نمط |
| `Metric` | Calculated number from events or states | رقم محسوب من الأحداث أو الحالات |
| `Indicator` | Displayed metric or KPI | مؤشر معروض |
| `Trigger` | Signal that starts evaluation | مشغل يبدأ التقييم |
| `Condition` | Rule that must be true before action | شرط قبل التنفيذ |
| `Automation Rule` | Logic that reacts to triggers and conditions | قاعدة أتمتة |
| `Campaign` | Marketing or engagement program | حملة تسويقية أو تفاعلية |
| `Goal` | Objective measured over time or behavior | هدف قابل للقياس |
| `Challenge` | Time-bound or campaign-bound goal | تحدي مرتبط بزمن أو حملة |
| `Reward` | Benefit granted after eligibility or completion | مكافأة |
| `Consumer` | System that uses an event | مستهلك الحدث |
| `Source Event` | Original event that starts evaluation | الحدث المصدر |
| `Result Event` | Event produced after action succeeds | حدث النتيجة |
| `Correlation` | Link between related events | ترابط بين أحداث |
| `Causation` | Link between cause event and result event | علاقة سبب ونتيجة |

---

# 5. State To Event Relationship / علاقة الحالة بالحدث

States and events are mirrors, but they are not the same.

الحالات والأحداث متقابلة، لكنها ليست الشيء نفسه.

States must follow:

    02_MY_PROJECT/pazarat/02_PLATFORM_STATE_TAXONOMY.md

## Rules

1. A state describes what is true now.
2. An event records what happened.
3. A meaningful state transition usually produces an event.
4. Staying in a state for too long may produce a derived signal.
5. Some behavior events do not change state.
6. Some metrics are calculated from many events and are not events themselves.
7. Not every minor state change deserves a central event.

## Examples

| Pattern | Example |
|---|---|
| State transition produces event | `ApprovalStatus: waiting_review → approved` produces `approval_approved` |
| State transition produces event | `ShipmentStatus: out_for_delivery → delivered` produces `shipment_delivered` |
| Time in state produces derived signal | `CartStatus = active` for X days without checkout produces `cart_abandoned` |
| Inactivity produces derived signal | no purchase for 30 days after previous purchase produces `user_inactive_for_30_days` |
| Behavior produces analytics event | product page opened produces `product_viewed` |
| Event produces metric | many `account_created` events produce `new_users_count` |

---

# 6. Metrics And Indicators Are Not Events / المؤشرات ليست أحداثًا

Metrics and indicators are calculated from events or states.

المؤشرات والأرقام تُحسب من الأحداث أو الحالات.

They are not events by themselves.

هي ليست أحداثًا بحد ذاتها.

| Metric / Indicator | Source |
|---|---|
| `new_users_count` | Count of `account_created` |
| `orders_today` | Count of `order_created` |
| `paid_orders_count` | Count of `order_paid` |
| `delivered_shipments_count` | Count of `shipment_delivered` |
| `conversion_rate` | `checkout_started` compared with `checkout_completed` |
| `cart_abandonment_rate` | `cart_created` / `cart_abandoned` / `checkout_completed` |
| `reactivated_users_count` | Count of `user_reactivated` |
| `active_sellers_count` | Count or state query of active seller capabilities |
| `reward_redemption_rate` | `reward_granted` compared with `reward_redeemed` |

Dashboards use metrics.

لوحات التحكم تستخدم المؤشرات.

Events feed metrics.

الأحداث تغذي المؤشرات.

Do not confuse a metric with an event.

لا تخلط المؤشر بالحدث.

---

# 7. Automation Grammar / قواعد الأتمتة

Automation uses events, states, conditions, schedules, and derived signals.

الأتمتة تستخدم الأحداث والحالات والشروط والزمن والإشارات المستنتجة.

## Standard Automation Pattern

    Source Event / Signal
    → Eligibility Conditions
    → Automation Rule
    → Action
    → Result Event
    → Consumers

## Example

    Source Event: account_created
    Condition: welcome_campaign_active = true
    Condition: country_eligible = true
    Automation Rule: welcome_coupon_campaign
    Action: grant coupon
    Result Event: coupon_granted
    Consumers: Notifications, CRM, Analytics, Rewards

## Example

    Source Event: order_completed
    Condition: user completed one purchase each month for six months
    Automation Rule: monthly_purchase_streak_goal
    Action: grant points
    Result Event: reward_granted
    Consumers: Rewards, CRM, Analytics, Notifications

## Example

    Derived Signal: user_inactive_for_30_days
    Condition: user has at least one previous purchase
    Automation Rule: retention_offer_campaign
    Action: send offer
    Result Event: retention_offer_sent
    Consumers: CRM, Notifications, Analytics

Automation rules belong to campaign, rewards, CRM, or automation PRDs.

قواعد الأتمتة التفصيلية مكانها في ملفات الحملات أو المكافآت أو CRM أو الأتمتة.

This file defines the grammar, not every rule.

هذا الملف يحدد القواعد اللغوية للأحداث، وليس كل قواعد التنفيذ.

---

# 8. Event Type Classification / تصنيف أنواع الأحداث

Every event should be classified by type when relevant.

يجب تصنيف الحدث عند الحاجة.

| Event Type | Meaning | Example |
|---|---|---|
| `operational_event` | Core system lifecycle event | `order_paid` |
| `behavior_event` | Behavior worth tracking | `product_viewed` |
| `derived_signal` | Inferred from time or pattern | `cart_abandoned` |
| `automation_result_event` | Result of automation action | `coupon_granted` |
| `notification_event` | Notification lifecycle event | `notification_sent` |
| `reward_event` | Reward lifecycle event | `reward_granted` |
| `audit_event` | Traceability or compliance event | `permission_changed` |
| `security_event` | Risk or protection event | `suspicious_login_detected` |
| `system_event` | Technical or admin configuration event | `setting_updated` |
| `ai_insight_event` | AI-generated insight or recommendation | `ai_insight_generated` |

---

# 9. Event Naming Standard / معيار تسمية الأحداث

Use factual, past-tense, snake_case names.

استخدم أسماء واقعية بصيغة الماضي وبنمط snake_case.

Preferred pattern:

    entity_action_past

Examples:

- `account_created`
- `approval_approved`
- `shipment_delivered`
- `reward_granted`

Avoid command-style names.

تجنب أسماء الأوامر.

Bad:

- `create_account`
- `approve_user`
- `send_coupon`
- `give_reward`

Good:

- `account_created`
- `approval_approved`
- `coupon_granted`
- `reward_granted`

The event name must describe what happened, not what should happen next.

اسم الحدث يصف ما حدث، وليس ما يجب تنفيذه لاحقًا.

---

# 10. Event Anatomy / بنية الحدث

A mature event may later include these fields.

قد يحتوي الحدث الناضج لاحقًا على هذه الحقول.

Parent PRDs do not need full payload definitions.

ملفات الأب لا تحتاج تعريف payload كامل.

| Field | Meaning |
|---|---|
| `event_id` | Unique event identifier |
| `event_name` | Canonical event name |
| `event_family` | Event family |
| `event_type` | Operational, behavioral, derived, automation result, etc. |
| `occurred_at` | Time the event happened |
| `recorded_at` | Time the system recorded it |
| `source_module` | Module that emitted the event |
| `actor_type` | User, admin, seller, driver, system, AI, etc. |
| `actor_id` | Actor identifier |
| `subject_type` | Main affected entity type |
| `subject_id` | Main affected entity identifier |
| `related_entities` | Related entities |
| `state_before` | Previous state if relevant |
| `state_after` | New state if relevant |
| `trigger_type` | Event, schedule, threshold, manual action, pattern |
| `correlation_id` | Groups related events |
| `causation_id` | Previous event or command that caused this event |
| `context` | Country, channel, device, campaign, workflow, dashboard |
| `metadata` | Event-specific additional data |
| `visibility` | internal, admin, user, seller, support, system |
| `priority` | critical, high, medium, low |

---

# 11. Event Consumers / مستهلكو الأحداث

| Consumer | Use |
|---|---|
| `Notifications` | Alerts, reminders, messages |
| `CRM` | Follow-up, segmentation, retention, reactivation |
| `Analytics` | Funnels, metrics, behavior analysis |
| `Audit` | Traceability and compliance |
| `Automation` | Trigger rules and actions |
| `Rewards` | Points, coupons, goals, milestones |
| `Campaigns` | Marketing journeys and promotions |
| `Security` | Fraud, suspicious behavior, access protection |
| `Support` | Customer and operational history |
| `Dashboards` | Operational monitoring |
| `AI Manager` | Insights, recommendations, anomaly detection |
| `Search / Recommendation` | Personalization and ranking |

---

# 12. Domain Event Route Index / فهرس ربط الأقسام بعائلات الأحداث

This section is only a route map.

هذا القسم خريطة توجيه فقط.

It does not define all local events for each section.

لا يحدد كل أحداث كل قسم.

Each Parent PRD and Child PRD must define its local events based on its scenario.

كل ملف أب وملف ابن يحدد أحداثه المحلية حسب السيناريو.

| Domain / Module | Main Event Families To Check |
|---|---|
| `User Management` | `AccountEvents`, `AuthenticationEvents`, `ProfileEvents`, `IntentEvents`, `CapabilityEvents`, `VerificationEvents`, `ApprovalEvents`, `RestrictionEvents`, `PolicyAgreementEvents`, `RequestEvents`, `CountryContextEvents`, `NotificationEvents`, `SecurityEvents`, `CRMEngagementEvents`, `BehaviorAnalyticsEvents` |
| `Store Management` | `StoreEvents`, `VerificationEvents`, `ApprovalEvents`, `ProductEvents`, `OrderEvents`, `PayoutCommissionEvents`, `ReviewRatingEvents`, `RequestEvents` |
| `Products / Catalog` | `ProductEvents`, `CategoryEvents`, `InventoryEvents`, `ReviewRatingEvents`, `BehaviorAnalyticsEvents` |
| `Orders` | `CartCheckoutEvents`, `OrderEvents`, `PaymentEvents`, `InventoryEvents`, `ShippingEvents`, `ReturnRefundEvents`, `NotificationEvents` |
| `Financial` | `PaymentEvents`, `WalletEvents`, `PayoutCommissionEvents`, `ReturnRefundEvents`, `RewardEvents`, `SecurityEvents`, `SubscriptionEvents` |
| `Shipping / Operations` | `ShippingEvents`, `FulfillmentWarehouseEvents`, `DriverEvents`, `AddressEvents`, `OrderEvents`, `NotificationEvents`, `RewardEvents` |
| `Marketing / CRM / Rewards` | `CampaignEvents`, `RewardEvents`, `GoalChallengeEvents`, `CRMEngagementEvents`, `BehaviorAnalyticsEvents`, `OrderEvents`, `AccountEvents`, `NotificationEvents` |
| `Support` | `SupportEvents`, `NotificationEvents`, `CRMEngagementEvents`, `ReviewRatingEvents`, `SecurityEvents` |
| `System / Security` | `SecurityEvents`, `SystemEvents`, `NotificationEvents`, `FileMediaEvents`, `AIInsightEvents` |
| `Smart Data / Analytics` | `BehaviorAnalyticsEvents`, `AIInsightEvents`, all domain event families as consumed analytics sources |

---

# 13. PRD Event Extraction Gate / بوابة استخراج الأحداث من PRD

When writing or reviewing any PRD, extract events from:

عند كتابة أو مراجعة أي PRD، استخرج الأحداث من:

- lifecycle transitions
- state transitions
- decisions
- approvals
- rejections
- submissions
- activations
- suspensions
- completions
- failures
- expirations
- retries
- assignments
- ownership changes
- payments
- shipments
- rewards
- user behaviors worth tracking
- time-based inactivity
- threshold crossing
- automation outputs
- notification outputs
- security incidents
- audit-worthy actions

If a PRD contains a meaningful lifecycle change but no event is listed, the PRD may be incomplete.

إذا احتوى PRD على انتقال مهم دون حدث مقابل، فقد يكون التوثيق ناقصًا.

---

# 14. PRD Event Documentation Standard / معيار توثيق الأحداث داخل PRD

A PRD that introduces events should document:

أي PRD يتضمن أحداثًا يجب أن يوثق:

| Item | Meaning |
|---|---|
| `Event Family` | Which event family it belongs to |
| `Event Name` | Canonical event name |
| `Event Type` | Operational, behavior, derived, reward, notification, etc. |
| `Source Module` | Module that emits it |
| `Subject` | Main affected entity |
| `Trigger` | What causes it |
| `State Change` | Related state transition if any |
| `Conditions` | Conditions if derived or automation-related |
| `Consumers` | Notifications, CRM, Analytics, Audit, Automation, Rewards |
| `Visibility` | Internal, admin, user, seller, support |
| `Parent / Child Level` | Parent-level or child-level |
| `Open Decision` | Unresolved naming, payload, ownership, or consumer question |

Parent PRDs list event families and key events.

ملفات الأب تسجل عائلات الأحداث والأحداث المهمة.

Child PRDs list precise local events.

ملفات الابن تسجل الأحداث المحلية بدقة.

Workflow and state/event models define transitions and side effects.

ملفات workflow و state/event model تحدد الانتقالات والآثار الجانبية.

---

# 15. Event Quality Gate / بوابة جودة الحدث

Before accepting event documentation, verify:

قبل اعتماد توثيق أي حدث، تحقق من:

1. Does the event describe something that actually happened?
2. Is it named in past tense?
3. Is it tied to an entity, workflow, action, decision, state change, time condition, threshold, or behavior?
4. Is it not an automation command?
5. Is it not a vague marketing objective?
6. Does it belong to the correct event family?
7. Does it have a source module?
8. Does it have a subject entity?
9. Does it have likely consumers?
10. Does it align with state taxonomy when state change is involved?
11. If derived, does it have evaluation logic?
12. If reward-related, does it avoid duplicate rewards?
13. If notification-related, does it avoid duplicate messages?
14. Does it avoid duplicating another event with a different name?
15. Does the related PRD document it at the correct level?

---

# 16. Event Feedback Loop / حلقة تغذية الأحداث

The central taxonomy and PRDs must improve each other.

يجب أن يطوّر ملف الأحداث وملفات PRD بعضهما.

If a PRD reveals a meaningful local event:

إذا كشف PRD حدثًا محليًا مهمًا:

- document it inside the PRD
- classify its event family
- decide if it is reusable platform-wide
- add it here only if it becomes central

If this taxonomy suggests an event a PRD forgot:

إذا اقترح هذا الفهرس حدثًا قد يكون مفقودًا في PRD:

- review the PRD
- decide whether the event applies
- add it if it reflects real section logic
- do not force it if it does not apply

The PRD owns local truth.

ملف PRD يملك الحقيقة المحلية.

This taxonomy guides discovery and consistency.

هذا الملف يوجه الاكتشاف والاتساق.

---

# 17. Event Anti-Patterns / أخطاء شائعة

| Anti-Pattern | Bad | Better |
|---|---|---|
| Command as event | `send_coupon` | `coupon_granted` |
| Command as event | `approve_store` | `store_approved` |
| Goal as event | `increase_sales` | `seller_sales_goal_completed` |
| Vague objective | `retain_customer` | `retention_offer_sent`, `user_reactivated` |
| Metric as event | `new_users_count` | metric from `account_created` |
| Duplicate naming | `user_verified`, `identity_verified`, `verification_approved` | choose clear ownership |
| Overtracking | every small click | only meaningful behavior events |
| Unowned event | event without source module | assign source module |
| Unclear subject | event without subject entity | define subject |

---

# 18. Final Rule / القاعدة النهائية

Events are the platform memory of what happened.

الأحداث هي ذاكرة المنصة لما حدث.

States describe what is true now.

الحالات تصف ما هو صحيح الآن.

Metrics summarize what happened.

المؤشرات تلخص ما حدث.

Automation decides what to do next.

الأتمتة تقرر ماذا نفعل لاحقًا.

Rewards define what is granted.

المكافآت تحدد ما يتم منحه.

Campaigns define why and when.

الحملات تحدد لماذا ومتى.

Analytics learns from patterns.

التحليلات تتعلم من الأنماط.

Notifications communicate important changes.

الإشعارات توصل التغيرات المهمة.

Audit preserves accountability.

التدقيق يحفظ المسؤولية والأثر.

Every mature Pazarat PRD must understand its events, document them at the correct level, and connect them to states, workflows, UX, automation, analytics, notifications, CRM, rewards, and governance when relevant.

كل PRD ناضج في بازارات يجب أن يفهم أحداثه ويوثقها في المستوى الصحيح ويربطها بالحالات، سير العمل، الواجهة، الأتمتة، التحليلات، الإشعارات، CRM، المكافآت، والحوكمة عند الحاجة.