# magdabutrym.com — Design System

## 1. Visual Theme & Atmosphere

Magda Butrym's site embodies luxury fashion minimalism taken to its logical extreme. The palette is an extended family of warm off-whites and parchments — barely perceptible tonal shifts between surface layers — with a single deep crimson red as the only departure. Nothing competes for attention except the photography. Typography splits into two distinct voices: a refined serif for editorial content and a compact sans-serif for UI chrome, with both kept small and unobtrusive. The design philosophy is restraint as aspiration. White space is not merely present; it is the design. The absence of decorative elements, shadows, and rounded corners (the sole radius token is `9999px` — exclusively for pill shapes) signals confidence that the garments carry all visual weight.

## 2. Color Palette & Roles

**Warm off-whites (surfaces)**

| Role | Hex | Notes |
|---|---|---|
| Pure white | `#fff` | Primary surface |
| Warm cream | `#fcfaf7` | Page background |
| Parchment | `#f5f3ef`, `#f5f2ee`, `#f5f2ed` | Alternate surface tones |
| Stone | `#efece7`, `#edeae6` | Hover states, muted fills |
| Off-white UI | `#f4f4f4`, `#fafafa`, `#f5f5f5` | Secondary surfaces |

**Grays (text hierarchy)**

| Role | Hex | Notes |
|---|---|---|
| Body text | `#212121` | Near-black |
| Secondary | `#616161`, `#757575` | Captions, metadata |
| Muted | `#9e9e9e`, `#bdbdbd`, `#e0e0e0`, `#eee` | Dividers, placeholders |

**Accents**

| Role | Hex | Notes |
|---|---|---|
| Brand red | `#cd3105` | Error states, critical actions |
| Link blue | `#0071e3` | Apple-style hyperlinks |
| Alert red | `#c9102e` | Validation, alerts |
| Overlay dark | `rgba(0,0,0,.7)` / `rgba(0,0,0,.3)` | Modal overlays |

## 3. Typography Rules

| Selector | Font | Size | Weight | Notes |
|---|---|---|---|---|
| `p` (editorial) | Custom Serif (`__fontSerif`) | 20px | 400 | 27px line-height — the reading voice |
| `label` | Times (fallback) | 22px | 400 | Form labels, large and light |
| `body` | Times (base) | 16px | 400 | Base reset; serif fallback |
| `a` | Custom Sans (`__fontSans`) | 13px | 400 | Compact navigation/UI links |
| `button` | Custom Sans (`__fontSans`) | 13px | 400 | 19.5px line-height |
| `input` | Arial | ~13px | 400 | Form inputs use system fallback |

**Philosophy:** The dual-font system enforces a strict editorial/UI split. Serif handles content and presence; sans-serif handles interaction and navigation. No font weight variation is used — every element is 400 (regular). Drama comes from size and proportion, not weight.

**Absent:** Bold headings, tracked uppercase, decorative ligatures.

## 4. Component Stylings

**Navigation**
- Compact sans at 13px, transparent backgrounds
- No detected hover/focus states — navigation is intentionally passive

**Buttons / Pills**
- Border radius: `9999px` — the only radius token, meaning all interactive controls use full pills
- No interactive states captured — consistent with a minimal, near-invisible UI layer

**Forms**
- Inputs use Arial at system size — functional, not designed
- Labels use Times at 22px — larger than body, creating an unusual and refined hierarchy

**Spacing tokens (dense and deliberate):**
`0px` → `2px` → `4px` → `6px` → `8px` → `10px` → `12px` → `14px` → `16px` → `18px` → `20px` → `24px` → `28px` → `32px` → `36px` → `40px` → `46px` → `48px` → `56px` → `60px` → `64px` → `72px` → `80px` → `96px` → `100px` → ... → `200px` → `240px` → `288px`

A full 8px-base spacing system is available, extending to macro layout values.

## 5. Layout Principles

The layout uses a Next.js app with a meticulous spacing token vocabulary. Footer padding is `56px 64px 72px` — generous, considered margins. Header padding is `~23px 0` — tight top rail.

**Breakpoints:** `375px`, `400px`, `420px`, `540px`, `739px`, `740px`, `800px`, `999px`, `1000px`, `1300px` — a dense responsive system suggesting pixel-perfect breakpoints at every garment gallery format change, not just standard device sizes.

**Width tokens:** `325px`, `468px`, `580px`, `670px`, `900px`, `1440px` — max-width containers mapped to content zones.

**Philosophy:** The grid is invisible. Content takes exactly as much space as it needs, no more.

## 6. Depth & Elevation

No box shadows detected. One shadow token exists in the CSS (`--sy5gny10`: `0px 2px 1px -1px rgba(0,0,0,.02), 0px 1px 1px 0px rgba(0,0,0,.14), 0px 1px 3px 0px rgba(0,0,0,.12)`) — a Material Design elevation-1 shadow, barely perceptible, used internally but not on visible surfaces. Depth is achieved through surface color layering: the warm off-white family provides five to six barely-distinguishable tonal steps that create surface hierarchy without shadows.

## 7. Do's and Don'ts

**Do:**
- Use the warm off-white progression for surface layering: `#fcfaf7` → `#f5f3ef` → `#efece7`
- Keep all typography at weight 400 — no bold type anywhere
- Reserve `#cd3105` / `#c9102e` exclusively for errors and alerts
- Use `9999px` border radius for all interactive pill shapes
- Keep font sizes small (13–22px) — nothing competes with imagery

**Don't:**
- Add decorative shadows, gradients, or texture
- Use rounded corners on cards or containers — the design is all right-angles except for pills
- Introduce any color outside the warm neutrals + red/blue pair
- Use large, bold typographic headlines
- Add hover animations — the site's interactions are deliberately understated

## 8. Responsive Behavior

Breakpoints span from `375px` to `1300px` with ten distinct steps — unusually granular. This suggests:
- Gallery layouts reflow at each breakpoint to maintain garment proportions
- At `739px`/`740px` there is a near-identical pair — likely a container-query or sub-layout transition
- Width tokens (`580px`, `670px`, `900px`) correspond to image-grid columns
- Transition duration: `300ms` (`--sy5gny2q`) — smooth but not theatrical

Footer collapses from `64px` horizontal padding toward minimal mobile gutters. Header remains compact across all sizes.

## 9. Agent Prompt Guide

**Quick reference:**
- Background: `#fcfaf7` → `#f5f3ef` (layered warm parchments)
- Brand red: `#cd3105`
- Text: `#212121` (body) / `#757575` (secondary)
- Fonts: Custom serif (editorial) + Custom sans (UI) both at weight 400
- Radius: `9999px` (pills only)

**Prompt starters:**
- "Design a fashion product card in the Magda Butrym style: warm `#f5f3ef` background, no shadows, right-angle corners, serif body text at 20px/27px, small sans UI labels at 13px."
- "Build a minimal navigation bar: 13px sans-serif links, transparent background, `#fcfaf7` top surface, no hover animations."
- "Create a full-bleed editorial layout: parchment surface layers, only `#cd3105` as the accent color, no decorative elements."

*Generated by Sparkbites — extracted from live CSS analysis*
