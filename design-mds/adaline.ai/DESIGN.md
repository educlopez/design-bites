# adaline.ai — Design System

## 1. Visual Theme & Atmosphere

Adaline.ai is built on restraint and organic warmth. The background is not white — it is a barely-there celadon: `rgb(251, 253, 246)`, a green-tinged off-white that reads as natural and calm rather than clinical. Text is near-black with a green undertone (`rgb(10, 29, 8)`), reinforcing the sense that the entire palette has been pulled from a single muted green source.

The aesthetic communicates trust and quiet intelligence — fitting for an AI product that wants to feel approachable rather than sci-fi. There are no bright accents, no neon blues, no gradient hero sections. What remains is a design that lets the content breathe. The absence of decorative shadows, radius values, and interactive states suggests a site in early-stage clarity: every pixel earns its place.

## 2. Color Palette & Roles

| Role | Value | Usage |
|------|-------|-------|
| Background | `rgb(251, 253, 246)` | Full page background — warm off-white with green cast |
| Primary Text | `rgb(10, 29, 8)` | Headings, body, borders — near-black, green-tinted |
| Border / Rule | `rgb(10, 29, 8)` | Same as text — borders share the ink color |
| Transparent | `rgba(0, 0, 0, 0)` | Element backgrounds (h2, transparent containers) |

**What's absent:** There is no accent color. No blue CTA, no purple gradient, no orange highlight. The palette is a two-value system — one warm background, one dark ink. This is unusual for an AI product and signals a deliberate departure from the tech-blue convention. The borders using the same value as text (rather than a lighter gray) creates a woodblock-print quality: everything is one ink on one paper.

## 3. Typography Rules

Adaline uses the system font stack exclusively — no custom webfonts are loaded:

- **Body:** `ui-sans-serif, system-ui, sans-serif` — 18px / weight 400 / 26px line-height
- **Headings (h2):** `system-ui, "Segoe UI", Roboto, Helvetica, Arial` — 14px / weight 400 / 28px line-height

**Key insight:** The h2 is *smaller* than the body (14px vs 18px), yet has a proportionally generous line-height (28px vs 26px). This is a design that uses spacing rather than size to establish hierarchy. The consistent weight 400 across all elements means nothing is bold — emphasis must come from layout, color, or positioning.

Feature settings `"calt", "kern"` are enabled globally, indicating attention to typographic detail despite the system-font choice. The font selection itself is a philosophical statement: no logo font, no custom identity type. The product speaks through content, not branding.

## 4. Component Styling

- **No border radius detected** — components use sharp corners, which pairs with the ink-on-paper aesthetic.
- **No shadows detected** — the design is entirely flat. Elevation is not a concept here.
- **No interactive states captured** — buttons and links may use subtle CSS transitions not detectable at extraction time, or the site deliberately minimizes interactive affordances.
- **Borders** share ink color (`rgb(10, 29, 8)`) rather than a softened gray — a bold choice that makes even structural lines feel intentional.
- **Text color on h2 matches body** — no typographic color differentiation; hierarchy is entirely structural.

## 5. Layout Principles

Built on **Next.js** with a single captured breakpoint at **900px** — a non-standard value suggesting a custom-designed layout rather than a framework default:

- The `900px` breakpoint sits between a typical tablet (768px) and desktop (1024px), implying a content-width-driven layout that collapses at a natural reading width.
- Zero padding/margin on body — spacing is component-managed.
- The sparse breakpoint set suggests a simple layout: perhaps a single-column article structure or a two-column split that collapses at 900px.
- No complex grid or multi-column detected — this is likely prose-forward, content-first layout.

## 6. Depth & Elevation

No depth. No shadows, no overlays, no blur effects. The design exists entirely on one plane — flat in the same tradition as editorial print design. This is not an oversight; it's coherent with the organic, ink-on-paper color system.

Any visual separation between sections likely comes from whitespace alone, which is the most minimal and confident way to build structure.

## 7. Do's and Don'ts

**Do:**
- Use `rgb(251, 253, 246)` as the page background — never pure white; the warmth is essential.
- Use `rgb(10, 29, 8)` for all text and borders — keep the two-value palette intact.
- Enable `font-feature-settings: "calt", "kern"` globally for refined system-font rendering.
- Let whitespace do the work of hierarchy rather than size or weight contrasts.
- Use sharp corners — no border radius on components.

**Don't:**
- Introduce accent colors, especially tech-blues or purples — they break the editorial calm.
- Use bold or heavy font weights to establish hierarchy.
- Add shadows or elevation; flatness is part of the design's identity.
- Use custom webfonts unless they match the quiet neutrality of the system stack.
- Add background color differentiation between sections — rely on spacing instead.

## 8. Responsive Behavior

A single breakpoint at **900px** governs the responsive behavior. This minimalist approach suggests:

- Mobile: single-column, full-width prose layout.
- Desktop (≥900px): the layout expands — possibly a centered content column with generous side margins, or a two-column arrangement.
- Font sizes remain fixed across breakpoints (no fluid type detected), keeping the reading experience consistent from tablet to desktop.

## 9. Agent Prompt Guide

Use this when generating UI in the style of adaline.ai:

> Design a flat, editorial AI product interface. Background: `rgb(251, 253, 246)` — a warm, celadon-tinted off-white. All text and borders in `rgb(10, 29, 8)` — near-black with green undertone. Use the system font stack; enable `font-feature-settings: "calt", "kern"`. Body at 18px, headings smaller at 14px with generous line-height. No border radius, no shadows, no accent colors. One breakpoint at 900px. The philosophy: two colors, one weight, infinite whitespace. The content earns attention; the design steps aside.

---

*Generated by Sparkbites — extracted from live CSS analysis*
