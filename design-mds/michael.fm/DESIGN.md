# michael.fm — Design System

## 1. Visual Theme & Atmosphere

michael.fm is a personal site that achieves personality through restraint and precision. Built with Geist Sans — Vercel's typeface — the entire typographic system collapses to a single font at a single size (16px), with variation coming only from weight and the unusual choice to lowercase `h2` elements via `text-transform: lowercase`. The color system is similarly compressed: a warm gray gradient background with zinc neutrals and only a small set of code syntax colors for technical content. What makes the design memorable is its use of physical depth: a deep multi-layered box-shadow on primary elements creates a 3D card or floating panel effect that is theatrical compared to the otherwise minimal chrome. The `--radius: 24` and `--gradient` values suggest a pill-heavy, glassmorphism-adjacent aesthetic for UI cards.

## 2. Color Palette & Roles

**Background**

| Role | Variable | Value | Notes |
|---|---|---|---|
| Page start | `--background-start-rgb` | `rgb(214, 219, 220)` | Cool gray-blue |
| Page end | `--background-end-rgb` | `rgb(255, 255, 255)` | Fades to white |
| Base bg | `--background` | `#f2f2f2` | Flat light gray |
| Foreground | `--foreground-rgb` | `rgb(0, 0, 0)` | Pure black text |

**Zinc scale (UI neutrals)**

| Variable | Value | Role |
|---|---|---|
| `--zinc-100` | `#f4f4f5` | Lightest surface |
| `--zinc-200` | `#e4e4e7` | Borders, dividers |
| `--zinc-300` | `#d4d4d8` | Hover states |
| `--zinc-400` | `#a1a1aa` | Muted text |
| `--zinc-500` | `#71717a` | Secondary text |
| `--zinc-600` | `#52525b` | Tertiary |
| `--zinc-700` | `#3f3f46` | Dark labels |
| `--zinc-800` | `#27272a` | Strong text |
| `--zinc-900` | `#09090b` | Near-black |

**Alpha variants (for layering):**
`--zinc-900-8` through `--zinc-900-20` — zinc-900 at 8%, 10%, 16%, 20% opacity for subtle overlays and borders.

