# kite.video — Design System

## 1. Visual Theme & Atmosphere

Kite is a screen recording product with a design language that mirrors the tools it serves: precise, dark, and deeply technical. Built on Chakra UI, the site inhabits a dark-mode world of near-blacks and muted navy surfaces, with Inter as the sole typeface — tight, feature-rich, and unapologetically digital. The hero typography is pushed to its limits: 60px at -3px letter-spacing, lnum and salt OpenType features engaged — this is type set by someone who cares. The interaction model is glass-like: translucent borders in graduated white opacity layers, hover states that barely reveal themselves (7.5% white fill). The atmosphere is that of a polished developer tool — capable, calm, and confidently understated.

---

## 2. Color Palette & Roles

| Role | Value | Notes |
|---|---|---|
| **Page Background** | `rgb(22, 22, 29)` approx | Deep dark — near-black with a cool undertone |
| **Primary Text** | `rgb(255, 255, 255)` — White | All text on dark |
| **Surfaces / Cards** | Dark navy variants | Layered dark blues/blacks |
| **Button Border (bottom)** | `rgba(255,255,255,0.24)` | Deepest border — creates a 3-layer glass edge |
| **Button Border (mid)** | `rgba(255,255,255,0.16)` | Mid-layer border |
| **Button Border (top)** | `rgba(255,255,255,0.08)` | Lightest border — near-invisible top edge |
| **Button Hover Fill** | `rgba(255,255,255,0.075)` | Barely-there fill on hover |
| **Section Backgrounds** | Various dark neutrals | Extracted from Chakra surface variants |

The color system is monochromatic dark with a glass/translucency layer system. The graduated button borders (`0.08` → `0.16` → `0.24` white opacity) create a subtle 3D depth effect that's become a hallmark of premium dark SaaS design. No accent color is used for interactive elements — white opacity alone carries all UI states.

---

## 3. Typography Rules

| Element | Font | Size | Weight | Line Height | Letter Spacing | Features |
|---|---|---|---|---|---|---|
| `h2` (hero) | Inter | 60px | 700 | 66px (1.1) | -3px | `lnum`, `pnum`, `salt` |
| `body` | Inter | 16px | 400 | normal | normal | — |

Inter is used at both extremes of its range: maximal display (60px, bold, tightly tracked) and neutral body (16px, regular). The OpenType features `lnum` (lining numerals), `pnum` (proportional numerals), and `salt` (stylistic alternates) are activated on the hero — making the display text measurably more refined than default Inter rendering. The gap between hero and body creates a dramatic scale contrast that draws the eye immediately. No serif, no display font — Inter handles everything.

---

## 4. Component Stylings

**Buttons (Chakra UI)**
- Transparent background by default
- White text
- Three-layer border: `rgba(255,255,255,0.08/0.16/0.24)` top/mid/bottom
- Hover: `rgba(255,255,255,0.075)` fill — glass shimmer effect
- No box shadow in default/hover state
- Solid 2px focus outline (transparent by default — accessible override needed)

**Navigation / Header**
- Transparent background
- White text

**Inputs**
- Chakra UI input system (dark-mode variant)
- White text on dark backgrounds

**Slider (Chakra)**
- `chakra-slider__thumb` detected — custom media/timeline control
- Implies a product demo or interactive timeline on page

**Links**
- White text, transparent background
- Consistent with button system — no underlines in default state

---

## 5. Layout Principles

- Body: zero padding and margin — full-bleed sections
- No breakpoints extracted — Chakra UI handles responsive internally via its theme system
- `--chakra-vh: 100vh` — full-viewport height sections
- Section-based layout: full-width alternating content blocks
- Gap management delegated to Chakra's spacing system (not custom tokens)
- The `section` element is the primary layout container

---

## 6. Depth & Elevation

No traditional box shadows. Depth is achieved through:
1. **Layered translucent borders** on buttons (graduated white opacity)
2. **Dark surface stacking** — sections at slightly different dark values
3. **Background blur** (likely on modals/popovers — Chakra's default glass behavior)

The system avoids cast shadows entirely, preferring a light-bending glass metaphor. Surfaces feel like dark glass panels rather than paper cards.

---

## 7. Do's and Don'ts

**Do:**
- Use Inter with OpenType features (`lnum`, `pnum`, `salt`) for display text
- Apply -3px letter-spacing to hero/display headings
- Use three-layer graduated white opacity for button borders
- Keep hover states subtle — 7.5% white fill is the ceiling
- Build full-viewport sections with Chakra's VH token
- Maintain dark, cool-neutral backgrounds throughout

**Don't:**
- Add a brand accent color — white opacity is the entire interactive language
- Use positive letter-spacing (it would break the tight, technical feel)
- Add drop shadows — this is a glass system, not a material one
- Mix in warm neutrals or cream tones — the atmosphere is cool and digital
- Use Inter at regular weight for headings — 700 is the display weight

---

## 8. Responsive Behavior

No explicit breakpoints extracted. Chakra UI's built-in responsive props and theme breakpoints handle all responsive behavior (typically: `sm:480px`, `md:768px`, `lg:992px`, `xl:1280px`). The single-VH section layout collapses gracefully to stacked mobile sections. The hero type (60px, -3px) will need responsive scaling on mobile — likely dropping to 32–40px with adjusted tracking. The Chakra slider/timeline component is the most complex responsive challenge.

---

## 9. Agent Prompt Guide

**Quick color reference:**
- Background: `rgb(22, 22, 29)` deep dark navy
- Text: `#ffffff` white
- Button borders: `rgba(255,255,255,0.08/0.16/0.24)` graduated
- Button hover: `rgba(255,255,255,0.075)`

**Prompt to recreate this style:**
> "Design a dark SaaS product landing page in the style of kite.video: deep near-black background, white Inter text, hero heading at 60px bold with -3px letter-spacing and OpenType lnum/pnum/salt features, glass-style buttons with three-layer graduated white opacity borders, no accent colors, Chakra UI components. Atmosphere: precision tool, dark studio, glass surfaces."

**Prompt for a component:**
> "Create a CTA button: transparent background, white label in Inter 700, border with three opacity layers (top: rgba(255,255,255,0.08), mid: rgba(255,255,255,0.16), bottom: rgba(255,255,255,0.24)), hover fill rgba(255,255,255,0.075). No shadow, no radius beyond Chakra default."

*Generated by Sparkbites — extracted from live CSS analysis*
