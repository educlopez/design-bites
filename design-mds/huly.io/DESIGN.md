# huly.io — Design System

## 1. Visual Theme & Atmosphere

Huly is a next-generation project management platform, and its site communicates that ambition through a sophisticated dark interface that blends code aesthetics with product confidence. The base is near-black (`rgb(9, 10, 12)`) — warmer than pure black, with a barely detectable cool tint. This creates a surface that feels like a high-quality OLED display.

The defining design decision is the **dual-font hierarchy**: headings use a custom monospace (`__esbuild_b38aaf`/Menlo-fallback) at extreme sizes with aggressive negative tracking, while body text uses Inter. This split persona — typewriter-machine headings paired with clean humanist body — signals a product for people who write code and also manage teams.

Syntax highlighting tokens in custom properties (via Shiki) reveal the site's soul: it's built by developers, for developers, and the design reflects that technical pride. The vibrant accent palette — electric blue, neon red-pink, green, orange — maps directly to code token colours.

## 2. Color Palette & Roles

**Background / Canvas**
- `rgb(9, 10, 12)` — Primary canvas; near-black with warm undertone
- `rgb(11, 13, 16)` — H2 text and slightly elevated dark surface
- `rgb(17, 17, 17)` / `rgb(48, 50, 54)` — Mid-dark surfaces for panel depth

**Light Surfaces (within dark sections)**
- `rgb(250, 250, 250)` / `rgb(246, 246, 246)` / `rgb(239, 239, 240)` — Bright card surfaces in UI preview areas; used to show mock app UI contrast

**Primary Accent**
- `rgb(61, 126, 255)` — Primary blue; CTA buttons, links, active states, hover on nav links (`rgb(93, 136, 220)`)

**Accent Spectrum (code token colours repurposed as UI accents)**
- `rgb(255, 77, 77)` — Red; status indicators, error-adjacent UI
- `rgb(86, 131, 218)` — Muted blue; secondary data bars
- `rgb(255, 137, 100)` — Orange; parameters, warm indicators
- `rgb(191, 106, 251)` — Purple; constants in syntax highlighting
- `rgb(71, 209, 140)` — Green; string tokens and success signals
- `rgb(255, 77, 137)` — Pink; keyword/operator colour

**Text**
- `rgb(255, 255, 255)` — Primary text on dark backgrounds
- `rgb(48, 50, 54)` — Secondary/muted text

## 3. Typography Rules

Two typefaces handle distinct roles:

**Headings: Custom Monospace (esbuild/Menlo fallback)**
- H1: 84px / 600 / −3.36px tracking / line-height 75.6px (compressed — shorter than font size)
- H2: 80px / 600 / −4px tracking / 64px line-height — extraordinarily tight
- H3: 28px / 400 / −0.56px tracking

The compressed line-height on large headings (smaller than font size) is a deliberate choice to create stacked, block-like typographic structures. Combined with the monospace typeface, headings feel like terminal output.

**Body: Inter**
- Body: 16px / 400 / 24px line-height
- Paragraphs: 18px / 400 / −0.72px tracking — slightly tracked in, refined
- Buttons: 14px / 400 / 21px line-height

**The separation is absolute.** Monospace for headings, humanist sans for everything else. Never mixed within a hierarchy level.

## 4. Component Stylings

**Buttons:** Transparent background by default, white text and border. Hover state on nav links shifts to `rgb(93, 136, 220)` — a blue softening, not a background fill.

**Code blocks:** Shiki syntax highlighting with full token colour set. Background `#111112`, foreground `#f9fafa`. This is the centrepiece UI component — treated as first-class design, not an afterthought.

**Cards / Panels:** Light surfaces (`rgb(246–250, 246–250, 246–250)`) inside the dark canvas create inset "app preview" areas. These use `rgb(48, 50, 54)` as a panel surface.

**Shadows:** Pure black drop shadows — `rgba(0,0,0,0.5) 0px 14px 20px` for deep elements, `rgba(0,0,0,0.15) 0px 4px 6px` for mild lift. No coloured shadows — darkness only.

**Border radii:** 4px (micro elements), 10px, 14px, 20px, 30px, `9999px` (pills).

**Hero mask:** CSS custom properties (`--hero-mask-x`, `--hero-mask-y`, `--hero-mask-size: 300px`) reveal a reveal/spotlight mask effect on the hero — a pointer-tracked glow area.

## 5. Layout Principles

Built with **Next.js + Tailwind CSS**. Sections have 184px top padding — generous vertical breathing room. The layout is primarily single-column for content sections with multi-column feature grids inside.

The hero section (`section.hero`) explicitly uses the dark background colour. Footer is minimal: 17px padding — almost no footer footprint.

**Breakpoints:** 413px, 639px, 767px, 1023px, 1279px/1280px, 1439px — a full 7-point responsive scale consistent with Tailwind's default breakpoint system.

## 6. Depth & Elevation

Elevation is achieved exclusively through:

1. **Dark-to-darker layering:** Background `rgb(9,10,12)` → surface `rgb(48,50,54)` → panel `rgb(17,17,17)` — depth through darkening, not lightening
2. **Strong black drop shadows:** 14–25px blur, 0.35–0.5 opacity — heavier than typical SaaS sites
3. **Light inserts:** Bright card surfaces (`rgb(246–250, 246–250)`) inside dark panels create inverted depth — islands of light
4. **Hero spotlight mask:** Pointer-tracked mask suggests a dynamic lighting source over static content

No elevation via border or inset glow. Pure shadow and contrast.

## 7. Do's and Don'ts

**Do:**
- Use the custom monospace for all heading levels — never Inter for H1/H2.
- Apply aggressive negative letter-spacing (−3px to −4px) on large headings.
- Compress line-height below font-size on large display headings.
- Use `rgb(61, 126, 255)` as the singular primary accent. Keep the vivid colour palette contained to product previews and code contexts.
- Build shadows with pure black opacity — no coloured shadows.
- Use 184px+ section padding to create breathing room.
- Apply the spotlight/mask CSS trick on the hero section.

**Don't:**
- Mix the monospace typeface into body text.
- Use colours outside the code-token palette as decorative accents.
- Use light surfaces for primary backgrounds — they are strictly for inset content areas.
- Add rounded corners larger than 30px — max is 30px except for pill elements.
- Introduce gradients — the dark canvas is flat, depth comes from shadows.

## 8. Responsive Behavior

Full 7-breakpoint Tailwind scale from 413px to 1439px. The 413px breakpoint catches small phones; 639px covers standard mobile; 767px is tablet portrait; 1023px–1279px covers laptop range; 1439px is wide desktop.

At mobile, the 80–84px monospace headings almost certainly scale down significantly. The section's 184px top padding likely collapses at tablet. The code preview component may collapse from multi-column to single-column below 1023px.

## 9. Agent Prompt Guide

> Design in the style of huly.io: near-black canvas (`rgb(9,10,12)`), dual-font system — custom monospace for all headings (84px H1, 80px H2, both 600 weight with −3.5px to −4px tracking and sub-font-size line-heights), Inter for body. Primary accent is electric blue `rgb(61,126,255)`. Code preview components use Shiki token colours: purple constants, red-pink operators, green strings, orange parameters. Shadows are pure black, heavy (50% opacity at 14–20px). Inside dark sections, embed light-surface card islands (`rgb(246–250)`). Section spacing: 184px top. Breakpoints: Tailwind standard 7-point scale. Hero has a pointer-tracked spotlight mask effect via CSS custom properties.

---

*Generated by Sparkbites — extracted from live CSS analysis*
