# granola.ai — Design System

## 1. Visual Theme & Atmosphere

Granola is one of the most coherent design systems in the AI productivity space — a full custom token library ("oats") that encodes not just colours but a philosophy: warm neutrals, olive-tinted greens, and a surface that feels like cream paper rather than a screen. The product is a meeting notes tool, and the design feels like what note-taking *should* feel like — calm, organic, analogue-adjacent. The olive/lime accent (`#788c15`, `#5b6f00`) runs through every interactive element, providing brand identity through colour chemistry rather than logos. Two custom typefaces — **Quadrant** for display and **Melange** for reading — signal that typography investment is the real differentiator here.

## 2. Color Palette & Roles

**Base surfaces** (the "oats" system)
- Surface: `#f7f7f2` — warm off-white, paper-like
- Surface elevated: `#ffffff` — pure white for cards/modals
- Surface sunken: `#f2f2ec` — slightly darker inset areas

**Ink (text)**
- Primary: `#292929` — warm dark, not cold black
- Secondary: `#72726e` — muted warm grey
- Secondary strong: `#4e4d4b`
- Tertiary: `#acada8` — placeholder/metadata level

**Brand accent (olive green)**
- `#788c15` — ink/text on accent contexts
- `#5b6f00` — fill/strong accent (darker olive)
- `#b2c248` — border focus ring (bright lime)
- Accent tint: `#788c1526` — gossamer green overlay

**Semantic**
- Danger: `#e95d3d` — warm coral red
- Danger hover: `#bd4a30`

**Data/status dots** (from content analysis)
- `rgb(178, 194, 72)` — lime/olive bullet
- `rgb(184, 213, 255)` — light blue bullet
- `rgb(237, 225, 161)` — pale yellow bullet
- `rgb(233, 93, 61)` — coral/red bullet
- `rgb(254, 190, 41)` — amber bullet

**Surface tints** (accent-blue, green, purple panels)
- `#eaf4fe`, `#f2f6e1`, `#f3f0fa` — section distinction without harsh borders

**What's absent:** No pure black, no dark mode, no neon colours. Everything is temperature-adjusted toward warm.

## 3. Typography Rules

The two-font pairing is rare and intentional: **Quadrant** (a display serif) for headings, **Melange** (a humanist text font) for reading.

| Element | Font | Size | Weight | Tracking |
|---------|------|------|--------|----------|
| H1 | Quadrant | 68px | 400 | −1.02px |
| H2 | Melange | 24px | 300 | +0.24px |
| H3 | Quadrant | 20px | 400 | −0.3px |
| Body | Melange | 16px | 400 | Normal |
| `<p>` | Melange | 14px | 500 | +0.14px |
| Blockquote | Quadrant | 24px | 400 | Normal |
| Button | Melange | 16px | 400 | Normal |

Quadrant at weight 400 (not bold) for the largest headings — this is deliberate restraint. The 68px H1 at −1.02px tracking achieves mass through size alone. Melange's slight positive tracking on paragraphs (+0.14px) improves reading rhythm at small sizes. The H2 at weight 300 feels like editorial subheadings in a printed magazine.

No uppercase transforms. No condensed variants. Vertical rhythm is tight — H1 at 1.0× line-height (68/68), body at 1.5×.

## 4. Component Stylings

**Buttons**
- Primary fill: `#292929` with white text — warm dark, not cold black
- Accent: `#5b6f00` (olive) fill
- Hover states live in the token system (defined via CSS variables)

**Cards** — `border-radius: 8px` standard, `9999px` for pill-shaped elements. An extreme `3.35544e+07px` (computed max) appears for fully-rounded elements where `border-radius: 50%` would be expected.

**Shadows** — extremely minimal:
- `rgba(0,0,0,.15) 0 0 0 1px` — 1px border-as-shadow for card outlines
- `rgba(0,0,0,.03) 0 0 36px` — barely-perceptible ambient glow
- `rgba(0,0,0,.03) 0 0 2px inset` — inner shadow for sunken inputs

**Borders** — `--oats-border-hairline: #47432a33` — a warm brown at 20% opacity, so borders feel like aged paper rather than sterile lines.

## 5. Layout Principles

Sections use 64px bottom padding — restrained compared to typical SaaS. The 16px gap within sections creates comfortable density. No horizontal padding on `<main>` — full bleed at the container level with inner gutters applied per-section.

Breakpoints: 480–1024px span, with 639px and 991px as the primary mobile/tablet pivots. Ten breakpoints total suggests careful responsive work but with a max-width of ~1024px implying a deliberately narrow, reading-focused layout.

## 6. Depth & Elevation

Granola achieves elevation almost entirely through background temperature shifts:
- White (`#fff`) floats above warm off-white (`#f7f7f2`)
- Sunken areas use `#f2f2ec` — slightly cooler
- The accent tints (`#eaf4fe` etc.) create visual sections without borders

Shadow is so minimal it's almost ornamental. The design trusts colour warmth gradations to signal hierarchy — a sophisticated, analogue approach that mirrors the product's notebook metaphor.

## 7. Do's and Don'ts

**Do:**
- Use `#f7f7f2` as the default page background — never pure white or grey
- Apply Quadrant only for H1, H3, and blockquotes — Melange handles everything else
- Use the olive accent (`#788c15`/`#5b6f00`) sparingly for CTAs and focus states
- Set borders using `#47432a33` — warm brown at low opacity, never cold grey
- Use the bullet-dot colour system for data visualisation inline elements

**Don't:**
- Use cool greys — every neutral should have warm undertones
- Bold headings — Quadrant at weight 400 is the intended voice
- Add shadow depth beyond the three minimal values
- Apply the accent tints (`#eaf4fe`, `#f2f6e1`, `#f3f0fa`) as primary backgrounds — they're accent zones
- Use pure `#000000` anywhere

## 8. Responsive Behavior

Ten breakpoints (480–1024px) including tight pairs at 639/640 and 991/992 indicate precision micro-adjustments. The narrow max (~1024px content width) means the design doesn't dramatically reflow — it's already narrow on desktop. The primary mobile collapse is at 640px. The 68px Quadrant H1 likely scales to ~36–44px at mobile.

## 9. Agent Prompt Guide

> Recreate the granola.ai design language. Set page background to `#f7f7f2` (warm off-white). Use **Quadrant** serif at weight 400 for H1 (68px, −1.02px tracking) and blockquotes. Use **Melange** humanist text for all body, buttons, and UI at 16px weight 400. Primary text is `#292929` (warm dark). Olive brand accent is `#5b6f00` for fills, `#788c15` for text. Card borders use `rgba(71,67,42,.2)` — a warm brown hairline. Shadows are near-invisible: `rgba(0,0,0,.15) 0 0 0 1px` for card outlines only. Use `#fff` elevated cards over `#f7f7f2` page background to create depth through warmth. The semantic danger colour is `#e95d3d` (coral, not red).

*Generated by Sparkbites — extracted from live CSS analysis*
