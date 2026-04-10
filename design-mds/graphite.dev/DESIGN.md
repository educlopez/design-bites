# graphite.dev — Design System

## 1. Visual Theme & Atmosphere

Graphite is a developer tool — and its design makes no apologies for that. The site is built in near-total darkness: a near-black zinc surface (`#0a0a0a`) that signals professional focus and zero distraction. Text lives at high contrast against this void, with the primary color being a warm near-white rather than pure white, keeping the experience intense but not harsh.

What lifts Graphite above the generic dark SaaS template is its animation investment. The CSS reveals an extensive custom easing vocabulary — glide curves, clip-path animations, chained translate-and-opacity sequences — suggesting that the UI is in motion as much as it is in stasis. The product communicates speed through movement, not just messaging.

The brand accent is a vivid orange (`#ff8833`) — a developer-flavored warmth against the zinc void. Footer moments introduce additional accent swatches (teal, yellow, bright blue) but these are contained; they don't bleed into the main product UI.

---

## 2. Color Palette & Roles

**Core Surfaces**
- Near-black `#0a0a0a` (neutral-950) — page background
- Zinc-900 `#18181b` — secondary background, panel fills
- Zinc-800 `#27272a` — card surfaces, PR page surface
- Zinc-700 `#3f3f46` — elevated surfaces, secondary panels
- Zinc-600 `#52525c` — tertiary surfaces

**Text**
- Primary text `#e8e8ed` — near-white, not stark
- Secondary text `#a1a1a6` — muted captions and labels
- Subtle text: white at 60% opacity — nav items at rest
- Hover text: white at 100% — nav items on hover
- Negative/error: `#ffa6b2`
- Positive/success: `#a0e3a6`
- Caution/warning: `#fac862`

**Brand & Accents**
- Brand orange `#ff8833` — primary accent, CTAs
- Brand teal `#2eead4`
- Brand blue `#04a9d7`
- Brand green `#7bf1a8`
- Category colors: magenta `#f252ff`, teal `#30ead5`, orange `#ff8632`, salmon `#ff82a4`

**Borders & Dividers**
- White at 10% opacity — universal border color on dark backgrounds
- Neutral-800 `#262626` — defined border-primary

---

## 3. Typography Rules

One primary typeface rules everything: **Matter** (`matterFont`) — a geometric sans-serif with clean, professional character. DM Mono and JetBrains Mono are available for code contexts.

**Scale**
- h1: `36px` / `500` weight / `40px` line-height — medium weight, not heavy; confidence without shouting
- h2: `16px` / `400` — used as a descriptor, not a heading in the traditional sense
- h3: `24px` / `600` — section feature headings
- Body: `16px` / `400` / `20px` line-height
- Paragraphs: `16px` / `400` / `24px` — slightly more open than body
- Links/Buttons: `14px` / `400–500` / `20px`

**Notes**
- Font feature settings disable ligatures: `"clig" 0, "liga" 0` — intentional for developer-tool readability
- No text transforms — no all-caps labels
- Tight letter-spacing tokens available (`--tracking-tighter: -0.05em`) but not applied to body
- Monospace fonts (DM Mono, JetBrains Mono) reserved for code snippets and the PR page

---

## 4. Component Stylings

**Navigation**
- Transparent background at rest; dark zinc (`lab(15.204...)` ≈ zinc-900) on focus
- Nav items: white at 60% opacity → white at 100% on hover — ghost to solid fade
- Minimal border radius: `8–10px` — subtle, not pill-shaped

**Buttons**
- Primary: brand orange or strong zinc fill
- Minimal box-shadow: `rgba(0,0,0,0.1) 0 1px 3px, 0 1px 2px -1px` — subtle ground shadow
- Radius: `10px` standard, `2px` for compact variants

**Footer Accent Blocks**
- Animated color blocks: orange `rgb(255, 98, 49)`, yellow `rgb(255, 185, 49)`, cyan `rgb(20, 199, 255)`, blue `rgb(16, 97, 255)` — Graphite's color identity lives in the footer marquee

**PR Page (product UI)**
- Surface: zinc-800 — matches main dark tone
- Accent: `#a5d6ff` — soft blue highlight for code changes
- Width: 800px, scaled proportionally for responsive containers

