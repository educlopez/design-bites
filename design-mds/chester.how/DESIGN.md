# chester.how — Design System

## 1. Visual Theme & Atmosphere

chester.how is a personal site with an unusually deliberate typographic personality. Where most developer portfolios default to a sans-serif system font, this one leads with **Fraunces** — an optical-size serif with a softly romantic, slightly literary feel — for headings, while using Inter for body text. The pairing creates a purposeful tension: the headings feel like a printed object, the prose feels like a web interface.

The palette is almost entirely white and grey — a light, airy canvas that lets the typography breathe. Colour is used exclusively as decoration in the project cards, where Tailwind utility classes introduce amber, lime, orange, green, purple, and sky tints as transparent background fills. These are playful, tag-like accent markers rather than semantic colors, and their semi-transparency (40%) keeps them from overwhelming the quiet base.

The atmosphere is personal and unhurried. Generous footer padding (144px top), readable line heights, and the serif/sans pairing suggest someone who cares more about the reading experience than visual spectacle.

---

## 2. Color Palette & Roles

**Structural**:
- Page background: transparent/white
- Body text: `rgb(0, 0, 0)` — pure black
- Link / primary text: `rgb(23, 23, 23)` — near-black, nearly identical to pure black
- H1 / muted heading text: `rgb(163, 163, 163)` — used for eyebrow/subhead contrast
- Border: `rgb(229, 231, 235)` — Tailwind `gray-200`, used consistently

**Surfaces**:
- Primary card: `rgb(250, 250, 250)` — barely-off-white
- Glassmorphic nav: `rgba(255, 255, 255, 0.7)` — frosted white, likely for sticky header
- Inactive area: `rgb(229, 229, 229)` — light grey

**Project tag accents** (all at 40% opacity):
- Amber: `rgba(251, 191, 36, 0.4)`
- Lime: `rgba(163, 230, 53, 0.4)`
- Orange: `rgba(251, 146, 60, 0.4)`
- Green: `rgba(74, 222, 128, 0.4)`
- Purple: `rgba(192, 132, 252, 0.4)`
- Sky: `rgba(56, 189, 248, 0.4)`

**What's absent**: No dark mode. No brand accent color. No filled colored buttons. The chromatic tags are the entire color story beyond grey.

---

## 3. Typography Rules

The pairing of Fraunces (serif) and Inter (sans-serif) is the defining design decision.

| Role | Typeface | Size | Weight | Tracking |
|------|----------|------|--------|----------|
| H1 | Fraunces | 36px | 300 | −1.08px |
| H3 | Fraunces | 30px | 300 | −0.90px |
| Body | Inter | 16px | 400 | −0.40px |
| Links / navigation | Inter | 14px | 400 | −0.35px |

Key rules:
- Fraunces is used **only for headings** — never body text. Its optical serif character would overwhelm at small sizes.
- Weight 300 (light) for headings is uncommon and deliberate — it creates softness rather than authority
- Negative tracking applies at all levels, tightening Inter's default loose spacing
- Line heights are generous: 45px on 36px heading (1.25×), 26px on 16px body (1.625×) — optimised for comfortable reading
- The body's native stack falls back to `Times` (as detected on the element) before Inter loads — an unusual fallback that may be intentional or a Next.js font-loading artefact

---

## 4. Component Stylings

**Navigation**: A frosted-glass sticky bar — `rgba(255, 255, 255, 0.7)` background, likely with `backdrop-filter: blur`. Navigation links default to `rgb(163, 163, 163)` (grey), turning `rgb(23, 23, 23)` (near-black) on hover. The active/current page link stays dark.

**Project cards**: Background `rgb(250, 250, 250)`, no border, subtle shadow `rgba(0,0,0,0.1) 0px 4px 6px -1px`. Inside the card, coloured tag chips use the Tailwind tint palette at 40% opacity. Rounded corners at 8px.

