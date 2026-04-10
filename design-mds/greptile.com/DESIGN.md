# greptile.com — Design System

## 1. Visual Theme & Atmosphere

Greptile is an AI code-search tool, and its design embodies a specific tension: organic warmth meets technical precision. The background is a creamy off-white — not the clinical white of most developer tools, but a warm stone (`rgb(241, 239, 235)`) that feels like aged paper or architectural concrete. Against this tactile base, the typography is spare and precise.

The headline typeface is TasaOrbiter at 96px — massive, tightly tracked, set to negative letter-spacing that makes each heading feel like a product stamp. Body paragraphs use Geist Mono (the same monospace font Vercel uses for code), which is an unusually bold typographic choice: prose that reads with the texture of code. This blurs the line between product and editorial — the content feels like it was generated, not written.

The primary accent is Greptile green (`rgb(16, 122, 77)`): a forest green that appears on the hero heading, CTA buttons, and key surfaces. It reads as natural, trustworthy, and slightly unexpected against the warm stone — not the electric green of a startup, but something more considered.

---

## 2. Color Palette & Roles

**Backgrounds & Surfaces**
- Warm stone `rgb(241, 239, 235)` — page background, input fill
- Warm white `rgba(249, 247, 243, 0.5)` — frosted card surface (group hover panels)
- Pure white `rgba(255, 255, 255, 0.15)` — overlay highlights
- Light gray `rgb(204, 204, 204)` — dividers, input borders

**Text**
- Near-black `rgb(0, 0, 0)` — primary body text
- Dark gray `rgb(42, 42, 42)` — h2 headings, input text, interactive labels
- Mid gray `rgb(74, 74, 74)` — labels, subdued content
- Muted `rgb(106, 106, 106)` — button text, tertiary content

**Brand**
- Greptile green `rgb(16, 122, 77)` — hero h1 color, primary CTA buttons, feature surfaces

**Categorical / Tag Colors** (used on badge-style rounded links)
- Red-orange `rgb(242, 78, 30)` — alert or feature category
- Pink `rgb(247, 131, 163)` — secondary category
- Gold `rgb(204, 145, 0)` — third category
- All with 64.7% opacity variants on surfaces for a pastel badge effect

**Borders**
- `rgb(229, 229, 229)` — universal border, consistent across all interactive elements

---

## 3. Typography Rules

Three font families, three distinct roles — a rare multi-font system that actually makes typographic sense.

**TasaOrbiter** — display headings only
- h1: `96px` / `600` / `-3.84px` letter-spacing / line-height `1:1` — monolithic, uncompromising
- h2: `48px` / `600` / `-1.92px` tracking
- h3: `36px` / `600` / `-1.44px` tracking
- h5/h6: `24px` and `18px` variants with proportional negative tracking
- Rule: negative letter-spacing scales with font size — larger text, more compression

**Geist Mono** — paragraphs, inputs, and labels
- Body paragraphs: `16px` / `400` / `24px` line-height — prose that reads like code
- Inputs: `14px` / `400` / `20px`
- Labels: `12px` / `400` / uppercase transform — the only all-caps usage in the system

**Inter** — body, links, buttons, captions
- Body/links/buttons: `16px` / `400` / `24px` — clean utility sans
- Figcaptions: `14px` / `400` / `24px`

What's absent: no decorative serif, no italic emphasis, no bold body text. The bold accent is carried entirely by TasaOrbiter's size, not weight variation within Inter or Geist.

---

## 4. Component Stylings

**Hero Heading**
- TasaOrbiter at 96px in Greptile green — the primary brand moment
- Negative letter-spacing `-3.84px` gives it a compressed, typeset quality

**Category Badges / Rounded Links**
- Background: green, orange, pink, or gold (with 64.7% opacity on hover surfaces)
- Color: white text on all backgrounds
- Shape: rounded (inferred from selector `a.rounded`)
- Shadow: `rgba(0,0,0,0.06) 0 2px 12px` — gentle lift