**Animations (the signature behavior)**
- Custom glide easing: `linear(0, .012 0.9%, .05 2%, ..., 1)` — spring-like without a spring library
- Translate-up with opacity: the primary reveal pattern for content entering view
- Clip-path reveals, gradient border rotation, marquee scrolling
- Duration baseline: `0.6s` for most transitions

---

## 5. Layout Principles

The layout is wide-container oriented, with explicit breakpoints from `554px` up to `1440px` — nine distinct breakpoints suggesting a carefully tuned responsive system. The header has `16px` horizontal padding and `64px` margin, centering content in a comfortable column. The footer uses `80px` top padding — generous to separate it from content.

The PR page uses a `800px` fixed width scaled down via CSS transforms for responsive behavior: `min(1, calc(150vw - 2rem) / 800px)` — a clever technique that preserves pixel-perfect rendering at desktop while gracefully shrinking. Cloud agents UI follows the same `container-query` based scaling pattern.

Sections use `0px` padding — layout control is pushed to inner components, allowing each section to define its own breathing room.

---

## 6. Depth & Elevation

The dark theme creates inherent elevation through luminance alone: lighter surfaces (`zinc-700/600`) float above darker ones (`zinc-900/950`) without requiring shadow. The shadow system is minimal and restrained:

- Standard shadow: `rgba(0,0,0,0.1) 0 1px 3px, 0 1px 2px -1px` — barely visible on dark surfaces, used for slight card lift
- Drop shadow token: `0 4px 4px rgba(0,0,0,0.15)` — available but rarely dominant

The primary depth mechanism is the color step system: zinc-950 → zinc-900 → zinc-800 → zinc-700 creates a four-level elevation stack. Blur is available (`blur-xs` through `blur-3xl`) for potential glass-morphism moments but is not a foundational pattern.

---

## 7. Do's and Don'ts

**Do:**
- Use zinc-950 (`#0a0a0a`) as the page base — not `#000` which reads as pure void
- Fade nav text from 60% to 100% white on hover — never change the color
- Use Matter for all UI text; reach for DM Mono or JetBrains only for code contexts
- Apply the glide easing curve to all motion — avoid standard `ease-in-out`
- Use the brand orange sparingly as a true accent, not a background color
- Keep border radius at 8–10px; avoid pill shapes on primary UI elements

**Don't:**
- Don't use white text at full opacity for body copy — it creates unnecessary visual tension
- Don't introduce light mode without a full design overhaul — the palette is built for dark
- Don't animate without the custom glide easing — generic CSS easing will feel mismatched
- Don't use the category/brand color palette in the main product UI — those belong in marketing footer blocks
- Don't stack shadows — the dark surface handles elevation through tone, not shadow

---

## 8. Responsive Behavior

Nine breakpoints (`554, 767, 768, 960, 1024, 1158, 1224, 1280, 1440px`) signal obsessive care for intermediate states. The product UI uses CSS `container-query` scaling (`min(1, calc(100cqw - 2rem) / target-width)`) rather than fixed breakpoint reflows — meaning embedded product previews always maintain their proportions.

At mobile widths the header collapses from a full navigation row to a compact form; the `--header-right: 1216px` token suggests the header has a maximum right boundary that snaps inward. Animation delays become more critical at mobile since users scroll through sections sequentially.

---

## 9. Agent Prompt Guide

Use this block when prompting an AI to generate UI in the style of graphite.dev:

```
Design a dark developer-tool interface. Page background is near-black #0a0a0a (zinc-950). Surfaces step up through #18181b, #27272a, and #3f3f46. Primary text is near-white #e8e8ed; secondary text is #a1a1a6. Primary accent is orange #ff8833. Font is Matter (or DM Sans as substitute) at 400–600 weight; use DM Mono for code. Nav items use white at 60% opacity, revealing to 100% on hover. Border radius is 8–10px. Borders use white at 10% opacity. Animations use a spring-like custom linear easing with 0.6s duration. Shadow is minimal — single-pixel lift only. No glass morphism, no gradients in the core UI. Footer may use bold color accent blocks in orange, yellow, cyan, and blue.
```

---

*Generated by Sparkbites — extracted from live CSS analysis*
