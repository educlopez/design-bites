# wiza.co — Design System

## 1. Visual Theme & Atmosphere

Wiza is a B2B prospecting tool that has chosen trust over trendiness. The entire visual language is built on deep indigo-violet — a colour family that reads as credible, premium, and slightly mysterious, sitting comfortably between navy's authority and purple's creativity. The background is white, but the white never feels cold: warm-toned purple shadows and translucent overlays keep every surface feeling inhabited. This is not a startup trying to look like a startup; it's a product that wants to feel like infrastructure you can rely on.

The typography makes an equally deliberate statement: a custom display face (Britti Sans) for headlines, Inter for everything operational. The combination signals a company that has invested in identity without abandoning legibility.

---

## 2. Color Palette & Roles

### Brand Core (Indigo-Violet Family)
| Role | Value | Usage |
|---|---|---|
| Brand deepest | `#26114a` (rgb 38,17,74) | Body text, primary nav text, dominant brand colour |
| Brand deep | `#231645` (rgb 35,22,69) | Section heading containers |
| Brand mid | `#3e0079` (rgb 62,0,121) | Inputs, labels, focused form elements |
| Brand button | `#26114a` | Primary CTA background |
| Interactive accent | `#7e43ff` (rgb 126,67,255) | Intercom launcher, secondary CTAs |

### Surfaces & Tints
| Role | Value | Usage |
|---|---|---|
| Nav (frosted) | `rgba(255,255,255,0.4)` | Sticky navigation background |
| Card subtle | `rgba(246,247,250,0.5)` | Monitor/feature cards |
| Rating pill | `#ecedf3` | Social proof pills |
| Divider line | `#e6e2e3` / `#c1c7cf` | Section and column dividers |
| Feature block (neutral) | `rgba(129,131,152,0.14)` | Tinted feature cards |
| Feature block (magenta) | `rgba(151,1,127,0.08)` | Subtle magenta-tinted feature cards |
| Feature block (blue) | `rgba(3,72,141,0.08)` | Subtle blue-tinted feature cards |

### Text
| Role | Value | Usage |
|---|---|---|
| Primary | `#26114a` | Headings, main body |
| Secondary | `#313749` (rgb 49,39,73) | Footer, supporting copy |
| Links | `#333333` | Anchor text |
| Form text | `#3e0079` | Input values, labels |

---

## 3. Typography Rules

Wiza maintains a strict two-typeface system: **Britti Sans** for display (headings) and **Inter** for all functional text.

| Selector | Font | Size | Weight | Line Height |
|---|---|---|---|---|
| H1 | Britti Sans | 64px | 500 | 64px (1:1) |
| H2 | Britti Sans | 56px | 500 | 56px (1:1) |
| H3 | Inter | 14px | 500 | 18.2px |
| Body | Inter | 16px | 400 | 24px |
| Paragraph | Inter | 16px | 400 | 24px |
| Button | Inter | 16px | 400 | 22.4px |
| Input | Inter | 14px | 400 | 21px |

The 1:1 line-height ratio on H1/H2 (64px size, 64px line-height) is an intentional tightness — headlines stack visually like typeset titles rather than web text. No letter-spacing adjustments are made at any size, trusting Britti Sans's own optical metrics. Weights are restrained: 500 for headings and labels, 400 everywhere else.

---

## 4. Component Styling

**Forms** are the hero component. Inputs carry a layered warm-purple shadow: `rgba(47,1,151,0.04) 0 11px 10px, rgba(47,1,151,0.06) 0 6px 8px, rgba(47,1,151,0.04) 0 3px 3px, rgba(47,1,151,0.04) 0 1px 1px`. On focus, a `rgba(147,113,240,0.286) 0 0 0 1.72px` glow ring appears. This multi-layer shadow approach gives inputs a floating, elevated quality uncommon in B2B tools.

**Cards** use 8px or 10px radius and carry only soft drop shadows: `rgba(18,55,105,0.08) 0 2px 4px, rgba(18,55,105,0.04) 0 1px 1px`. The gold-tinted shadow variant (`rgba(134,98,45,0.03)`) appears on premium feature surfaces.

**Navigation** uses pill-shaped elements (up to 1280px radius for full-pill), a frosted-glass `rgba(255,255,255,0.4)` backdrop, and a 10% opacity purple divider between sections.

**Border radii** range: `6px`, `8px`, `10px`, `14px`, `16px`, `17px`, `28px`, `40px`, `1280px`.

---

## 5. Layout Principles

Layout uses fluid spacing via CSS custom properties with `clamp()` for all spacing units — spacing scales continuously between a min and max viewport width (`--site--viewport-min` / `--site--viewport-max`). The main content width is bounded by `--max-width--main` (viewport-max × 1rem). Gutters are also fluid: `clamp(1rem … 3rem)` based on viewport. Sections carry only an 8px top margin; all internal spacing is handled by component-level gaps and padding.

---

## 6. Depth & Elevation

Wiza uses warm-tinted multi-layer shadows for elevation — unusual in B2B. The indigo-purple shadow family (`rgba(18,55,105,…)`) appears on cards and nav. The gold-tinted shadow (`rgba(134,98,45,…)`) adds warmth to premium content. The frosted nav sits at the highest visual plane. Nothing uses hard edges or heavy drop shadows; the palette's depth comes from translucent layering of the brand purple family over white.

---

## 7. Do's and Don'ts

**Do:**
- Use `#26114a` as the single dominant brand colour — avoid using multiple purple shades as equal-weight primaries
- Apply multi-layer warm-purple shadow to form inputs; it is the product's signature micro-detail
- Keep headlines at 1:1 line-height for the Britti Sans display sizes
- Use tinted feature blocks (`rgba` of magenta or blue at 8%) for product grid variety without breaking colour harmony

**Don't:**
- Add saturated bright colours — there are none in this system; it lives in muted tints
- Use Britti Sans below 40px; it is a display face and loses distinction at small sizes
- Apply border-radius below 6px; the system's smallest radius is 6px
- Use Inter heavier than 500 weight; the system explicitly avoids bold type

---

## 8. Responsive Behavior

All spacing tokens are fluid `clamp()` values — the layout reflows continuously, not at hard breakpoints. The nav collapses from its desktop frosted panel form; a single breakpoint at 375px (mobile minimum) is referenced in `--site--viewport-min`. Max content width is calculated as `viewport-max × 1rem`, giving a controlled reading width on wide screens.

---

## 9. Agent Prompt Guide

> Build a light-mode B2B SaaS section in the style of wiza.co. White background, deep indigo text (`#26114a`). Use Britti Sans (or any geometric sans-serif) for headlines at 64px/500 with 1:1 line-height — no letter-spacing. Body text is Inter 16px/400. Primary CTA button: `#26114a` background, white text, 8px radius. Feature cards: 8px radius with `rgba(18,55,105,0.08) 0 2px 4px` shadow. Forms: white input with multi-layer purple shadow and a `rgba(147,113,240,0.286)` glow ring on focus. Avoid saturated accent colours — all tints should be translucent purple/indigo derivatives. Spacing is generous and fluid.

---

*Generated by Sparkbites — extracted from live CSS analysis*
