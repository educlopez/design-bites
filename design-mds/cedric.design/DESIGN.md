# cedric.design — Design System

## 1. Visual Theme & Atmosphere

cedric.design is a portfolio built entirely in Framer, and its design philosophy is unapologetic darkness. The canvas sits on a near-black `rgb(20, 20, 20)` background — not pure black, which would feel lifeless, but a dark charcoal that adds just enough warmth to feel like a physical surface. Layered on top, slightly lighter cards at `rgb(26, 26, 26)` and `rgb(38, 38, 38)` create a sense of depth through luminance steps rather than through shadows.

The atmosphere is editorial and quiet. Typography is the hero: custom web-licensed cuts of the Suisse type family (SuisseWorks for display, SuisseIntl for interface) give the site a distinctly Swiss-modernist sensibility. The type is small and precise — body text runs at just 13px with tight tracking — signaling that the work is meant to be read closely, not skimmed.

Built on Framer, the site also inherits subtle micro-interactions: links scale up 6% on hover via CSS transform rather than any color change, a restrained gesture that feels mechanical and deliberate.

---

## 2. Color Palette & Roles

**Background surfaces** (luminance-ordered, layered):
- Page background: `rgb(20, 20, 20)` — base canvas
- Mid-layer cards: `rgb(26, 26, 26)` — section containers
- Elevated elements: `rgb(38, 38, 38)` — inputs, interactive surfaces

**Text**:
- Primary / headings: `rgb(224–242, 224–242, 224–242)` — near-white, slight warmth
- Secondary / navigation links: `rgb(135, 135, 135)` — muted grey, becomes `rgb(170, 170, 170)` on hover
- Body copy: `rgb(0, 0, 0)` is overridden by the Framer layer; effective body text is light on dark

**Accent / interactive**:
- No brand accent color is present. The site deliberately avoids color as emphasis.
- Focus rings use the browser default blue `rgb(0, 95, 204)` — accessibility without decoration

**What's absent**: No primary brand color, no gradient, no hue. The palette is entirely achromatic. Color would feel intrusive here.

---

## 3. Typography Rules

The site uses the Suisse type family exclusively — a conscious investment in premium web fonts that positions the work before a single word is read.

| Role | Typeface | Size | Weight | Tracking |
|------|----------|------|--------|----------|
| Display / H1 | SuisseWorks-Book | 32px | 450 | −0.96px |
| Section / H2–H3 | SuisseIntl-Book | 16px | 450 | −0.32px |
| Body / Paragraphs | SuisseIntl-Regular | 13px | 400 | −0.13px |
| Inputs | SuisseIntl-Regular | 13px | 400 | normal |

Key rules:
- Negative letter-spacing is applied at every level — this is a precision aesthetic, not loose.
- Weight 450 is used instead of 400 or 500, taking advantage of the variable-font capabilities of Suisse.
- Line heights are tight: H1 at 1.15× (36.8/32), body at ~1.23× (16/13). This creates density without crowding.
- Inputs use the `"ss02"` OpenType feature set — a detail that shows typographic intentionality even in form elements.
- No uppercase, no decorative text transforms.

---

## 4. Component Stylings

**Cards / content blocks**: Dark surface elevation using the three luminance steps. No borders — separation is achieved purely through background color contrast.

**Inputs**: `rgb(38, 38, 38)` background with a subtle inset shadow `rgba(38, 38, 38, 0.5) 0px 0px 0px 1px inset` acting as a border. On focus, the inner shadow deepens slightly rather than changing color.

**Navigation links**: Rendered in `rgb(135, 135, 135)`, transitioning to `rgb(170, 170, 170)` on hover. No underlines, no background changes — just luminance shift.

**Interactive links (large)**: Scale 1.06× on hover via CSS `transform: matrix(1.06, 0, 0, 1.06, 0, 0)`. This is the only motion on the page, making it feel considered.

**Border radii in use**: 6px, 7px, 8px, 10px, 12px, 17px, 24px — the variance suggests Framer-generated components rather than a strict token system.

**Shadows**: Two layered shadow styles:
- Inset white highlight: `rgba(255, 255, 255, 0.5) 0px -1px 0px 0px inset` — adds a subtle top-edge shimmer to cards
- Multi-layer drop: a stacked box-shadow for subtle depth on elevated elements

---

## 5. Layout Principles

The layout is controlled by Framer's auto-layout engine. Key observations:

- **Breakpoints at 810px and 1200px** — a two-breakpoint system covering mobile, tablet, and desktop
- **Tight body padding**: The page resets to `padding: 0` and relies on Framer's internal grid
- **Content density**: Small type sizes and compressed line heights maximise information without scrolling
- **No visible grid lines** — structure is implied by consistent card widths and alignment, not borders or rules
- No max-width container is detectable from CSS; Framer manages this internally

---

## 6. Depth & Elevation

Depth is created through the three-step surface stack rather than shadow:

1. Page (`rgb(20, 20, 20)`) → lowest
2. Section containers (`rgb(26, 26, 26)`) → mid
3. Interactive / form elements (`rgb(38, 38, 38)`) → highest

Shadows serve as refinement, not structure:
- A 1px inset white line at the top of cards simulates a lit edge
- The three-layer drop shadow uses very small spreads (0.6–2.3px) for a barely-there lift effect

---

## 7. Do's and Don'ts

**Do:**
- Use achromatic surfaces only — the palette is intentionally without hue
- Apply negative letter-spacing to all typographic elements
- Use weight 450 for display/UI text when Suisse fonts are available
- Separate content zones with surface luminance, not borders
- Reserve motion for scale transforms on interactive elements

**Don't:**
- Introduce color as decorative emphasis
- Use font-weight 700 (bold) — the aesthetic demands restraint
- Add drop shadows with large spread or high opacity
- Use uppercase transforms — this aesthetic eschews them
- Mix fonts outside the Suisse family

---

## 8. Responsive Behavior

The site uses two meaningful breakpoints:
- **≤810px**: Mobile/tablet layout — likely single column, compact navigation
- **810px–1200px**: Intermediate — possible two-column grid
- **≥1200px**: Full desktop layout with widest content grid

Since the site is Framer-built, responsive behavior is entirely handled by Framer's layout engine. CSS breakpoints are minimal; most adaptation happens through Framer's variant system. Type sizes do not appear to scale responsively — the small body text remains fixed.

---

## 9. Agent Prompt Guide

When recreating or referencing cedric.design:

> "Design a dark portfolio site with an achromatic palette using three surface luminance levels: page `#141414`, containers `#1a1a1a`, and interactive elements `#262626`. Typography is exclusively the Suisse family — SuisseWorks-Book at 32px/−0.96px tracking for display, SuisseIntl-Book at 16px/−0.32px for UI, SuisseIntl-Regular at 13px/−0.13px for body. No brand colors. Links use a 6% scale transform on hover instead of color change. Shadows are ultra-subtle: inset 1px white edge highlight, multi-layer drop at <3px spread. Two breakpoints: 810px and 1200px."

---

*Generated by Sparkbites — extracted from live CSS analysis*
