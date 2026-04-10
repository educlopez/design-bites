# geniestudio.app — Design System

## 1. Visual Theme & Atmosphere

Genie Studio presents a quietly confident design — it doesn't shout. Built on Astro, the site feels handcrafted rather than template-stamped. The canvas is near-white with a barely-perceptible blue tint (`rgb(250, 253, 255)`) for the hero, grounding the page in a cool, airy register. The defining aesthetic choice is pastel sectional colour-coding: each feature icon receives a distinct, soft tinted background (peach, sky blue, mint, lavender, pale yellow) that catalogues capabilities without the visual noise of a full colour palette. Typography is a confident two-tier system — large editorial headlines in Aeonik against tight UI copy in Geist. No dark mode, no glassmorphism, no gradients. Honest surfaces, warm pastels, and restrained layout.

## 2. Color Palette & Roles

**Base**
- Background: `rgb(255, 255, 255)` — clean white
- Body text: `rgb(83, 88, 98)` — desaturated slate, not harsh
- Heading text: `rgb(10, 13, 18)` — deep ink, nearly black
- Secondary/muted text: `rgb(147, 151, 159)` — light slate for captions

**Interactive**
- CTA button fill: `rgb(24, 29, 39)` — dark navy-black
- CTA button text: `rgb(255, 255, 255)`

**Feature icon backgrounds** (the identity palette)
- Peach: `rgb(255, 207, 180)`
- Sky blue: `rgb(153, 207, 255)`
- Mint: `rgb(168, 236, 199)`
- Lavender: `rgb(228, 204, 255)`
- Pale yellow: `rgb(255, 242, 190)`

**Feature card fills**
- Card blue: `rgb(204, 231, 255)`
- Card green: `rgb(211, 246, 227)`
- Card purple: `rgb(241, 230, 255)`

**Surfaces**
- Hero tint: `rgb(250, 253, 255)` — blue-white
- Styles section: `rgb(249, 245, 255)` — purple-white
- Chat bubble: `rgb(232, 234, 236)` — neutral grey

**What's absent:** no semantic reds, no strong accent, no dark surfaces. All contrast is achieved through text colour shifts, not background darkness.

## 3. Typography Rules

A deliberate two-font system: **Aeonik** for display, **Geist** for UI.

| Element | Font | Size | Weight | Tracking |
|---------|------|------|--------|----------|
| H1 | Aeonik | ~43px | 500 | Normal |
| H2 | Aeonik | 64px | 500 | −1.28px |
| H3 | Aeonik | ~43px | 500 | Normal |
| H4 | Geist | ~14px | 600 | −0.14px |
| Body | Geist | 16px | 500 | Normal |
| `<p>` | Geist | 16px | 500 | −0.16px |
| Links | Geist | ~14px | 500 | −0.14px |

The `"case"` font feature is applied universally — this OpenType feature adjusts punctuation and symbol positioning for mixed-case text, a detail that signals typographic intentionality. H2 at 64px with −1.28px tracking is the dominant editorial voice. Weight is consistently 500 (medium) rather than bold or light — avoiding extremes.

## 4. Component Stylings

**Navigation** — full-width, white background, no shadow or border (floats cleanly).

**Buttons** — dark fill (`rgb(24, 29, 39)`) with subtle two-layer shadow: `rgba(10,13,18,.8) 0 1px 2px, rgb(10,13,18) 0 0 0 1px` — this creates a solid engraved border-plus-shadow in one declaration. No separate border property needed.

**Feature icons** — circular or rounded square containers (50% or 8px radius) with the pastel tint backgrounds. The icon itself sits in the centre of the tinted area.

**Feature cards** — large rounded containers (32px or 36px radius) with pastel card fills. Notably generous radius compared to most SaaS sites.

**Chat bubbles** — `rgb(232, 234, 236)` fill, 14px radius — demo UI elements that feel native/OS-level.

**Avatars** — `rgb(246, 247, 248)` background, circular (50%).

## 5. Layout Principles

Sections use generous bottom margins (~180px between sections) creating clear chapter breaks as you scroll. Internal section padding is modest (~18px). The breakpoint system centres around 768px (mobile/desktop pivot) with 424–425px handling small phone sizes. 1441px is the wide breakpoint, suggesting a 1440px max-width content area — classic for marketing pages.

Layout is single-column for mobile, likely two- or three-column grid for desktop feature sections. No sidebar detected — this is a pure linear marketing layout.

## 6. Depth & Elevation

Elevation is almost entirely flat. Only two shadow values exist:
1. Button engraved shadow — `rgba(10,13,18,.8) 0 1px 2px, rgb(10,13,18) 0 0 0 1px`
2. A slightly heavier version of the same pattern (scaled 1.149×) — likely for modals or feature highlights

No drop shadows on cards. Depth is achieved through background tinting (pastel sections recede/advance based on their hue warmth) rather than shadow. This creates a flat-depth rather than layered-shadow aesthetic.

## 7. Do's and Don'ts

**Do:**
- Reserve Aeonik for headings only; use Geist for all body, labels, and UI
- Use the `"case"` font feature setting on all text elements
- Apply pastel tinted backgrounds to icon containers — rotate through the five colours systematically
- Use the engraved button shadow pattern (no separate border needed)
- Set generous border radii on cards (32px+)

**Don't:**
- Use harsh black (`#000`) — the darkest ink is `rgb(10, 13, 18)`
- Add drop shadows to cards or sections — tinting handles depth
- Mix Aeonik in UI elements (buttons, labels, captions)
- Use accent colours as page backgrounds — they're confined to icon/card containers
- Stack multiple tints in the same visual zone

## 8. Responsive Behavior

Nine breakpoints with near-duplicate pairs (424/425, 767/768/769) suggest precise pixel-level adjustments rather than loose zones. Key pivots:
- **~425px** — small phone optimisation
- **768px** — tablet/mobile breakover
- **919px** — likely intermediate layout shift (two-column to three-column)
- **1441px** — wide screen max cap

The section bottom margin (180px on desktop) likely reduces sharply on mobile. The large H2 (64px) presumably scales down to ~32–40px at 768px and below.

## 9. Agent Prompt Guide

> Recreate the geniestudio.app aesthetic: white background, deep ink (`rgb(10,13,18)`) headings, desaturated slate (`rgb(83,88,98)`) body text. Use **Aeonik** for headings at 64px weight 500 with −1.28px tracking. Use **Geist** at 16px weight 500 for all body and UI copy. Apply the `font-feature-settings: "case"` rule globally. For feature sections, assign each icon a pastel tinted circular container — rotate through peach `rgb(255,207,180)`, sky `rgb(153,207,255)`, mint `rgb(168,236,199)`, lavender `rgb(228,204,255)`, yellow `rgb(255,242,190)`. Cards use 32–36px border-radius. Buttons are dark filled (`rgb(24,29,39)`) with a single engraved shadow. No drop shadows on surfaces — let tinted backgrounds create depth.

*Generated by Sparkbites — extracted from live CSS analysis*
