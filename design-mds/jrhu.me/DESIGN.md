# jrhu.me — Design System

## 1. Visual Theme & Atmosphere

jrhu.me is a personal portfolio built in Framer that strips back to near-zero. The design philosophy is stark minimalism: pure white background, pure black text, a single custom typeface, and no decorative system whatsoever. No colours, no gradients, no shadows, no defined border radii, no spacing scale. The entire emotional register is carried by the typeface choice and the content itself.

The custom font — GT Standard M Regular — is a distinctive editorial grotesque with strong optical character at small sizes. At 14px, it reads with more personality than Inter or system-ui would at the same size. This is a typographer's minimalism: everything removed so the letterforms can speak.

The browser default blue (`rgb(0,0,238)`) appears on anchor links — notably left as the unmodified browser default, which reads as an intentional retro-web gesture or a deliberate anti-branding statement. Framer Motion handles interactions.

---

## 2. Color Palette & Roles

The palette is binary with a browser default intrusion:

| Role | Value | Notes |
|------|-------|-------|
| Page background | `#ffffff` | Pure white |
| Primary text | `rgb(0, 0, 0)` | Pure black |
| Link default | `rgb(0, 0, 238)` | Browser default blue — unmodified |
| Focus outline | `rgb(0, 95, 204)` | Browser default focus ring |

No custom properties defined. No named colour tokens. No accent, no grey scale, no surface colours.

The decision not to override the browser-default link blue is striking. It could be read as: minimal effort, intentional retro statement, or a philosophical position that links should look like links. On a site this spare, it reads as deliberate.

What is absent is as telling as what is present: no hover colour change on links, no brand colour, no secondary palette, no dark mode consideration.

---

## 3. Typography Rules

Single custom typeface: **GT Standard M Regular** (Grilli Type). Loaded via Framer as a custom font with a placeholder fallback.

| Role | Font | Size | Weight | Line Height |
|------|------|------|--------|-------------|
| Body / paragraphs | GT Standard M Regular | 14px | 400 | 20px (1.43×) |
| Links | GT Standard M Regular | 14px | 400 | 20px |
| Base fallback | sans-serif | 12px | 400 | normal |

The base `body` is set to `sans-serif` at 12px (browser reset layer), but all content uses GT Standard M at 14px. The gap between fallback and loaded font is narrow, reducing layout shift.

GT Standard M is a grotesque with ink-trap-influenced details — it has warmth and distinctiveness without being decorative. At 14px with a 1.43× line-height, it creates a comfortable, unhurried reading rhythm. No uppercase, no tracking adjustments, no weight variation.

There is no heading typography defined in the extracted data — suggesting either flat information architecture (no h1/h2 hierarchy) or that headings receive no special CSS treatment and inherit body styles.

---

## 4. Component Stylings

**Links**
- Colour: `rgb(0, 0, 238)` default — browser blue
- No hover state detected
- Focus: `rgb(0, 95, 204)` outline (browser default)
- Framer text links: some use the browser blue, some are pure black (matching body) — context-dependent

**Navigation**
- No navigation element or component styling detected
- Content is likely structured as a single scrolling page or minimal navigation

**Surfaces / Cards**
- One white `div.framer-Mnehu` surface captured at luminance 1.0
- No elevation, no border, no shadow — Framer component wrapper only

**Interactive states**
- Hover: `null` on all captured links — no hover colour change
- Focus: browser default outline only
- The experience is Framer Motion animation driven, not CSS-state driven

---

## 5. Layout Principles

Built in Framer — layout is frame-based rather than grid/flexbox CSS:

- Body: `padding: 0`, `margin: 0` — Framer controls all layout
- No CSS grid or flexbox tokens detected
- No spacing scale or gap variables
- Breakpoints: `809.98px` and `810px` (likely Framer's internal mobile/desktop split), `1199.98px`

Layout is entirely managed by Framer's visual editor. The CSS output is Framer-specific class names (`framer-Mnehu`, `framer-mCPrT`) — not a portable design system.

The design likely uses generous whitespace managed visually in the Framer canvas rather than through a mathematical spacing scale.

---

## 6. Depth & Elevation

There is no depth system.

- `shadows: []` — explicitly empty in the extracted data
- `borderRadii: []` — explicitly empty
- No background layering
- No backdrop filters

The interface is a flat, white plane. The only contrast is black text on white. This is a zero-elevation design — content does not float, group, or layer. The experience is reading a page, not navigating a spatial interface.

---

## 7. Do's and Don'ts

**Do:**
- Use GT Standard M Regular exclusively — it is the only design element with personality
- Keep the palette binary: `#000000` on `#ffffff`
- Maintain 14px / 20px line-height for all body content — this is the sole typographic rhythm
- Leave ample whitespace managed through Framer's canvas — content needs room to breathe at this scale
- Accept the browser-default blue on links if replicating faithfully

**Don't:**
- Introduce any surface colours, card backgrounds, or tonal steps
- Add shadows, borders, or border-radius of any kind
- Use font weights other than 400 — no bold, no medium
- Override the link colour with a branded alternative if replicating the original intent
- Add navigation patterns, hero sections, or UI components — this is a pure content page

---

## 8. Responsive Behavior

Framer-managed responsive layout:

- **Mobile**: below 810px
- **Desktop**: 810px and above
- **Wide**: 1200px and above (1199.98px breakpoint)

At mobile, Framer reflows frames to a single column. GT Standard M at 14px is legible on mobile without size adjustment. The simple content structure means minimal adaptation is needed across viewports.

Touch targets for links are limited by the inline text size (14px) — accessibility padding may be handled by Framer's link wrapper rather than visible UI.

---

## 9. Agent Prompt Guide

**Quick reference:**
- Background: `#ffffff`
- Text: `#000000`
- Links: `rgb(0, 0, 238)` (browser default)
- Font: GT Standard M Regular, 14px / 400 / 20px line-height
- No colours, no shadows, no border-radius, no spacing scale

**Prompt to replicate this aesthetic:**
> "Design a minimal personal portfolio page. Pure white background, pure black text. Single typeface: GT Standard M Regular (or a comparable editorial grotesque) at 14px with 1.43× line-height. No colour accent. Links use browser-default blue. No shadows, no cards, no decorative elements. All whitespace is editorial — generous and intentional. The content is the only visual event."

**Prompt to extend a component:**
> "Add a work listing section to jrhu.me. Black GT Standard M text on white. Project titles as plain text or browser-blue links at 14px. No hover effects, no containers, no borders. Whitespace separates items — no dividers. The design is a document, not an interface."

---

*Generated by Sparkbites — extracted from live CSS analysis*
