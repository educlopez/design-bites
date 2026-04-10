# fluar.com — Design System

## 1. Visual Theme & Atmosphere

Fluar occupies the increasingly rare middle ground of polished SaaS that doesn't mistake darkness for sophistication. The canvas is pure white with near-black text (`rgb(10, 10, 10)`), but this minimalism is a vessel, not an end. The real personality lives in controlled injections of vivid colour — a spiral-animated purple blob, OS-style traffic-light dots, and vibrant gradient accent chips (`#ff4242` red, `#a142fe` violet, `#40a1ff` sky, `#43d0ff` cyan, `#a0ff42` lime). The effect is "calm dashboard with confetti moments": professional enough for enterprise buyers, energetic enough for developer audiences. Everything is rendered at the pixel level via Tailwind, with Satoshi as the sole expressive voice.

## 2. Color Palette & Roles

**Base**
- Background: `#ffffff` — the whole page is a white canvas
- Foreground: `rgb(10, 10, 10)` — near-black, not harsh black
- Muted text: `hsl(0 0% 45.1%)` via `--muted-foreground`

**Brand accent cluster** (custom properties `--color-1` through `--color-5`)
- `#ff4242` — danger/energy red
- `#a142fe` — violet, primary brand highlight
- `#40a1ff` — sky blue, secondary brand
- `#43d0ff` — cyan, tertiary brand
- `#a0ff42` — lime, success/growth signal

**Semantic UI**
- Primary button: `hsl(0 0% 9%)` — dark fill with white text
- Destructive: `hsl(0 84.2% 60.2%)` — standard error red
- Border: `rgb(229, 229, 229)` — light grey divider
- Ring/focus: `rgb(99, 71, 255)` — violet focus outline

**Surface tints**
- Cards/hover: `rgb(249, 250, 251)` to `rgb(243, 244, 246)` — barely-there grey layers
- Status green badge: `rgb(220, 252, 231)` bg / `rgb(21, 128, 61)` text
- Light blue cell: `rgb(224, 242, 254)` — data table highlight

**What's absent:** dark mode, gradients in backgrounds, black fill outside interactive states.

## 3. Typography Rules

The entire site runs on **Satoshi**, a geometric sans-serif chosen for its friendly curves without sacrificing professionalism.

| Element | Size | Weight | Tracking | Case |
|---------|------|--------|----------|------|
| H1 | 48px | 800 | −1.2px | Normal |
| H2 | 18px | 400 | Normal | Normal |
| H3 | 18px | 700 | −0.45px | Normal |
| Body | 16px | 400 | Normal | Normal |
| `<p>` label | 13px | 600 | +1.3px | UPPERCASE |
| Button | 14px | 400 | Normal | Normal |

The uppercase tracking label pattern (`p` at 13px, weight 600, +1.3px) is the signature micro-typographic detail — it creates section labels that feel editorial without a second font. Line heights are tight (1.1× for H1, 1.5× for body), keeping the UI dense and purposeful.

## 4. Component Stylings

**Buttons** come in three flavours:
1. *Ghost/outline* — transparent background, `rgb(229,229,229)` border, dark text
2. *Primary filled* — `hsl(0 0% 9%)` background with white text, ring shadow in violet on focus
3. *Brand ring* — violet-outlined variant using `rgb(99, 71, 255)` shadow

Border radius is **8px** for cards and containers, **6px** for small form elements, **9999px** for pills and badges.

Shadow language is layered with three-part box-shadows: white inner reset → border ring → soft drop. Example: `white 0 0 0 0, rgb(229,229,229) 0 0 0 1px, rgba(17,24,39,.1) 0 1px 3px`. Cards get a bilateral soft-glow variant (`rgba(190,190,190,.2) 5px 5px 20px`).

**Status indicators** use the macOS traffic-light trio (red `#ff5f57`, yellow `#febc2e`, green `#28c840`) — a knowing wink at developer tooling culture.

## 5. Layout Principles

Horizontal padding is 24px on `<main>`, creating a generous but not excessive content channel. Sections breathe with 56px top / 64px bottom padding — roughly 4-column Tailwind spacing. No evidence of CSS Grid beyond Tailwind utilities; layout is flex-first. Max-width breakpoints span 480px through 1536px (8 steps), suggesting a fully responsive grid that reflows progressively.

The sidebar system (noted via `--sidebar-*` tokens) implies a two-panel dashboard layout underneath the marketing shell — collapsible nav beside a main content area.

## 6. Depth & Elevation

Elevation is communicated primarily through **border + shadow** rather than opacity shifts. Three tiers:
1. **Flat** — content on white, no shadow
2. **Raised** — `rgba(0,0,0,.04) 0 2px 8px, 0 4px 16px` — cards and panels
3. **Modal/overlay** — `rgba(0,0,0,.25) 0 25px 50px -12px` — full-screen dropdowns

The violet focus ring (`rgb(99,71,255) 0 0 0 1px`) adds a fourth functional layer that signals interactivity without a shadow.

Glassmorphism appears sparingly: `rgba(255,255,255,.7)` on overlay containers — more frosted affordance than aesthetic statement.

## 7. Do's and Don'ts

**Do:**
- Use Satoshi at weight 800 only for the hero H1; step down to 700/400 elsewhere
- Apply the uppercase label pattern (`13px 600 +1.3px`) for section eyebrows and metadata
- Keep brand colour chips (the five `--color-N` values) as accents in illustrations and small indicators, never as large fills
- Use the three-part shadow formula for all card-like surfaces
- Pair `rgb(220,252,231)` green badges with `rgb(21,128,61)` text for status states

**Don't:**
- Mix multiple brand colours in the same interactive element
- Use Satoshi at weight 800 below 40px — it reads as clunky
- Remove the border from buttons; the ring shadow depends on its presence
- Use fully opaque black (`#000000`) — prefer `rgb(10,10,10)` or `rgba(0,0,0,.8)`
- Add box shadows heavier than the modal tier outside of dialog contexts

## 8. Responsive Behavior

Eight breakpoints (480 → 1536px) indicate meticulous tuning. Key transitions:
- **480px** — mobile layout starts, likely single-column
- **768px** — tablet pivot, sidebar may collapse
- **1024px** — desktop two-column layout activates
- **1280/1400/1536px** — wide-screen refinements, content max-width capping

The `main` padding of `0 24px` likely increases at wider breakpoints. Dashboard sidebar tokens suggest the nav becomes a fixed rail at ≥1024px.

## 9. Agent Prompt Guide

> Build a SaaS marketing/dashboard page in the style of fluar.com. Use a pure white background with near-black (`#0a0a0a`) text. Load the **Satoshi** font. Set the hero H1 to 48px, weight 800, tracking −1.2px. Use an uppercase eyebrow label pattern at 13px, weight 600, letter-spacing 1.3px. Apply `hsl(0 0% 9%)` for primary CTAs with white text and 8px radius. Add a three-part box-shadow to cards: `0 0 0 1px rgb(229,229,229), 0 1px 3px rgba(17,24,39,.1)`. Use the five brand accent colours (`#ff4242`, `#a142fe`, `#40a1ff`, `#43d0ff`, `#a0ff42`) only as small chips, badges, or animated blobs — never as page backgrounds. Keep spacing generous: 56–64px vertical section padding, 24px horizontal gutter.

*Generated by Sparkbites — extracted from live CSS analysis*
