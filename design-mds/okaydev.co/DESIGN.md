# okaydev.co — Design System

## 1. Visual Theme & Atmosphere

okaydev.co occupies a specific niche: developer tooling or community with personality. The design is built on a base of near-absolute black (`#0c0c0c`) and white (`#ffffff`), but what distinguishes it is a deliberate yellow accent — `rgb(238, 230, 66)` — that reads as both energetic and technical, like a terminal highlight or a linter warning badge. The typography is activated via an extensive set of OpenType features: contextual alternates, discretionary ligatures, stylistic sets (`ss05`, `ss06`, `ss07`, `ss12`) — signals of a type-obsessed team that chose a font specifically because of its expressiveness at the glyph level. The overall character is bold, opinionated, and slightly irreverent. This is a product site that refuses to be generic.

## 2. Color Palette & Roles

The system is token-first, defined through RGB component variables for composability.

| Role | Value | Usage |
|---|---|---|
| Text / Ink | `#0c0c0c` (`--text-current`) | Body text, icon fills |
| Canvas | `#ffffff` (`--bg-current`) | Page background |
| Background Black | `rgb(12, 12, 12)` | Dark section backgrounds |
| Gray Dark 2 | `rgb(82, 82, 82)` | Secondary text on dark |
| Gray Dark 1 | `rgb(129, 129, 129)` | Muted / disabled on dark |
| Gray Light 4 | `rgb(242, 242, 242)` | Subtle surface, tag backgrounds |
| Gray Light 3 | `rgb(234, 234, 234)` | Dividers, input borders |
| Gray Light 2 | `rgb(204, 204, 204)` | Placeholder text |
| Gray Light 1 | `rgb(184, 184, 184)` | Disabled states |
| **Yellow Accent** | `rgb(238, 230, 66)` (`--color-bg-yellow-rgb`) | Primary accent — CTAs, highlights, badges |
| Yellow Light | `rgb(255, 253, 217)` | Tinted yellow surface for card hovers or tags |
| Red | `rgb(236, 66, 66)` | Error, destructive |
| Gutter / Layout | `--gutter-cap`, `--gutter-y` | Responsive spacing tokens |

**What's absent:** No blue. No brand purple. No gradients. The chromatic strategy is surgical: one yellow accent in an otherwise achromatic system. The `--color-bg-*-rgb` pattern (storing raw RGB triples) enables `rgba()` composition throughout — a sophisticated token approach.

## 3. Typography Rules

- **Primary font:** A custom typeface with rich OpenType activation — `"case"`, `"dlig"` (discretionary ligatures), `"ss05"`, `"ss06"`, `"ss07"`, `"ss12"` enabled; `"ss12" 0` disabling one stylistic set. Based on the feature set, this is likely a grotesque or geometric sans with character variants (possibly Söhne, Neue Haas Grotesk, or similar).
- **Monospace:** System mono stack — `Monaco, Menlo, Courier, Lucida Console` — for code and technical content.
- **Fallback mono:** `--fallbackfontmono` variable suggests a defined fallback for the custom mono face.

| Context | Family | Size | Notes |
|---|---|---|---|
| Body | Custom grotesque | 16px | Full OT feature set active |
| UI labels | Custom grotesque | 14px | Compact sizing |
| Headings | Custom grotesque | 36–40px | Large scale for hierarchy |
| Code / mono | Monaco stack | — | Terminal-feel technical content |

**Letter-spacing:** Normal; the OpenType features handle opticals. **Text transform:** None.

## 4. Component Stylings

- **Cards:** `card-asset-bg` token suggests image or asset cards with controlled background fills. Card surfaces likely use the gray-light spectrum for differentiation.
- **Buttons:** Yellow accent for primary CTAs against the dark or light canvas. Likely border-radius tokens not extracted but expected to be moderate (4–8px given the product's personality).
- **Tags / badges:** `rgb(242, 242, 242)` or `rgb(255, 253, 217)` surfaces for light-mode tags; yellow-tinted for highlighted tags.
- **Inputs:** 16px base font. Box model follows the standard gray-light border system.
- **Navigation header:** A `header` element with gutter tokens (`--gutter-cap`) managing responsive horizontal padding.

## 5. Layout Principles

- **Gutter system:** `--gutter-cap` (horizontal edge padding) and `--gutter-y` (vertical rhythm) as first-class layout tokens — responsive gutters that adjust per viewport.
- **Breakpoints:** `1024px` and `1070px` (inferred from extracted values) — a standard desktop breakpoint with a slight wide-screen offset.
- **Grid:** Token-based gutters suggest a fluid grid rather than fixed-column definitions.
- **Whitespace:** Generous at `36px`, `40px` scale for section spacing. Tight at `14–16px` for in-component density.

## 6. Depth & Elevation

- **Box-shadow** is present as a CSS property (detected in extraction) but specific values weren't surfaced — likely subtle `0 1px 3px rgba(0,0,0,0.1)` style shadows for card lift.
- **Transform:** Present — animations or interactive card tilts possible. The combination of `transform` + `opacity` suggests hover micro-interactions.
- **No layered elevation system** — depth is binary: flat surface or single-layer card shadow.

## 7. Do's and Don'ts

**Do:**
- Use yellow `rgb(238, 230, 66)` exclusively as the accent — one per page view
- Activate OpenType features on all primary text: `"case", "dlig", "ss05", "ss06", "ss07"`
- Store all colors as RGB triples for flexible `rgba()` composition
- Use `--gutter-cap` and `--gutter-y` for all edge spacing — never hardcode margins

**Don't:**
- Don't introduce a second accent color — the yellow-only system is intentional
- Don't use the yellow background at full saturation for large areas — it's a highlight, not a canvas
- Don't skip OpenType features on headings — they're load-bearing for the brand's typographic identity
- Don't use red outside of error/destructive contexts

## 8. Responsive Behavior

- `--gutter-cap` and `--gutter-y` are explicitly responsive tokens, adjusting at breakpoints to collapse page margins on mobile.
- The `1024px` breakpoint triggers a layout mode change — likely from multi-column to single-column.
- Touch targets follow the 16px body default; no explicit minimum sizing tokens extracted.
- The monospace fallback stack ensures code elements render consistently across platforms.

## 9. Agent Prompt Guide

**Quick reference:**
- Ink: `#0c0c0c` | Canvas: `#ffffff`
- Yellow accent: `rgb(238, 230, 66)` / light yellow: `rgb(255, 253, 217)`
- Error: `rgb(236, 66, 66)`
- Gray scale: 82 / 129 / 184 / 204 / 234 / 242
- Primary font: Custom grotesque with OT features (`"case"`, `"dlig"`, `"ss05-07"`)
- Mono: Monaco / Menlo / Courier stack

**Prompt starters:**
- *"Developer brand: near-black `#0c0c0c` canvas, single yellow accent `rgb(238,230,66)`, custom grotesque typeface with activated OpenType features, achromatic gray scale."*
- *"Bold tech site: black and white base, yellow-only accent, type-obsessed with discretionary ligatures and stylistic alternates, gutter-token responsive layout."*

---

*Generated by Sparkbites — extracted from live CSS analysis*
