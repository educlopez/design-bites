# animejs.com — Design System

## 1. Visual Theme & Atmosphere

Anime.js presents itself as a living color laboratory. The site's soul is a near-black canvas — warm charcoal rather than pure black — against which an extraordinary 16-hue spectrum (each with 8 tonal steps) pulses and breathes. The atmosphere is developer-focused but viscerally expressive: code documentation wrapped in the aesthetic sensibility of a motion design studio. Everything is dark by default, not as a fashion choice but as a stage for chromatic performance. The warmth in the neutral tones (slight brown undertone in `#252423`) prevents the interface from feeling cold or corporate.

## 2. Color Palette & Roles

**Base / Structure**
- Canvas: `#252423` — warm near-black, body background
- Surface raised: `#2f2e2d` to `#3b3937` — card and code block backgrounds
- Footer: `#252423` — consistent with canvas

**Text hierarchy**
- Primary text: `#f6f4f2` — slightly warm off-white, never harsh
- Secondary text: `#cccac9` — muted but legible
- Tertiary / disabled: `#85837e`, `#706e69`, `#5b5855`

**Accent spectrum (the brand's signature)**
The design defines 16 named color families — red, coral, orange, yellow, citrus, lime, green, turquoise, cyan, sky, sega (teal-blue), king (royal blue), indigo, lavender, purple, magenta, pink. Each has 8 tonal steps (1 = brightest, 8 = darkest, approaching the canvas). Used in interactive demos, syntax highlighting, and feature callouts. No single accent "owns" the brand — the palette itself is the brand.

**Interactive / code**
- Code blocks: `rgb(47, 46, 45)` bg, `rgb(180, 177, 175)` text
- Inputs: `rgb(53, 52, 51)` — slightly lifted from canvas

## 3. Typography Rules

A single typeface rules everything: **DIN** (with Helvetica Neue fallback). This is a deliberate, disciplined constraint. DIN is geometric, industrial, and highly legible at small sizes — the typographer's choice for technical documentation that still needs personality.

- **h2 (hero)**: 64px / 700 weight / 55.36px line-height — tight leading creates tension
- **h1, h3**: 16px / 700 and 600 — headings are used for labels and navigation, not hierarchy
- **body**: 16px / 400 — comfortable reading weight
- **p (feature text)**: 20px / 600 — prominent semi-bold for key statements
- **code**: Custom `Mono` typeface, 14px — clearly distinct from prose

The absence of variable weights, serifs, or display typefaces is a statement: clarity over decoration.

## 4. Component Stylings

**Buttons**: Transparent background, warm off-white border and text (`rgb(180, 177, 175)`), 700 weight — ghost style as default. No filled primary button seen in base styles.

**Code blocks**: `background: rgb(47, 46, 45)`, `color: rgb(180, 177, 175)`, monospace font. Inline code uses the same palette — no jarring contrast shifts.

**Navigation**: Transparent header over canvas. Sticky nav doesn't introduce a new background color.

**Interactive demos**: Colored with individual hue families from the 16-color spectrum, each demo assigned its own palette step.

**Border radius**: Not specified in extracted data — likely minimal/sharp, consistent with the DIN/industrial aesthetic.

## 5. Layout Principles

The layout is content-forward with minimal structural chrome. Navigation stays out of the way. Content sections are wide, breathing, without excessive sidebar divisions. The color spectrum functions as spatial punctuation — color blocks demarcate sections rather than traditional dividers or borders.

Spacing favors generous vertical rhythm. The tight line-height on h2 (55.36px for 64px type) creates dense headline blocks that contrast with open body text.

## 6. Depth & Elevation

Depth is achieved through color temperature shifts, not shadows. Darker surfaces (`#3b3937` to `#252423`) create foreground/background separation. Code blocks at `rgb(47,46,45)` float slightly above the canvas. There are no drop shadows visible in the base component layer — elevation is implicit.

## 7. Do's and Don'ts

**Do**
- Use the 16-color spectrum for accent, highlight, and demo elements
- Keep the canvas near-black and warm — avoid true `#000000`
- Use DIN exclusively; introduce Mono only for code contexts
- Let color carry visual hierarchy rather than size or weight alone

**Don't**
- Use filled button backgrounds — ghost style is intentional
- Apply bright accent colors to large areas; they're for accents only
- Mix in additional typefaces or decorative fonts
- Use pure white (`#ffffff`) — always reach for `#f6f4f2` or `#cccac9`

## 8. Responsive Behavior

No explicit breakpoints extracted. The site likely collapses multi-column demo grids to single column on mobile. The DIN typeface holds well at all sizes. Hero text (64px h2) would need significant reduction on small viewports.

## 9. Agent Prompt Guide

> Recreate animejs.com's design language: warm near-black canvas (`#252423`), single DIN typeface throughout, ghost-style UI elements with off-white borders. Accent with any of 16 named hue families (red through pink) but keep accents small — large surfaces stay dark. No shadows; elevation via surface color steps. Text is always warm off-white (`#f6f4f2`), never pure white. Code blocks use custom Mono at 14px with slightly lighter surface (`rgb(47,46,45)`).

---

*Generated by Sparkbites — extracted from live CSS analysis*
