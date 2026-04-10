# amie.so — Design Language

## 1. Visual Theme & Atmosphere

Amie is a calendar and productivity app whose marketing site mirrors its product: clean, white, app-like — but with surprising warmth and personality. The canvas is pure white with a near-black foreground (`#262626`), but what distinguishes amie visually is the breadth of its colour system. Behind the monochromatic surface sits a complete palette of named semantic colours — rose, orange, purple, red, blue, green, teal — each expressed in a full 9-step scale. The pink accent (`#f6a6a6`) is the brand's heartbeat, appearing in product UI as a pastel emotional touch. The design philosophy is "joyful utility": professional enough for a serious productivity tool, warm enough to make people want to spend time in it.

## 2. Color Palette & Roles

**Primary text & foreground**
- `#262626` (`--foreground`) — Near-black body text; slightly warm, prevents harshness.
- `rgb(0, 0, 0)` — Pure black for max-contrast labels and headlines.

**Background surfaces**
- `rgb(255, 255, 255)` — Primary page and card backgrounds.
- `rgba(250, 250, 250, 0.8)` — Frosted header/nav surface; near-white with subtle transparency for sticky layers.
- `rgba(235, 235, 235, 0.5)` — Secondary surface; muted background zone for content grouping.

**Brand accent**
- `#f6a6a6` (`--color-amie-pink`) — The brand signature; a soft rose-pink. Used sparingly in product UI to humanise the experience.

**Semantic colour system** (full scale, RGB-based, used in product UI)
- `--color-primary` → `--color-gray-900` (`rgb(23,23,23)`) — Primary UI text.
- `--color-secondary` → `--color-gray-600` (`rgb(92,92,92)`) — Secondary labels.
- `--color-tertiary` → `--color-gray-350` (`rgb(160,160,160)`) — Tertiary/placeholder text.
- `--color-accent` → `--color-red-500` (`rgb(253,43,56)`) — Destructive actions, notifications, unread dots.
- `--color-background` → `--color-gray-50` (`rgb(250,250,250)`) — App background.

**Status & data colours (surfaces)**
- `rgb(204, 244, 218)` — Mint green; success/confirmed event backgrounds.
- `rgb(88, 144, 231)` — Blue widget surface.
- `rgb(17, 168, 255)` — Bright blue for feature highlights.
- `rgb(231, 88, 97)` — Notification/unread dot red.
- `rgb(115, 115, 115)` — Mid-grey UI zone.

**Border**
- `rgb(205, 205, 205)` — Universal interactive element border colour.

## 3. Typography Rules

**Inter var** — The primary marketing typeface, loaded as a variable font. Two fallback chains reveal dual rendering contexts:

| Element | Font | Size | Weight | Leading | Tracking |
|---------|------|------|--------|---------|---------|
| h2 | Inter var | 20px | 700 | 26px (1.3) | normal |
| h3 | Inter / Inter Fallback | 20px | 600 | 28px (1.4) | −0.003px |
| body / p | Inter var | 16px | 400 | 24px (1.5) | normal |
| input | Inter var | 12px | 400–600 | varies | normal |
| button | Inter var | 12px | 700 | varies | normal |

Headings at 20px with weights 600–700 signal an app-first design — headings are section markers, not visual centrepieces. The 12px button/input size reflects the product's dense, information-rich UI bleeding through to the marketing layer. No negative tracking at marketing sizes (unlike many contemporaries) — Inter reads naturally at these weights.

What is absent: no display serif, no custom brand typeface beyond Inter, no uppercase transforms.

## 4. Component Stylings

**Shadow system** — Amie uses a layered box-shadow vocabulary as its elevation language:
- **Level 1 (card border)**: `rgba(0,0,0,0.06) 0px 0px 0px 1px, rgba(0,0,0,0.06) 0px 1px 1px -0.5px, rgba(0,0,0,0.06) 0px 3px 3px -1.5px` — Subtle border + micro-lift.
- **Level 2 (elevated card)**: Extends Level 1 with `rgba(0,0,0,0.06) 0px 6px 6px -3px, rgba(0,0,0,0.04) 0px 12px 12px -6px, rgba(0,0,0,0.04) 0px 24px 24px -12px, rgba(0,0,0,0.1) 0px 24px 24px 2px` — Deep layered ambient shadow for modals/dropdowns.
- **Minimal**: `rgba(0,0,0,0.1) 0px 1px 3px, rgba(0,0,0,0.1) 0px 1px 2px -1px` — Standard Tailwind shadow-sm equivalent.

