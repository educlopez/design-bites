# DESIGN.md — cossistant.com

## 1. Visual Theme & Atmosphere

Cossistant presents as a developer-first documentation and tooling product built on restraint. The visual language is clinical and precise: a near-white canvas, near-black typography, and a single vibrant emerald accent that punctuates otherwise monochromatic space. There is an intentional absence of decoration — no gradients, no photography, no illustrative noise. The site communicates competence through sparseness, trusting whitespace to convey quality. The result feels like a well-maintained open-source project that has grown up: opinionated, structured, and quietly proud of its clarity.

---

## 2. Color Palette & Roles

### Background
- **Near-White Canvas** (`lab(98.84 0 0)` ≈ `#fafafa`): The default page surface. Not pure white — the almost imperceptible warmth prevents harshness under ambient light.

### Text
- **Near-Black** (`lab(2.75 0 0)` ≈ `#080808`): Body and heading text. Deep enough to read clearly, stops just short of pure black.
- **Muted Dark** (`oklab(0.205 0 0 / 0.7)`): Secondary text at 70% opacity — used for supporting headings that shouldn't compete with primary copy.
- **Code Gray** (`lab(7.78 0 0)` ≈ `#121212`): Code block text. Marginally lighter than pure black for optical balance inside code surfaces.

### Accent
- **Emerald** (`#0ebe78`): The sole chromatic accent. Used sparingly on a single highlighted UI element. Its saturation makes it unmistakeable against the neutral ground.

### Borders
- **Light Gray** (`lab(90.95 0 0)` ≈ `#e6e6e6`): Consistent border tone across buttons, dividers, and structural elements. Low-contrast, structural rather than decorative.

---

## 3. Typography Rules

Two families divide all content:

**F37Stout** handles headings exclusively. It is a display serif with character — used at 48px/60px (H1) and 34px/55.25px (H2) at weight 400. The relatively light weight at large sizes gives it editorial refinement rather than brute-force impact. It is never used for body or UI copy.

**Geist** (sans-serif) carries all interface text. Body and links sit at 16px/24px weight 400. Subheadings use 16px weight 600. Buttons use 14px/20px weight 400. The type scale is compact — only two display sizes, one body size, and one UI size.

**Geist Mono** handles all code: labels at 12px/16px weight 500, body code at 14px/14px, and inline at 16px/24px. The monospace family is part of the brand — Cossistant builds developer tooling, so code typography is treated with the same care as prose.

No text transforms. No tracked letter spacing. Type is left to breathe naturally.

---

## 4. Component Styling

- **Buttons**: Background matches the page surface (`#fafafa`), text at medium gray. Border radius choices split into: nearly-square (`2px`), slightly rounded (`6px`), and pill (`9999px`). The default button does not demand attention — it fits into the content stream.
- **Code blocks**: Rendered with Geist Mono, inherit the near-black surface treatment. Background is transparent, relying on page whitespace for separation.
- **Navigation**: Transparent background on header — no solid bar, content bleeds through. Clean separation through whitespace rather than surface contrast.
- **Custom Properties**: The `--co-theme-radius` variable and `--background` scale suggest a theming system with multiple tonal steps (50–600), indicating dark mode readiness.

---

## 5. Layout Principles

- Content width is controlled through breakpoints at 640, 768, 1024, 1280, 1536 — a standard Tailwind responsive ladder.
- Spacing is restrained: body padding is 0, margin is 0. Layout relies on grid/flex gap rather than padding hacks.
- The single surface element (emerald card) suggests a feature-highlight layout: one primary call-to-action zone set apart from documentation flow.
- No visible horizontal scrolling constructs. The layout appears single-column with sidebar (the `--fd-sidebar-drawer-offset` custom property signals a collapsible doc sidebar).

---

## 6. Depth & Elevation

Elevation is deliberately absent. The shadows array returns only transparent `rgba(0,0,0,0)` values — no drop shadows, no blur layers, no elevation hierarchy. Depth is instead communicated through:
- Typography weight contrast (F37Stout display vs. Geist body)
- The singular emerald surface breaking the monochrome plane
- Whitespace as breathing room rather than visual layering

There is no card hover lift, no modal overlay shadow. The interface is intentionally flat.

---

## 7. Do's and Don'ts

**Do:**
- Use F37Stout exclusively for display headings (H1, H2). Never for body or UI copy.
- Keep the emerald accent singular — one call-to-action surface per viewport, not a recurring color.
- Rely on whitespace over borders for separation where possible.
- Use Geist Mono for all code samples, even inline ones.
- Honor the near-white background — do not swap for pure white.

**Don't:**
- Add shadows or elevation effects. The design is intentionally flat.
- Introduce additional brand colors. The system is built on one accent.
- Use F37Stout below 28px — it is a display typeface, not a UI typeface.
- Add decorative illustrations, gradients, or photography to content zones.
- Overload the navigation — it should remain transparent and minimal.

---

## 8. Responsive Behavior

The breakpoint system mirrors Tailwind's defaults: 640, 768, 1024, 1280, 1536px. The doc sidebar (signaled by `--fd-sidebar-drawer-offset`) converts to a drawer on mobile. Typography scales down modestly — F37Stout headings drop from 48px to smaller display sizes. The compact type scale (only two sizes to manage) makes responsive adjustments straightforward. Layouts are expected to stack to single-column below 768px.

---

## 9. Agent Prompt Guide

> Build a documentation-style page that matches cossistant.com's design language: near-white background (`#fafafa`), near-black text (`#080808`), F37Stout display serif for H1/H2, Geist sans for body and UI, Geist Mono for all code. One emerald accent (`#0ebe78`) for a single highlight surface. Border radius 6px for most UI, pill radius for toggle-style elements. No shadows. No gradients. Flat, clinical, developer-focused.

---

*Generated by Sparkbites — extracted from live CSS analysis*
