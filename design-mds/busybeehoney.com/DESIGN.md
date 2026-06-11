# Busy Bee Honey — Design System Reference

## 1. Visual Theme & Atmosphere

Busy Bee Honey is a consumer honey brand that dresses an everyday grocery product in the warmth and craft of a heritage label. The page opens with a "GATHERING NECTAR…" loader and an animated bee — body and two wings as separate layers — that sets a hand-made, storybook tone before the first headline lands. The canvas is a warm pale-cream the color of honeycomb wax, with deep cocoa-brown ink, and the whole identity is carried by two bespoke display faces (TayMakawao and TayBirdie) that feel hand-drawn and a little rustic. Honey-gold, brick-red, dusty-cyan, and meadow-green appear as full-bleed circle transitions that wipe between sections like spreading drops of color. The atmosphere is honest, folksy, and warm — "REAL HONEST HONEY™" — built on traceability storytelling (flowers → hives → harvest → you) rather than slick e-commerce gloss.

---

## 2. Color Palette & Roles

**Foundation**
- `rgb(242, 235, 208)` (`#f2ebd0`) `--color-pale-cream` — page canvas, the honeycomb-wax base; also the loader bar and inverted nav text
- `rgb(59, 39, 34)` (`#3b2722`) `--color-dark` — cocoa ink: text, borders, link color

**Brand accents** (used as full-bleed circle transitions and section fills)
- `rgb(255, 202, 80)` (`#ffca50`) `--color-yellow` — honey gold; the footer fill and the signature accent
- `rgb(160, 52, 42)` (`#a0342a`) `--color-red` — brick red
- `rgb(106, 172, 194)` (`#6aacc2`) `--color-dusty-cian` — dusty cyan / sky
- `rgb(111, 161, 98)` (`#6fa162`) `--color-green` — meadow green (link underlines, transitions)

**Utility**
- `#ffffff` `--color-white` — input surfaces only
- `#000000` plus an alpha ramp (`--color-black-10` … `--color-black-50`) — scrims and dialog overlays

The system is anchored on cream + cocoa, with four saturated brand colors that arrive almost exclusively as animated circle wipes and section grounds — color is an *event* in the scroll, not constant chrome. The footer commits fully to honey-gold.

---

## 3. Typography Rules

Three bespoke/character faces split the work, all at weight 400 — there is no bold in the system. Hierarchy is built from face, dramatic size jumps, and a uppercase display headline.

**Typefaces**
- **TayMakawao-Regular** — the display voice: every heading from the giant `258px` display-1 down to h8, plus mobile nav. Rustic, hand-drawn, all caps at the top of the scale.
- **TayBirdie-Regular** — the detail/CTA voice: buttons, nav links, captions, footer detail, small labels.
- **AnonymousPro-Regular** — the body/reading voice: paragraphs at 12–20px, a friendly monospace-adjacent face for running copy.

**Scale** (desktop tokens)

| Role        | Font           | Size  | Weight | Transform |
|-------------|----------------|-------|--------|-----------|
| Display 1   | TayMakawao     | 258px | 400    | uppercase |
| H1          | TayMakawao     | 135px | 400    | uppercase |
| H2          | TayMakawao     | 90px  | 400    | —         |
| H3          | TayMakawao     | 72px  | 400    | —         |
| H4–H8       | TayMakawao     | 56→28px | 400  | —         |
| Detail/CTA  | TayBirdie      | 12–20px | 400  | —         |
| Body S/M/L  | AnonymousPro   | 12–20px | 400  | —         |

(Live-rendered h1 measured at 72px / line-height 57.6px, uppercase — the tokens describe the full ramp; sections clamp down from the headline maximums.)

**Principles**
- Weight is a constant 400 — never bold. Size and the all-caps display treatment carry every bit of hierarchy.
- Display headlines set with **tight, sub-unity line-height** (e.g. 72px font / 57.6px leading) so big TayMakawao type stacks densely like a stamped label.
- The big top-of-scale headings are uppercase; mid headings drop to sentence case as the eye moves into content.
- A clean reading face (AnonymousPro) keeps body copy legible against two highly characterful display faces.

---

## 4. Component Stylings

**Buttons / CTAs**
- TayBirdie label, transparent fill on the cream canvas, cocoa text and a cocoa hairline border — the field is defined by a thin outline, not a filled block.

**Links**
- Cocoa `#3b2722` text on transparent; an animated `LinkLine` underline rendered as a meadow-green (`rgb(111,161,98)`) bar that draws in rather than a static text-decoration.

**Nav**
- Transparent over hero media, cream text and cream hairline borders so it reads against imagery; a "Skip to content" link is animated in/out via `translateY` rather than display toggling (good a11y).

**Circle transitions** (`CircleTransition_circle`)
- Full brand-color discs (yellow, red, dusty-cyan) that scale up to wipe between sections — the primary motion signature.

