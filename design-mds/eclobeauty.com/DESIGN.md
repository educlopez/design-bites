# Éclo Beauty — Design System

## 1. Visual Theme & Atmosphere

Éclo Beauty distils luxury clean beauty into its design language. The palette is an organic warm cream (#fbf6f0), anchored by a deep charcoal footer (#212121) that creates a satisfying tonal bookend. The type system is genuinely exceptional: Cigar (a stylised serif or script) for hero h1, ABC Monument Grotesk Bold for section headings, SF Mono for uppercase category labels, and Monument Grotesk Semi-mono for UI text. This is a brand that has invested in typography as the primary luxury signal — no neon, no gradient, just quality type on warm paper. Border-radius is zero throughout: sharp edges on an organic palette for sophisticated tension.

---

## 2. Color Palette & Roles

| Role | Value | Notes |
|------|-------|-------|
| Page background | `#fbf6f0` | Warm cream — dominant |
| Brighter background | `#f6eadc` | Deeper warm cream (video bg) |
| Text primary | `#212121` | Deep charcoal |
| Text light | `#62615f` | Warm grey-brown for secondary copy |
| Border hairline | `#f8efe4` | Near-invisible warm border |
| Border dark | `#cccccc` | Standard divider |
| Footer background | `#212121` | Charcoal — matches primary text |
| Footer hairline | `#292929` | Subtle footer section divider |
| Footer text | `#bcbab7` | Warm light grey |
| Header background | `#fbf6f0` | Matches page — continuous scroll |
| Sale badge | `#00d072` | Bright green — sale highlight only |
| Badge bg | `#212121` | Matches footer/text for badges |
| Badge text | `#faf6f0` | Near-cream on dark badge |
| Error | `#721C24` on `#F8D7DA` | Standard error treatment |
| Accent (warm rose) | `#855656` | Primary light — subtle brand warmth |

The colour system is masterfully restrained. The cream/charcoal binary does all the work; the green sale badge is the only saturated colour on the whole site.

---

## 3. Typography Rules

**h1 typeface:** Cigar — stylised, editorial, brand-defining.
**h2 typeface:** ABC Monument Grotesk Bold — geometric grotesque for section headings.
**h3 typeface:** SF Mono — monospace for category/product labels, uppercase.
**h5 typeface:** Monument Grotesk Semi-mono — for UI-level labels.

| Level | Size | Weight | Line Height | Transform |
|-------|------|--------|-------------|-----------|
| h1 | 45px | 400 | 54px | none |
| h2 | 38px | 400 | 45.6px | none |
| h3 | 16px | 700 | 16px | uppercase |
| h5 | 14px | 700 | — | — |

- Cigar at 400 weight — the font's character does the styling work, not the weight.
- Monument Grotesk at 400 weight in h2 — same logic: the face is the style.
- SF Mono h3 at 1:1 line-height (16px/16px) — labels are tight, dense, tag-like.
- Uppercase transformation reserved exclusively for the monospace label tier (h3).
- No custom letter-spacing tokens — spacing is handled at the font level.
- Border-radius is explicitly set to 0 (`--RADIUS: 0px`) — sharp corners are a system-wide rule.

---

## 4. Component Styling

- **`--RADIUS: 0px`** — zero border-radius everywhere. Buttons, inputs, cards, selects are all sharp-cornered.
- **Shadows:**
  - Product card hover: `rgba(0,0,0,0.2) 0 0 10px` — soft ambient glow.
  - Subtle card: `rgba(0,0,0,0.1) 0 1px 3px, rgba(0,0,0,0.1) 0 1px 2px -1px` — near-invisible lift.
  - Elevated panel: `rgba(0,0,0,0.3) 0 30px 70px` — dramatic depth for modals/drawers.
- **Overlay system:** Full alpha scale from 5% to 95% using the text colour (#212121) as base — extremely refined overlay toolkit.
- **Header:** Transparent-capable — supports scrolled state with dedicated transparent token.
- **Error state:** `#F8D7DA` background, `#721C24` text, `#F5C6CB` border.

---

## 5. Layout Principles

- Section padding: 15px top, 32px horizontal, 10px bottom — minimal vertical, moderate horizontal breathing room.
- Scrollbar width is forced to 0 — the layout assumes no visible scrollbar.
- Header, menu, submenu, and footer all have explicit, matching colour tokens — a fully-considered vertical flow.
- The footer uses a hairline divider (#292929 on #212121) — almost invisible structural separation.

---

## 6. Depth & Elevation

- Three shadow tiers: micro (1px lift), ambient (10px glow), dramatic (70px drop).
- Warm shadows are not used — the black alpha shadows sit neutrally on the cream background.
- The 30px/70px dramatic shadow suggests a drawer or full-panel reveal animation.
- Flat surfaces with sharp corners dominate; shadow appears only on interactive or elevated states.

---

## 7. Do's and Don'ts

**Do:**
- Use Cigar exclusively for h1 — it is the brand voice typeface.
- Maintain sharp corners (0 border-radius) on all interactive components.
- Apply SF Mono in uppercase for all category/label tiers (h3 equivalent).
- Keep the cream/charcoal binary — resist adding colours beyond the sale green.

**Don't:**
- Add border-radius to buttons, cards, or inputs — zero radius is a system rule.
- Use Cigar for subheadings or UI text — it belongs at the hero level only.
- Introduce warm-shadow or coloured-glow effects — neutral black alpha shadows only.
- Use the sale green (#00d072) outside of sales/promotion contexts.

---

## 8. Responsive Behavior

- Scrollbar is hidden (`--scrollbar-width: 0px`) — ensure content is not obscured on overflow.
- Section padding (15/32/10px) is compact enough to work across screen sizes without major adjustment.
- The dramatic 70px shadow is likely tied to a drawer/modal animation — needs to scale with the panel size.
- The Cigar typeface at 45px needs responsive scaling (suggest `clamp(28px, 4vw, 45px)`).

---

## 9. Agent Prompt Guide

> Build a clean beauty e-commerce site using Éclo's design language. Background #fbf6f0 (warm cream), text #212121 (deep charcoal), footer #212121 with #bcbab7 text. Four typefaces: Cigar at 45px/400 for h1; ABC Monument Grotesk Bold at 38px for h2; SF Mono 700 uppercase for category labels; Monument Grotesk Semi-mono for UI text. Zero border-radius everywhere. Shadows: ambient (10px), subtle (3px), dramatic (70px) — all black alpha, no warm tones. Only one saturated colour: sale green #00d072. Section padding 15px/32px.

---

*Generated by Sparkbites — extracted from live CSS analysis*
