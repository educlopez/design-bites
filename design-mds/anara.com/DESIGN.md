# anara.com — Design Language

## 1. Visual Theme & Atmosphere

Anara is a product that leans into warmth, craft, and approachability — unusual for a B2B SaaS. The design's most distinctive choice is its headline typeface: "Perfectly Nineties", a custom serif with retro editorial character, used at large display sizes to give the marketing site a personality that stands apart from generic tech products. Beneath that expressive layer, Inter carries the functional UI work. The palette is restrained: white, near-black, and a single light grey — but four named font tokens (including "ITC Garamond" for testimonials) hint at a rich typographic philosophy. The overall atmosphere is polished and grounded, with craft details in the type choices that reward close attention.

## 2. Color Palette & Roles

**Primary backgrounds**
- `hsl(0 0% 100%)` (`--background-primary`) — Pure white page canvas.
- `rgba(255, 255, 255, 0.9)` — Header background; near-opaque white for sticky navigation with subtle see-through effect.
- `rgb(247, 247, 247)` — Section background (`div.md:mt-16`); very light grey for content zone separation.
- `rgb(255, 255, 255)` (`--background-object`) — Object/card surfaces.

**Text hierarchy**
- `hsl(0 0% 9%)` (`--text-primary`) → `rgb(23, 23, 23)` — Primary body and heading text; not pure black, reads with warmth.
- `#666666` (`--text-secondary`) — Secondary labels and captions.
- `#9a9a9a` (`--text-tertiary`) — Tertiary text, placeholder content.
- `hsl(0 0% 0%/20%)` (`--text-muted`) — Muted/disabled text at 20% opacity.
- `hsl(0 0% 100%)` (`--text-inverse`) — White text on dark surfaces.
- `hsl(0 0% 0%)` (`--background-inverse`) — Inverse surfaces (black backgrounds for contrast sections).

**Borders & controls**
- `#e5e5e5` (`--border-primary`) → `rgb(229, 229, 229)` — Universal border colour; consistent across all interactive elements.
- `hsl(0 0% 0%/5%)` (`--border-muted`) — Very subtle borders on nested elements.
- `hsl(0 0% 94.9%)` (`--control-primary`, `--control-secondary`) — Control/input background.
- `hsl(0 0% 0%/10%)` (`--control-background`) — Tinted control surface.

**No accent colour is defined.** The design deliberately avoids a brand accent, relying entirely on the typeface personality and layout craft to create visual distinction.

**Interactive hover surface**
- `rgba(237, 237, 237, 0.99)` — Button/nav item hover fill; a light grey tint, no colour shift.

## 3. Typography Rules

Four typefaces, each with a precise semantic role:

**Perfectly Nineties** — Display / hero serif. Used only for `h1` and `h2`:
| Element | Size | Weight | Leading | Tracking |
|---------|------|--------|---------|---------|
| h1 | 72px | 550 | 80px (1.11) | −0.96px |
| h2 | 56px | 550 | 60px (1.07) | −0.32px |

Weight 550 is a mid-weight between regular and semibold — supported via a variable font or OpenType fvar. Tight line-height (near 1:1) creates dense, magazine-editorial title blocks. Negative tracking at large sizes only.

**Inter** — UI / functional sans. Used for all non-display elements:
| Element | Size | Weight | Leading | Tracking |
|---------|------|--------|---------|---------|
| h3 | 20px | 600 | 28px (1.4) | −0.32px |
| body | 16px | 500 | 24px (1.5) | −0.32px |
| p | 16px | 500 | 24px (1.5) | −0.40px |
| a | 16px | 500 | 24px (1.5) | −0.32px |
| button | 14px | 550 | 20px (1.43) | −0.32px |

Body text uses `font-weight: 500` (medium) universally — heavier than the standard 400, giving copy a confident, slightly editorial presence. Buttons use 550, same as the display headings.

**ITC Garamond** (`--font-testimonial`) — Used exclusively for testimonial/quote blocks. Classic advertising serif that lends authority and warmth to social proof sections.

**Inter Display** (`--font-inter-display`) — Defined as a token but not observed in the extracted typography selectors. Reserved for larger Inter usage (Inter Display is optically tuned for large sizes).

What is absent: no monospace, no uppercase transforms, no font-feature-settings beyond defaults.

## 4. Component Stylings

