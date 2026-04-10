# amelieschlueter.com — Design Language

## 1. Visual Theme & Atmosphere

Amelie Schlueter's site inverts the expected designer portfolio. Rather than the clean white editorial look common in the space, it commits fully to a dark interface — near-black backgrounds, cool-grey text, and a single electric blue that cuts through the darkness with precision. The token system is shadcn/ui-based (Tailwind CSS), meaning the design language is systematic and transferable. The atmosphere is focused and technical: this is a developer-designer hybrid portfolio that values clarity over decoration, where the dark mode is the default, not an option.

## 2. Color Palette & Roles

The site uses HSL-defined CSS custom properties following shadcn/ui conventions, resolved to:

**Backgrounds (dark layer stack)**
- `hsl(0 0% 3.9%)` → `rgb(10, 10, 13)` — Body background; rich near-black with a barely-perceptible blue-grey cast.
- `hsl(0 0% 100%)` → `--card`, `--popover` — Defined as white in tokens (shadcn convention), though not visually rendered in dark mode.

**Text & foreground**
- `rgb(230, 230, 230)` — Primary text; light grey on dark background, never pure white — prevents harsh glare.
- `hsl(240 3.8% 46.1%)` → `--muted-foreground` — Secondary/muted text; medium warm-grey for captions and metadata.
- `hsl(0 0% 98%)` → `--primary-foreground` — Text on primary-coloured backgrounds.

**Accent & interactive**
- `rgb(59, 130, 246)` → Tailwind `blue-500` — The sole accent; used for links (default state), button hover states, and the tag badge background (`div.mt-2`). On hover, text shifts from grey to this blue.
- `rgb(153, 200, 255)` — Focus ring outline; lighter accessible blue for keyboard navigation.

**Borders & structure**
- `rgb(39, 39, 42)` — Consistent border colour across all elements; subtle, matches the dark surface family.
- `hsl(240 5.9% 90%)` → `--border`, `--input` — Token-level border/input definition (light-mode values in token; dark-mode overrides rendered values).

**Surface accent**
- `rgb(230, 230, 230)` — Appears on `div.absolute`; a near-white surface element used as an overlay or highlight band (luminance 0.902).

## 3. Typography Rules

Single typeface throughout:

**Söhne** (`__soehne_b34e2f`) — A contemporary grotesque with warm humanist curves. Used at every level.

| Element | Size | Weight | Leading |
|---------|------|--------|---------|
| h1 | 20px | 500 | 24px (1.2) |
| h4 | 16px | 400 | 24px (1.5) |
| body | 16px | 400 | 24px (1.5) |
| button | 16px | 400 | 24px (1.5) |

The typographic hierarchy is deliberately compressed — `h1` at only 20px signals that this is an application-style interface rather than a marketing page. Weight differentiates heading (500) from body (400), but the size difference is minimal. Letter-spacing is browser default (not negative-tracked), letting Söhne's natural spacing breathe. No uppercase transforms, no decorative font weights.

What is absent: no display face, no serif contrast, no variable font axes, no font-feature-settings. Söhne alone carries the entire type system.

## 4. Component Stylings

**Tags / Badges** — `rgb(59, 130, 246)` blue background with `rgb(230, 230, 230)` text. Uses `--radius: 0.5rem` (8px) corner rounding. Compact label style.

**Buttons** — Transparent background by default, `rgb(230, 230, 230)` text. On hover: text transitions to `rgb(59, 130, 246)` blue (no background change — text-only colour shift). On focus: `rgb(153, 200, 255)` outline at 1px. No shadow, no fill change on hover.

**Borders** — Universal `rgb(39, 39, 42)` across all bordered elements; consistent, never changes.

**Base radius** — `--radius: 0.5rem` (8px). Applies to cards, inputs, and interactive elements. Consistent, moderate rounding — not sharp, not pill.

**No shadows** — Shadow array is empty. Dark surfaces create their own depth hierarchy without elevation effects.

## 5. Layout Principles

Built on Next.js + Tailwind CSS. Breakpoints at: `600px`, `640px`, `768px`, `800px`, `1024px` — a combination of Tailwind defaults (640/768/1024) and custom widths (600/800).

Spacing is utility-driven (no explicit spacing tokens in custom properties). The shadcn/ui component system provides consistent padding and gap values through Tailwind classes. Content appears constrained to a readable max-width column, centred — appropriate for a portfolio with primarily text and project cards.

## 6. Depth & Elevation

No box-shadows are used. Elevation language:
- **Dark background stack**: `rgb(10,10,13)` base → `rgb(39,39,42)` borders → `rgb(230,230,230)` surface overlay creates a three-level dark hierarchy.
- **Blue accent** creates focal point without needing shadow.
- **Luminance contrast** between the body (near 0) and the surface overlay (0.902) provides the strongest depth signal.

This is a flat dark UI where depth comes from colour lightness steps, not shadows.

## 7. Do's and Don'ts

**Do:**
- Use `rgb(10,10,13)` as the base dark background — not pure black, it reads warmer.
- Use `rgb(59,130,246)` sparingly: links, hover states, one badge colour. No more.
- Keep Söhne at 400/500 weight — the restraint is part of the aesthetic.
- Apply `border-radius: 0.5rem` universally to all interactive elements.
- Use `rgb(39,39,42)` as the single border colour; never vary it.

**Don't:**
- Don't use white text on the dark body — use `rgb(230,230,230)` to avoid harshness.
- Don't add shadows; the dark palette creates depth through lightness steps.
- Don't introduce additional typefaces; Söhne is sufficient.
- Don't use blue for decorative purposes — only for interactive elements and active states.
- Don't scale h1 beyond the application-size 20px; the tight scale is intentional.

## 8. Responsive Behavior

Five breakpoints (640/768/1024 Tailwind defaults + 600/800 custom):
- Below `600px`: Likely single-column stacked layout.
- `640px–768px`: Tablet range; standard Tailwind `sm` breakpoint.
- `768px–1024px`: Standard Tailwind `md`–`lg` range.
- Above `1024px`: Full desktop layout.

Dark mode is the single, fixed appearance — no light/dark toggle observed.

## 9. Agent Prompt Guide

> "Design in the style of amelieschlueter.com: dark base `rgb(10,10,13)`, light grey text `rgb(230,230,230)`, single blue accent `rgb(59,130,246)` for links and hover states only. Söhne typeface at 400/500 weight, 16–20px scale. Consistent `border-radius: 8px` on all components. Border colour `rgb(39,39,42)` everywhere. No shadows — depth via lightness steps. shadcn/ui-compatible token structure. Tailwind CSS responsive breakpoints."

---

*Generated by Sparkbites — extracted from live CSS analysis*
