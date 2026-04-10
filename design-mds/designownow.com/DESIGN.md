# Design OWO Now — Design System

## 1. Visual Theme & Atmosphere

Design OWO Now is unapologetically loud — a dark, near-black base canvas (#0f0f0f) punched through with neon candy: soft lavender, acid green, coral pink, and cyan. Built in Framer, the composition layers glassmorphic pill-shapes and translucent cards with subtle inset/ambient shadow systems that create a tactile sense of depth. The typographic choice is striking: Death Star for decorative/display moments and TT Firs Neue for navigation and body text — both unconventional, both signalling that this is a design statement, not a template.

---

## 2. Color Palette & Roles

| Role | Value | Notes |
|------|-------|-------|
| Page background | `#0f0f0f` | Deep near-black |
| Default links/text | `#aaaaaa` | Cool mid-grey on dark |
| Accent 1 — Lavender | `rgb(167,125,255)` | Pill/tag backgrounds |
| Accent 2 — Mint green | `rgb(163,254,196)` | Highlight surfaces |
| Accent 3 — Coral pink | `rgb(255,108,122)` | Alert/warm highlight |
| Accent 4 — Cyan | `rgb(73,236,255)` | Cool highlight |
| Frosted overlay | `rgba(173,179,189,0.4)` | Glassmorphic card surface |

The four accent colours appear in dedicated surface panels — they are never mixed on the same element. The frosted overlay creates the glassmorphic card language. Link/body text in mid-grey (#aaaaaa) ensures readability on the dark background without competing with the neon accents.

---

## 3. Typography Rules

**Display typeface:** Death Star — decorative, used for large graphical text moments.
**Navigation / body typeface:** TT Firs Neue Regular — clean geometric grotesque.

| Level | Size | Weight | Line Height | Tracking |
|-------|------|--------|-------------|----------|
| p (display, computed) | 7px scaled | 400 | 8.5px | +0.28px |
| a / nav | 14px | 400 | 31px | -0.42px |
| Base body | 12px | 400 | normal | normal |

- The `p` size of 7px is a scaled/computed value — actual display sizes will be significantly larger through transforms or viewport scaling.
- Navigation links have unusual 31px line-height at 14px — nearly 2.2 ratio, very airy nav.
- Death Star is a pure design statement typeface — not suitable for body or UI text.
- Positive tracking on Death Star (+0.28px) vs. negative on nav links (-0.42px) creates contrast between display and functional text.

---

## 4. Component Styling

- **Cards / pill shapes:** Framer-generated with layered inset and drop shadows for glassmorphic depth.
- **Glass surfaces:** `rgba(173,179,189,0.4)` frosted overlay — combined with backdrop-filter (implied by Framer).
- **Shadow system (glass card):** Multi-layer —
  - Inset dark: `rgba(0,0,0,0.25) 0px -0.94px 3.75px inset`
  - Inset light: `rgba(255,255,255,0.3) 0px 1.87px 1.87px inset`
  - Outer ambient: `rgba(0,0,0,0.5) 0px 0px 1.87px`
  - Outer drop: `rgba(0,0,0,0.29) 0px 3.48px 7.84px`
  - Large depth: `rgba(0,0,0,0.26) 0px 14.8px` — layered volumetric effect.
- No border-radius tokens visible — radii are set inline within Framer.

---

## 5. Layout Principles

- Section padding: 10px — minimal, nearly edge-to-edge content.
- Framer's absolute positioning system governs placement — not a CSS grid/flex layout.
- Content is layered and overlapping — not a grid-aligned document layout.
- Designed for viewport-scale, full-bleed visual impact.

---

## 6. Depth & Elevation

- Multi-layer shadow system creates volumetric glassmorphic cards (see Component Styling).
- Depth is the primary aesthetic — dark base + transparent overlays + multi-inset shadows.
- Frosted glass effect on cards requires `backdrop-filter: blur()` — not captured in CSS data but implied by design.
- The shadow stack is unusually complex for simple cards — this is considered, intentional elevation work.

---

## 7. Do's and Don'ts

**Do:**
- Keep the near-black (#0f0f0f) base unbroken — the dark field makes neon accents work.
- Use each neon accent on its own dedicated surface — one colour per panel.
- Apply the full multi-layer shadow system to glass cards for authentic depth.
- Use Death Star only for large graphical/display moments.

**Don't:**
- Mix multiple neon accents on a single component.
- Use the glassmorphic surface on light backgrounds — it only works on dark.
- Substitute Death Star for navigation or body text.
- Use solid white or pure black backgrounds in place of the near-black (#0f0f0f).

---

## 8. Responsive Behavior

- Framer absolute-position layout needs explicit breakpoint overrides.
- The 14px/31px nav link rhythm may need tighter line-height on mobile.
- Neon accent surfaces (pill cards) should maintain full-bleed character at mobile — avoid shrinking to unreadable sizes.

---

## 9. Agent Prompt Guide

> Build a dark creative portfolio using Design OWO Now's aesthetic. Background #0f0f0f, body links #aaaaaa. Four neon accent surfaces: lavender rgb(167,125,255), mint rgb(163,254,196), coral rgb(255,108,122), cyan rgb(73,236,255) — one per panel, never mixed. Glassmorphic cards with rgba(173,179,189,0.4) surface and multi-layer inset+drop shadow. Death Star typeface for large display moments. TT Firs Neue for nav at 14px with -0.42px tracking. Framer-style absolute positioning, full-viewport-scale sections.

---

*Generated by Sparkbites — extracted from live CSS analysis*
