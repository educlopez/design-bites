# dupe.com — Design Language

## 1. Visual Theme & Atmosphere

Dupe.com presents itself as a modern consumer product — polished, approachable, and with a single bold brand identity anchored in electric blue. The base is an off-white canvas (`#FAFAFA`) that reads softer than pure white, giving the interface a gentle warmth before any color lands. Against this neutral ground, a vivid cyan-teal blur element (`rgba(138, 242, 255, 0.6)`) floats behind hero content, creating the impression of ambient light or refracted glass — a technique common in contemporary SaaS and fintech design.

The overall mood is "confident utility with a consumer face": Inter for legibility, a single strong action color, and generous whitespace. It's approachable but not playful, modern but not experimental.

## 2. Color Palette & Roles

**Backgrounds**
- `#FAFAFA` — Page body; slightly warm off-white, avoids clinical harshness
- `#FFFFFF` — Main content area; elevated one step above the body
- `rgba(0, 0, 0, 0)` — Transparent overlays (footer, textarea)

**Text**
- `rgb(24, 29, 39)` — Primary body text; near-black with a slight cool blue cast, never pure black
- `rgba(0, 0, 0, 0.8)` — Secondary/input text; 80% black for de-emphasis
- `rgb(0, 0, 0)` — High-contrast contexts (main content)

**Brand / Action**
- `rgb(0, 135, 224)` — Primary CTA blue; strong, accessible, unmistakable. Used on primary buttons and links.

**Ambient / Decorative**
- `rgba(138, 242, 255, 0.6)` — Cyan glow blur; decorative background element only, never on interactive components

**Borders & Dividers**
- `rgb(233, 234, 235)` — Universal border; cool light grey throughout

Notably absent: no secondary action color, no warning/success semantic colors in the surface layer, no dark mode tokens.

## 3. Typography Rules

Inter is the sole typeface — loaded as `Inter` with `"Inter Fallback"` and the full `ui-sans-serif` system chain as backup. This is the definitive contemporary neutral sans-serif choice: readable at any size, invisible as a stylistic statement.

**Scale**
| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| H3 | 24px | 700 | 30px |
| Body | 16px | 400 | 24px |
| H1* | 16px | 400 | 24px |

*H1 renders at body size — a pattern where the semantic heading level is set in markup but visual differentiation is achieved through layout, not type size. The real hero text is likely a styled `<p>` or `<div>`.

Headings use weight 700 (bold), body uses 400 — a clean binary split. No italic, no letter-spacing adjustments, no text-transform. The typographic system's restraint lets layout carry visual hierarchy.

## 4. Component Stylings

**Primary Button**
`rgb(0, 135, 224)` fill, white text, no border. Shadow: `rgba(0, 0, 0, 0.1) 0px 10px 15px -3px` — a floating elevation effect that lifts the button off the surface. Focus state adds `rgba(0, 80, 203, 0.5)` ring.

**Input / Textarea**
Transparent background, `rgb(233, 234, 235)` border, `rgba(0, 0, 0, 0.8)` text. Inset shadow: `rgba(0, 0, 0, 0.05) 0px 1px 0px 0px inset` — a hairline top shadow that mimics a pressed/inset feel. No background fill reinforces a lightweight, open feel.

**Cards**
White surface on off-white body creates subtle card lift without any shadow being needed. The body-to-surface luminance difference (0.961 → 1.0) does the elevation work invisibly.

**Blur Decoration**
The cyan `blur-[50px]` div is a purely decorative layer — absolutely positioned, pointer-events none, used as ambient light behind hero content.

## 5. Layout Principles

Built on Next.js with Tailwind CSS. Breakpoints: 1000 / 1200 / 1600px (a tighter, fewer-breakpoint system than default Tailwind, suggesting a custom configuration).

The footer uses `256px 64px 600px` padding — the extreme bottom padding (600px) is a spacing technique to push content above a fixed or sticky bottom element, or to create a long scroll before a secondary section appears. Main and section elements have zero padding, suggesting all spacing is handled by inner container divs.

Layout is content-driven flex/grid at the component level, with no declared body max-width — full bleed sections with inner constrained columns.

## 6. Depth & Elevation

Two-level shadow system:

**Surface elevation (cards/containers):**
`rgba(0, 0, 0, 0.05) 0px 25px 50px -12px inset` — a deep inset shadow that creates a subtle bowl/concave feel on container surfaces.

**Button elevation:**
`rgba(0, 0, 0, 0.1) 0px 10px 15px -3px, rgba(0, 0, 0, 0.1) 0px 4px 6px -4px` — standard floating card shadow, applied to the primary CTA button to lift it above the page plane.

The background-to-main color shift (`#FAFAFA` → `#FFFFFF`) also functions as implicit elevation — the main canvas appears one step "higher" than the body without any shadow.

## 7. Do's and Don'ts

**Do**
- Use `rgb(0, 135, 224)` as the single action color — do not introduce a second CTA color
- Keep body text at `rgb(24, 29, 39)`, not pure black — the slight blue cast is intentional
- Use `rgba(138, 242, 255, 0.6)` only as a blurred decorative background element, never on interactive elements
- Apply the floating button shadow to elevate primary CTAs
- Use `#FAFAFA` for page body, `#FFFFFF` for card/main content areas

**Don't**
- Use border-radius extremes — the design favors clean, minimal rounding
- Add secondary accent colors; the cyan is ambient, not semantic
- Apply the inset shadow effect to buttons; it belongs to containers only
- Make Inter bold (700) except for headings — body at 400 is intentional

## 8. Responsive Behavior

Three primary breakpoints: 1000px, 1200px, 1600px. This smaller breakpoint set suggests a layout that adapts in fewer, larger jumps — fewer micro-adjustments, more definitive reflows. The extreme footer padding (600px) likely collapses at mobile breakpoints.

No mobile-specific type scaling detected — Inter's neutrality means sizes hold well across screen widths without adjustment. The 16px base body size is the mobile-safe default.

## 9. Agent Prompt Guide

> Build a UI in the style of dupe.com: off-white body (`#FAFAFA`), white main content canvas, Inter typeface, primary action color `rgb(0, 135, 224)` on buttons with a floating drop shadow. Body text is `rgb(24, 29, 39)`. Borders are `rgb(233, 234, 235)`. Add a blurred cyan orb (`rgba(138, 242, 255, 0.6)`) behind hero content as ambient decoration. Heading weight is 700, body is 400. No secondary action colors. Keep the palette minimal: off-white, white, one blue, one ambient cyan. Clean, modern, consumer-product feel.

---

*Generated by Sparkbites — extracted from live CSS analysis*
