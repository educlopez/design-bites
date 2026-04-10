# jakub.kr — Design Language

## 1. Visual Theme & Atmosphere

jakub.kr is a personal site that achieves what few portfolios manage: genuine quietude. Built with Next.js and Tailwind CSS, it forgoes the usual portfolio gestures — no hero text at 120px, no dark mode drama, no animated entrance sequences. Instead: off-white canvas, Inter Variable at a consistent 16px throughout, wide editorial margins, and a shadow system so delicate it could be dismissed as nothing. The design communicates trust and confidence through what it removes. The use of `lab()` color space for text and borders signals a developer who thinks precisely about perceptual uniformity. This is the portfolio of someone who has solved the problem of taste by refusing to perform it.

## 2. Color Palette & Roles

| Role | Value | Usage |
|---|---|---|
| Background | `rgb(252, 252, 252)` — off-white | Body, main, inputs |
| Primary text | `lab(12.304 0 0)` ≈ `#1e1e1e` — near-black | All body copy |
| Button background | `lab(12.304 0 0)` ≈ `#1e1e1e` — near-black | CTA buttons |
| Button text | `lab(98.956 0 0)` ≈ `#fafafa` — near-white | Button labels |
| Border default | `lab(96.752 0 0)` ≈ `#f3f3f3` — barely-there | Dividers, card outlines |
| Border mid | `lab(91.996 0 0)` ≈ `#e8e8e8` — input rest | Input border |
| Border strong | `lab(75.872 0 0)` ≈ `#bfbfbf` — input focus | Focused input |
| Outline / focus | `lab(42.348 0 0)` ≈ `#636363` — mid gray | Focus ring |

The entire palette is achromatic — no hue anywhere. Color values are expressed in `lab()` space, which ensures perceptually equal steps between gray levels. The gradient from near-black text to barely-visible borders is tuned with perceptual precision, not hex eyeballing.

**What's absent:** No accent colors, no brand hues, no dark mode surfaces, no gradients.

## 3. Typography Rules

**Inter Variable** (with `cv01` feature enabled) is the only typeface. The `cv01` OpenType feature activates alternate letterforms in Inter — specifically a one-story lowercase 'a' — giving the text a slightly warmer, less mechanical character. Every typographic element uses the same 16px size; hierarchy is created entirely through weight (400 vs. 500).

| Element | Family | Size | Weight | Line-height | Feature |
|---|---|---|---|---|---|
| Body | Inter Variable | 16px | 400 | 24px (1.5) | `cv01` |
| Paragraphs | Inter Variable | 16px | 400 | 26px (1.625) | `cv01` |
| h2 / Labels | Inter Variable | 16px | 500 | 26px (1.625) | `cv01` |
| Links / a | Inter Variable | 16px | 500 | 26px (1.625) | `cv01` |
| Buttons | Inter Variable | 16px | 500 | 26px (1.625) | `cv01` |
| Inputs | Inter Variable | 16px | 400 | 26px (1.625) | `cv01` |

The zero variance in font size is the design statement. Everything is 16px; nothing is large. Reading is linear, not hierarchical in the visual-impact sense. The slightly higher line-height on paragraphs (26px vs. 24px body) adds 2px of grace to running text.

**What's absent:** No display type, no letter-spacing, no text transforms, no italic usage.

## 4. Component Styling

- **Buttons:** Near-black background (`lab(12.304)`) with near-white text — filled, high-contrast, no border-radius decoration beyond the component's `8px`–`16px` radius range.
- **Border-radius scale:** 8px, 12px, 14px, 16px, and a single pill-radius (`3.35e+07px`) — rounded components coexist with the flat typographic aesthetic.
- **Inputs:** White fill, barely-visible border at rest (`lab(91.996)`), darkening to `lab(75.872)` on focus — no colored focus ring, just a darker gray.
- **Cards / shadows:** A multi-layer shadow: `0 0 0 1px rgba(0,0,0,0.06)` (outline) + `0 1px 2px -1px rgba(0,0,0,0.06)` (lift) + `0 2px 4px 0 rgba(0,0,0,0.04)` (depth). Combined opacity stays under 6% — essentially invisible until the eye specifically looks for elevation.
- **No surface colors** beyond the off-white base — no panels, no tinted backgrounds.

## 5. Layout Principles

- Wide editorial margins: `main` has `margin: 0 294px` on desktop — a very wide gutter that creates a narrow central column.
- Vertical rhythm: `main` top padding 96px, sections stacked with `margin-top: 128px` — generous, unhurried scroll spacing.
- No breakpoints detected — the design appears to handle responsive behavior through Tailwind utility classes rather than explicit media query tokens.
- Single-column content strip centered in a wide viewport — no grid, no columns, pure linear reading.

## 6. Depth & Elevation

The shadow system is the most sophisticated element of this design: a three-layer compound shadow where each layer is under 6% opacity. Together they create a card outline that is perceived rather than seen — the brain registers "slightly elevated surface" without consciously registering a shadow. This technique avoids the heaviness of visible box-shadows while still providing spatial clarity.

Input focus reinforces this approach: border darkens from `lab(91.996)` to `lab(75.872)` — a perceptually uniform step without using color.

## 7. Do's and Don'ts

**Do:**
- Set Inter Variable with `font-feature-settings: "cv01"` — the alternate 'a' is part of the character.
- Use `lab()` color values or their perceptually calibrated hex equivalents for border steps.
- Keep the shadow layers at or below 6% opacity — visibility kills the effect.
- Respect the `294px` horizontal margins; the narrow column is intentional editorial discipline.
- Use only weight (400/500) to distinguish hierarchy — never size.

**Don't:**
- Add accent colors or brand hues — the achromatic palette is the identity.
- Increase font sizes above 16px for headings; the flat type hierarchy is the statement.
- Replace `lab()` borders with pure `#eee` equivalents — perceptual uniformity matters here.
- Reduce the 128px section margins — the breathing room is structural.

## 8. Responsive Behavior

No breakpoint tokens were detected, meaning responsive behavior is entirely in Tailwind utility classes at the component level. The `294px` horizontal margin almost certainly collapses to a narrower value on tablet and a padding on mobile. The 96px top padding likely steps down. The typographic system requires no adjustment — 16px throughout reads well at any width without scaling.

## 9. Agent Prompt Guide

> Build a minimal personal portfolio in the style of jakub.kr: off-white background `rgb(252,252,252)`, near-black text in `lab(12.304 0 0)` (≈`#1e1e1e`). Single typeface: Inter Variable at 16px throughout — no display sizes, no uppercase. Weight 400 for body, 500 for labels and actions. Enable `font-feature-settings: "cv01"`. Borders in barely-visible `lab(91.996 0 0)` (≈`#e8e8e8`). Card shadow: `0 0 0 1px rgba(0,0,0,0.06), 0 1px 2px -1px rgba(0,0,0,0.06), 0 2px 4px 0 rgba(0,0,0,0.04)`. Main content column with `margin: 0 294px` and `padding-top: 96px`. No color accents anywhere.

---

*Generated by Sparkbites — extracted from live CSS analysis*