**Border radii** — Multiple scales in active use:
- `3px` — Micro elements, badges, tight UI.
- `6px` — Small interactive elements.
- `8px` — Standard component radius (inputs, cards).
- `12px` — Larger cards, panels.
- `0px 0px 12px 12px` — Bottom-only rounding (bottom sheet / drawer pattern).
- `9999px` — Pill buttons and tags.

**Buttons** — 12px font, weight 700 (bold for small size), transparent default with `rgba(0,0,0,0.05)` fill on hover. No border-colour change on hover; subtle background tint only.

**WYSIWYG shadows**: `--shadow-wysiwyg-inner: rgba(0,0,0,0.04)` / `--shadow-wysiwyg-outer: rgba(0,0,0,0.12)` — defined for rich-text editor components.

## 5. Layout Principles

Built on Next.js + Tailwind CSS with a rich set of layout custom properties:
- `--nav-width: 74px` — Narrow icon sidebar (product UI convention).
- `--inbox-width: 200px` — Secondary panel width.
- `--sidebar-top-height: 36px` / `--sidebar-bottom-height: 64px` — Fixed chrome heights.
- `--grid-row-height: 60px` — Calendar grid row height.

These tokens expose the product layout system leaking into the marketing layer — unusual and intentional.

Breakpoints: `640px`, `768px`, `1024px`, `1280px`, `1536px`, `2000px` — Tailwind defaults plus a `2000px` ultrawide breakpoint for large display optimisation.

## 6. Depth & Elevation

The shadow system is sophisticated and tiered. Unlike flat designs, amie uses multi-stop shadows to create genuine optical depth:
- Zero elevation: flat surface, no shadow.
- Low elevation: 1px border shadow only.
- Medium elevation: border + 3px ambient.
- High elevation: full 9-layer stack up to 24px spread.

The frosted header `rgba(250,250,250,0.8)` combined with a light shadow creates a glassmorphic sticky nav without blur (no `backdrop-filter` in extracted CSS).

## 7. Do's and Don'ts

**Do:**
- Use the full tiered shadow vocabulary — don't collapse to a single shadow value.
- Keep the amie-pink `#f6a6a6` as a pastel emotional accent, used once per view.
- Use Inter var as a variable font; weight 700 at small sizes (12px buttons) for legibility.
- Use the `9999px` pill radius for primary CTAs; `8px` for cards and inputs.
- Express status with surface colour (mint green for success, red for alerts) rather than text colour alone.

**Don't:**
- Don't substitute a different accent colour for `#f6a6a6` — the brand's warmth depends on it.
- Don't use the full semantic colour scale decoratively; it exists for data, status, and events.
- Don't collapse the typography scale — h2 and body are close in size by design; weight carries the distinction.
- Don't use hard borders in place of the layered shadow-as-border pattern.
- Don't add decorative display typefaces; Inter's variable weight range is the only typographic tool.

## 8. Responsive Behavior

Six breakpoints including a `2000px` ultrawide:
- `≤640px`: Mobile, stacked single-column.
- `640px–768px`: Small tablet / Tailwind `sm`.
- `768px–1024px`: Tablet / Tailwind `md`.
- `1024px–1280px`: Desktop / Tailwind `lg`.
- `1280px–1536px`: Large desktop / Tailwind `xl`.
- `≥1536px`: Ultra-wide; `2000px` variant for very large displays showing more product UI.

The layout custom properties (`--nav-width`, `--inbox-width`, etc.) remain constant across breakpoints — they are product app chrome dimensions, not responsive variables.

## 9. Agent Prompt Guide

> "Design in the style of amie.so: pure white background, `#262626` foreground text, Inter var typeface at 400/600/700 weights. Use layered multi-stop box-shadows for elevation — never flat borders. Brand accent is soft rose `#f6a6a6`, used sparingly. Multiple border-radius values: 3px for micro, 8px standard, 12px panels, 9999px pills. Full semantic colour scale (gray/rose/blue/green/red) for data and status. Button hover uses `rgba(0,0,0,0.05)` tint only. Tailwind breakpoints plus 2000px ultrawide."

---

*Generated by Sparkbites — extracted from live CSS analysis*
