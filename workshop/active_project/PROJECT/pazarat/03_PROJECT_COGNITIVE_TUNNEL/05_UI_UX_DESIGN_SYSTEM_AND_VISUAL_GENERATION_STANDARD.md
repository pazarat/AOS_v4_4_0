# UI/UX DESIGN SYSTEM AND VISUAL GENERATION STANDARD

# Purpose / الهدف

This file defines the central UI/UX design system and visual generation standard for Pazarat.

هذا الملف يعرّف معيار التصميم المركزي ومعيار توليد صور UI/UX داخل مشروع بازارات.

Its purpose is to ensure that every generated screen, visual reference, Figma direction, and UI/UX concept follows one consistent product identity, component logic, layout system, interaction model, and documentation hierarchy.

هدفه ضمان أن كل صورة واجهة أو مرجع بصري أو اتجاه تصميم أو شاشة UI/UX يتم توليدها ضمن هوية واحدة ومنطق واحد ومكونات مشتركة ونظام تخطيط موحد.

This file is not a final Figma design file.

هذا الملف ليس ملف Figma نهائي.

This file is not a frontend implementation file.

هذا الملف ليس ملف تنفيذ Frontend.

This file is the design intelligence standard that allows PRDs, Screen PRDs, and future AI-generated images to remain visually and logically consistent across the whole platform.

هذا الملف هو معيار ذكاء التصميم الذي يجعل ملفات PRD وصور الواجهات الناتجة من الذكاء الاصطناعي متسقة بصريًا ومنطقيًا على مستوى المشروع كله.

---

# 1. Core Design Principle / المبدأ الأساسي للتصميم

Pazarat UI/UX must be designed as one connected product system, not as isolated images.

يجب تصميم واجهات بازارات كنظام منتج مترابط، وليس كصور منفصلة.

Every visual output must inherit from:

1. Project identity
2. Target dashboard or app context
3. Parent PRD
4. Child PRD
5. Screen PRD when available
6. State and event logic
7. Reusable component library
8. Existing visual references
9. Current user request

The model must not generate a random modern dashboard from general memory.

لا يجوز للنموذج أن يولد لوحة حديثة عشوائية من ذاكرته العامة.

It must generate a screen that belongs to Pazarat.

يجب أن يولد شاشة تنتمي إلى بازارات.

---

# 2. Visual Reference Role / دور الصور المرجعية

Generated UI/UX images are visual references.

صور UI/UX الناتجة هي مراجع بصرية.

They are used to:

- clarify layout direction
- communicate visual hierarchy
- guide Figma design
- align product, design, and engineering understanding
- test whether documentation produces coherent screens
- support frontend implementation planning later

They are not final production UI unless explicitly converted into a design system and implemented.

ليست هذه الصور واجهات نهائية للإنتاج إلا إذا تم تحويلها لاحقًا إلى Design System وتنفيذ Frontend.

---

# 3. Reference Image Interpretation / تفسير الصور المرجعية

The provided visual references show the desired direction:

تعكس الصور المرجعية الحالية الاتجاه المطلوب:

- modern SaaS dashboard style
- clean white or dark-blue admin shell
- card-based structure
- soft borders
- subtle shadows
- generous spacing
- purple / blue primary identity
- green success indicators
- amber warning indicators
- red danger indicators
- icon-led sections
- dashboard sidebar navigation
- topbar with search, notifications, messages, cart or admin actions
- profile headers
- metric cards
- status badges
- timeline sections
- quick actions
- cross-system summary cards
- operational admin profile views
- customer-facing profile and edit-profile screens

These images are references for visual intelligence, not exact templates to copy blindly.

هذه الصور مراجع لفهم الاتجاه البصري، وليست قوالب يجب نسخها حرفيًا.

The model should extract the design logic from them:

- layout rhythm
- component consistency
- visual hierarchy
- operational clarity
- soft modern interface
- reusable cards and badges
- readable dense dashboard content

The model should not reproduce inconsistent versions of the same component across screens.

لا يجب أن ينتج النموذج مكونات مختلفة لنفس الوظيفة في كل شاشة.

---

# 4. Design Entry Sequence / تسلسل الدخول قبل التصميم

Before generating any UI/UX image or visual reference for Pazarat, the model must inspect or infer from available repository context:

