# sequencehq.com — Design System

## 1. Visual Theme & Atmosphere

Sequence communicates trust and precision — the visual language of a serious B2B finance tool that has invested in taste. The palette is near-monochrome: a very dark charcoal body text on a clean white canvas, softened by a warm mid-grey border system. Nothing shouts. The typography is restrained to a single bespoke typeface at low weights, letting white space do the heavy lifting. The overall feeling is that of a well-typeset financial report: efficient, considered, and deliberately undecorated. Shadows appear sparingly and only at low opacity to lift interactive cards without drama.

## 2. Color Palette & Roles

| Role | Value | Usage |
|---|---|---|
| Body text | `rgb(29, 29, 32)` | All primary text, headings |
| Secondary text | `rgb(80, 80, 80)` | Button labels, meta text |
| Border / divider | `rgb(229, 231, 235)` | Inputs, card edges, separators |
| Surface / canvas | `rgb(255, 255, 255)` | Header, card backgrounds |
| Page background | transparent / white | Body default |

The palette is intentionally minimal — no accent color appears in the extracted data. Brand differentiation is carried entirely by typography and layout, not color. Avoid introducing any color that feels "startup blue" or attention-grabbing; neutrality is the brand.

## 3. Typography Rules

**Typeface:** `twkLausanne` (custom, with system fallback). A geometric grotesk with optically balanced strokes — it reads as modern-neutral rather than tech-cold.

| Element | Size | Weight | Line Height |
|---|---|---|---|
| Body | 16px | 400 | 24px |
| Links | 13px | 400 | 24px |
| Paragraphs | 12px | 400 | 24px |
| Headings (h3) | 12px | 400 | 24px |
| Buttons | 14px | 400 | 14px (tight) |

Notable: headings use the same size as body or smaller — hierarchy is established through layout and spacing, not size jumps or weight changes. Letter-spacing is kept at `normal` throughout; no expanded or condensed tracking. Font weight never rises above 400 in base styles — variations (if any) are contextual.

## 4. Component Stylings

- **Buttons:** Transparent background with `rgb(229, 231, 235)` border, secondary-grey label. Low visual footprint — text-forward over icon-forward.
- **Cards / surfaces:** White background with a very subtle drop shadow (`rgba(0,0,0,0.05) 0 10px 15px -3px, rgba(0,0,0,0.05) 0 4px 6px -4px`). This is the only elevation used.
- **Inputs / dividers:** Unified border color (`rgb(229, 231, 235)`) — no special focus ring colors detected; minimalist treatment.
- **Header:** Full white, no shadow, flush edges.
- No border-radius values were detected — components likely use sharp or very subtly rounded corners, or radius is applied inline per component via utility classes.

## 5. Layout Principles

- Zero margin/padding on `body`, `main`, `header` — layout is handled entirely by inner components and grid containers.
- Footer uses a minimal bottom padding (`4px`) — almost flush.
- Breakpoints detected: `1266px` and `1280px` — a single wide-layout breakpoint, implying a primarily desktop-first product (likely a SaaS dashboard).
- Stack: **Next.js** — App Router likely, with Tailwind-managed spacing via class names rather than global CSS rules.
- Dense information layouts are expected; the type scale skews small (12–16px) to accommodate data-rich views.

## 6. Depth & Elevation

Sequence uses a single-level elevation system. The only shadow found (`rgba(0,0,0,0.05)` at two offsets) is used to lift card-like surfaces above the page — essentially a layer-1 floating surface. There is no layer-2 or modal-level shadow in the extracted data. This restraint prevents visual noise in data-heavy interfaces.

- **Layer 0:** Page background (white/transparent)
- **Layer 1:** Cards, dropdowns — `box-shadow: rgba(0,0,0,0.05) 0 10px 15px -3px, rgba(0,0,0,0.05) 0 4px 6px -4px`
- No glassmorphism, no gradients, no border-glow effects.

## 7. Do's and Don'ts

**Do:**
- Use `twkLausanne` at weight 400 exclusively for UI text.
- Establish hierarchy through spacing, not font size or weight escalation.
- Keep all borders at `rgb(229, 231, 235)` — one border color, used everywhere.
- Use `rgb(29, 29, 32)` for all primary text; never pure `#000`.
- Limit elevation to a single soft two-layer shadow.

**Don't:**
- Add accent colors, gradient fills, or colorful CTAs.
- Use bold (`700+`) font weights in the main UI.
- Apply border-radius unless it matches existing component patterns.
- Introduce multiple shadow levels or glows.
- Use uppercase or tracked-out letter-spacing for labels.

## 8. Responsive Behavior

Single major breakpoint at ~1280px. The design is desktop-first and primarily serves a professional dashboard context. Mobile layout data is minimal, suggesting:
- Sidebar navigation likely collapses.
- Dense table/data views reflow to single-column or horizontal scroll.
- Type sizes remain constant (no detected responsive scaling).
- No fluid typography (`clamp`) patterns in extracted data.

## 9. Agent Prompt Guide

> Build a Sequence-style UI: monochrome professional with `twkLausanne` at 400 weight throughout. Use `#1d1d20` for text, `#fff` surfaces, and `#e5e7eb` for all borders and dividers. No accent colors — hierarchy via spacing only. Cards float with a single two-layer `rgba(0,0,0,0.05)` shadow. Keep font sizes in the 12–16px range. Think financial SaaS: precise, quiet, trustworthy.

---

*Generated by Sparkbites — extracted from live CSS analysis*