**Focus rings**: Blue — `rgb(191, 219, 254)` (Tailwind `blue-200`) at 4px spread. Soft and accessible without being jarring.

**Border radii**: 8px for cards, 4px for small chips, `9999px` for pill-shaped tags/badges.

**Shadows** (three levels):
- Small: `rgba(0,0,0,0.1) 0px 4px 6px -1px, rgba(0,0,0,0.1) 0px 2px 4px -2px` — card lift
- Medium: `rgba(0,0,0,0.1) 0px 10px 15px -3px` — elevated modal or active card
- Inset: `rgba(0,0,0,0.1) 0px 0px 0px 1px inset` — subtle inner border

---

## 5. Layout Principles

- **Five breakpoints**: 640px, 768px, 1024px, 1280px, 1536px — the full Tailwind default scale, suggesting responsive behaviour is handled granularly
- **Main padding**: `0px 32px` — comfortable lateral breathing room
- **Footer**: `padding: 144px 0px 80px` — very generous top padding, the footer section acts as a visual resting point
- Likely uses a max-width container centered on larger viewports
- No explicit gap values detected from the surface data — spacing managed through Tailwind utility classes
- The frosted navigation suggests a sticky/fixed position at the top, full-width

---

## 6. Depth & Elevation

A light, approachable elevation system:

- **Base**: pure white / transparent
- **Cards**: `rgb(250, 250, 250)` — barely elevated off the page
- **Active overlay**: `rgba(255, 255, 255, 0.7)` — frosted glass for navigation
- **Shadows**: three-tier — subtle card lift → medium elevation → inset border

The transparent nav blur creates the most visible depth effect on the page. Cards use standard Tailwind shadow utilities. The overall effect is light and modern without any dramatic darkness or blur theatrics.

---

## 7. Do's and Don'ts

**Do:**
- Use Fraunces at weight 300 exclusively for headings — never body
- Keep Inter with negative tracking (−0.35–0.40px) for all sans-serif elements
- Use the Tailwind tint palette (amber, lime, orange, green, purple, sky) at 40% opacity for tags/labels only
- Apply `rgba(255, 255, 255, 0.7)` + backdrop-filter for sticky navigation
- Reserve `rgb(163, 163, 163)` for secondary / inactive states

**Don't:**
- Use Fraunces at weight 400 or 700 — the lightness is the aesthetic
- Use pure saturated colors as fills — always apply 40% transparency to tint chips
- Use shadows with spreads over 15px — keep elevation subtle
- Add dark surfaces or backgrounds — this is a light-only design
- Use uppercase or text transforms

---

## 8. Responsive Behavior

The full Tailwind breakpoint set (640/768/1024/1280/1536px) is present, indicating detailed per-breakpoint control:

- **<640px**: Single column, reduced padding, navigation likely collapses
- **640–1024px**: Two-column project grid, standard navigation
- **1024–1280px**: Wider grid, possible sidebar or multi-column layout
- **≥1280px**: Full desktop layout with max-width centering

Type sizes appear fixed (no detected responsive scaling), but generous line heights and the 32px lateral padding ensure comfortable reading at all widths.

---

## 9. Agent Prompt Guide

When recreating or referencing chester.how:

> "Design a personal portfolio with a serif/sans pairing: Fraunces weight 300 at 36px/−1.08px for headings, Inter weight 400 at 16px/−0.40px for body. Light palette: white canvas, near-black `#171717` primary text, `rgb(163,163,163)` for muted headings, `rgb(229,231,235)` borders. Frosted glass sticky nav using `rgba(255,255,255,0.7)`. Project cards at `rgb(250,250,250)` with Tailwind tint tags at 40% opacity (amber, lime, orange, green, purple, sky). Generous footer padding (144px). Full Tailwind breakpoint set. Blue `rgb(191,219,254)` focus rings."

---

*Generated by Sparkbites — extracted from live CSS analysis*