```txt
1. 00_PRD_COGNITION_AND_TRACEABILITY_STANDARD.md
2. 01_PAZARAT_PRD_PLATFORM_IDENTITY_AND_OBJECTIVES.md
3. 02_PLATFORM_STATE_TAXONOMY.md
4. 03_PLATFORM_EVENT_TAXONOMY.md
5. 04_PROJECT_STRUCTURE_TREE_INDEX.md
6. 05_UI_UX_DESIGN_SYSTEM_AND_VISUAL_GENERATION_STANDARD.md
7. Relevant Parent PRD
8. Relevant Child PRD
9. Relevant Workflow PRD if available
10. Relevant State/Event Model if available
11. Relevant Screen PRD if available
12. Existing visual references if available
13. Current conversation request
```

A screen must not be generated from the screen name alone.

لا يتم توليد الشاشة من اسمها فقط.

---

# 5. Product Visual Identity / الهوية البصرية العامة

Pazarat visual identity should feel:

- premium
- modern
- operational
- trustworthy
- scalable
- clean
- data-aware
- marketplace-oriented
- suitable for multi-role dashboards
- suitable for both customer and admin experiences

The visual system should support:

- customer dashboards
- admin dashboards
- seller dashboards
- driver dashboards
- support dashboards
- operational tools
- financial tools
- marketing tools
- analytics tools

The design must not look like a generic template marketplace.

يجب ألا تبدو الواجهة كقالب عام بلا هوية.

It must feel like a serious multi-vendor commerce platform.

يجب أن تبدو كمنصة تجارة إلكترونية متعددة البائعين ومتقدمة.

---

# 6. Visual Tone / النبرة البصرية

Preferred visual tone:

| Property | Direction |
|---|---|
| Layout | spacious, structured, dashboard-native |
| Background | light neutral background, optional dark admin sidebar |
| Cards | white surfaces, soft borders, subtle shadows |
| Corners | rounded, modern, consistent |
| Typography | clean SaaS typography, strong hierarchy |
| Icons | thin-line modern icons, consistent style |
| Colors | purple/blue primary, green success, amber warning, red danger |
| Density | information-rich but not crowded |
| Motion | implied modern smoothness, not decorative chaos |
| Data Display | clear, segmented, scannable |
| Status Display | badge-driven and state-aware |
| UX Feeling | confident, calm, operational, premium |

---

# 7. Design Tokens / رموز التصميم

The final tokens may be adjusted later, but generated references should follow this general direction.

يمكن تعديل القيم لاحقًا، لكن يجب أن تتبع الصور الناتجة هذا الاتجاه.

## Color Intent

| Token | Purpose |
|---|---|
| `primary` | Main action, active navigation, key brand moments |
| `primary_soft` | Active menu background, light highlights |
| `success` | Verified, active, completed, approved |
| `warning` | Pending, needs update, partial risk |
| `danger` | Rejected, failed, blocked, suspended |
| `info` | Neutral guidance, notes, system information |
| `surface` | Cards and panels |
| `background` | Page background |
| `border` | Dividers and card borders |
| `text_primary` | Main text |
| `text_secondary` | Descriptions and metadata |
| `muted` | Low-emphasis text and passive UI |

## Shape And Spacing

| Token | Direction |
|---|---|
| `radius_card` | large rounded cards |
| `radius_button` | medium rounded buttons |
| `radius_badge` | pill or soft rounded |
| `section_gap` | generous vertical spacing |
| `card_padding` | comfortable dashboard spacing |
| `grid_gap` | consistent grid spacing |
| `sidebar_width` | stable navigation width |
| `topbar_height` | consistent page topbar |

---

# 8. Layout System / نظام التخطيط

Pazarat screens should follow predictable layout patterns.

يجب أن تتبع شاشات بازارات أنماط تخطيط واضحة.

## Main Dashboard Layout

Expected structure:

```txt
Sidebar
→ Topbar
→ Breadcrumb / Page Title
→ Primary Content Area
→ Cards / Sections / Tables / Panels
→ Footer Actions when needed
```

## Admin Layout

Admin screens may use:

- dark sidebar
- wide content area
- dense operational cards
- profile context headers
- admin action bars
- internal notes
- impersonation actions
- audit and event timelines
- cross-system summaries

