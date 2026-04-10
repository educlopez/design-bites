# kihealth.com — Design System

## 1. Visual Theme & Atmosphere

KI Health presents as a warm, approachable wellness brand — a deliberate departure from the clinical sterility typical of healthcare. The palette centers on a creamy off-white (`#FFFCF8`) ground with deep forest green as the primary brand expression. Accent yellows and oranges introduce warmth and optimism without veering into the garish. The typography system (Assistant, a humanist sans-serif) reinforces accessibility and friendliness. Animation tokens are unusually detailed — six duration levels from `.1s` to `3s` — signaling a brand that uses motion expressively to guide users through an intentional journey. The result feels like a premium wellness app brought to web: warm, trustworthy, alive.

---

## 2. Color Palette & Roles

| Role | Value | Notes |
|---|---|---|
| **Background / Canvas** | `#FFFCF8` — Cultured Cream | Warm off-white; the defining surface |
| **Brand / Primary** | `#003F3C` — Dark Green | Deep forest; headers, CTAs, key UI |
| **Input / Muted UI** | `#9EB4B1` — Sage Mist | Form fields, secondary borders |
| **Accent Yellow** | `#FFF7B2` — Lemon Chiffon | Highlights, callout backgrounds |
| **Accent Orange** | `#FFD79A` — Peach Gold | Warm accent; badges, highlights |
| **Error** | `#EB0000` — Red | Form validation only |
| **Header Gradient End** | `#DCFFDD00` — Transparent Mint | Fade-out on header gradient |
| **Text on Dark** | `#F1F3F9` approx — Near White | Headings/links on dark surfaces |

The palette tells a clear story: a warm, earthy wellness brand rooted in nature (forest green, cream) with optimistic accents (yellow, peach). The error red is kept purely functional. No cool greys — warmth is maintained throughout.

---

## 3. Typography Rules

| Element | Font | Weight | Notes |
|---|---|---|---|
| `body` | Assistant, sans-serif | 400 | Humanist sans; approachable, legible |
| `headings` | Assistant, sans-serif | 400 | Same family; differentiated by size, not weight |
| `bold text` | Assistant, sans-serif | 700 | Used for emphasis within copy |

A single-family system (Assistant) across all contexts. Heading weight token is 400 — hierarchy is established through size and spacing rather than weight contrast. Letter-spacing of `0.6px` is used on certain elements, adding a subtle openness. Font scale token `1.0` means no global scaling — type renders at designed sizes throughout. Clean, democratic, and accessible.

---

## 4. Component Stylings

**Buttons**
- Shadow system: vertical offset + blur radius custom properties (`--buttons-shadow-vertical-offset`, `--buttons-shadow-blur-radius`)
- Corner radius controlled by `--buttons-radius` token
- Full opacity on background and border by default (`--alpha-button-background: 1`, `--alpha-button-border: 1`)
- Slide-in animation on appearance: `slideIn var(--duration-extra-long) var(--ease-out-slow) forwards`

**Cards (Collection)**
- Corner radius: `--collection-card-corner-radius`
- Text alignment: `--collection-card-text-alignment`
- Shadow opacity: `--collection-card-shadow-opacity`

**Blog Cards**
- Shadow blur: `0.5rem`
- Distinct shadow system from collection cards

**Media / Images**
- Border: 1px at 5% opacity — near-invisible structure
- Radius: 0px — rectangular by default (overridable)
- Shadow: disabled (`--media-shadow-opacity: 0.0`)

**Badges**
- Corner radius: `--badge-corner-radius`
- Border at 10% opacity — subtle definition

**Inputs / Forms**
- Radius: `--inputs-radius`
- Border width: `--inputs-border-width`
- Input color: `#9EB4B1` (sage mist)

**Navigation / Header**
- Gradient fade from brand color to transparent mint
- `--header-sticky-height` token for sticky positioning

---

## 5. Layout Principles

- Grid system uses `--grid-desktop-horizontal-spacing: 8px` — tight column gutters
- `--grid-mobile-vertical-spacing` for vertical rhythm on mobile
- Body padding at `4rem` on sides — generous breathing room
- Max-width suggested at `1440–1500px` range
- `--page-width` and `--content-max-width-with-nav` tokens control layout bounds
- Full-width variant available via `--full-page-width`

---

## 6. Depth & Elevation

The shadow system is token-driven and multi-layered:
- **Media**: shadows disabled by default (flat cards)
- **Buttons**: configurable vertical offset + blur — subtle lift
- **Blog cards**: `0.5rem` blur — moderate card depth
- **Collection cards**: separate opacity-based shadow control
- **Popup**: `--popup-corner-radius`, `--popup-border-opacity` — modal-level elevation

Depth escalates with UI importance: flat media → button lift → card depth → modal prominence. A clear, intentional elevation scale.

---

## 7. Do's and Don'ts

**Do:**
- Use `#FFFCF8` as the default background — never pure white
- Use `#003F3C` for all primary brand expressions (CTAs, headers, key labels)
- Apply the 6-step animation duration scale for all motion (`.1s` → `3s`)
- Use `cubic-bezier(0, 0, .3, 1)` (ease-out-slow) for all UI transitions
- Keep Assistant at 400 for headings; use size, not weight, for hierarchy
- Use `#9EB4B1` only for input/form contexts

**Don't:**
- Use pure white (#FFF) as a background — it breaks the warm brand tone
- Add cold greys to the palette
- Override media radius to non-zero without a strong reason (flat is default)
- Mix in a second typeface — Assistant handles everything
- Use the error red (#EB0000) outside of form validation

---

## 8. Responsive Behavior

- Desktop grid: 8px horizontal spacing
- Mobile: vertical spacing token (`--grid-mobile-vertical-spacing`)
- Content max-width: ~1440–1500px with generous side padding (4rem desktop)
- Navigation height collapses via `--header-sticky-height` token
- The `--media-padding` token (currently `px` — likely 0) suggests full-bleed images on mobile

---

## 9. Agent Prompt Guide

**Quick color reference:**
- Canvas: `#FFFCF8` warm cream
- Brand: `#003F3C` forest green
- Sage input: `#9EB4B1`
- Accent yellow: `#FFF7B2`
- Accent peach: `#FFD79A`
- Error: `#EB0000`

**Prompt to recreate this style:**
> "Design a wellness brand website in the style of kihealth.com: warm cream background (#FFFCF8), deep forest green (#003F3C) for primary brand elements, humanist sans-serif (Assistant 400) throughout, subtle card shadows, optimistic yellow and peach accents. Atmosphere: approachable, premium wellness, warm and trustworthy."

**Prompt for a component:**
> "Create a product card: cream background, forest green heading in Assistant, peach or yellow accent badge, 0.5rem shadow blur, rectangular image (no radius), 8px grid gutter. Slide in on load using ease-out-slow."

*Generated by Sparkbites — extracted from live CSS analysis*
