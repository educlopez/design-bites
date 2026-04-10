# unito.shop — Design System

## 1. Visual Theme & Atmosphere

Unito presents a sustainable or artisanal commerce aesthetic — earthy, muted, deliberate. The canvas is near-white (`rgb(250,250,250)`) with a faintly warm reading that avoids the sterility of pure white. The primary brand surface is a deep olive-khaki (`rgb(58,60,35)`) — an unusual, organic color that signals craft, nature, and intentionality rather than conventional retail energy.

The single electric accent — a neon chartreuse `rgb(245,255,103)` — cuts sharply against the earthtone palette, functioning as a CTA or highlight device with unmistakable clarity. This tension between quiet and electric is the design's defining move. Built on Framer.

## 2. Color Palette & Roles

| Role | Value | Usage |
|------|-------|-------|
| **Canvas** | `rgb(250,250,250)` | Page background — barely-warm white |
| **Primary surface** | `rgb(58,60,35)` / `rgb(57,60,35)` | Hero backgrounds, primary buttons, dark sections |
| **Warm sand** | `rgb(194,190,173)` / `rgb(215,213,205)` | Card backgrounds, secondary link surfaces |
| **Input surface** | `rgb(235,235,235)` | Form field backgrounds — neutral gray |
| **Electric lime** | `rgb(245,255,103)` | Hero accent block, CTA highlight — the key contrast move |
| **Text** | `rgb(0,0,0)` | Primary text — pure black on light surfaces |

The olive-khaki and electric lime pairing is the signature. Everything else is a supporting neutral. The sand tones (`rgb(194,190,173)`) provide warm mid-ground surfaces for cards and secondary elements.

## 3. Typography Rules

**Typeface:** Roobert Medium — a friendly, rounded geometric sans with humanist warmth. Used consistently across all levels.

| Selector | Size | Weight | Line Height | Notes |
|----------|------|--------|-------------|-------|
| `h1` | 54px | 400 (Medium) | 54px (1.0×) | Tight, block-style headlines |
| `h2` | 28px | 400 (Medium) | ~33.6px | Section headers |
| Body / p | 15–18px | 400 | ~22–27px | Comfortable reading |
| Labels | 12px | 400 | ~15px | Tags, metadata |
| Input | matches body | 400 | normal | Form fields use same face |

Line height of 1.0× on H1 creates dense, editorial headlines — text as a designed block rather than flowing prose. This is a deliberate choice that reinforces the craft-object aesthetic.

**Notably absent:** No italic, no bold (weight 700), no serif, no monospace, no uppercase text-transform.

## 4. Component Stylings

Framer-generated classes present:

- **Primary button** (`button.framer-n9xSr`) — olive-khaki `rgb(57,60,35)` background; white or cream text; likely rounded
- **CTA block** (`div.framer-0ezNT`) — electric lime `rgb(245,255,103)` background; black text; full-contrast accent panel
- **Secondary link** (`a.framer-zP3jx`) — warm sand `rgb(194,190,173)` background
- **Input fields** — `rgb(235,235,235)` background; clean, minimal
- **Spacing tokens:** 4px base, 12px, 15px, 18px, 28px, 40px — a tight spacing scale for a product-oriented layout

## 5. Layout Principles

- Built on Framer's layout engine; breakpoints at `999px` (tablet/mobile)
- Likely full-bleed hero sections with the olive-khaki primary surface
- Product grid below fold, likely 2–3 columns on desktop
- Compact spacing scale (`4px`, `12px`) suggests tight, product-card-heavy layout
- `40px` padding for section-level breathing room

## 6. Depth & Elevation

No explicit shadow tokens detected. Depth through:

1. **Color contrast** — electric lime `rgb(245,255,103)` blocks create immediate visual pop against neutrals
2. **Surface layering** — olive-khaki hero → warm sand cards → near-white canvas
3. **Typography weight** — Roobert Medium's rounded geometry creates presence without needing shadows

## 7. Do's and Don'ts

**Do:**
- Use the electric lime exclusively as the accent/CTA color — its power comes from singularity
- Place lime against the olive-khaki dark for maximum impact; it's a complementary contrast
- Use Roobert Medium throughout — no weight switching, let size carry hierarchy
- Set H1 at 1.0× line height for dense, block-style headlines
- Use warm sand as the mid-tier surface for cards and secondary panels

**Don't:**
- Add more colors to the palette — three surfaces (white, sand, olive) plus one accent is the whole system
- Use the electric lime as a background for large sections; it's a punctuation color, not a canvas
- Mix in other geometric sans typefaces; Roobert's personality is singular
- Apply shadows — the flat layering approach defines the aesthetic

## 8. Responsive Behavior

| Range | Behavior |
|-------|----------|
| `< 999px` | Mobile/tablet — likely single-column product grid |
| `≥ 999px` | Desktop — multi-column layout, larger hero sections |

The 54px H1 should scale down via responsive font-size or `clamp()` on mobile.

## 9. Agent Prompt Guide

> "Design in the style of unito.shop: near-white canvas `rgb(250,250,250)`, deep olive-khaki `rgb(58,60,35)` for primary surfaces and buttons, warm sand `rgb(194,190,173)` for cards, electric lime `rgb(245,255,103)` as the single CTA accent, Roobert Medium typeface throughout, 54px H1 at 1.0 line height, no shadows, no additional accent colors — artisanal sustainable commerce with a single electric punctuation."

*Generated by Sparkbites — extracted from live CSS analysis*