## Customer / Seller Layout

Customer or seller screens may use:

- light sidebar
- softer profile cards
- membership and benefits sections
- wallet / orders / rewards summaries
- quick actions
- support blocks
- friendly account context

## Form Layout

Large forms should use:

- section numbering when multi-step
- grouped cards
- clear field labels
- helper text
- inline validation
- action footer
- locked/read-only state display when needed

## Profile Layout

Profile screens should use:

- header identity card
- role/status badges
- key identity fields
- linked operational summaries
- cross-system cards
- timeline / milestones
- insights or alerts
- quick actions

---

# 9. Component Registry / سجل المكونات المشتركة

The following component patterns should be reused across screens.

يجب إعادة استخدام هذه الأنماط بدل اختراع شكل جديد في كل مرة.

| Component | Purpose |
|---|---|
| `AppShell` | Sidebar + topbar + content layout |
| `SidebarNav` | Primary navigation |
| `Topbar` | Search, notifications, profile, quick icons |
| `Breadcrumbs` | Hierarchical location |
| `PageHeader` | Title, subtitle, primary actions |
| `SectionCard` | Main content section |
| `MetricCard` | KPI or summary value |
| `StatusBadge` | State display |
| `RoleBadge` | User role or account type |
| `CapabilityBadge` | Active capability display |
| `VerificationBadge` | Verification state |
| `RiskBadge` | Risk level display |
| `ActionButton` | Primary/secondary/ghost action |
| `ActionMenu` | More actions |
| `DataTable` | Lists and records |
| `FilterBar` | Quick filtering |
| `FilterDrawer` | Advanced filtering |
| `SavedViewsTabs` | Saved operational views |
| `ProfileHeaderCard` | User/store/account identity header |
| `LinkedEntityCard` | Related store, wallet, order, shipment |
| `Timeline` | Events and lifecycle milestones |
| `ActivityFeed` | Recent activity |
| `RequirementBuilder` | Verification or dynamic requirements |
| `ApprovalQueue` | Review and decision workflow |
| `AuditTrail` | Admin/security traceability |
| `InsightCard` | AI or smart insight |
| `QuickActionsGrid` | Common action shortcuts |
| `EmptyState` | No data state |
| `LoadingSkeleton` | Loading state |
| `ErrorPanel` | Error or failure state |
| `InfoNotice` | Informational message |
| `WarningNotice` | Warning message |
| `FooterActionBar` | Save/cancel or batch actions |

The model must not invent a new component shape if one of these components already fits.

لا يجوز اختراع مكوّن جديد إذا كان هناك مكوّن مناسب في هذا السجل.

---

# 10. Screen Pattern Library / مكتبة أنماط الشاشات

## Profile Screen Pattern

Use for:

- user profile
- seller profile
- store profile
- driver profile
- staff profile

Expected zones:

```txt
Header identity card
→ Key status badges
→ Contact / identity / role summary
→ Cross-system summary sections
→ Activity or lifecycle timeline
→ Security / verification / risk sections
→ Quick actions
→ Smart insights when available
```

## Edit Form Pattern

Use for:

- edit profile
- account preferences
- verification template editing
- settings forms

Expected zones:

```txt
Page header
→ Sectioned form cards
→ Step numbers when useful
→ Helper text
→ Inline validation
→ Locked fields when verification-sensitive
→ Info/warning notices
→ Sticky or bottom action bar
```

## Review Queue Pattern

Use for:

- verification center
- approval center
- product review
- store approval
- payout review

Expected zones:

```txt
Queue metrics
→ Filters / saved views
→ Case table or card list
→ Status badges
→ Priority / SLA indicators
→ Assigned reviewer
→ Action panel
→ Timeline / audit trail
```

## Detail Management Pattern

Use for:

- order detail
- shipment detail
- wallet transaction detail
- support ticket detail

Expected zones:

```txt
Header summary
→ Current status
→ Linked entities
→ Timeline
→ Operational sections
→ Actions
→ Audit / notes
```

## Analytics Pattern

Use for:

- user analytics
- sales analytics
- shipping analytics
- marketing analytics

Expected zones:

```txt
KPI cards
→ trend charts
→ segmentation filters
→ funnel or lifecycle view
→ table details
→ AI insights
```

