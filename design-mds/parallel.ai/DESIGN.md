# parallel.ai — Design System

## 1. Visual Theme & Atmosphere

Parallel.ai projects the measured confidence of enterprise AI infrastructure: clean, precise, and never loud. The palette is predominantly white and light grey with controlled dark zones that frame benchmark data and technical content. Warmth is deliberately absent — this is a product that wants to be trusted over time, not immediately delighted. Custom tokenized spacing and a purpose-built typeface signal that every decision was made, not defaulted to.

## 2. Color Palette & Roles

**Backgrounds**
- `rgb(255, 255, 255)` — Primary surface; most cards and sections
- `rgb(246, 246, 246)` — Secondary surface; section alternation
- `rgb(245, 244, 241)` — Warm off-white; asset/callout zones

**Structure & Chrome**
- `rgb(229, 229, 229)` — Border and divider color throughout
- `rgb(238, 238, 238)` — Bar chart backgrounds / chart rails
- `rgb(233, 240, 245)` — Subtle blue-grey; data highlight bands

**Content / Text**
- `rgb(24, 24, 24)` — Near-black body text and primary foreground
- `rgb(133, 132, 131)` — Subdued body / meta text
- `rgb(67, 67, 67)` — Secondary dark surface (dark sections)
- `rgba(34, 34, 34, 0.8)` — Translucent dark overlay
- `rgb(24, 24, 24)` — Darkest band surface (footer, hero dark)

**Accent / Interactive**
- `rgb(13, 110, 165)` — Primary blue; CTAs, links, interactive text
- `rgb(20, 55, 75)` — Hover darkening of primary blue
- `rgb(213, 110, 61)` — Orange hover on nav items
- `rgb(111, 162, 232)` — Data visualization fill (light blue)
- `rgb(143, 182, 204)` — Data visualization fill (muted blue-grey)
- `rgb(105, 190, 120)` — Success / positive indicator (green badge)

## 3. Typography Rules

A single custom family — **gerstnerProgramm** — handles every text role on the page. Named after the Swiss graphic designer Karl Gerstner, it carries a precise, Swiss-rationalist character. Code and technical output switches to **ftSystemMono**.

| Role | Size | Weight |
|------|------|--------|
| H1 / Hero | 36px | 500 |
| H2 / Section title | 26px | 500 |
| H3 / Label / Tag | 13px | 500 |
| Body | 16px | 400 |
| Code / Pre | 13px | 400 (ftSystemMono) |
| Link text | 13px | 400 |

No serif, no display fonts, no italic emphasis. Weight variation (400 vs 500) does all the hierarchy work. Letter-spacing is always `normal` — never tracked out.

## 4. Component Styling

**Buttons**: Transparent background; text colored `#0D6EA5`; hover shifts to `#14374B`. No fill, no border. Purely typographic CTAs.

**Cards / Asset panels**: `border-radius: 4px` or `8px`; extremely subtle layered shadow (`rgba(0,0,0,0.02–0.04)`) on lightweight cards; stronger `rgba(0,0,0,0.4)` drop shadow reserved for elevated content.

**Benchmark bars**: Two-layer system — a light rail `rgb(238,238,238)` with a fill in `rgb(111,162,232)` or `rgb(143,182,204)`. Purely data-driven, no decorative radius on bars.

**Nav**: Transparent background, `#181818` text, orange hover `rgb(213,110,61)` on items.

## 5. Layout Principles

A rigid custom token system defines all spacing: `--space-{N}` tokens from `0.125rem` to `5rem`. The max container width is `1504px`, with a dedicated machine panel constrained to `640px`. The main element applies `48px` horizontal padding on desktop.

Layout is columnar and grid-driven. No decorative whitespace — every gap is purposeful and derived from the token scale. Content stacks cleanly: hero, benchmark section, product section, footer.

## 6. Depth & Elevation

Three elevation levels:
1. **Flat** — most surfaces; no shadow
2. **Raised card** — `rgba(0,0,0,0.02–0.04) 0px 1–13px` triple-layered soft shadow
3. **Lifted** — `rgba(0,0,0,0.4) 0px 16px 16px` for modal-weight panels

Translucency is used sparingly: `rgba(34,34,34,0.8)` for a frosted dark overlay. No blur effects detected.

## 7. Do's and Don'ts

**Do:**
- Use `gerstnerProgramm` at weight 500 for any heading; never bold (700+)
- Pair `#0D6EA5` blue with white backgrounds for interactive elements
- Use the token spacing scale; don't introduce ad-hoc pixel values
- Reserve the dark band (`rgb(24,24,24)`) for footer or high-contrast hero sections
- Use orange hover only on nav — it's contextual, not a general accent

**Don't:**
- Don't use decorative border radius above `8px` — this system is sharp-cornered by intent
- Don't add shadows to text or nav items
- Don't mix serif fonts — there are none here
- Don't use saturated colors for backgrounds; accent blues are for interaction only
- Don't reduce type size below 13px

## 8. Responsive Behavior

An unusually fine-grained breakpoint ladder: `320, 360, 380, 400, 440, 480, 520, 580, 768, 1023, 1024, 1080`. The density of mobile breakpoints suggests precise layout reflows at nearly every 40–60px step below 600px — possibly driven by benchmark chart container resizing. The `--machine-container-width: 640px` token implies a dedicated panel that collapses at tablet widths.

## 9. Agent Prompt Guide

> Build a product section in the style of parallel.ai. Use `gerstnerProgramm` (fallback: system sans-serif) at weight 500 for headings (36px hero, 26px section). Body text is `rgb(24,24,24)` at 16px/400. Background is pure white; section dividers use `rgb(246,246,246)`. Interactive text links are `rgb(13,110,165)`, darkening to `rgb(20,55,75)` on hover. Border radius is 4–8px max. Spacing follows an 8-point scale capped at 80px. No shadows on text; subtle layered box-shadow only on cards. No decorative color — accent blue is reserved for CTAs and data fills.

---

*Generated by Sparkbites — extracted from live CSS analysis*
