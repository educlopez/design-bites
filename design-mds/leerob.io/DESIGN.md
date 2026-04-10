# leerob.io — Design System

## 1. Visual Theme & Atmosphere

leerob.io reads as a writer's site first and a developer's site second. The dominant design decision is the choice of **STIX Two Text**, a serif typeface designed for scientific and mathematical publishing. This immediately signals intellectual seriousness without academic stuffiness. The canvas is pure white with near-black text — a blank page aesthetic that defers entirely to content. There are no decorative graphics, no gradient splashes, no hero imagery. The atmosphere is that of a well-typeset essay: quiet, considered, and built for sustained reading. Code blocks introduce a secondary layer — syntax-highlighted with a muted Tokyo Night palette — creating the only moment of colour on an otherwise monochrome page.

## 2. Color Palette & Roles

| Role | Value | Usage |
|---|---|---|
| Background | `#ffffff` | Page canvas |
| Foreground | `#171717` | Body text, headings |
| Muted text | `#737373` | Dates, captions, secondary labels |
| Border / divider | `#e5e5e5` | Subtle separators |
| Surface / card | `#fafafa` | Sidebar, card backgrounds |
| Accent / ring | `#a1a1a1` | Focus rings, hover states |
| Syntax: class/prop | `#7aa2f7` | Blue — identifiers |
| Syntax: string | `#9ece6a` | Green — string literals |
| Syntax: keyword | `#bb9af7` | Purple — keywords |
| Syntax: sign/punct | `#89ddff` | Cyan — operators |
| Syntax: entity | `#e0af68` | Gold — special names |
| Syntax: comment | `#565f89` | Slate — comments |

The palette is essentially greyscale with colour reserved entirely for code. There is no call-to-action colour, no brand accent, no hover highlight. Restraint is the entire colour strategy.

## 3. Typography Rules

**Primary typeface:** STIX Two Text (serif, weight 400–500)  
**Fallback:** Generic serif

- **H1:** 24px / 24px line-height / −0.48px tracking / weight 500 — tight and headline-dense
- **Body / links:** 17px / 25.5px line-height / weight 400 — comfortable reading measure
- **Code:** Implied monospace via syntax token system

The choice to set H1 at exactly the same line-height as its font-size (24/24) creates a visually dense, tightly packed headline — more like a typeset chapter title than a web heading. Body text at 17px with a 1.5× line-height is generous and readable. There are no display typefaces, no variable font features beyond standard ligatures. The typographic palette is intentionally minimal.

## 4. Component Stylings

- **Links:** Plain text, no underline decoration by default; inherit foreground colour
- **Code blocks:** Dark surface (`#1a1b26` Tokyo Night base implied by syntax tokens), multi-colour syntax highlighting
- **Cards / surfaces:** `#fafafa` background, `1px solid #e5e5e5` border, `4px`–`8px` border-radius
- **Focus rings:** `2px solid #a1a1a1` — visible but restrained
- **Pill / badge radius:** `999px` for fully rounded tags; `16px` for softer cards; `48px` for avatar-style elements
- **Shadows:** Subtle — `rgba(0,0,0,0.1) 0 0 0 2px` ring shadows only; no drop shadows

## 5. Layout Principles

The layout is narrow and centred — a single-column reading column, likely constrained to ~65ch or equivalent. Navigation is minimal. Content sections are separated by whitespace, not borders. Spacing tokens are sparse in the extracted data (body padding 0, sections inherit), suggesting spacing is handled through typographic rhythm rather than explicit component gaps. The design avoids multi-column layouts at content level entirely.

## 6. Depth & Elevation

Depth is almost entirely absent. There are no drop shadows on content elements. The only elevation signals are:
- Subtle `2px ring` box-shadows on interactive focus states
- `#fafafa` surface vs `#ffffff` background — a 1-step elevation through near-identical tones
- Code blocks create visual weight through dark-on-light contrast, not shadow

This is a flat design in the purest sense.

## 7. Do's and Don'ts

**Do:**
- Use STIX Two Text for all editorial content
- Keep the colour palette monochrome; reserve colour for syntax highlighting only
- Maintain tight letter-spacing on headings (−0.02em range)
- Use whitespace generously between content sections
- Keep interactive states subtle — ring borders, not fills

**Don't:**
- Add decorative background colours or gradients
- Use more than two font weights (400, 500)
- Introduce icon sets or illustrative elements
- Apply box-shadows to content cards
- Use colour for navigation or CTAs

## 8. Responsive Behavior

Breakpoints extracted: 420px, 810px, 1200px (mobile / tablet / desktop).  
The design is content-first and single-column, so responsive changes are likely typography scaling and padding adjustments rather than layout reflows. At mobile widths the reading column fills the viewport with modest horizontal padding. No multi-column grids to collapse.

## 9. Agent Prompt Guide

> Replicate leerob.io's design system: white canvas, near-black (`#171717`) text, STIX Two Text serif at 17px/1.5 line-height for body. Single-column centred layout, no decorative colour. Use `#fafafa` for subtle surface elevation. Code blocks use Tokyo Night syntax colours. Headings tight at −0.02em tracking, weight 500. Borders at `#e5e5e5`, 1px. No drop shadows. Focus rings as 2px ring in `#a1a1a1`. Border-radius 4px–8px for cards, 999px for pills.

---
*Generated by Sparkbites — extracted from live CSS analysis*
