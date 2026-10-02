# HEX — Design System Reference

## 1. Visual Theme & Atmosphere

HEX describes itself as "an experimental creative studio" that builds "monopolizing brands for cutting edge companies," and its own site is the proof of concept. The page sits on a very dark teal (`rgb(3, 27, 29)`) with soft light-grey text (`rgb(235, 235, 235)`), and a single electric mint green (`rgb(33, 255, 188)`) cuts through it, most visibly on the h1. The palette is named in its own tokens: `--hex-green`, `--hex-dark-green`, `--hex-light-green`, `--hex-mist-green`. A single grotesk, Lausanne, carries all text with tight negative tracking on headings. Faint mint hairlines (`rgba(183, 255, 233, 0.1)`) and ring-style shadows give the interface a technical, circuit-diagram quality. The studio's client list is shown as funding rounds ("$85M Series B", "$7M Series A"), which fits the confident, tech-company register. Built on Webflow.

---

## 2. Color Palette & Roles

**Foundation**
- `rgb(3, 27, 29)` / `#031b1d` — page canvas and navbar (`--hex-dark-green`, also aliased as `--hex-mist-green`)
- `rgb(235, 235, 235)` / `#ebebeb` — body text, light panels (`--hex-light-green`, `--white`)
- `#d9d9d9` — light grey (`--grey`)
- `#9b9b9b` — mid grey for accessible secondary components (`--accessible-components--dark-grey`)

**Accent**
- `rgb(33, 255, 188)` / `#21ffbc` — electric mint (`--hex-green`), used on the h1 and the menu icon line
- `#05d194` — deeper aquamarine (`--medium-aquamarine`)

**Strokes**
- `#ebebebcc` — light stroke (`--stoke`, as spelled in the source)
- `#0e5a5836` — dark teal stroke (`--dark-stroke`), used as the navbar bottom and side border
- `rgba(183, 255, 233, 0.1)` — faint mint line and ring colour

**Interactive**
- `rgb(77, 101, 255)` — 2px solid focus outline on the menu button
- `rgb(51, 51, 51)` — default link colour in the extraction

The system is dark-first, with one mint accent and a restrained set of neutrals.

---

## 3. Typography Rules

**Typeface**
- **Lausanne** — the only family, across every role

**Scale**

| Role   | Font     | Size   | Weight | Line-height | Tracking | Transform |
|--------|----------|--------|--------|-------------|----------|-----------|
| H1     | Lausanne | 40px   | 400    | 44px        | -0.64px  | none      |
| H2     | Lausanne | 32px   | 400    | 35.2px      | -0.64px  | none      |
| H3     | Lausanne | 48px   | 300    | 52.8px      | -0.4px   | none      |
| H4     | Lausanne | 20px   | 500    | 20px        | -0.4px   | none      |
| Body   | Lausanne | 16px   | 400    | 24px        | normal   | none      |
| P      | Lausanne | 14px   | 400    | 14px        | +0.14px  | none      |
| Link   | Lausanne | 16px   | 400    | 24px        | normal   | none      |

**Principles**
- One family, three weights (300, 400, 500); hierarchy comes from size and weight shifts, not from a second typeface.
- The h3 is the largest step (48px) and the lightest weight (300), a deliberate inversion where big text is also delicate.
- Headings carry negative tracking (-0.4px to -0.64px) at line-height of about 1.1, giving tight headline blocks.
- Small `p` text (14px) opens up slightly with +0.14px tracking and a line-height equal to the size.
- Body is set at a comfortable 1.5 ratio (16px on 24px).

---

## 4. Component Stylings

**Navbar**
- Background `rgb(3, 27, 29)`, bottom and side border in `rgba(14, 90, 88, 0.21)` teal
- Logo link plus a menu button (`div.navbar_menu-button`, `role="button"`) with an icon whose line is `rgb(33, 255, 188)`
- Menu button focus: `rgb(77, 101, 255)` solid 2px outline
- Logo link focus: `rgb(16, 16, 16)` auto 1px outline

**Links**
- 16px Lausanne, line-height 24px
- Hover on the logo link produces no visible style change in the extraction

**Hairlines**
- `div.line` in `rgba(183, 255, 233, 0.1)` used as faint dividers

