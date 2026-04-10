# oem.care — Design System

## 1. Visual Theme & Atmosphere

oem.care presents itself as a premium, minimal healthcare or wellness brand with a distinctly editorial aesthetic. The design philosophy is reduction: near-pure black (`#040404`) as the canvas, white as the counter-surface, no color accents. Two custom typefaces — Diatype and Tiny — do the heavy lifting. This is not a corporate health site buried in blue gradients and stock photography; it reads more like a boutique fashion or beauty brand that happens to serve a wellness audience. The tone is calm, precise, and slightly austere. Every element earns its space. Decoration is not in the vocabulary.

## 2. Color Palette & Roles

| Role | Value | Usage |
|---|---|---|
| Foreground / Text | `#040404` | Nearly-black primary text and icon color (`--rc-color`) |
| Background Active | `#efefef` | Active/selected state background (`--rc-active-bg`) |
| Active Text | `#000000` | Text on active elements (`--rc-active-color`) |
| Pure Black | `#000000` | Button fill, star icons, primary interactive elements |
| Button Outline | `rgba(0, 0, 0, 0.5)` | Outlined button border with softened opacity |
| Button Text | `#ffffff` | Text on filled black buttons |
| Border | `rgba(0, 0, 0, 0.08)` | Card and input borders — extremely subtle, nearly invisible |
| Utility Gray | `#637381` | Outline / secondary UI elements |

**What's absent:** No hue anywhere. No brand blue, no accent orange, no success green. The entire chromatic vocabulary is black and white with opacity-modulated grays. This is a deliberate rejection of conventional healthcare color conventions (the "medical blue"). The `#040404` near-black (rather than pure `#000000`) for body text adds a microscopic warmth that prevents harshness.

## 3. Typography Rules

Two custom typefaces anchor the identity:

- **Diatype** (`"diatype", sans-serif`) — A neo-grotesque, geometric sans by ABC Dinamo. Primary UI and body typeface. Rational, contemporary, authoritative.
- **Tiny** (`"tiny", sans-serif`) — A micro typeface for labels, captions, or decorative fine print. Its presence signals attention to typographic detail at every scale.
- **System fallback:** `ui-sans-serif, system-ui, sans-serif` with emoji sets — used where custom fonts haven't loaded or in utility contexts.

| Selector | Family | Size | Notes |
|---|---|---|---|
| `body` | System UI fallback | 16px | Default before custom fonts resolve |
| UI / body | Diatype | — | Primary after font load |
| Captions / labels | Tiny | — | Fine detail layer |
| `input` | ui-sans-serif | 16px | Form fields use system stack |

**Letter-spacing:** Normal throughout. No tracking adjustments — Diatype's own metrics are considered sufficient. **Text transform:** None by default.

## 4. Component Stylings

- **Buttons (filled):** Black `#000000` background, white `#fff` text. Outline variant uses `rgba(0,0,0,0.5)` border. Both styles are stark and confident.
- **Buttons (outlined):** Transparent fill, `#00000080` border. Star icon in `#000000`. Juniper review integration (`--junip*` variables) uses the same black/white system.
- **Form inputs:** 16px system font, standard padding. The border-radius and padding weren't extracted explicitly — expect minimal styling consistent with the brand.
- **Announcement overlay:** Custom `announcements-overlay__item` and `announcement-dot` components suggest a banner/notification system — likely a top bar with minimal styling.
- **Header:** A `header` element with defined spacing; sticky or fixed treatment likely given the `--vh: 8px` variable (viewport-height tracking).

## 5. Layout Principles

- **Base unit:** 8px (inferred from standard spacing; `--vh: 8px` is a JS-injected viewport height unit for mobile Safari fixes).
- **Spacing values observed:** 5px, 8px, 13px, 15px, 16px, 24px. Tight increments suggesting an 8px grid with 4px half-steps.
- **Content width:** Not explicitly tokenized — likely a max-width centered container.
- **Whitespace philosophy:** Luxurious. A brand of this restraint demands air between elements. The color system's near-invisibility means whitespace carries the entire layout rhythm.

## 6. Depth & Elevation

- **Border:** `rgba(0, 0, 0, 0.08)` — At 8% opacity, card and input borders are barely perceptible, more texture than structure.
- **No box-shadows detected.** Elevation is non-existent as a concept — surfaces sit flat on the page. The design's depth comes from contrast between black type and white surface, not light simulation.
- **`--rc-active-bg: #efefef`** provides the only elevation-adjacent treatment: a light gray fill for selected/active states.

## 7. Do's and Don'ts

**Do:**
- Use Diatype for all primary text — it's the voice of the brand
- Keep buttons in pure black-on-white or white-on-black — no color variants
- Use `rgba(0,0,0,0.08)` for borders — never a heavier stroke
- Let whitespace be the primary design element

**Don't:**
- Don't add color accents — not even a subtle brand blue or green
- Don't use Tiny at sizes above 11–12px; it's a detail typeface
- Don't use shadows or elevation — keep surfaces flat
- Don't deviate from the near-black `#040404` for body text; it's warmer than `#000000` by design

## 8. Responsive Behavior

The `--vh: 8px` variable indicates JavaScript-assisted viewport height calculation for mobile Safari's dynamic toolbar. This is a production-grade solution to the classic mobile viewport unit bug. Typography uses `px` units suggesting a fixed-size approach; the 16px body on inputs satisfies iOS's minimum to prevent auto-zoom. The system-UI fallback ensures text remains legible even on devices where Diatype hasn't loaded.

## 9. Agent Prompt Guide

**Quick reference:**
- Text: `#040404` | Background: `#ffffff`
- Active surface: `#efefef`
- Border: `rgba(0,0,0,0.08)`
- Primary font: Diatype (neo-grotesque), fallback system-ui
- Detail font: Tiny (micro captions)
- Buttons: `#000000` filled / `rgba(0,0,0,0.5)` outlined

**Prompt starters:**
- *"Ultra-minimal wellness brand: near-black `#040404` text on white, Diatype typeface, zero color accents, flat surfaces, `rgba(0,0,0,0.08)` borders."*
- *"Editorial health brand aesthetic: black-and-white only, custom Diatype sans-serif, micro Tiny typeface for labels, stark button styles, no shadows."*

---

*Generated by Sparkbites — extracted from live CSS analysis*
