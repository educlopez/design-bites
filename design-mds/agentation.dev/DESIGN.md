# agentation.dev — Design System

## 1. Visual Theme & Atmosphere

Agentation.dev projects quiet confidence. The design deliberately avoids spectacle — no gradients, no dark heroics — in favor of a near-white canvas that reads like a blank sheet of paper. The philosophy is editorial restraint: let the product demonstration speak, not the chrome around it. The serif/sans pairing creates a print-like authority, nodding to longform documentation traditions while the compact UI density signals precision tooling. The hero "browser demo" embedded in the page is the single theatrical moment, simulating a real interface with macOS-style chrome — everything else recedes to let that work.

## 2. Color Palette & Roles

**Background**
- Page: `#fdfdfc` — barely-off-white, warmer than pure white, avoids clinical sterility

**Text**
- Primary body: `#111` — near-black, high contrast, never pure `#000`
- Headings h1: `rgba(0,0,0,0.85)` — softened, creates hierarchy without size alone
- Headings h2: `rgba(0,0,0,0.78)` / h3: `rgba(0,0,0,0.70)` — stepped opacity for depth
- Footer / secondary: `rgba(0,0,0,0.40)` — muted, clearly subordinate

**Accent**
- Links (active): `rgb(229,72,77)` — warm coral-red, the only vivid hue in the content layer
- Focus ring: `rgba(0,122,255,0.5)` — system blue, accessibility-only, never decorative

**Brand palette (defined but used sparingly in UI chrome)**
- Indigo `#6155F5`, Blue `#0088FF`, Cyan `#00C3D0`, Green `#34C759`
- Yellow `#FFCC00`, Orange `#FF8D28`, Red `#FF383C`
- These appear inside the demo component as status/state colors (markers, buttons), not in the editorial layout

**Demo surfaces (dark layer)**
- Toolbar: `rgb(26,26,26)` — deep near-black
- Checkbox container: `rgb(37,37,37)` / Switch: `rgb(72,72,72)` — dark UI shell contrasts the light page

**Borders**
- Inputs: `rgba(0,0,0,0.1)` — hairline, nearly invisible
- Footer top: `rgba(0,0,0,0.06)` — structural divider, not decoration

## 3. Typography Rules

The dual-typeface strategy is intentional and precise. IBM Plex Serif carries only h1 at `font-weight: 500` (medium, not bold) — it signals intellectual gravitas and humanist quality. Everything else uses Inter, the workhorse. This split is unusual: most tools use sans everywhere; the serif-for-headlines-only choice signals editorial maturity.

| Element | Font | Size | Weight | Notes |
|---------|------|------|--------|-------|
| h1 | IBM Plex Serif | 32px | 500 | −0.16px tracking, tight leading 36.8px |
| h2 | Inter | 13px | 550 | Microscopic — used as section labels, not structural headings |
| h3 | Inter | 13px | 500 | Same size as h2, lighter weight distinguishes |
| body | Inter | 15px | 400 | Standard reading text |
| p | Inter | 14px | 450 | Slightly condensed weight for paragraph blocks |
| code | SF Mono | 11px | 400 | Compact, developer-facing |

Notable: font-weight `450` and `550` are variable-font values — not standard CSS weights. This requires Inter variable font, enabling micro-adjustments unavailable on static fonts.

## 4. Component Stylings

**Buttons**
- Primary (dark): `rgb(17,17,17)` bg, white text — hover lightens to `rgb(51,51,51)`
- Ghost/install snippet: transparent bg, `rgba(0,0,0,0.4)` text — hover increases opacity to `0.7`
- Border radius: `6px` — barely rounded, avoids the pill aesthetic

**Inputs**
- White background, `rgba(0,0,0,0.1)` border at rest
- Focus: border jumps to solid `rgb(60,130,247)` (brand blue) — clean, no box-shadow theatrics
- No shadow on default state

**Demo browser chrome**
- Layered surfaces: white bar → `rgb(250,249,247)` terminal → `rgb(246,245,244)` browser → dark toolbar
- macOS traffic-light dots: red `rgb(255,95,87)`, yellow `rgb(254,188,46)`, green `rgb(40,200,64)`
- Shadows: single inset ring `rgba(0,0,0,0.12) 0px 0px 0px 1px` — very subtle framing

## 5. Layout Principles

Content lives in a narrow editorial column, not a full-width grid. Footer margin of `0 352px` on desktop implies a deliberate reading width around 700px max. Sections stack vertically with `12px` top margin — micro-spacing that keeps things dense. The header is spare: `0 0 12px` padding with only `4px` gap between items. There is no explicit grid system visible; layout is prose-first.

Breakpoints: 500px, 600px, 640px, 980px — the 500px breakpoint is unusually small, suggesting fine-grained mobile control below standard sm breakpoint.

## 6. Depth & Elevation

Elevation is achieved through the light/dark contrast of the demo component, not through shadows or layering elsewhere. The page itself is completely flat — no cards, no panels, no drop shadows outside the demo chrome. The single shadow (`inset 0 0 0 1px rgba(0,0,0,0.12)`) is a border substitute rather than true elevation. This flat aesthetic is intentional: depth only appears where there's something worth demoing.

## 7. Do's and Don'ts

**Do**
- Use IBM Plex Serif exclusively for primary headlines (h1 only)
- Apply the brand color palette inside interactive/demo components
- Keep borders hairline and opacity-based
- Let the coral-red link color stand as the sole accent in content
- Maintain the stepped opacity pattern for heading hierarchy (0.85 → 0.78 → 0.70)

**Don't**
- Use the brand rainbow colors in editorial layout — they belong in UI demo contexts only
- Add box shadows or card backgrounds to content sections
- Go bolder than weight 550 — the design ethos is medium, not heavy
- Use pure `#000` or `#fff` — the palette is always slightly warm/off

## 8. Responsive Behavior

The design collapses the centered editorial column to full-width below 980px. The 640px breakpoint likely triggers single-column stacking. The 500px breakpoint (unusually low) suggests the demo component has specific small-screen adaptations. Footer margin (`0 352px`) will reduce or collapse at smaller viewports. No explicit dark mode tokens are defined — this is a light-mode-only design.

## 9. Agent Prompt Guide

> Design a developer tool landing page in the style of agentation.dev: near-white background (`#fdfdfc`), IBM Plex Serif for the single hero headline at `font-weight: 500`, Inter for all body text using variable-font weights (400–550). Keep the color palette monochromatic except for one warm coral-red accent (`rgb(229,72,77)`) on links. Use a dark embedded demo component (near-black `rgb(26,26,26)` toolbar) as the primary visual. No card shadows, no gradients. Border radius max `8px`. Stepped opacity headings: 0.85 / 0.78 / 0.70. Focus states use blue `rgba(0,122,255,0.5)`. Editorial column width, not full-width.

---

*Generated by Sparkbites — extracted from live CSS analysis*