**Inputs / dialogs**
- White input surface with a gray hairline; dialogs sit over a `rgba(0,0,0,0.3)` scrim.

**Border radius**
- `500px` / `1000px` / `50%` — everything rounds to full pills and circles. The shape language is entirely soft and bubble-like, echoing honey drops and bee bodies.

**Shadows**
- None in the system. Depth is color-and-motion, not soft shadow.

---

## 5. Layout Principles

- A scroll-driven narrative: a loader → animated bee intro → trace-your-honey journey → bestsellers → brand story → reviews → honey-gold footer.
- Sections are separated by full-bleed circle-wipe transitions in brand colors rather than hard rules, so navigation reads as a continuous, colorful pour.
- Oversized TayMakawao headlines set the vertical rhythm; bestseller products line up in a simple, generous card grid.
- The bee mark is composited from separate body/wing layers (`bee-body`, `bee-left-wing`, `bee-right-wing`) so it can animate — a recurring brand motif placed throughout the scroll.

---

## 6. Depth & Elevation

Depth comes from **color layering and motion**, not from shadow:
- **Circle transitions** — saturated brand discs (`#ffca50`, `#a0342a`, `#6aacc2`) scale over the cream ground to reveal the next section; the depth is temporal.
- **Surface ramp** — pale-cream (luminance 0.92) is the floor; honey-gold (0.80), dusty-cyan (0.61), green (0.55), brick-red (0.33), and cocoa (0.17) step down through the brand palette as section grounds.
- **Scrims** — a black alpha ramp (`--color-black-10` … `-50`) darkens media and dialog backdrops.

No `box-shadow` anywhere in the extracted system.

---

## 7. Do's and Don'ts

**Do**
- Use pale-cream `#f2ebd0` as the canvas and cocoa `#3b2722` as ink — warm, never stark white-on-black.
- Set headlines in **TayMakawao** at weight 400, large, with tight sub-unity leading; uppercase at the very top of the scale.
- Use **TayBirdie** for CTAs/labels and **AnonymousPro** for body copy.
- Deploy the four brand colors (honey-gold, brick-red, dusty-cyan, meadow-green) as full-circle section transitions and grounds.
- Round everything — `500px`/`1000px`/`50%` pills and circles, echoing honey drops.
- Animate the bee from layered body + wings; animate link underlines and the page loader.
- Commit the footer to honey-gold `#ffca50`.

**Don't**
- Don't use bold weights — the faces carry character at 400; scale up instead.
- Don't add drop shadows — use color wipes and surface steps for depth.
- Don't let the brand colors become persistent UI chrome; they belong to transitions and section grounds.
- Don't introduce sharp corners — the identity is fully rounded.
- Don't swap the bespoke display faces for a generic sans; TayMakawao/TayBirdie are the signature.

---

## 8. Responsive Behavior

A dense breakpoint set — **699/700, 959/960, 1279/1280, 1440, 1920** — drives a complete dual type scale: every role has explicit `--desktop-*` and `--mobile-*` tokens (e.g. display-1 drops from `258px` desktop to `100px` mobile; h1 from `135px` to `68px`). Notably, the detail-nav face *switches* between breakpoints — TayBirdie on desktop, TayMakawao on mobile — so the mobile menu leans harder on the display face. A `LandscapeFallback` cocoa panel (`#3b2722`) handles awkward orientations. Type holds its rustic character across sizes because the bespoke faces do the work at any scale.

---

## 9. Agent Prompt Guide

> Build a UI that matches Busy Bee Honey's design language.

Set the canvas to warm pale-cream `#f2ebd0` and all ink to cocoa-brown `#3b2722` — never stark white or black for content. Use a rustic, hand-drawn display face (here **TayMakawao**) for every heading at weight 400, sized large with tight sub-unity line-height and uppercase at the top of the scale; use a second character face (**TayBirdie**) for CTAs, nav, and small labels, and a clean reading face (**AnonymousPro**) for body copy at 12–20px. Never use bold — drive hierarchy with face and size only. Buttons are outline-only: transparent fill, cocoa text, cocoa hairline border. Round everything to full pills/circles (`border-radius: 500px`/`50%`). Reserve four saturated brand colors — honey-gold `#ffca50`, brick-red `#a0342a`, dusty-cyan `#6aacc2`, meadow-green `#6fa162` — for full-circle section transitions that scale up to wipe between sections, and as occasional section grounds; commit the footer fully to honey-gold. Add no drop shadows; build depth from color wipes and a luminance ramp through the brand palette. Include playful brand motion: a "gathering nectar" loader, a bee composited from separate body + wing layers, and link underlines that draw in. Keep the whole thing honest, folksy, and warm — heritage label, not slick SaaS.

---

*Generated by Sparkbites — extracted from live CSS analysis*
