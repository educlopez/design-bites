# joebell.studio — Design System

## 1. Visual Theme & Atmosphere

Joe Bell's studio site is built on an unusual typographic bet: Inter at 48px bold for the hero, while the section headings (h2) are 14px uppercase with tracked-out spacing. The hierarchy is inverted from convention — the biggest element screams, everything else whispers. This creates a stark, magazine-influenced rhythm where the display type is the only decoration.

The colour system is defined in OKLCH — a perceptually uniform colour space — which indicates careful attention to colour consistency across displays. The palette is cool, near-monochrome: very dark cool grey for primary text, mid grey for secondary, light grey for borders. There is no named accent colour; the design relies entirely on typographic contrast and whitespace.

Built with Astro and Tailwind CSS v5, this is a statically generated site where performance and precision are design values as much as aesthetics.

---

## 2. Color Palette & Roles

All colours are expressed in OKLCH (perceptually uniform). Approximate hex equivalents provided for reference.

| Role | OKLCH Value | Approx Hex | Notes |
|------|-------------|-----------|-------|
| Primary text | `oklch(0.274 0.006 286)` | `#333a42` | Dark cool grey |
| Secondary text / H2 | `oklch(0.442 0.017 286)` | `#5a6370` | Mid cool grey |
| Border / dividers | `oklch(0.92 0.004 286)` | `#e8eaec` | Light cool grey |
| Surface hover | `oklch(0.871 0.006 286)` | `#d8dadc` | Focus ring bg |
| Near-white overlay | `oklab(1 0 0 / 0.95)` | `rgba(255,255,255,0.95)` | Skip-nav bg |

The blue-grey hue angle (~286°) runs consistently through the entire palette, giving the design a cool, cohesive temperature. There is no warm tone, no accent, and no dark mode — the system is light-only monochrome.

Notable absence: no background colours captured on surfaces. The page likely uses the browser default white, with no layering of background surfaces. The design is typographic, not spatial.

---

## 3. Typography Rules

Single typeface: **Inter** (subsetted, loaded as a custom font asset via Astro/Vite). Only one CSS variable is defined: `--font-inter`.

| Role | Size | Weight | Line Height | Tracking | Transform |
|------|------|--------|-------------|----------|-----------|
| H1 / hero | 48px | 700 | 48px (1:1) | normal | none |
| H2 / section labels | 14px | 400 | 20px | +0.7px | UPPERCASE |
| Body | 16px | 400 | 24px (1.5×) | normal | none |
| Paragraph | 16px | 400 | 24px | normal | none |
| Small / nav | 14px | 400 | 20px | normal | none |

The h2 typographic treatment is a signature move: 14px uppercase with positive tracking creates section labels that read as structural metadata rather than headings. This is a design pattern borrowed from editorial and print — where section markers don't compete with the hero.

The 1:1 line-height on h1 (48px/48px) creates a dense, tightly stacked display block. No loose leading at the top.

---

## 4. Component Stylings

**Navigation**
- Font: Inter 14px / 400
- Text colour: `oklch(0.274 0.006 286)` — same as body text
- Background: transparent
- No hover colour change detected — interaction may be underline or opacity-based

**Links (inline)**
- Default: `oklch(0.274 0.006 286)` — matches body, not a distinct link colour
- Focus ring: `oklch(0.871 0.006 286)` 1px border (via Tailwind ring utilities)
- No hover state captured — clean, quiet

**Borders / Dividers**
- `oklch(0.92 0.004 286)` 1px — used as ring/outline shadows via Tailwind's ring system
- Shadow formula: `oklch(0.92 ...) 0px 0px 0px 1px` — border rendered as `box-shadow`

**Skip navigation**
- `oklab(1 0 0 / 0.95)` background — near-opaque white overlay
- Accessible-first component with careful focus management

---

## 5. Layout Principles

Built on Tailwind CSS v5 with Astro. Layout is utility-driven with no custom grid token system detected.

- Content appears to be single-column, constrained-width on desktop
- `inline-flex` used on navigation items — horizontal toolbar pattern
- No explicit grid column count or gap tokens in the CSS custom properties
- Spacing entirely managed through Tailwind utility classes

The philosophy is content-first: no ornamental structure. The 48px hero lands immediately; section labels at 14px uppercase provide minimal wayfinding. Every spacing decision defers to Tailwind's default scale.

---

## 6. Depth & Elevation

Shadows are used only as border simulations via `box-shadow`:

- Card / focus ring: `oklch(0.92 0.004 286) 0px 0px 0px 1px` — a 1px border rendered through shadow
- No `drop-shadow`, no elevation layers, no blur effects

The design is entirely flat. There is no Z-axis — no cards, no modals with elevated shadows, no sticky headers with background blur. The visual weight comes from typographic mass, not surface depth.

---

## 7. Do's and Don'ts

**Do:**
- Use OKLCH colours when extending the system — the hue consistency matters
- Keep h2 labels at 14px uppercase with positive tracking (+0.7px) — this is the section marker pattern
- Let h1 stay at 48px/700 with 1:1 line-height — the density is intentional
- Use `box-shadow` as 1px borders rather than `border` property
- Keep all interactive elements in the same text colour as body — no decorative link colours

**Don't:**
- Add a chromatic accent colour — the monochrome is a design statement
- Increase line-height on h1; the tight 1:1 stack is the signature
- Introduce background surface colours (cards, panels) — this is a typography-first flat layout
- Mix typeface weights above 700 or use styles like italic
- Add decorative shadows or elevation — the design lives entirely in 2D

---

## 8. Responsive Behavior

No explicit breakpoints captured in CSS custom properties. Tailwind handles breakpoints via utility classes (sm/md/lg/xl).

- Default Tailwind breakpoints apply: 640px, 768px, 1024px, 1280px
- The hero (48px) likely scales down via responsive Tailwind classes on mobile
- 14px uppercase labels read cleanly at all viewport sizes
- Single-column layout means minimal reflow required
- Touch targets on navigation links need careful review — 14px text may need padding augmentation for mobile

---

## 9. Agent Prompt Guide

**Quick reference:**
- Primary text: `oklch(0.274 0.006 286)` ≈ `#333a42`
- Secondary text: `oklch(0.442 0.017 286)` ≈ `#5a6370`
- Borders: `oklch(0.92 0.004 286)` ≈ `#e8eaec`
- Font: Inter, hero 48px/700, labels 14px uppercase +0.7px, body 16px/400
- No accent, no surfaces, no shadows

**Prompt to replicate this aesthetic:**
> "Design a studio portfolio page with a single font (Inter). Hero heading 48px/bold with 1:1 line-height. Section labels 14px uppercase with +0.7px tracking in mid-grey. Body 16px/400. Colour palette is cool grey monochrome (OKLCH ~286° hue). No accent colour, no card surfaces, no shadows. Flat typography-first layout."

**Prompt to extend a component:**
> "Add a project listing to joebell.studio. Section label: 14px uppercase `#5a6370` tracking +0.7px. Project title: 16px/400 `#333a42`. Dividers: 1px `#e8eaec` rendered as box-shadow. No hover colour change — use opacity or underline for interaction. No background fill on the list items."

---

*Generated by Sparkbites — extracted from live CSS analysis*
