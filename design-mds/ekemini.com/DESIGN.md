# ekemini.com — Design Language

## 1. Visual Theme & Atmosphere

ekemini.com is a personal portfolio built in Framer that communicates creative confidence through color density. Where most portfolios retreat to black-and-white minimalism, this one uses color assertively — a vivid electric blue for CTAs, a deep indigo-violet for featured work cards, and a saturated green for status/availability indicators. The white canvas grounds these without competition, letting each color land with full impact.

The design philosophy is "directness." Typography runs at slightly negative tracking. The Framer animation layer (Framer Motion) handles transitions. Every element is precisely placed — this is not a layout that breathes loosely, it is a layout that controls.

The overall atmosphere is that of a working designer or developer who knows exactly what they want to say and how to say it.

## 2. Color Palette & Roles

**Foundation**
- `#FFFFFF` — Full white page background; no tinting, no grey warmth — pure and direct
- `rgb(246, 246, 246)` — Light secondary surface for card backgrounds
- `rgb(227, 227, 227)` — Tertiary surface; slightly deeper grey for nested containers

**Brand / Action**
- `rgb(0, 102, 255)` — Electric blue; primary CTA button fill and possibly link accent. Bright, modern, high-energy.
- `rgb(84, 68, 242)` — Indigo-violet; used on featured project cards or section backgrounds. A deeper, more considered blue-purple.

**Status / Semantic**
- `rgb(0, 128, 55)` — Saturated green; availability badge or "open to work" indicator. Communicates positive status clearly.

**Text**
- `rgb(0, 0, 0)` — Primary text; pure black, no softening
- `rgb(0, 0, 238)` — Browser-default link blue on anchor elements; notable that this raw browser default is not overridden — possibly intentional for its raw, undesigned quality

**Absent:** No muted greys for secondary text, no border color beyond black, no dark mode tokens. The system is high-contrast by default.

## 3. Typography Rules

Two typefaces operate at different layers:

**Graphik Medium** — Used for body paragraphs. A geometric sans with a distinct editorial personality. At 16px / 500 weight / -0.18px tracking, it reads with precision and slight compression. The negative letter-spacing is the defining choice: text feels tightly composed, intentional.

**Inter Medium** — Used for button labels. 16px / 500 / -0.2px tracking. A neutral companion to Graphik — Inter's regularity makes it ideal for UI controls while Graphik carries the content voice.

**System sans-serif** — Body element fallback; not meaningful at the design level.

The lack of a display typeface (no editorial heading font) is notable — Framer's layout engine handles display-size text with the same Graphik stack, relying on size and weight rather than typeface personality for hierarchy.

No text transforms, no ligature features enabled. The negative tracking across both fonts is the typographic signature of this design.

## 4. Component Stylings

**CTA Button**
`rgb(0, 102, 255)` fill, white text, 16px Inter Medium, -0.2px tracking. Border-radius: 50px — fully pill-shaped. This creates maximum contrast against the sharp geometric content: the one soft shape in an otherwise angular layout. White border on the button itself.

**Project Cards**
The indigo-violet card (`rgb(84, 68, 242)`) is a featured surface — high luminance contrast against white, used to make certain projects command the eye. Standard cards use `rgb(246, 246, 246)` fill.

**Availability Badge**
`rgb(0, 128, 55)` — A small, circular or pill-shaped indicator. No text needed; the color communicates "available/active."

**Links**
Unstyled browser-default blue (`rgb(0, 0, 238)`). This is either an homage to the raw web aesthetic or simply unoveridden — in either case, it reads as a deliberate rawness.

## 5. Layout Principles

Built with Framer (generator: Framer 5235a87) and Framer Motion. Breakpoints: 810 / 1200 / 1512px — a three-tier responsive system focused on tablet, standard desktop, and wide desktop.

Framer's absolute-positioning model means layout is pixel-precise at each breakpoint rather than fluid. Components reposition rather than reflow. This gives the design more visual control but less flexibility than CSS grid/flex implementations.

No explicit padding or margin data at the body level — spacing is managed within Framer's frame-and-layer system.

## 6. Depth & Elevation

No shadows in the dataset. Elevation is achieved entirely through color contrast: the indigo-violet card (`luminance: 0.363`) reads as visually dominant against white (`luminance: 1.0`) without any shadow. The green badge (`luminance: 0.319`) similarly commands attention through saturation.

The Framer animation layer likely adds motion-based depth — components animating into view, parallax scrolling — but these are runtime effects not captured in static CSS.

Focus states use the browser default outline (`rgb(0, 95, 204) auto 1px`) — not styled.

## 7. Do's and Don'ts

**Do**
- Use `rgb(0, 102, 255)` exclusively for the primary action button — it's the single most energetic element on the page
- Apply negative letter-spacing (-0.18px to -0.2px) to all text in Graphik and Inter — this is the typographic fingerprint
- Use 50px border-radius (pill) only for buttons; maintain sharp or minimal rounding elsewhere
- Let the indigo card (`rgb(84, 68, 242)`) do the heavy visual lifting for featured content
- Keep the white background pure — no tinting

**Don't**
- Add shadows — this design reads depth through color, not shadow
- Introduce additional accent colors beyond the blue/indigo/green triad
- Override letter-spacing to zero — the compression is essential to the voice
- Use rounded cards (the 4px radius is for subtle softening only; 50px is reserved for buttons)
- Add secondary type styles; the two-font system is complete as-is

## 8. Responsive Behavior

Three breakpoints: 810px (tablet), 1200px (desktop), 1512px (wide). Framer's layout at each breakpoint is a distinct composition rather than a fluid adaptation — expect significant layout changes at each threshold, not just padding adjustments.

The pill button (50px radius) holds its shape at all sizes. The color system is invariant across breakpoints — no responsive color swaps.

## 9. Agent Prompt Guide

> Build a UI in the style of ekemini.com: pure white background, Graphik Medium for body text at 16px / -0.18px tracking, Inter Medium for buttons. Primary action color is `rgb(0, 102, 255)` with 50px pill border-radius. Featured cards use deep indigo-violet `rgb(84, 68, 242)`. Status badges use `rgb(0, 128, 55)`. No shadows — depth comes from color contrast alone. Keep letter-spacing negative throughout. Text is pure black. The design is precise, confident, and color-forward — let three strong colors do the work against a white ground.

---

*Generated by Sparkbites — extracted from live CSS analysis*
