# portfolio.ricoui.com — Design System

## 1. Visual Theme & Atmosphere

Rico's UI portfolio pairs editorial serif warmth with a structured blue-toned system to create something that feels simultaneously hand-crafted and technically credible. The warm parchment background (`#FDFAF5`) grounds the design in analog quality, while the primary blue family anchors it in digital professionalism. It's a portfolio that says "I understand both taste and craft." The interplay between Instrument Serif for display and Inter for UI creates deliberate tension — one voice for ideas, another for execution.

## 2. Color Palette & Roles

**Backgrounds**
- `rgb(253, 250, 245)` — Parchment white; warm page ground
- `rgb(255, 255, 255)` — Card surfaces (case study squares); pure white lifts off the parchment

**Text**
- `rgb(63, 74, 90)` — Primary body text; desaturated blue-grey, never pure black
- `rgb(103, 116, 135)` — Secondary / meta text; lighter blue-grey
- `rgb(25, 34, 47)` — Dark anchor text (active nav, emphasis)

**Primary Accent — Blue**
- `rgb(45, 109, 195)` — Primary blue; CTAs, active states, h1 color, button fill
- `rgb(44, 106, 190)` / `rgb(46, 108, 191)` — Hover states on links (same family, slight variation)
- `rgb(127, 161, 255)` — Light blue; decorative divs, illustration elements
- `rgba(138, 127, 255, 0.2)` — Soft purple-blue border; subtle boundary on interactive elements

**Shadow Accent**
- `rgba(91, 84, 211, 0.3)` — Purple-tinted shadow on prominent CTA/button; unusual and distinctive

## 3. Typography Rules

A conscious dual-voice system: **Instrument Serif** for expressive display, **Inter** for all functional UI text. The contrast between them is the design's defining typographic gesture.

| Role | Family | Size | Weight |
|------|--------|------|--------|
| H2 / Section hero | Instrument Serif | 48px | 400 |
| H3 / Sub-section | Instrument Serif | 28px | 400 |
| H1 (nav/label role) | Inter | 16px | 400 |
| Body | Inter | 16px | 400 |
| Captions / micro text | Inter | 11px | 400 |
| Links | Inter | 16px | 400 |

Instrument Serif is always weight 400 — its personality comes from form, not weight. Inter similarly stays at 400 throughout; no bold weights are used. The type scale is contained: 48px display, 28px section, 16px body, 11px caption.

## 4. Component Styling

**Cards (case squares)**: Pure white (`#FFFFFF`) surfaces with `border-radius: 12px` and a standard `box-shadow: rgba(0,0,0,0.1) 0px 2px 3px`. Clean, card-like, softly elevated.

**Primary button**: `rgb(45, 109, 195)` fill, white text, `border-radius: 50%` on icon variants, `12px` on rectangular buttons. Shadow uses the distinctive purple tint: `rgba(91,84,211,0.3) 0px 4px 12px`.

**Nav links**: Default `rgb(25,34,47)` (active) or `rgb(63,74,90)` (inactive); hover shifts uniformly to `rgb(44–46, 106–108, 190–191)` blue. Clean directional feedback.

**Decorative elements**: `rgb(127,161,255)` light blue divs and `rgb(45,109,195)` fills appear as illustration/decoration rather than functional UI.

## 5. Layout Principles

Tailwind CSS drives a standard responsive grid. Breakpoints at `639, 640, 767, 768, 960, 1400` align with Tailwind's `sm/md/lg/xl` ladder. The `1400px` upper breakpoint suggests a max-width container constraint.

No custom spacing tokens — Tailwind's default scale applies. Layout is column-based, likely a 12-column grid collapsing to single-column on mobile.

## 6. Depth & Elevation

Three shadow levels:
1. **Micro** — `rgba(0,0,0,0.1) 0px 2px 3px` on cards; barely perceptible lift
2. **Standard** — `rgba(0,0,0,0.1) 0px 10px 15px, 0px 4px 6px` Tailwind `shadow-lg` equivalent
3. **Accent** — `rgba(91,84,211,0.3) 0px 4px 12px` on primary CTA; the purple tint makes the shadow feel branded rather than neutral

Border radius vocabulary: `12px` for cards and buttons, `50%` for circular/icon elements. No sharp corners.

## 7. Do's and Don'ts

**Do:**
- Use Instrument Serif at 48px/400 for any hero or section-lead display text
- Pair with Inter at 16px/400 for all body and UI copy — keep both at weight 400
- Ground every layout on the parchment background `#FDFAF5`
- Use `rgb(45,109,195)` as the sole action color; let it appear in CTAs, active states, and H1 labels
- Apply the purple-tinted shadow exclusively on primary buttons — it's the system's most distinctive detail

**Don't:**
- Don't use bold (700+) in either typeface — the design avoids visual shouting
- Don't mix pure white backgrounds with parchment at the same level (they're for different layers)
- Don't introduce warm or saturated accent colors — the system is blue-anchored
- Don't use the `50%` border-radius on anything except circular icon elements
- Don't drop below 11px for any text

## 8. Responsive Behavior

Tailwind breakpoints: mobile-first, adapting at `sm (640px)`, `md (768px)`, `lg (960px)`, `xl (1400px)`. The `960px` breakpoint (rather than the standard `1024px`) suggests a customized config to accommodate a specific content width. Case study grids likely go from 1 column (mobile) → 2 columns (sm) → 3 columns (lg+).

## 9. Agent Prompt Guide

> Build a portfolio section in the portfolio.ricoui.com style. Page background is `#FDFAF5` (warm parchment). Cards are pure white with `border-radius: 12px` and `box-shadow: rgba(0,0,0,0.1) 0px 2px 3px`. Display headings use Instrument Serif at 48px/400; all UI text uses Inter at 16px/400 (captions: 11px). Primary color is `rgb(45,109,195)` — used for CTAs, active nav, and h1 labels. Body text is `rgb(63,74,90)`. The primary button gets a distinctive purple shadow: `rgba(91,84,211,0.3) 0px 4px 12px`. Nav links default to near-black and shift to blue on hover. No bold weights anywhere. Breakpoints follow Tailwind sm/md/lg.

---

*Generated by Sparkbites — extracted from live CSS analysis*
