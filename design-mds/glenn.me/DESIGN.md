# Glenn.me — Design Language Reference

## 1. Visual Theme & Atmosphere

Glenn.me is a personal site built in Framer that achieves something rare in the portfolio genre: restraint as a statement. The design is almost architecturally minimal — pure white canvas, pure black text, a single serif typeface, no shadows, no decorative elements. It communicates through what it removes rather than what it adds.

The prevailing mood is deliberately quiet. Newsreader, a contemporary optical-size serif, gives the typography a literary quality — this is someone who thinks carefully about what they put on the page. The use of `rgba(0,0,0,0.66)` for headings (rather than full black) creates a perceptual softening that makes the text feel considered rather than blunt.

This is a site that trusts white space completely.

---

## 2. Color Palette & Roles

**Foundation**
- `rgb(255,255,255)` — Pure white; page background, all surfaces
- `rgb(0,0,0)` — Pure black; default text and borders

**Text Opacity Variants**
- `rgba(0,0,0,0.66)` — H1 headings: softened black, slightly withdrawn; creates editorial restraint
- `rgba(0,0,0,0.1)` — Subtle surface (`framer-1w1k45k`): near-invisible tint for barely-there separation

**Links**
- `rgb(0,0,238)` — Browser-default blue, unmodified; deliberately neutral, signals that links haven't been "designed over"

**Buttons**
- White background, black border at rest; opacity `0` (invisible) by default — buttons reveal only on interaction
- Focus outline: `rgb(0,95,204) auto 1px` — system focus ring, unmodified

**What's absent:** No brand color. No accent. No gray scale beyond the opacity variants. The entire site lives in black, white, and their transparent forms. The browser-default link blue is left intact — a choice that signals confidence over convention.

---

## 3. Typography Rules

Glenn.me uses a single typeface: **Newsreader**, a contemporary serif designed for long-form reading and available via Google Fonts. The fallback is `"Newsreader Placeholder"` — a size-matched system font loaded during FOUT.

| Element | Size | Weight | Line Height |
|---------|------|--------|-------------|
| H1 | 24px | 400 | 36px |

The H1 at weight 400 (regular) is unusual — most sites bold their headlines. Here, the regular-weight serif creates an editorial tone closer to a book than a marketing page. The 36px line height on 24px text (1.5× ratio) adds generous breathing room even at moderate size.

No secondary typeface. No monospace. No sans-serif. The serif holds the entire design together, which means every word choice and typographic decision carries more weight.

**Framer generation note:** Built with `generator:Framer bbed9c4` and Framer Motion — the site uses Framer's component model throughout.

---

## 4. Component Styling

**Surfaces**
- All surfaces are white; distinction between sections comes from content rhythm, not background color
- `rgba(0,0,0,0.1)` tint used for one subtle container (`framer-1w1k45k`) — effectively invisible at casual glance, present for layout scaffolding

**Buttons**
- Default opacity is `0` — the button exists in the DOM but is visually hidden until triggered
- On focus: blue system outline appears (`rgb(0,95,204) auto 1px`)
- This pattern suggests buttons are used as invisible click targets layered over larger visual areas — a Framer interaction pattern

**Border Radii**
- `32px` — Generous, modern rounded rectangle (for pill-adjacent cards or tags)
- `100px` — Full pill shape

The combination of 32px and 100px radii suggests a two-tier rounding system: rounded containers and pill badges, consistent with clean personal-site conventions.

---

## 5. Layout Principles

No CSS custom properties for layout or spacing — Framer manages all layout logic in its runtime. The structural decisions are made in Framer's canvas, not in CSS tokens.

Breakpoints are Framer's standard set: `679.98`, `680`, `809`, `810`, `999.98`, `1199` — six breakpoints covering mobile, tablet, and desktop with graceful edge handling around each threshold.

Content is likely centered with consistent horizontal padding, the type doing all the structural work.

---

## 6. Depth & Elevation

No box-shadows detected. No gradients. No blurs or filters.

The site achieves depth through opacity alone: `rgba(0,0,0,0.66)` text feels closer than `rgba(0,0,0,0.1)` surfaces; the eye reads opacity as proximity. This is minimalist depth — entirely perceptual, zero decoration.

Framer Motion handles any dimensional interactions (hover lifts, page transitions) in JavaScript, not CSS, which is why the static CSS data shows no elevation tokens.

---

## 7. Do's and Don'ts

**Do**
- Use `rgba(0,0,0,0.66)` for primary display text — not full black; the restraint is deliberate
- Trust white space completely; do not fill empty areas with decorative elements
- Keep Newsreader at regular weight (400) for headings — the lightness is the statement
- Use the `100px` border radius for pill elements, `32px` for container rounding
- Leave browser-default blue (`rgb(0,0,238)`) on links; over-styling them would break the aesthetic

**Don't**
- Introduce any accent or brand color — this design has none by choice
- Bold the headlines; weight 400 is the intentional typographic voice
- Add shadows or overlays; depth comes from opacity, not elevation effects
- Use more than one typeface; Newsreader's quiet authority depends on its singularity

---

## 8. Responsive Behavior

Six breakpoints ensure careful responsive handling: the site adapts at both narrow mobile (≤679px) and standard desktop (≥1200px) transitions. Framer's built-in responsive canvas handles layout reflow.

Framer Motion likely manages scroll-triggered entrance animations and hover interactions — neither visible in the CSS layer.

---

## 9. Agent Prompt Guide

> "Design in the style of Glenn.me: pure white background, pure black text at `rgba(0,0,0,0.66)` opacity. Single typeface: Newsreader serif, weight 400 (never bold). No brand color, no accent, no gradients, no shadows. Browser-default blue for links — unmodified. Border radius `32px` on containers, `100px` for pills. White space is the primary design element. No decorative elements of any kind. The aesthetic is editorial minimalism: quieter than quiet, trusting the reader completely."

---

*Generated by Sparkbites — extracted from live CSS analysis*
