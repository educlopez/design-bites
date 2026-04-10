# uxtools.co — Design System

## 1. Visual Theme & Atmosphere

UX Tools reads as a carefully considered editorial product — warm, readable, and data-rich without feeling overwhelming. The canvas is a whisper-warm off-white (`#fffbf7`) that immediately distinguishes the site from sterile white-background SaaS. Body text lands in a warm dark gray (`#4a4844`) rather than black, creating a reading experience that feels like a premium print publication translated to screen.

The accent color — a muted terracotta-coral (`#c9624d`) — is used with surgical precision: for links, for emphasis, for the data "delta" indicators that are central to the site's UX tools comparison functionality. It's warm enough to feel human, restrained enough to feel professional. Built with a mature token system, Inter typeface, and a display font for headers.

## 2. Color Palette & Roles

**Backgrounds:**

| Role | Token | Value | Usage |
|------|-------|-------|-------|
| **Canvas** | `--bg-canvas` | `#fffbf7` | Page background |
| **Card** | `--bg-card` | `#ffffff` | Card surfaces |
| **Card inner** | `--bg-card-inner` | `#fafaf8` | Nested card backgrounds |
| **Callout** | `--bg-callout` | `#f5f4f0` | Highlighted blocks |

**Text:**

| Role | Token | Value |
|------|-------|-------|
| **Primary** | `--text-primary` | `#1a1a1a` |
| **Body** | `--text-body` | `#4a4844` |
| **Secondary** | `--text-secondary` | `#8a8680` |
| **Muted** | `--text-muted` | `#6b6560` |
| **Accent** | `--text-accent` | `#c9624d` |

**Interactive:**

| Role | Token | Value |
|------|-------|-------|
| **Link** | `--link` | `#a04d3c` (darker terracotta) |
| **Link hover** | `--link-hover` | `#c9624d` |
| **Delta background** | `--delta-bg` | `rgba(44,41,36,0.08)` |

## 3. Typography Rules

**Display / Headings:** Custom display font (`--font-display`) — likely a humanist or editorial face for hero and section titles.  
**Body:** Inter (`--font-inter`) — the workhorse for all readable copy.  
**Monospace:** Space Mono (`--font-space-mono`) — for code snippets or technical data.

| Selector | Size | Weight | Letter Spacing | Notes |
|----------|------|--------|----------------|-------|
| `h1` | 36px | 700 | -0.9px | Strong entry point with negative tracking |
| `h2` | ~28px | 600–700 | slight | Section anchors |
| Body | 16px | 400 | normal | Inter; comfortable and tested |
| Secondary | 14px | 400 | normal | Captions, metadata |
| Mono | varies | 400 | normal | Space Mono for data/code |

Weight 700 appears on headings — unlike many portfolios, UX Tools uses bold confidently. The display font layers on top for hero moments, Inter carries everything else.

**Notably absent:** Italic is used sparingly if at all; uppercase text-transform not detected.

## 4. Component Stylings

Rich token system revealed in CSS custom properties:

- **Cards** — `#ffffff` surface, `--card-radius` rounded corners, `--card-padding` internal spacing
- **Callout blocks** — `#f5f4f0` warm gray background; used for tips, highlights
- **Accent elements** — terracotta `#c9624d` for links, labels, and the comparison delta indicators
- **Delta badges** — `rgba(44,41,36,0.08)` tinted background on comparison data; `#4a4844` text
- **Navigation** — `--nav-height`, `--nav-padding-inline` tokens; transparent background over canvas
- **Borders** — `--border-card`, `--border-grid`, `--border-nav` — three distinct border contexts

**Layout tokens:**
- `--content-width` — readable content column width
- `--page-width` — full page constraint (1440px)
- `--section-gap` — vertical rhythm between sections
- `--hero-padding-block` — hero section top/bottom padding
- `--divider-margin` — spacing around horizontal rules

## 5. Layout Principles

- **Max width:** `--page-width: 1440px` / `--content-width` for text columns (~720–800px)
- Breakpoints at `280px`, `720px`, `1280px` — covers small mobile through large desktop
- Reading-optimized content width ensures comfortable line lengths for editorial content
- Grid-based comparison tables (the core product) likely use a fixed-column approach with `--card-margin-block` for rhythm

## 6. Depth & Elevation

Four-level background system creates clear elevation hierarchy:

1. **Canvas** `#fffbf7` — ground level
2. **Card** `#ffffff` — first elevation (slightly brighter)
3. **Card inner** `#fafaf8` — nested content (slightly recessed)
4. **Callout** `#f5f4f0` — emphasized/highlighted (warm gray)

Borders (`--border-card`) provide crisp delineation at each level. Shadow use is minimal — the warm background sequence does the depth work.

## 7. Do's and Don'ts

**Do:**
- Use the full four-level background system for card nesting — it creates clarity without shadows
- Apply terracotta `#c9624d` for all interactive and accent elements; it's the system's single warm signal
- Use Inter for all body copy; display font only for hero and major section titles
- Use Space Mono for any numerical or code data — it adds the right technical credibility
- Token-name everything: this system was built for consistency at scale

**Don't:**
- Use `#1a1a1a` (primary text) for body paragraphs — `#4a4844` (body) is the correct reading weight
- Add accent colors beyond terracotta — the warm neutrals do all supporting work
- Place cards directly on canvas without padding — `--card-padding` exists for a reason
- Use bold (700) for body text — reserve it for headings only

## 8. Responsive Behavior

| Breakpoint | Context |
|-----------|---------|
| `280px` | Small mobile |
| `720px` | Tablet / mid |
| `1280px` | Desktop |
| `1440px` | Wide (page-width cap) |

At mobile, comparison tables likely collapse to stacked card views. Content width narrows to full-viewport with padding.

## 9. Agent Prompt Guide

> "Design in the style of uxtools.co: warm off-white canvas `#fffbf7`, body text in `#4a4844`, primary headings in `#1a1a1a`, terracotta accent `#c9624d` for links and emphasis, four-level white/card surface hierarchy, Inter for body copy, display font for heroes, Space Mono for data, token-driven spacing and borders, editorial warmth over SaaS sterility — a thoughtful data-rich product aesthetic."

*Generated by Sparkbites — extracted from live CSS analysis*
