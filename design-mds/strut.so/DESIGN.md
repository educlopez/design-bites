# strut.so — Design System

## 1. Visual Theme & Atmosphere

Strut.so feels like a studio visit — warm, physical, unhurried. Where most presentation-tool startups lean into dark glass or electric blue, Strut chooses an entirely different register: the background is a muted sand (`rgb(229, 223, 213)` — named `--oatmeal` in the code), and the typographic workhorse is GT Pressura Standard at display sizes that would feel at home on a printed book jacket. The effect is tactile rather than digital. You sense paper and ink, not glass and light.

The amber/amber-gold custom cursor (`rgb(255, 181, 70)`) brings the only warmth into the palette — a blink of energy in an otherwise settled, editorial space. This is a product confident enough to be quiet.

## 2. Color Palette & Roles

| Role | Value | CSS Variable | Usage |
|---|---|---|---|
| Canvas / background | `rgb(229, 223, 213)` | `--oatmeal` | Page background, mobile menu |
| Primary text | `rgb(51, 51, 51)` | — | All headings, body copy |
| Secondary / link | `rgba(0, 0, 0, 0.55)` | — | Navigation links, secondary labels |
| Link hover | `rgba(0, 0, 0, 0.8)` | — | Slightly darker on hover |
| Accent / cursor | `rgb(255, 181, 70)` | — | Custom cursor indicator |
| Overlay | `rgba(0, 0, 0, 0.5)` | `--border-color: #00000080` | Image overlays, section dividers |
| Transparent grid | `rgba(255, 255, 255, 0.1)` | — | Subtle grid-image highlights |

The named custom property `--oatmeal` says everything about brand intent: warm, natural, food-adjacent. No blues, no purples, no tech-cold neutrals.

## 3. Typography Rules

**Display/Headings:** `GT Pressura Standard` — a contemporary geometric that reads as "designed" without being austere. At 104px with a tight 96px line-height (line-height < font-size), it achieves the condensed block-letter quality of editorial typography.

**Body:** `Inter` — the workhorse, kept at small sizes and low visual weight.

| Element | Size | Weight | Line Height |
|---|---|---|---|
| H1 / H3 | 104px | 400 | 96px (tight) |
| H2 | 68px | 400 | 68px (1:1) |
| Body | 14px | 400 | 20px |
| Paragraphs | 20px | 400 | 28px |
| Links/nav | 14px | 400 | 20px |

The display type uses a line-height *shorter* than its font size (96px for 104px text), creating the stacked, compressed feel of a print poster. This is intentional and defining — do not "correct" it to 1.2 or 1.5. Body text is split into two: Inter at 14px for UI chrome and at 20px for readable content paragraphs.

No font weights above 400 are used anywhere in the system.

## 4. Component Stylings

- **Navigation links:** Semi-transparent (`rgba(0,0,0,0.55)`), brightening to `rgba(0,0,0,0.8)` on hover — a restrained, analog feel.
- **Cursor:** A custom circular element in amber (`rgb(255, 181, 70)`) with `--oatmeal` text, adding kinetic brand personality.
- **Border radii:** `80px` and `48px` — used on pill-shaped elements (likely CTAs or feature badges), large and generous in proportion to the massive display type.
- **No shadows** detected anywhere — the design is entirely flat. Depth comes from color area and scale contrast.
- **Mobile menu:** Shares the `--oatmeal` background, maintaining the warm canvas even at small sizes.
- **Grid image boxes:** `rgba(255,255,255,0.1)` — frosted white-on-warm, barely visible.

## 5. Layout Principles

- Main content: `padding: 0 0 64px 80px` — a prominent left offset creating an editorial column feel.
- Header: `padding: 0 24px` — slim horizontal inset.
- Stack: **Webflow** + **GSAP** — indicating heavy animation involvement. Layout is Webflow-grid based; motion is GSAP-driven.
- Breakpoints: `479px`, `767/768px`, `991px` — standard Webflow responsive tiers (mobile portrait, mobile landscape, tablet, desktop).
- Custom properties `--margin-desktop: 0px` and `--margin-tablet: 40px` suggest the main content shifts inward on tablet but bleeds full-width on desktop.

## 6. Depth & Elevation

Zero shadows, zero elevation. Strut.so achieves its sense of depth through **scale contrast** alone: 104px headlines next to 14px navigation create enormous visual hierarchy without any Z-axis manipulation. The semi-transparent overlays (`rgba(0,0,0,0.5)`) on images are the only layering mechanism. This reinforces the flat, print-inspired aesthetic.

## 7. Do's and Don'ts

**Do:**
- Use `--oatmeal` (`rgb(229, 223, 213)`) as the constant background tone — it defines the brand temperature.
- Set display headings in GT Pressura Standard at 400 weight with tight line-heights (≤1.0).
- Use Inter for all body and UI text; keep it small (14px) for chrome, larger (20px) for reading content.
- Apply large pill radii (`48–80px`) to CTAs.
- Let the amber cursor accent (`rgb(255, 181, 70)`) be the only saturated color.

**Don't:**
- Add shadows or elevation — the design is intentionally flat.
- Increase font weights — no bold in the system.
- Use cool neutrals (grey, slate, blue) — every neutral should read warm.
- Scale the display type down aggressively; its size is the design.
- Override the tight line-height on headings.

## 8. Responsive Behavior

Webflow's four-tier system: `<479px` (mobile portrait), `480–767px` (landscape), `768–991px` (tablet), `992px+` (desktop). At tablet, `--margin-tablet: 40px` insets the main column. At mobile, the custom cursor disappears and navigation collapses to a slide-in menu that inherits the oatmeal canvas. Display font sizes scale down significantly below tablet — the 104px hero becomes manageable through Webflow's responsive scaling tools.

## 9. Agent Prompt Guide

> Build a Strut.so-style site: warm oatmeal background (`rgb(229,223,213)`), GT Pressura Standard for display headings at 104px with line-height 96px (tighter than font size), Inter for body. No shadows, no elevation, entirely flat. Single amber accent (`rgb(255,181,70)`) for interactive highlights. Semi-transparent links at `rgba(0,0,0,0.55)`. Large pill radii (48–80px) on CTAs. Think print editorial translated to web — quiet, warm, confident.

---

*Generated by Sparkbites — extracted from live CSS analysis*
