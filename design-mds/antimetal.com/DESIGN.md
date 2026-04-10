# antimetal.com — Design System

## 1. Visual Theme & Atmosphere

Antimetal reads as enterprise software that has been quietly, confidently designed. The palette is cool blue-navy on near-white: a pairing that signals financial trustworthiness without the stiffness of traditional fintech. There is no garish CTA orange, no startup gradient. The atmosphere is restrained premium — the kind of design that lets the product's capabilities speak first. A subtle translucent header, soft shadow on a primary card, and a lone accent of sky blue (`rgb(224, 246, 255)`) are the only ornamental gestures.

## 2. Color Palette & Roles

**Backgrounds**
- Page: `rgb(248, 249, 252)` — near-white with a barely-perceptible cool tint
- Header: `rgba(248, 249, 252, 0.8)` — frosted glass over the page background
- Card/elevated surface: `rgba(12, 38, 77, 0.04)` — the navy bleeds slightly into surfaces

**Text**
- Primary: `rgb(27, 37, 64)` — deep navy, not black; sophisticated and warm
- Secondary/muted headings: `oklab(0.959716 -0.0186663 -0.0181907 / 0.56)` — navy at 56% opacity, for h3 labels

**Accent / Highlight**
- Sky blue surface: `rgb(224, 246, 255)` — used sparingly for icon backgrounds or feature callouts
- Dark hero block: `rgb(27, 37, 64)` — the navy used as a full-bleed dark section

**Borders / Inputs**
- Input border: `rgba(12, 38, 77, 0.06)` — barely visible
- Input background: `rgba(12, 38, 77, 0.02)` — almost invisible tint

The palette is architecturally simple: one dark color (navy), one light ground (near-white), one highlight (sky blue). All other values are opacity variants of the same navy.

## 3. Typography Rules

A single custom typeface — **abcdFont** — handles every text element, with `system-ui` as fallback. This is a bespoke or licensed grotesque, signaling brand investment. No serif, no mono, no decorative weight.

- **body, links, labels**: 16px / 400 / 24px line-height — comfortable reading
- **h3 (section labels)**: 15px / 400 / 20px — deliberately not large; hierarchy comes from position
- **buttons**: 14px / 450 weight — slightly heavier than body, tighter at 20px
- **inputs**: 15px / 400 with a subtle `-0.075px` letter-spacing

Weight variation is minimal (400 to 450). This is a design that earns distinction through spacing and color, not typographic loudness. No italic usage detected.

## 4. Component Stylings

**Primary card/panel**: `rgba(12, 38, 77, 0.04)` background with a sophisticated multi-layer shadow — three outer shadows creating depth, plus four inset shadows for a glossy highlight on top edge. The shadow recipe: `rgba(24,37,66,0.32) 0px 1px 3px, rgba(24,37,66,0.12) 0px 0.5px 0.5px, rgba(24,37,66,0.44) 0px 12px 24px -12px` (outer) + `rgba(219,247,255,0.48) 0px 0.5px 0.5px inset` (inner highlight).

**Buttons**: Transparent background, navy text, no visible border on default state. Focus state brings no visible change — interaction is minimal by design.

**Inputs**: Near-invisible styling — `rgba(12,38,77,0.02)` background, `rgba(12,38,77,0.06)` border. Form elements dissolve into the page.

**Border radius**: Two values only — `10px` for cards/inputs, and an extreme `3.35544e+07px` (effectively 100%) for pill/circular elements.

## 5. Layout Principles

Single-column, centered content with clear max-width containment. Breakpoint at 992px suggests a tablet-first pivot. The nav is sticky and frosted. Content hierarchy is managed through vertical spacing and subtle color differentiation rather than columns or dividers.

The dark hero block (`rgb(27, 37, 64)`) is used as a full-bleed section to break the light-ground monotony — a single dramatic contrast moment.

## 6. Depth & Elevation

The signature shadow is the brand's most expressive detail: a seven-value compound shadow combining hard edge, ambient fill, long drop, and inner highlight. This creates a card that looks almost physically lifted from the page surface. No other elevation level is visible — it's binary: flat page or one elevated card.

## 7. Do's and Don'ts

**Do**
- Use navy (`rgb(27,37,64)`) as the sole text and accent color
- Apply the compound shadow only to primary cards — it's precious
- Keep forms invisible; let content breathe on the near-white ground
- Use `10px` radius for interactive components, pill radius for badges/tags only

**Don't**
- Introduce additional accent colors; the sky-blue is already at the edge
- Use bold or heavy type weights — 450 is the ceiling
- Add decorative borders or dividers; spacing does that work
- Use pure black or pure white; every value should carry the cool blue undertone

## 8. Responsive Behavior

One breakpoint at 992px. Below this, the nav likely collapses, single-column layout persists. The frosted header may adjust opacity. Button and input sizing stays consistent — no dramatic font scaling.

## 9. Agent Prompt Guide

> Build with Antimetal's visual language: near-white page (`rgb(248,249,252)`), deep navy text (`rgb(27,37,64)`), bespoke grotesque typeface at regular weight only. One elevated card style using the compound multi-layer shadow. Inputs and forms are near-invisible. The only accent is sky blue (`rgb(224,246,255)`) used sparingly on icon backgrounds. No gradients, no color explosions — restraint is the brand.

---

*Generated by Sparkbites — extracted from live CSS analysis*
