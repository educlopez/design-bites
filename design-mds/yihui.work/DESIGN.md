# yihui.work — Design System

## 1. Visual Theme & Atmosphere

Yihui.work is a product designer's portfolio that manages to feel both systematic and personal. The visual language is calm blue-grey — a palette extracted from digital interfaces rather than nature — with electric blue (`#1178ff`) as the single accent that carries all interactive weight. White background, generous vertical padding, and a carefully named custom property system reveal a designer who has thought hard about their tokens before writing a single component. The result feels like a design tool itself: precise, considered, subtly interactive.

The chip/tag component system — the site's primary navigation device — demonstrates the philosophy concisely: muted grey at rest, blue-tinted on hover, blue-ringed on focus. No animation, just state changes that feel inevitable.

---

## 2. Color Palette & Roles

### Foundation
| Token | Value | Role |
|---|---|---|
| `--dom-bg` | `#ffffff` | Page canvas |
| `--text-primary` | `#2f3540` | Primary text, body, labels |
| `--text-secondary` | `rgba(47,53,64,0.6)` | Supporting text, metadata |
| `--text-muted` | `rgba(47,53,64,0.5)` | Tertiary, captions |

### Blue Accent System
| Token | Value | Role |
|---|---|---|
| `--accent-blue` | `#1178ff` | Primary interactive colour |
| `--accent-blue-weak` | `rgba(17,120,255,0.2)` | Chip hover background |
| `--accent-blue-soft` | `rgba(17,120,255,0.36)` | Medium emphasis states |
| `--accent-blue-subtle` | `rgba(17,120,255,0.16)` | Very light tint fills |
| `--accent-blue-strong` | `rgba(17,120,255,0.8)` | Near-full opacity accent |
| `--accent-blue-border` | `rgba(17,120,255,0.5)` | Chip hover border |

### UI Chrome
| Token | Value | Role |
|---|---|---|
| `--chip-selected` | `#dee8f6` | Selected chip background |
| `--chip-bg` | `#f4f5f6` | Unselected chip background |
| `--chip-border-default` | `rgba(0,0,0,0.2)` | Chip resting border |
| `--chip-highlight` | `rgba(17,120,255,0.2)` | Chip hover fill |
| `--chip-border-hover` | `rgba(17,120,255,0.6)` | Chip hover border |
| `--control-bg` | `rgba(0,0,0,0.05)` | Control/button backgrounds |
| `--ring` | `rgba(0,0,0,0.12)` | Focus rings |
| `--fill` | `rgba(0,0,0,0.02)` | Subtle surface fills |

Note: Raw link colour is browser-default `rgb(0,0,238)` — footnote references intentionally use the web's native hyperlink colour as a typographic device.

---

## 3. Typography Rules

SuisseIntl is the sole typeface — a refined grotesque with Swiss neutrality and slight warmth. The system uses a single weight (400) with no display variant, meaning all hierarchy comes from size and spacing.

| Selector | Font | Size | Weight | Line Height |
|---|---|---|---|---|
| Body | SuisseIntl | 16px | 400 | normal |
| Paragraph | SuisseIntl | 16px | 400 | 25.6px (1.6) |
| Anchor | SuisseIntl | 16px | 400 | normal |
| Button/chip | SuisseIntl | 16px | 400 | 22.4px (1.4) |

Everything is 16px/400 — radical size uniformity that places all emphasis on layout, colour, and spacing rather than typographic contrast. The 1.6 line-height on paragraphs creates a generous, readable essay-like quality. No letter-spacing overrides. No uppercase. No bold.

---

## 4. Component Styling

**Chips** are the signature component. They come in two states:
- **Selected**: `#dee8f6` background, no border, `#2f3540` text
- **Unselected**: `#f4f5f6` background, `rgba(0,0,0,0.2)` border
- **Hover**: `rgba(17,120,255,0.2)` background, `rgba(17,120,255,0.6)` border
- **Focus**: `rgba(17,120,255,0.5) 0 0 0 2px` box shadow ring

**Buttons** use `#dee8f6` (same as selected chip) — chips and buttons share a visual vocabulary, unifying navigation and actions.

**Border radii**: `8px` and `10px` — close enough to feel like a single rounded family, distinct enough for visual variety between component types.

**Main layout padding**: `96px 24px 120px` — very generous top and bottom padding creates a floaty, calm reading environment. Sections use `gap: 12px`.

---

## 5. Layout Principles

Content lives in a narrow centered column with `24px` horizontal padding and `96px / 120px` top/bottom breathing room. This tall vertical padding is the single most distinctive layout decision — it makes the page feel unhurried, the opposite of content-maximising. Section gaps of `12px` keep related content close while the 96px outer padding separates the page from the viewport edges. No grid or multi-column layout is apparent at the CSS level.

---

## 6. Depth & Elevation

Shadows are entirely absent — `--ring: rgba(0,0,0,0.12)` is defined but used only for focus rings, not elevation. The depth model relies entirely on background colour contrast (white canvas vs. `#f4f5f6` chips vs. `#dee8f6` selected chips). Elevation is flat by design. The only "raised" experience comes from the focus ring appearing on interaction, giving a 2px blue glow to the active element.

---

## 7. Do's and Don'ts

**Do:**
- Use the full blue opacity scale (`--accent-blue-weak` through `--accent-blue-strong`) for graduated interactive states — the token names describe their hierarchy
- Apply generous vertical padding (96px+) to the main container; the spaciousness is integral to the identity
- Use `#dee8f6` for both selected chips and primary buttons; the shared colour unifies the UI vocabulary
- Let footnote/reference links retain browser-default blue (`rgb(0,0,238)`) — it is intentional

**Don't:**
- Add font weights above 400 — the entire type system is weight-uniform
- Introduce shadows for card elevation — this system has no shadow model
- Use border-radius values outside `8px`/`10px` for primary components
- Add background colours to section or main elements; white canvas is absolute

---

## 8. Responsive Behavior

No explicit breakpoint tokens were found in the CSS snapshot. Based on the `24px` horizontal padding and narrow column layout, the design likely remains single-column across all breakpoints, with the main change being a reduction in the `96px` vertical padding on mobile. The chip grid with `gap: 12px` would wrap naturally on narrow viewports.

---

## 9. Agent Prompt Guide

> Build a portfolio page in the style of yihui.work. White background, `#2f3540` primary text. Single font: SuisseIntl (or Inter as substitute) at 16px / 400 weight. Paragraphs at 1.6 line-height. Generous outer padding: `96px 24px 120px`. One accent colour: `#1178ff`. Navigation uses pill-shaped chips — resting state `#f4f5f6` with `rgba(0,0,0,0.2)` border; hover state `rgba(17,120,255,0.2)` fill with `rgba(17,120,255,0.6)` border; selected state `#dee8f6`. Focus rings: `rgba(17,120,255,0.5) 0 0 0 2px`. No shadows. No bold weights. Sections at `gap: 12px`. Let inline footnote links use native browser blue.

---

*Generated by Sparkbites — extracted from live CSS analysis*