**Syntax highlighting (code blocks):**
`--sh-class` (#2d5e9d), `--sh-string` (#007f7a), `--sh-keyword` (#e02518), `--sh-jsxliterals` (#6266d1), `--sh-property`/`--sh-entity` (#e25a1c), `--sh-comment` (#a19595), `--sh-sign` (#8996a3).

**Accent:** `--red-500` (`#ef4444`) — sparse, likely for error states only.

## 3. Typography Rules

| Selector | Font | Size | Weight | Transform | Notes |
|---|---|---|---|---|---|
| `h2` | Geist Sans | 16px | 600 | `lowercase` | Headings are body-sized, lowercased |
| `body` | Geist Sans | 16px | 400 | none | 24px line-height |
| `a` | Geist Sans | 16px | 400 | none | Matches body exactly |

**Philosophy:** The entire site uses one font, one size. The only typographic differentiation is weight (400 vs 600) and the radical choice to lowercase headings. This creates a flatness and informality that signals personal/portfolio context — "this is me, not a brand." No display fonts, no type scale, no hierarchy through size.

**Absent:** Serif typefaces, large display headings, tracked uppercase, decorative styles.

## 4. Component Stylings

**Cards / floating panels**
- `--radius: 24` — large rounded corners
- `--gradient`: `linear-gradient(0deg, hsla(0,0%,100%,.2), hsla(0,0%,100%,0) 50%, hsla(0,0%,100%,.3))` — a subtle glass highlight effect
- Border: `--border: 1` with zinc-based border colors

**Deep shadow (primary feature):**
`rgba(0,0,0,0.39) 0 4px 9px, rgba(0,0,0,0.34) 0 17px 17px, rgba(0,0,0,0.2) 0 39px 23px, rgba(0,0,0,0.06) 0 69px 28px, rgba(0,0,0,0.01) 0 108px 30px` — a five-layer shadow that extends to 108px, creating a dramatic 3D card lift effect.

**Interactive links**
- Default: pure black text, transparent bg
- Hover: not captured — likely subtle
- Focus: `rgb(0, 95, 204) auto 1px`

**Navigation:** Links appear as plain text with no visible decoration.

## 5. Layout Principles

Sections use `padding: 8px 112px 64px` with `gap: 32px` — very large horizontal gutters (`112px`) suggesting a narrow centered column on a wide viewport. Body and main are zero-padded. The `32px` gap between section children creates a card-list or grid layout.

**Breakpoints:** `600px`, `700px`, `768px`, `900px`, `1000px`, `1280px`, `1300px` — a dense responsive progression spanning from compact mobile to wide desktop.

**Scale transform variables** (`--scale-1` through `--scale-6`) with values like 0.35, 0.65, 1, 1.5, 2 suggest animated or stacked card layouts where items are scaled by position (e.g., a deck of cards or carousel).

## 6. Depth & Elevation

Two distinct elevation modes:

**Dramatic elevation (feature):** The five-layer shadow reaching 108px creates a floating card that would cast a shadow as if the element is physically lifted ~10–20px off the surface. This is the visual signature of the site.

**Subtle elevation (UI chrome):**
- `rgba(9,9,11,0.03) 0 0 0 1px, ...` multi-step micro-shadow — a stacked, nearly invisible border-shadow combination at 3–6% opacity for UI components.
- `rgba(0,0,0,0.05) 0 2px 4px inset` — inset for pressed states.

The contrast between these two modes is intentional: feature surfaces float dramatically; UI chrome nearly disappears.

## 7. Do's and Don'ts

**Do:**
- Apply `text-transform: lowercase` to all heading elements — it's the site's typographic signature
- Use the five-layer deep shadow on featured cards — it's the visual hook
- Use zinc alphas (`--zinc-900-8` through `--zinc-900-20`) for subtle borders and overlays
- Keep all body, heading, and link text at 16px — the design refuses typographic hierarchy through size
- Apply `--gradient` as a glass highlight on `--radius: 24` (large-radius) cards

**Don't:**
- Increase font sizes beyond 16px for headings — it breaks the aesthetic flatness
- Add color accents beyond zinc + `#ef4444` (red errors) + code syntax colors
- Use the dramatic shadow on small UI elements — reserve it for feature/hero cards
- Use uppercase text transforms — only lowercase is employed
- Add decorative borders with width >1px

## 8. Responsive Behavior

Seven breakpoints from `600px` to `1300px` suggest the `112px` section gutters collapse significantly:
- Below `768px`: gutters likely drop to `16–24px`
- Below `600px`: single-column layout
- The `--scale-*` variables suggest a card deck or stacked layout that adapts transform values at each breakpoint
- `700px` and `900px` are non-standard — likely tied to the scale-card layout's comfortable viewing widths

The gradient background (`214, 219, 220 → 255, 255, 255`) likely remains consistent across all sizes.

## 9. Agent Prompt Guide

**Quick reference:**
- Background: `#f2f2f2` flat / gradient from `rgb(214,219,220)` to `white`
- Text: `rgb(0,0,0)` primary / `#71717a` secondary / zinc scale
- Font: Geist Sans, 16px throughout, weight 400/600 only
- Headings: `text-transform: lowercase`
- Signature: five-layer deep box-shadow (to 108px)
- Radius: 24px cards + `9999px` pills

**Prompt starters:**
- "Design a portfolio project card in michael.fm style: `#f2f2f2` background, Geist Sans 16px, lowercase bold title, five-layer deep shadow, 24px corners, glass gradient overlay."
- "Build a minimalist nav in this style: single font at 16px/400, pure black text, zinc-200 dividers, no decoration."
- "Create a music track listing: Geist Sans throughout, lowercased labels at 600 weight, zinc alpha borders at 0.1 opacity, subtle inset shadow on active state."

*Generated by Sparkbites — extracted from live CSS analysis*