**Input Fields**
- Background: matches page surface `rgb(241, 239, 235)` — flush, not floating
- Border: `rgb(204, 204, 204)` — defined but not heavy
- Focus: ring via box-shadow `rgb(204, 204, 204) 0 0 0 1px` — same color, just a tighter ring
- No color change on focus — the subtlety is deliberate, letting content speak

**Buttons**
- Default: transparent with dark gray text `rgb(106, 106, 106)` — restrained
- Primary CTA: green fill `rgb(16, 122, 77)` with white text

**Cards / Group Surfaces**
- Frosted warm-white at 50% opacity — layered over the stone background
- Subtle `0 1px 2px rgba(0,0,0,0.05)` shadow — almost imperceptible lift

---

## 5. Layout Principles

The layout uses a conventional centered content approach without visible edge-to-edge color blocking. All `section`, `main`, `footer` elements have `0px` padding set at the element level — layout control flows to inner containers. This suggests a component-level padding system rather than section-level.

The page has a warm, editorial reading quality: generous whitespace, content that breathes. Breakpoints at `480, 600, 640, 768, 1024, 1280, 1536px` cover the full spectrum from mobile to ultrawide.

No horizontal scrollers or slider patterns are evident — the layout reads as vertical, stacking section by section in a calm editorial flow.

---

## 6. Depth & Elevation

Depth is extremely restrained, consistent with the warm-paper aesthetic. Nothing should feel "lifted" dramatically — the design values tactility over elevation.

- **Micro shadow**: `rgba(0,0,0,0.05) 0 1px 2px` — the lowest possible elevation signal
- **Card shadow**: `rgba(0,0,0,0.06) 0 2px 12px` — slightly more present for interactive cards
- No inset shadows, no blur-heavy glass effects

Surfaces use semi-transparency against the warm stone background (`rgba(249,247,243,0.5)`) to create subtle frosting — depth through translucency rather than shadow.

---

## 7. Do's and Don'ts

**Do:**
- Use the warm stone background `rgb(241, 239, 235)` — not white, not gray-100
- Set h1 in TasaOrbiter at large scale with strong negative letter-spacing
- Use Geist Mono for paragraph copy as the brand's typographic signature
- Apply Greptile green `rgb(16, 122, 77)` to the most important heading on each page
- Keep input fields surface-flush (same background as page, not white)
- Use soft borders (`rgb(229, 229, 229)`) rather than strong dividers

**Don't:**
- Don't use Inter for headings — TasaOrbiter at large scale is the identity
- Don't add drop shadows heavier than `2px 12px` — the aesthetic is paper-flat
- Don't use pure white `#fff` as a background — it would kill the warm stone atmosphere
- Don't use color fills on interactive states — prefer subtle color shifts (`rgb(42,42,42)` → `rgb(74,74,74)`)
- Don't introduce gradients or dark mode elements — this is a purposefully light design

---

## 8. Responsive Behavior

Seven breakpoints from `480px` to `1536px` provide full coverage. The hero typography at `96px` will need significant scaling on mobile — likely down to `48–64px`. The negative letter-spacing must scale proportionally (the formula appears to be `fontSize * -0.04`).

Labels using uppercase Geist Mono at `12px` should remain legible at all widths — no further reduction. Input fields being surface-flush means no visual reflow needed for form layouts at different breakpoints. Category badges/pills are inherently flexible and should wrap naturally in flex containers.

---

## 9. Agent Prompt Guide

Use this block when prompting an AI to generate UI in the style of greptile.com:

```
Design a light AI developer tool with a warm stone background (#F1EFEB, not white). Primary text is near-black. Brand accent is forest green (#107A4D) used on the hero heading and primary CTAs. Use TasaOrbiter (or similar compressed display sans) at large scale with heavy negative letter-spacing (-0.04em rule) for headings. Body paragraphs use a monospace font like Geist Mono — prose that reads like code output. UI elements (buttons, inputs, nav) use Inter. Input fields are surface-flush with a light border (#CCC) and a minimal 1px ring focus state. Cards use 50% opacity frosted warm-white. Category tags/badges come in green, red-orange, pink, and gold. Shadows are barely present — max 2px 12px blur. No gradients, no dark backgrounds, no heavy drop shadows.
```

---

*Generated by Sparkbites — extracted from live CSS analysis*