---

# 11. State Display Standard / معيار عرض الحالات

States must be visible and understandable.

يجب أن تكون الحالات ظاهرة ومفهومة.

State displays may use:

- badges
- labels
- icons
- color-coded chips
- progress steps
- timeline milestones
- required action panels
- disabled action reasons

State display must follow:

```txt
02_MY_PROJECT/pazarat/02_PLATFORM_STATE_TAXONOMY.md
```

Examples:

| State Meaning | UI Pattern |
|---|---|
| `active` | green badge |
| `verified` | green badge with check icon |
| `pending_review` | amber badge |
| `needs_update` | amber warning panel |
| `rejected` | red badge or error panel |
| `suspended` | red/danger badge |
| `locked` | lock icon + muted field |
| `completed` | success icon |
| `expired` | muted warning badge |

Never show a state without enough context.

لا تعرض حالة عامة دون سياق.

Bad:

```txt
Pending
```

Better:

```txt
Verification: Pending Review
Approval: Waiting Review
Payment: Pending Capture
```

---

# 12. Event And Timeline Display Standard / معيار عرض الأحداث والجداول الزمنية

Events should appear visually when they help the user or operator understand what happened.

تعرض الأحداث بصريًا عندما تساعد المستخدم أو المشغل على فهم ما حدث.

Event display must follow:

```txt
02_MY_PROJECT/pazarat/03_PLATFORM_EVENT_TAXONOMY.md
```

Possible UI outputs:

- lifecycle timeline
- recent activity
- audit trail
- event feed
- milestone row
- smart insight card
- notification history
- operational status history

Not every event should be visible.

ليس كل حدث يجب أن يظهر في الواجهة.

Classify event visibility:

- internal only
- admin visible
- user visible
- seller visible
- support visible
- system only

---

# 13. Actions And Permissions Display / عرض الإجراءات والصلاحيات

Every actionable screen must clarify:

- primary actions
- secondary actions
- destructive actions
- disabled actions
- permission-dependent actions
- role-specific actions
- required action reasons

Examples:

```txt
Save Changes
Manage 2FA
Open Store Profile
Add Internal Note
Impersonate User
Approve
Reject
Request Update
Suspend Account
Reactivate
```

If an action is disabled, the UI should explain why when relevant.

إذا كان الإجراء معطلًا يجب توضيح السبب عند الحاجة.

---

# 14. Empty, Loading, Error States / حالات الفراغ والتحميل والخطأ

Screen PRDs and generated visuals should consider:

## Empty State

When no data exists.

Example:

```txt
No verification templates created yet.
Create your first template to define required documents by account type.
```

## Loading State

When data is being fetched or processed.

Use skeleton cards or table rows.

## Error State

When data cannot load or action fails.

Show:

- concise error
- reason when available
- recovery action
- support link if needed

## Permission State

When user cannot access or perform action.

Show:

- locked section
- permission message
- request access or contact admin path when appropriate

---

# 15. Data Density And Hierarchy / كثافة البيانات والهرمية

Pazarat dashboards may contain dense information.

يجب أن تكون الواجهات قادرة على عرض معلومات كثيرة دون فوضى.

Rules:

- group related data into cards
- avoid one huge unstructured page
- use visual hierarchy
- use section titles
- use dividers lightly
- use metric cards for summaries
- use tables for records
- use timeline for history
- use badges for status
- use linked cards for cross-system relationships
- avoid burying actions inside long text

Dense does not mean crowded.

الكثافة لا تعني الازدحام.

---

# 16. Visual Generation Prompt Structure / بنية طلب توليد الصورة

When generating a UI/UX image, the prompt should be structured.

عند توليد صورة واجهة يجب أن يكون الطلب منظمًا.

A strong visual generation prompt should include:

```txt
Product: Pazarat
Target Surface: Admin Dashboard / User Dashboard / Seller Dashboard / etc.
Screen Name:
Parent PRD:
Child PRD:
User Role:
Screen Purpose:
Layout Pattern:
Main Sections:
Data Groups:
States To Show:
Events / Timeline To Show:
Actions:
Permissions:
Reusable Components:
Visual Tone:
Reference Images:
Do Not Include:
```

The model should not use vague prompts such as:

```txt
Create a modern dashboard.
```

