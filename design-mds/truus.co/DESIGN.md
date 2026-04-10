# truus.co — Design System

## 1. Visual Theme & Atmosphere

Truus is a design agency site that refuses to pick a single mood — instead it cycles through a vivid, almost reckless palette of tag colors against a warm off-white base, creating an atmosphere that is simultaneously professional and playful. The canvas (`#f0ebe6`) is warm linen — not pure white, not cream, but something that reads like good paper stock. Black is absolute and uncompromising as the primary text and border color.

What makes Truus memorable is its deliberate use of color as categorization: each service card and tag carries a distinct saturated hue (dusty pink, coral orange, sage green, periwinkle blue), while the overall page stays grounded in that warm neutral base. The result is a portfolio that feels curated and alive without becoming chaotic.

## 2. Color Palette & Roles

**Foundations:**

| Role | Token | Value | Usage |
|------|-------|-------|-------|
| **Canvas** | `--color-offwhite` | `#f0ebe6` | Page background — warm linen |
| **Text / Border** | `--color-black` | `black` | All body text, borders |
| **Dark grey** | `--color-darkgrey` | `#2d2d2d` | Deep surface elements |

**Accent system (tags & cards):**

| Color | Token | Value | Usage |
|-------|-------|-------|-------|
| **Pink** | `--color-pink` / `--color-primary` | `#f0befa` | Primary brand accent, tags |
| **Orange** | `--color-orange` | `#f5693c` | Service cards, energetic tags |
| **Light green** | `--color-lightgreen` | `#e6fab9` | Soft tag variant |
| **Blue** | marquee logo bg | `rgb(75,105,240)` | Marquee/logo strip |
| **Periwinkle** | tag variant | `rgb(130,160,255)` | Tag accent |
| **Forest** | services card | `rgb(45,120,100)` | Dark service card |
| **Burgundy** | services card | `rgb(160,50,90)` | Dark service card |

The accent colors are never used for typography — they only appear as backgrounds on categorical elements (tags, cards, marquee strips). Text on them is always black.

## 3. Typography Rules

The typography data shows very large scale values — `113.778px` for display headings — combined with standard body sizes. This is a site built on display typography as visual sculpture.

| Level | Approx. Size | Weight | Notes |
|-------|-------------|--------|-------|
| Display / H1 | ~114px | 400–900 | Oversized, fills viewport width |
| Section heading | ~36–48px | 700 | Bold section anchors |
| Body | 16px | 400 | Clean reading size |
| Labels/tags | 12–14px | 400–500 | All-caps or normal |

No custom font family was captured definitively — the system likely uses a grotesque or geometric sans. Weight 900 appears in the data, suggesting an ultra-bold display weight for the hero.

**Notably absent:** No serif face, no italic, no letter-spacing on body text. The heavy-weight display type creates hierarchy without needing multiple faces.

## 4. Component Stylings

- **Tags** — pill-shaped, 4 distinct background colors (pink, orange, green, periwinkle), black text, tight horizontal padding
- **Services cards** — two-tone: forest green and burgundy variants; off-white text on dark backgrounds; likely square or wide-ratio cards
- **Marquee logo strip** — periwinkle blue `rgb(75,105,240)` background, scrolling logos
- **Modal/overlay** — `.modal-work` class present; dark surface implied
- **Team cards** — neutral surface; `.div.team-card` selector; likely off-white or dark

CSS custom property tokens for sizing:
- `--unit-width` — base unit for fluid scaling
- `--size-container-ideal` — max content width
- `--border-radius-l` — larger radius token for card corners

## 5. Layout Principles

- Fluid layout implied by `--unit-width` variable scaling
- `75em` and `25em` breakpoints suggest a `1200px` / `400px` responsive range
- Display headings fill viewport width — likely using `vw`-based `font-size` or `clamp()`
- Gap values: `16px` standard gap, with larger section gaps inferred from the display scale
- Marquee scrolling strip suggests full-bleed horizontal layout patterns

## 6. Depth & Elevation

- No shadows on the base palette — the flat design philosophy lets color carry distinction
- **Background color contrast** creates all elevation: off-white page → colored tag pill → dark service card
- The warm linen canvas acts as a subtle ground; pure black text reads slightly warmer than it would on `#fff`
- Border color is absolute black — used sparingly, likely only on structural elements

## 7. Do's and Don'ts

**Do:**
- Use the accent colors (pink, orange, green, blue) only as backgrounds on tags and cards — never for text
- Keep text black on all colored surfaces
- Push display type to full-viewport scale; restraint here would undermine the identity
- Use `#f0ebe6` as the warm ground — never pure white
- Embrace the multi-color tag system; it's the site's visual fingerprint

**Don't:**
- Mix accent colors into body or heading text
- Use the dark service card colors (`rgb(45,120,100)`, `rgb(160,50,90)`) for UI chrome — they're content-level colors
- Add gradients — the palette is deliberately flat
- Use the marquee blue outside the scrolling strip context

## 8. Responsive Behavior

| Range | Behavior |
|-------|----------|
| `< 400px` (`25em`) | Mobile — display type likely scales down |
| `400px – 1200px` | Tablet — intermediate layout |
| `≥ 1200px` (`75em`) | Full desktop — oversized display type, multi-column card grid |

Display headings at ~114px need `clamp()` or `vw`-based sizing to degrade gracefully on mobile.

## 9. Agent Prompt Guide

> "Design in the style of truus.co: warm linen canvas `#f0ebe6`, absolute black text and borders, accent tags in pink `#f0befa` / orange `#f5693c` / sage `#e6fab9` / periwinkle `rgb(130,160,255)` — always with black text on them, oversized display headings at viewport-filling scale, flat surfaces with no shadows, full-bleed marquee strips, dark service cards in forest green and burgundy — a vivid-yet-grounded agency aesthetic."

*Generated by Sparkbites — extracted from live CSS analysis*
