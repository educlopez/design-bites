# henry.codes — Design System

## 1. Visual Theme & Atmosphere

henry.codes is a portfolio that takes a formal, typographically rigorous stance uncommon in developer portfolios. Built with Eleventy, it combines two contrasting fonts — **Louize Display** (a high-contrast display serif) and **Neue Montreal** (a geometric sans-serif) — in a system where uppercase is the default grammar, not an exception. The near-black on near-white palette uses a warm dark brown (`rgb(42, 39, 34)`) rather than pure black, lending the site an analogue quality. The defining structural moment is a footer that inverts the entire colour scheme — dark warm brown background with near-white text — creating a book-cover-like conclusion to the page. No shadows, no borders, no radii. Just type, spacing, and two surfaces.

## 2. Color Palette & Roles

**Base**
- Background: `rgb(250, 250, 250)` — clean near-white (very slightly warm)
- Primary text: `rgb(42, 39, 34)` — warm brown-black
- H1 text: `rgb(102, 102, 102)` — mid grey (the display serif in grey creates a ghost-like quality)
- H2 text: `rgb(159, 159, 159)` — light grey for secondary headings

**Footer inversion**
- Background: `rgb(42, 39, 34)` — the same dark brown as body text
- Text: `rgb(250, 250, 250)` — the same near-white as body background

**What's absent:** No accent colour. No brand colour. No coloured links. No semantic palette. No surfaces beyond the two used in body and footer. This is a pure two-colour design.

## 3. Typography Rules

Two fonts, strictly allocated.

| Element | Font | Size | Weight | Case | Tracking |
|---------|------|------|--------|------|----------|
| H1 | Louize Display | 30.72px | 400 | UPPERCASE | Normal |
| H2 | Neue Montreal | 12px | 400 | UPPERCASE | −0.12px |
| H3 | Neue Montreal | 20px | 400 | UPPERCASE | −0.2px |
| Body | Neue Montreal | 16px | 400 | Normal | Normal |
| `<p>` | Neue Montreal | 16px | 400 | UPPERCASE | Normal |
| Links | Neue Montreal | 16px | 400 | UPPERCASE | Normal |

**Louize Display** is used only for H1 — a high-contrast display serif in uppercase at 30.72px with a tight line-height of 0.9× (27.648px). This creates extremely dense, compressed display text — the heading sits below its own cap height. It's a typographic choice that signals design craft literacy.

**Neue Montreal** handles everything else — all uppercase. The `text-transform: uppercase` applied to `<p>` and `<a>` means body text also runs in all-caps. This unusual choice gives the site a printed/editorial quality — like reading a catalogue or monograph.

The H1 in grey (`rgb(102,102,102)`) while body text is dark brown creates an inverted hierarchy where the headline is quieter than the content — another unconventional choice.

## 4. Component Stylings

**No border radii** — the site has zero border-radius values. Every container is sharp-cornered.

**No shadows** — zero elevation beyond colour contrast.

**Navigation** — transparent background, uppercase links.

**Sections** — 16px padding on all sides, 80px bottom margin, 16px internal gap. The section bottom margin creates generous chapter separation.

**Footer** — inverted dark brown background, 16px horizontal / 48px bottom padding, with a negative bottom margin (`-176px`) that pulls subsequent content or acts as an overlapping design element.

**Aside** — `rgb(250, 250, 250)` background matching the page — blends into the layout without distinction.

## 5. Layout Principles

Extensive breakpoint set (15 breakpoints from 364px to 1512px) suggests an obsessively tuned responsive layout. The fine-grained breakpoints (364, 404, 504, 658, 900, 1000, 1064, 1099, 1100, 1200, 1270) indicate precise layout shifts at specific content widths — likely driven by typographic measure and grid column changes rather than generic device categories.

The 16px section padding creates a tight, newspaper-like gutter. Content is likely set in a narrow column (reading measure) at all sizes.

## 6. Depth & Elevation

The simplest elevation system possible: two surfaces.
1. **Light surface** — `rgb(250, 250, 250)` — page and aside backgrounds
2. **Dark surface** — `rgb(42, 39, 34)` — footer inversion

No shadows, no borders, no overlapping elements (except the negative footer margin). Depth is communicated solely through the light/dark surface contrast at the page's conclusion.

## 7. Do's and Don'ts

**Do:**
- Use Louize Display only for the H1, uppercase, with tight line-height below 1× (0.9)
- Set H1 in grey (`rgb(102,102,102)`) — the subordinate headline is intentional
- Apply uppercase to `<p>`, `<a>`, `<h2>`, `<h3>` — it's the default case
- Use `rgb(42,39,34)` as the dark colour (never pure `#000`)
- Invert the palette completely for the footer: dark background, light text

**Don't:**
- Add border radii — all corners are sharp
- Add shadows — the two-surface system handles depth
- Bold any text — weight 400 is used throughout without exception
- Introduce accent or brand colours
- Reduce the H1 line-height above 1× — the tight 0.9 is the typographic signature

## 8. Responsive Behavior

Fifteen carefully tuned breakpoints (364–1512px). This level of granularity suggests column-count changes and typographic scale adjustments at very specific widths — likely optimised through visual testing rather than systematic grid logic. The Louize Display H1 at ~30px needs careful control at narrow widths given its tight line-height. The all-uppercase prose remains legible to ~10px on mobile due to the letterform clarity of Neue Montreal.

## 9. Agent Prompt Guide

> Recreate henry.codes: near-white background `rgb(250,250,250)`, warm brown text `rgb(42,39,34)`. Use **Louize Display** uppercase for H1 at ~30px, weight 400, line-height 0.9 (text below its own cap height). Use **Neue Montreal** weight 400 for all other text — uppercase for headings, `<p>`, and `<a>`. No border-radius anywhere — sharp corners only. No shadows. Build a footer that fully inverts: `rgb(42,39,34)` background with `rgb(250,250,250)` text. H1 should render in `rgb(102,102,102)` grey — quieter than body text. Section spacing is 16px padding + 80px bottom margin. No accent colour — the only contrast is the two-tone light/dark surface flip.

*Generated by Sparkbites — extracted from live CSS analysis*