It should use project-aware prompts.

يجب أن يكون الطلب مرتبطًا بالمشروع والمنطق والملفات.

---

# 17. Visual Consistency Gate / بوابة اتساق التصميم

Before accepting any generated UI/UX image, verify:

1. Does it belong visually to Pazarat?
2. Does it use the same product identity?
3. Does it follow the right dashboard/app context?
4. Does it inherit from the correct Parent PRD?
5. Does it reflect the correct Child PRD or Screen PRD?
6. Does it use reusable components?
7. Does it avoid inventing a new style for existing patterns?
8. Does it show correct states?
9. Does it show correct actions?
10. Does it respect permissions?
11. Does it support operational clarity?
12. Does it support later Figma implementation?
13. Does it avoid decorative UI with no product logic?
14. Does it avoid overcrowding?
15. Does it avoid generic marketplace template style?

A beautiful image that violates the PRD is not acceptable.

الصورة الجميلة التي تخالف التوثيق غير مقبولة.

---

# 18. Figma Handoff Standard / معيار التسليم إلى Figma

Generated images should be useful for Figma designers.

يجب أن تكون الصور مفيدة لمصمم Figma.

A good visual reference should clarify:

- page structure
- layout zones
- component choices
- spacing rhythm
- hierarchy
- states
- actions
- data groups
- cross-system blocks
- responsive implications if relevant

A visual reference should not require the designer to guess the product logic again.

لا يجب أن يضطر المصمم إلى إعادة تخمين منطق المنتج من الصورة.

---

# 19. Design-To-Code Awareness / الوعي بالتحويل من التصميم إلى الكود

The design standard should support future frontend implementation.

يجب أن يدعم معيار التصميم تنفيذ Frontend لاحقًا.

Generated UI should encourage:

- reusable components
- consistent props
- predictable layout
- consistent state badges
- consistent table behavior
- reusable forms
- reusable filters
- reusable cards
- consistent empty/loading/error states

The image is not code, but it should not fight code.

الصورة ليست كود، لكنها يجب ألا تعارض قابلية التنفيذ.

---

# 20. When To Generate Image From Which Artifact / متى نولد الصورة ومن أي ملف

## From Parent PRD

Only generate broad conceptual or overview images.

يستخدم ملف الأب لتوليد صور عامة أو مفاهيمية.

## From Child PRD

Generate section-level UI direction.

يستخدم ملف الابن لتوليد اتجاه واجهة لقسم محدد.

## From Screen PRD

Generate precise screen UI/UX reference.

يستخدم Screen PRD لتوليد صورة شاشة دقيقة.

## From Workflow PRD

Generate flow visualization or workflow-specific operational screen.

يستخدم Workflow PRD لتوليد شاشة أو تصور لتدفق عملية.

## From State/Event Model

Generate timeline, lifecycle, status map, or state-aware UI.

يستخدم نموذج الحالات والأحداث لتوليد واجهات تعرض الحالة أو الخط الزمني.

---

# 21. Do Not Rules / قواعد المنع

Do not:

- generate a screen from name only
- ignore parent PRD
- ignore state/event logic
- invent new components unnecessarily
- create unrelated visual styles
- mix customer dashboard style with admin dashboard style without reason
- show actions not allowed by permissions
- show statuses not defined by PRD or taxonomy
- hide important operational data
- overuse decorative gradients
- overuse random colors
- generate visually impressive but product-incorrect screens
- create a Figma reference that cannot be decomposed into components

---

# 22. Final Rule / القاعدة النهائية

Pazarat UI/UX generation must be system-based.

توليد واجهات بازارات يجب أن يكون مبنيًا على نظام.

The visual image is a product artifact.

الصورة البصرية هي أثر من آثار المنتج.

It must inherit from documentation, respect reusable components, show correct states, support clear actions, and remain consistent with the platform identity.

يجب أن ترث من التوثيق، وتحترم المكونات المشتركة، وتعرض الحالات الصحيحة، وتدعم الإجراءات بوضوح، وتبقى متسقة مع هوية المنصة.

The goal is not one beautiful image.

الهدف ليس صورة جميلة واحدة.

The goal is a coherent visual language for the entire platform.

الهدف هو لغة بصرية موحدة ومترابطة لكل المنصة.