**Navigation buttons** — Transparent default, `rgba(237,237,237,0.99)` fill on hover and focus. No border colour change. No shadows. Colour shifts from `rgb(0,0,0)` to `rgb(23,23,23)` on hover — a subtle warming rather than a true colour change.

**Border radius vocabulary** — Multiple radii for different component scales:
- `8px` — Standard small components, inputs, tight cards.
- `10px` — Slightly larger interactive elements.
- `12px` — Medium cards and panels.
- `16px` — Large cards.
- `20px` — Large rounded panels.
- `16px 16px 0px 0px` — Top-only rounding; drawer/panel headers.
- `20px 20px 0px 0px` — Larger top-only variant.
- `9999px` — Full pill for badges and CTAs.

**Shadows** — None extracted. The design relies entirely on surface-colour contrast and borders for depth.

**Header** — Frosted white at `rgba(255,255,255,0.9)` with `#e5e5e5` border; sticky with subtle transparency.

## 5. Layout Principles

Pure Tailwind CSS. A rich breakpoint set reflecting mobile-first product marketing:
`375px`, `480px`, `600px`, `640px`, `768px`, `1024px`, `1270px`, `1280px`, `1536px`

The custom breakpoints at `375px` (iPhone SE) and `480px` (small mobile) indicate careful mobile attention. `1270px` (near Tailwind `xl`) suggests a custom container max-width. The token `--unriddle-orange` appearing in custom properties suggests design system cross-pollination (possibly shared with a related product).

Body spacing is utility-driven; no explicit spacing tokens beyond the structural layout props. Sections use `div.md:mt-16` for top margins — a Tailwind-native approach.

## 6. Depth & Elevation

No box-shadows. Depth is constructed from:
- **Background steps**: white `#ffffff` → light grey `rgb(247,247,247)` for section layering.
- **Header transparency**: `rgba(255,255,255,0.9)` creates a perception of content scrolling behind.
- **Border lines**: `#e5e5e5` at every component boundary; subtle but consistent.
- **Top-only border-radius** (`16px 16px 0px 0px`) creates panel-docking depth illusion.

This is an exceptionally flat design where the personality comes entirely from typography, not chrome.

## 7. Do's and Don'ts

**Do:**
- Use Perfectly Nineties only for `h1`/`h2` display text — it's the visual signature, not a body font.
- Set body text at `font-weight: 500`; the medium weight is deliberate and distinctive.
- Use ITC Garamond for any testimonial or pull-quote elements.
- Apply consistent negative tracking (`−0.32px`) at 16px and above.
- Keep the hover state as a light grey fill (`rgba(237,237,237,0.99)`) — no colour accent.

**Don't:**
- Don't introduce an accent colour; the palette is intentionally accent-free.
- Don't add drop shadows; the design is purposefully flat.
- Don't use Perfectly Nineties below `h2` — it loses impact and becomes illegible at small sizes.
- Don't use `font-weight: 400` for body text; 500 is the baseline here.
- Don't use sharp corners (`border-radius: 0`) — even minimal UI elements use at least 8px.

## 8. Responsive Behavior

Nine breakpoints covering the full device spectrum:
- `375px` / `480px`: Small/standard mobile — careful attention to small screens.
- `600px`: Large mobile / small tablet boundary.
- `640px` / `768px`: Tailwind `sm` / `md`.
- `1024px`: Tailwind `lg` / desktop.
- `1270px` / `1280px`: Custom container max-width + Tailwind `xl`.
- `1536px`: Tailwind `2xl`.

Display typography (`h1: 72px`, `h2: 56px`) will need meaningful reduction on mobile (suggest 40px / 32px) though explicit mobile overrides are handled in Tailwind utility classes not captured in the CSS selector extraction.

## 9. Agent Prompt Guide

> "Design in the style of anara.com: pure white background, `rgb(23,23,23)` text (not pure black). Hero headlines in 'Perfectly Nineties' serif at 550 weight with tight 1.1 line-height and slight negative tracking. Body and UI in Inter at weight 500 (not 400 — medium is the baseline). ITC Garamond for testimonials only. Border `#e5e5e5` everywhere, no accent colour, no shadows. Border-radius vocabulary: 8px (small), 12–16px (cards), 9999px (pills). Button hover: `rgba(237,237,237,0.99)` fill only. Nine responsive breakpoints from 375px to 1536px."

---

*Generated by Sparkbites — extracted from live CSS analysis*
