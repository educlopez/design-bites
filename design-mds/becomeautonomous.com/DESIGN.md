# becomeautonomous.com — Design System Reference

## 1. Visual Theme & Atmosphere

Become Autonomous is a Next.js financial/autonomy platform that leads with editorial scale. The dominant design gesture is typographic: display headings set in the custom typeface **Diatype** at 170px with light weight (300) and extreme negative tracking create an almost poster-like presence. The background is a warm near-white (`#f2f2f2`) that reads as off-paper — not clinical white, but soft and considered. Electric blue (`rgb(0, 0, 200)`) punctuates as the brand action colour — a bold, unapologetic choice that references early web while feeling deliberate. The system is built on a rigorous fluid typography scale using `clamp()` values, signalling careful engineering beneath the expressive surface. The overall atmosphere is confident and intellectual — a publication-meets-product sensibility.

## 2. Color Palette & Roles

| Role | Value | Usage |
|------|-------|-------|
| Page background | `rgb(242, 242, 242)` | Body — warm off-white |
| Pure white | `rgb(255, 255, 255)` | Cards, elevated surfaces |
| Light section fill | `rgb(242, 242, 242)` | Thinking-section panels |
| Divider / skeleton | `rgb(148, 163, 184)` | Slate-400, loading states, separators |
| Brand / CTA | `rgb(0, 0, 200)` | Links, skip-links, primary buttons |
| True black | `rgb(0, 0, 0)` | Body text, borders |

The palette is intentionally minimal: neutral ground with a single electric-blue accent. The slate-400 value (`#94a3b8`) appears to be a Tailwind-influenced utility colour used for secondary UI elements. No warm accent, no gradient — the blue does all the tonal work.

## 3. Typography Rules

**Primary typeface:** `diatype` (ABCDiatype) — a geometric grotesque with a distinctive mechanical quality. Loaded in Regular and Mono variants.

**Mono typeface:** `diatypeMono` — used exclusively for labels and metadata (eyebrow text), uppercase with `0.22px` tracking.

**System fallback:** `-apple-system, BlinkMacSystemFont, "Segoe UI", "Helvetica Neue", Arial, sans-serif`

| Level | CSS Variable | Clamp Range | Weight | Tracking |
|-------|-------------|-------------|--------|----------|
| Display XXL | `--font-size-display-xxl` | 60px → 170px | 300 | −9.35px |
| H1/H2 | `--font-size-h1/h2` | 42–96px → 62–64px | 300 | tight |
| Body | — | 16px | 300–500 | −0.4px |
| Eyebrow / label | `--font-size-eyebrow` | 11px → 12px | 300 | +0.22px uppercase |

The entire scale is fluid — every level uses `clamp()`, enabling smooth scaling between 320px and 1600px viewports. Weight 300 throughout creates a consistent lightness; heavier weights (500) appear only on paragraphs and interactive elements for contrast.

## 4. Component Stylings

**Primary buttons / CTAs:** White background (`#fff`), black text, subtle shadow (`rgba(0,0,0,0.15) 0px 2px 8px`), `100px` border-radius (pill). Active tab states drop to transparent background with white text at 70% opacity on dark sections.

**Links:** `rgb(0, 0, 200)` background with white text — an inverted, badge-like link style that's distinctive and bold.

**Focus states:** `rgb(0, 0, 189) solid 1px` outline — consistent brand-blue focus ring, meets WCAG contrast on white backgrounds.

**Tabs:** Ghost style on dark sections (transparent bg, semi-transparent white text); solid style on light sections (white bg, black text, shadow).

**Hover:** Tab hover shifts text opacity from 70% to ~89% — a subtle luminosity lift without colour change.

## 5. Layout Principles

Nine breakpoints span from 320px to 1600px: `320, 480, 768, 769, 960, 961, 1280, 1599, 1600`. This is one of the most granular responsive scales in the dataset — every major device width is addressed. Section padding is `52px` all sides. Main content padding is `16px` horizontal with `100px` bottom. Footer carries `48px` top/bottom margin. The fluid type scale means layout transitions feel smooth rather than abrupt.

## 6. Depth & Elevation

One shadow: `rgba(0, 0, 0, 0.15) 0px 2px 8px 0px` — used on the active/elevated tab component and card surfaces. Soft, low-altitude lift. No multilayer shadow system. Depth is primarily communicated through the warm background vs white card contrast and the bold electric-blue accent cutting through neutral surfaces.

## 7. Do's and Don'ts

**Do:**
- Use `clamp()` for all typographic sizes — the fluid scale is central to this system's craft
- Apply `diatype` weight 300 for display text; reserve 500 for interactive labels
- Use electric blue (`rgb(0,0,200)`) exclusively for primary actions — never decoratively
- Uppercase monospaced labels for metadata/eyebrow text with positive tracking
- Maintain the warm off-white (`#f2f2f2`) as the ground — avoid pure white pages

**Don't:**
- Break the fluid scale with fixed pixel sizes on headings
- Use more than one accent colour — the blue carries full brand weight
- Apply the card shadow to non-elevated components — it signals interactivity
- Use Diatype Regular (400) for body — 300 is the intended weight throughout
- Mix the mono variant into display contexts — it's a metadata-only register

## 8. Responsive Behavior

Nine breakpoints give extremely fine-grained control. Critical transitions: 480px (mobile landscape), 768/769px (tablet), 960/961px (tablet-large), 1280px (desktop), 1600px (wide). The `clamp()` type scale handles in-between sizes gracefully. Section padding (`52px`) likely collapses at mobile breakpoints via media queries not captured in this extraction.

## 9. Agent Prompt Guide

> "Design in the style of becomeautonomous.com: warm off-white canvas (`#f2f2f2`), Diatype light (300) typeface at display scale with extreme negative tracking. Electric blue (`rgb(0,0,200)`) as the sole accent colour for all CTAs and links. Fluid typography using `clamp()` from mobile to wide desktop. White pill-shaped cards with a subtle `8px` shadow. Uppercase mono labels for metadata. No decorative elements — let scale and weight carry the visual hierarchy."

---

*Generated by Sparkbites — extracted from live CSS analysis*
