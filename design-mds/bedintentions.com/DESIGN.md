# Bed Intentions — Design System Reference

## 1. Visual Theme & Atmosphere

Bed Intentions is a Shopify-based bedding brand that has escaped the template trap. The design language is typographically sophisticated, layering multiple custom fonts with clearly differentiated roles: a serif-adjacent round display font for editorial headings, a condensed social font for callouts, a monospaced condensed font for metadata and pricing, and a grotesque sans for body copy. The palette leans light and airy — off-white, white, pale sage/khaki accents — with careful animation timing built into the custom property system. The overall atmosphere is that of a premium lifestyle brand: considered, quiet, and confident in its whitespace.

---

## 2. Color Palette & Roles

**Foundation**
- `rgb(255,255,255)` — primary background (`--color-background-1`)
- Off-white page surfaces (inherited from Shopify Dawn/custom theme variables)

**Text**
- `rgb(11,11,11)` — primary text (`--oke-text-primaryColor`)
- `rgb(76,74,74)` — secondary text (`--oke-text-secondaryColor`)
- `rgb(182,182,182)` — border / divider tone

**Interactive**
- `rgb(232,230,216)` — active button border (`--oke-button-borderColorActive`) — a warm warm off-white
- `rgb(219,221,228)` — default button border (`--oke-button-borderColor`) — a cool light gray

**Review / badge system (OK ENDI)**
- Primary text: `rgb(11,11,11)`
- Secondary: `rgb(76,74,74)`
- Borders: `rgb(182,182,182)` and `rgb(219,221,228)`

The palette is deliberately muted and natural. No bright accent colors. The button border shift between cool gray and warm off-white encodes a tactile directional signal.

---

## 3. Typography Rules

Bed Intentions is one of the more ambitious typographic systems in this set, with four named font roles:

| Variable | Font | Role |
|----------|------|------|
| `--font-body` | ABCMonumentGrotesk | Primary body copy |
| `--font-body-alt` | ABCSocialCondensed | Alternate / callout text |
| `--font-title` | LMMonoLtCond10 | Titles (monospace condensed) |
| `--font-title-alt` | OfficeTimesRound | Heading fallback / editorial |
| `--font-heading-family` | OfficeTimesRound | Shopify heading slot |
| `--font-body-family` | Assistant | Shopify body slot |

**Key typographic decisions:**
- `LMMonoLtCond10` as the primary title font — a monospace condensed at `font-weight: 300` — creates a technical, editorial precision uncommon in e-commerce
- `ABCSocialCondensed` adds tall, compressed energy for accent text
- `OfficeTimesRound` provides a soft, rounded serif personality for editorial headings
- The Shopify theme variables (`--font-heading-family`, `--font-body-family`) use different fonts than the custom theme variables — there are effectively two parallel type systems in use

---

## 4. Component Stylings

**Buttons (OK ENDI review widget)**
- Border: `rgb(219,221,228)` default → `rgb(232,230,216)` active (cool-to-warm shift)
- Border-radius: `4px` — subtly rounded, not pill-shaped
- Font-weight: `700` — bold, assertive labels
- Font-size: `14px` via `--oke-text-regular`

**Animation system (explicit timing tokens)**
- Short: `0.1s`
- Default: `0.2s`
- Announcement bar: `0.25s`
- Medium: `0.3s`
- Long: `0.5s`
- Extra-long: `0.6s`
- Extra-longer: `0.75s`
- Extended: `3s`
- All use `cubic-bezier(0, 0, .3, 1)` ease-out — fast start, gradual finish

The animation token system is unusually detailed — eight named durations signal that transitions are choreographed, not incidental.

---

## 5. Layout Principles

6-column grid with `16px` gutters and `30px` page margins. Layout width is `calc(100vw - (2 * 30px))` — responsive to viewport without fixed breakpoints. Column width is derived: `calc((layout-width - (5 * 16px)) / 6)`. This is a genuine grid system, not utility classes pretending to be a grid. The precision suggests the design was spec'd before it was built.

---

## 6. Depth & Elevation

The extracted data shows minimal shadow use:
- `--media-shadow-opacity: 0.0` — media elements have no shadow by default
- `--focused-base-box-shadow: 0 0 0 .3rem rgb(var(--color-background)), 0 0 .5rem .4rem rgba(var(--color-foreground), .3)` — focus states use a glow + ring technique

Depth is editorial: whitespace and typographic contrast do the layering work. The focused state is the most complex shadow in the system.

---

## 7. Do's and Don'ts

**Do:**
- Use the four-font system purposefully: Monument Grotesque for body, Social Condensed for callouts, LM Mono for prices/metadata, OfficeTimesRound for editorial headings
- Apply the animation timing tokens — never use arbitrary transition values
- Use the 6-column/16px-gutter/30px-margin grid system for all layouts
- Shift button border from cool gray to warm off-white on active state

**Don't:**
- Introduce bright accent colors — the palette is deliberately muted and warm-neutral
- Use font-weight below `300` for title fonts (`LMMonoLtCond10` is already light)
- Mix the Shopify theme fonts (`Assistant`) with the custom theme fonts at the same typographic level
- Skip animation — the eight-token duration system implies motion is expected everywhere

---

## 8. Responsive Behavior

Breakpoints: not defined in custom properties — the grid uses `calc()` and viewport units to be intrinsically responsive. The layout width formula (`100vw - 60px`) works at any breakpoint. The `--layout-columns-count: 6` variable could be overridden at a media query level to collapse to 4 or 2 columns without changing the column-width formula.

---

## 9. Agent Prompt Guide

> Build a UI that matches Bed Intentions' design language.

Light off-white page. Use ABCMonumentGrotesk for body copy, LMMonoLtCond10 (light, 300 weight) for prices and metadata, OfficeTimesRound for editorial headings, ABCSocialCondensed for callout text. 6-column grid, 16px gutters, 30px page margins. Button borders are light cool-gray (`rgb(219,221,228)`) by default, shift to warm off-white (`rgb(232,230,216)`) on active — a subtle but intentional temperature shift. Focus states use a double glow: background-color ring + foreground-color soft glow. Animate everything using the `cubic-bezier(0, 0, .3, 1)` easing at the appropriate duration tier (0.1s–0.75s). The palette is muted naturals only.

---

*Generated by Sparkbites — extracted from live CSS analysis*
