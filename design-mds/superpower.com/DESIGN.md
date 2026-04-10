# superpower.com — Design System

## 1. Visual Theme & Atmosphere

Superpower positions itself at the intersection of health technology and consumer aspiration — and the design reflects exactly that tension. The base is clinical white with a near-black zinc text system, but the accent is Vermillion: a warm, living orange (`#fc5f2b`) that reads as biological rather than digital. This is not a startup orange; it's the color of effort, blood, and metabolic heat. Combined with Nb International Pro — a typeface used extensively in editorial and luxury branding — the result feels premium, body-forward, and quietly urgent.

The layout is Webflow-built with GSAP animations; motion is core to the experience but the design tokens themselves are carefully systematized with a full semantic token layer.

## 2. Color Palette & Roles

**Brand / Accent — Vermillion**
| Token | Value | Usage |
|---|---|---|
| `--_base-color-brand--vermillion-900` | `#fc5f2b` | Primary CTA, `--orange`, link accent |
| `--_base-color-brand--vermillion-500` | `#fdba74` | Soft orange tint |
| `--_base-color-brand--vermillion-300` | `#fed7aa` | Light peach tint |
| `--_base-color-brand--vermillion-100` | `#ffedd5` | Warm background wash |
| `--_base-color-brand--vermillion-50` | `#fff6ea` | Barely-there warm white |

**Zinc — Neutral System**
| Token | Value | Usage |
|---|---|---|
| `--zinc-900` / `--black` | `#18181b` | Body text, primary surfaces |
| `--zinc-700` | `#3f3f46` | Dark secondary text |
| `--zinc-500` | `#71717a` | Secondary/icon text |
| `--zinc-400` | `#a1a1aa` | Disabled states, borders |
| `--zinc-200` | `#e4e4e7` | Dividers, borders |
| `--zinc-100` | `#f4f4f5` | Tertiary background |
| `--white` | `#ffffff` | Canvas, primary surface |

Semantic aliases: `--text-color--text-primary`, `--background-color--background-primary`, etc. This is a production-grade design token system. The golden color (`rgba(255, 212, 57, 0.8)`) appears as an animated shine effect — not a base palette color.

## 3. Typography Rules

**Typeface:** `Nb International Pro Webfont` — a precise, optical-weight grotesque used in Swiss editorial and luxury contexts. Its proportions are slightly condensed at display sizes, giving it authority without aggression.

| Element | Size | Weight | Line Height | Tracking |
|---|---|---|---|---|
| H1 | 51.29px | 400 | 58.58px (1.143) | −1.28px |
| H2 | 43.97px | 400 | 51.26px | −0.99px |
| H3 | 29.31px | 400 | 36.64px | −0.59px |
| H4 / Body | 14.66px | 400 | 20.52px | normal |
| Paragraphs | 16.49px | 400 | 21.93px | −0.09px |

The fractional pixel sizes indicate fluid/viewport-relative scaling (`vw`-based sizing via Webflow's responsive typescale). Negative tracking escalates with size — the larger the heading, the tighter the tracking — a hallmark of premium typographic systems. Font weight is uniformly 400 throughout; all hierarchy comes from size and spacing.

## 4. Component Stylings

- **Primary CTA:** `rgb(252, 95, 43)` background with white text — the Vermillion accent as the single most important interactive element.
- **Buttons (dark):** `rgb(24, 24, 27)` fill — zinc-900 as secondary CTA.
- **Slider bullets:** Zinc-900 fill for inactive, `rgba(0,0,0,0.25)` for stepped/indicator states.
- **Border radii:** Extensive system — `2px` (hairline), `5px` (small input), `14.66px` (body-scale), `16px` (cards), `21.98px` (badges), `73.28px` (large pill), `100px` / `9999px` / `1280px` (full pill/circle). The navbar height is `6rem`.
- **Trustpilot section:** `rgb(244, 244, 245)` (zinc-100) tinted band.
- **Shadows:** `rgba(0,0,0,0.15) 0 3px 14px` (prominent lift) + `rgba(0,0,0,0.05) 0 2px 2px` (hairline bottom shadow).

## 5. Layout Principles

- Full responsive range: `479`, `767`, `768`, `968`, `991`, `992`, `1215`, `1439`, `1920px` — comprehensive Webflow breakpoint set covering every major viewport class.
- Navbar: `--navbar-height: 6rem` — generous, premium top bar.
- Stack: **Webflow** + **GSAP** — layout via Webflow grid, interaction via GSAP timelines.
- The semantic token architecture (`--background-color--background-*`, `--text-color--text-*`) suggests this was designed with a Figma variables system before being exported.
- Sections have no padding declared at the global level — all spacing is handled per-component.

## 6. Depth & Elevation

Two-tier shadow system:
- **Subtle (hairline):** `rgba(0,0,0,0.05) 0 2px 2px` — barely visible lift, used on inline elements.
- **Card lift:** `rgba(0,0,0,0.15) 0 3px 14px` — visible float for modals, video wrappers, hovering cards.

The animated `shine` element (`rgba(255, 212, 57, 0.8)`) creates a light sweep effect — depth through motion rather than static shadow.

## 7. Do's and Don'ts

**Do:**
- Use the full semantic token system — reference `--text-color--text-primary` not raw zinc hex values.
- Apply Vermillion (`#fc5f2b`) exclusively to the single primary CTA per screen.
- Use negative letter-spacing that scales with font size (−1.28px at 51px, less at smaller sizes).
- Maintain weight 400 throughout — no bold anywhere in the base system.
- Use the full radius range purposefully: `5px` for form inputs, `16px` for cards, `9999px` for pill buttons.

**Don't:**
- Introduce non-zinc neutrals — the grey system is tightly controlled.
- Use the golden shine color as a static palette element — it's animation-only.
- Place Vermillion on secondary or tertiary actions.
- Add new border-radius values outside the defined token set.
- Use shadows heavier than `rgba(0,0,0,0.15)`.

## 8. Responsive Behavior

Nine breakpoints cover every meaningful viewport from mobile portrait (479px) to 4K (1920px). The fluid typography (fractional `vw`-based px values) ensures headings scale smoothly between breakpoints without jarring jumps. The `6rem` navbar is likely sticky and may reduce height on mobile. GSAP animations are presumably disabled or simplified on reduced-motion preference.

## 9. Agent Prompt Guide

> Build a Superpower.com-style health-tech UI: white canvas, zinc neutral system (`#18181b` text, `#71717a` secondary, `#e4e4e7` borders), single Vermillion accent (`#fc5f2b`) for primary CTAs only. Nb International Pro webfont at weight 400 with negative tracking that scales with size. Full radius range: `5px` inputs, `16px` cards, `9999px` pills. Two shadows: `rgba(0,0,0,0.05)` hairline + `rgba(0,0,0,0.15)` card float. Nine responsive breakpoints. Semantic token architecture throughout. Premium, body-forward, motion-enhanced.

---

*Generated by Sparkbites — extracted from live CSS analysis*
