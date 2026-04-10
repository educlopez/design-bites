# proofeditor.ai — Design System

## 1. Visual Theme & Atmosphere

Proofeditor.ai presents a document-first design philosophy rooted in quiet legibility. The overall atmosphere is warm parchment — a deliberate departure from the clinical whites of most SaaS tools. By grounding the UI in an off-white cream (`#F5F3EC`) that echoes aged paper, the product feels like a natural extension of the writing and editing process rather than software imposing on it. Dark tones are almost-black with a warm undertone (`#26251E`), reinforcing this analog warmth rather than reaching for pure black. The result is a calm, focused environment where the document content — not the UI chrome — commands attention.

The interface signals credibility through restraint. Decorative color is used only where it carries semantic weight: green for collaborative presence and tracked insertions, red/yellow/green macOS-style window dots as a product metaphor, and a soft violet-blue for threaded comments. Everything else recedes.

---

## 2. Color Palette & Roles

**Surfaces**
- `#F5F3EC` — Page background (warm cream, primary canvas)
- `#F7F7F4` — Near-white surface for overlaid panels and button foregrounds
- `rgba(38, 37, 30, 0.04)` — Subtle tinted background on link hovers

**Text & Borders**
- `#26251E` — Primary text and borders (warm near-black)
- `rgba(38, 37, 30, 0.1)` — Hairline borders on interactive elements

**Brand / Semantic**
- `#26684` — Forest green; h3 accents, tracked-insert highlights, presence indicators
- `rgba(38, 104, 84, 0.18)` — Green wash for inserted text suggestions
- `rgba(190, 72, 72, 0.12)` / `rgba(130, 70, 70, 0.9)` — Muted red for deleted text suggestions
- `rgba(101, 117, 224, 0.88)` — Violet-blue for comment thread badges

**Status dots (macOS metaphor)**
- `#FF5F57` — Red (close)
- `#FEBC2E` — Yellow (minimize)
- `#28C840` — Green (expand)

---

## 3. Typography Rules

The sole typeface is **Switzer** (with Switzer Variable as the primary loading strategy), falling back to system sans-serif. Switzer is a geometric grotesque with humanist touches — professional without being sterile, and at home in both editorial and product contexts.

- **h1**: 58px / weight 400 — large and confident, normal weight keeps it literary not bold
- **h2**: 40px / weight 400 — section titles, maintains the unhurried rhythm
- **h3**: 24px / weight 500 — subheadings, slightly heavier to anchor content groups
- **body / p**: 18px / weight 400 — generous body size reflects writing-tool priorities
- **code / pre**: 12px monospace fallback stack — small, utilitarian

Letter spacing and line height are not aggressively manipulated. The type scale is evolutionary rather than dramatic — no extreme size jumps. Text transforms and feature settings are left at defaults, reinforcing the document-native aesthetic.

---

## 4. Component Stylings

**Buttons**: Pill-shaped (border-radius `9999px`). Background transparent by default with white text — they appear to float over darker surfaces. No heavy drop shadows.

**Suggestion spans**: Track changes are rendered with inline color washes — green for insertions, red-tinted for deletions — directly in the document flow, mimicking traditional redlining.

**Thread badges**: Small pill with `rgba(101, 117, 224, 0.88)` violet-blue — they stand apart from editorial colors to signal a different mode (conversation vs. document).

**Presence indicators**: `#61BA85` / `#82C29A` green dots — collaborative "who's here" signals use the same green family as tracked insertions, unifying the collaboration metaphor.

**Lock spans**: Semi-transparent white text on sage green — a locked/editing-in-progress state.

No card shadows or heavy surface borders detected. The editor chrome is deliberately lightweight.

---

## 5. Layout Principles

Proofeditor.ai uses a centered document layout with the editor occupying the focal column. Breakpoints at 600, 700, 768, 900, 1000, 1280, and 1300px suggest a carefully tiered responsive scale — not just mobile/desktop binary thinking.

Spacing is generous: body padding is removed to allow sections to self-manage their breathing room. The navigation is transparent (`rgba(0,0,0,0)`) overlaid on the canvas, keeping the document surface uninterrupted above the fold.

There is no sidebar-heavy layout detected — the design favors linear, top-to-bottom document reading. The UI wraps the document rather than competing with it.

---

## 6. Depth & Elevation

Shadows are absent from the extracted data — Proofeditor.ai achieves depth through color rather than shadow. The warm cream background and subtle tinted overlays (`rgba(38, 37, 30, 0.04)`) create soft layering without drop shadows. The editor showcase element uses a slightly different surface treatment from the surrounding page, suggesting tonal elevation rather than physical lift.

The macOS window-dot chrome adds a skeuomorphic layer of implied depth — the editor is presented as "a window into a real application."

---

## 7. Do's and Don'ts

**Do**
- Use `#F5F3EC` as the base canvas; never pure white
- Keep body text at 18px minimum to honor the writing-tool context
- Reserve green tones exclusively for collaborative and editorial-state signals
- Use violet-blue only for comment/thread UI — keep it distinct from content
- Pair Switzer at regular (400) weight for editorial headings; avoid heavy weights

**Don't**
- Add card shadows or heavy borders — they break the document-native feel
- Use pure black (`#000000`) — always use the warm near-black `#26251E`
- Mix the semantic suggestion colors (red/green) with decorative purposes
- Apply transforms or uppercase to text — the tone is literary, not promotional

---

## 8. Responsive Behavior

The breakpoint ladder (600 → 700 → 768 → 900 → 1000 → 1280 → 1300px) suggests fine-grained layout control. At smaller breakpoints the document likely goes full-width with minimal padding. The header remains transparent at all sizes, relying on the canvas color for visual grounding. No horizontal scroll detected — the layout is fluid within each tier.

The Next.js + Tailwind stack makes column-based responsive adjustments predictable. Component widths likely use `max-w-*` containers centered on the page.

---

## 9. Agent Prompt Guide

> "Design in the style of proofeditor.ai: warm cream background (`#F5F3EC`), near-black warm text (`#26251E`), single Switzer typeface at normal weight. Use forest green (`#26684`) only for collaborative state signals. No card shadows — achieve depth through tonal surface variation. Pill-shaped interactive elements. Editorial calm over SaaS urgency. The document is the hero."

---

*Generated by Sparkbites — extracted from live CSS analysis*
