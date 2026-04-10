# pranathiperi.com — Design System

## 1. Visual Theme & Atmosphere

Pranathi Peri's portfolio opens with a bold typographic statement that almost defies navigation — a 166px Instrument Serif heading rendered in deep indigo-violet against a matching page background. The design is high-contrast, bold-yet-refined, and structured around an unusual combination: expressive serif display set in a rich purple brand color, with monospaced body text that evokes terminal precision. The contrast between the expressive headline voice and the mono body creates a portrait of a designer who codes — or a coder with taste. A deep teal panel (`rgb(21,33,36)`) provides the second visual anchor, while a soft mint green offers relief.

## 2. Color Palette & Roles

**Brand / Primary**
- `rgb(67, 51, 182)` — Page/HTML background; deep indigo-violet (hero zone)
- `rgb(59, 44, 162)` — H1 heading color; slightly darker violet (renders on top of brand bg)

**Dark Panel**
- `rgb(21, 33, 36)` — Deep teal-black panel; used for a featured section or footer

**Light / Content Surfaces**
- `rgb(255, 255, 255)` → `rgb(245, 245, 245)` — A cascade of near-white surfaces; content sections built on light backgrounds
- `rgb(235, 247, 232)` — Soft mint green; accent surface, likely for a skills or highlight section

**Text**
- `rgb(255, 255, 255)` — Primary text on dark/brand backgrounds; all links use white
- `rgb(0, 0, 0)` — Base body color on light sections

**Supporting**
- `rgb(167, 168, 167)` — Mid-grey; likely used for subtle dividers or de-emphasized text

## 3. Typography Rules

A three-voice typographic system: massive Instrument Serif for the hero, system sans-serif for general body, and a custom **mono** typeface for body copy and links. The mono choice is the most distinctive decision — it brings a code-aesthetic to prose, intentionally blurring the line between designer and developer.

| Role | Family | Size | Weight |
|------|--------|------|--------|
| H1 / Hero display | Instrument Serif | 166.4px | 400 |
| Body / General | System sans-serif (ui-sans-serif) | 16px | 400 |
| Paragraphs | mono (custom) | 14px | 400 |
| Links | mono (custom) | 14px | 400 |

The 166.4px hero heading is essentially a typographic poster — it occupies most of the viewport, likely cropped or overflowing intentionally. Line height equals font size (1:1 ratio), creating a dense, stacked display block. Mono body text at 14px/24px has generous line height (1.71×) for readability.

## 4. Component Styling

**Links**: White text, transparent background. The `group` class pattern on links (e.g., `a.group "Email ↗"`) suggests arrow-appended link components with group-hover animations in Tailwind.

**Panels**: The dark teal panel (`rgb(21,33,36)`) and the brand violet (`rgb(67,51,182)`) serve as the two featured surface types — both dark, high-contrast, used for hero or feature sections.

**Mint card**: `rgb(235,247,232)` as a surface likely wraps a skills list or highlighted content block.

**No borders, no shadows, no border-radius detected.** The design relies entirely on color and typographic scale for structure.

## 5. Layout Principles

Built with Next.js and Tailwind CSS. No breakpoints were detected in the extracted CSS, which suggests either a single-column layout throughout, or responsive behavior driven by Tailwind utility classes rather than media query breakpoints captured by the extractor.

Tailwind's default spacing scale governs layout. The surface cascade (multiple near-white values from `#FFFFFF` to `#F5F5F5`) suggests a card-stacking layout where sections sit on progressively grounded white-to-light backgrounds.

## 6. Depth & Elevation

No shadows detected. No border-radius detected. Elevation is implied entirely through color transitions: from the vivid violet brand zone to the light near-white content sections to the dark teal feature panel. The design layers moods, not surfaces.

The transparency of links and CTAs (`rgba(0,0,0,0)` backgrounds) reinforces the flat, layered-color approach.

## 7. Do's and Don'ts

**Do:**
- Use the hero heading at 166px+ — scale is the entire point of the opening section
- Pair Instrument Serif (display) with mono (body); this pairing is the design's personality
- Apply the indigo-violet (`rgb(67,51,182)`) as a background zone, not just a text color
- Use white text exclusively on the violet and teal panels
- Use the mint green `rgb(235,247,232)` as a single accent surface — it should appear once

**Don't:**
- Don't reduce the hero heading below 100px — the poster scale is non-negotiable
- Don't substitute a sans-serif for the mono body copy — it changes the persona entirely
- Don't add border-radius or shadows; this system is deliberately flat
- Don't introduce warm colors — the palette is cool-violet, teal, and mint
- Don't use `rgb(59,44,162)` on a white background; it's calibrated for the violet surface only

## 8. Responsive Behavior

No breakpoints detected in the CSS extraction. This is consistent with a Tailwind-built layout using responsive utility classes (`sm:`, `md:`, `lg:`) that aren't captured as explicit media queries. The hero heading at 166.4px would need a significant `text-[clamp(...)]` or responsive size reduction for mobile — likely handled via Tailwind responsive prefixes. The layout is presumed single-column throughout.

## 9. Agent Prompt Guide

> Recreate the pranathiperi.com visual style. Page background is `rgb(67,51,182)` (deep violet) for the hero zone. H1 uses Instrument Serif at 160–170px, weight 400, color `rgb(59,44,162)` — slightly darker than the background for subtle contrast. Body paragraphs and links use a custom mono typeface at 14px/24px, white text on dark backgrounds. Content sections transition to near-white backgrounds (`#F9F9F9` to `#FFFFFF`). A deep teal panel `rgb(21,33,36)` anchors a featured section. One mint-green surface `rgb(235,247,232)` provides accent relief. No shadows, no border-radius, no hover color changes. The design is flat, poster-like, and typographically aggressive.

---

*Generated by Sparkbites — extracted from live CSS analysis*