**Border radius**
- `8px` and `4px`

**Shadows**
- `rgba(183, 255, 233, 0.1) 0px 0px 0px 4px` — a 4px translucent mint ring
- `rgba(0, 0, 0, 0.66) 5px 2px 14px -1px inset, rgba(183, 255, 233, 0.1) 0px 0px 0px 4px` — an inset dark shadow combined with the same mint ring, producing a recessed, glowing-edge field

---

## 5. Layout Principles

- `main` has `0px 20px` horizontal padding, with a `64px` row gap and `32px` column gap, so sections are separated by generous vertical air and compact horizontal gutters.
- `body` resets padding and margin to `0px`.
- Content on the live site is a studio index: a project list with funding-stage tags, select case studies (Grafana, Composio, Exa, Fuser), and nav entries for Work, Clients, Info, Web Work, Swipe File, Writings and /Rejected.
- A light panel (`div.intro-image`, `rgb(235, 235, 235)`) sits against the dark canvas, creating contrast within the dark-first layout.
- Breakpoints at **479 / 767 / 768 / 991**, the Webflow defaults.

---

## 6. Depth & Elevation

Depth is created with light and rings, not drop shadows.
- **Mint ring** — a 4px `rgba(183, 255, 233, 0.1)` spread ring outlines elements like a faint halo.
- **Inset recess** — a `rgba(0, 0, 0, 0.66)` inset shadow (`5px 2px 14px -1px`) presses a field into the surface.
- **Surface contrast** — `rgb(3, 27, 29)` (luminance 0.079) against `rgb(235, 235, 235)` (luminance 0.922) panels gives the main depth jump.
- **Line work** — the 10% mint hairlines and `#0e5a5836` strokes define structure at very low contrast.

---

## 7. Do's and Don'ts

**Do**
- Use `rgb(3, 27, 29)` as the canvas and `rgb(235, 235, 235)` for text.
- Reserve `rgb(33, 255, 188)` for the highest-emphasis element, such as the h1 and menu icon.
- Set everything in Lausanne; vary weight (300, 400, 500) and size for hierarchy.
- Track headings tight (-0.4px to -0.64px) with line-height near 1.1.
- Define edges with translucent mint rings and low-contrast teal strokes rather than solid borders.
- Use `8px` and `4px` radii.

**Don't**
- Don't use pure black or pure white; the neutrals are teal-black and `#ebebeb`.
- Don't introduce a second typeface.
- Don't use the mint accent for body text or large backgrounds.
- Don't use soft outer drop shadows; use rings and inset shadows.
- Don't suppress focus outlines; the menu button relies on a visible `rgb(77, 101, 255)` ring.

---

## 8. Responsive Behavior

Breakpoints at **479, 767, 768 and 991** match Webflow's defaults. The navbar collapses to a menu button (`navbar_menu-button`, with a line icon in mint) on smaller screens. Main content keeps a tight `20px` side padding and a `64px` vertical gap, so the layout reads as a single flowing column on narrow widths while preserving the dark-first palette.

---

## 9. Agent Prompt Guide

> Build a UI that matches HEX's design language.

Set the canvas to very dark teal `rgb(3, 27, 29)` and body text to `rgb(235, 235, 235)`. Use electric mint `rgb(33, 255, 188)` as the single accent, for the h1 and key icons only, with `#05d194` as the deeper variant. Set all type in **Lausanne**: h1 40px/44px at -0.64px tracking, h2 32px, h3 48px at weight 300, h4 20px at weight 500, body 16px/24px, small text 14px with +0.14px tracking. Define structure with faint mint hairlines `rgba(183, 255, 233, 0.1)` and teal strokes `rgba(14, 90, 88, 0.21)`, and give fields a `0 0 0 4px rgba(183, 255, 233, 0.1)` ring, optionally with an inset `rgba(0, 0, 0, 0.66) 5px 2px 14px -1px` shadow. Use `8px` and `4px` radii. Pad `main` with `0 20px` and separate sections with a `64px` gap. Keep focus outlines visible (`rgb(77, 101, 255)` 2px). Let one accent colour and one typeface carry the brand.

---

*Generated by Sparkbites — extracted from live CSS analysis*
