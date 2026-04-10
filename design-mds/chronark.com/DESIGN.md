# chronark.com — Design System

## 1. Visual Theme & Atmosphere

chronark.com is a developer portfolio defined by radical restraint. The design makes a single, powerful visual statement: a 128px heading in Cal Sans — a display typeface with personality — set against pure black. Everything else recedes. Body text, navigation, and secondary content use Inter at muted grey (`rgb(113, 113, 122)`), functioning more as annotations to the main heading than as primary content.

The aesthetic is **terminal meets editorial** — the kind of portfolio a developer makes when they want their code to speak but still care deeply about the frame. Pure black background, zinc-grey text, no borders, no shadows, no surface layers. The only depth cue is the contrast between the display text's implied white fill and the surrounding darkness.

Noticeably, the H1 element has `color: rgba(0,0,0,0)` with a `backgroundColor: rgb(255,255,255)` — a classic background-clip text technique, rendering the giant heading as a white/transparent knockout. This is the site's entire visual centerpiece.

---

## 2. Color Palette & Roles

**Core — entirely achromatic**:
- Page background: `rgb(0, 0, 0)` — absolute black
- Navigation/body text: `rgb(113, 113, 122)` — Zinc-500, muted
- Link hover: `rgb(164, 164, 170)` — Zinc-400, a brightness step up
- H1 text (background-clip): white/transparent over black canvas
- Border: `rgb(229, 231, 235)` — appears in CSS but likely invisible against black

**What's absent**: No accent color. No surfaces. No backgrounds beyond pure black. No cards, panels, or containers. No shadows (none detected). This is one of the most minimal palettes in the canon — two greys and a black.

The simplicity is a statement: the work stands on its own.

---

## 3. Typography Rules

The pairing of Cal Sans (display) and Inter (interface) is the only visual decision this site needs.

| Role | Typeface | Size | Weight | Notes |
|------|----------|------|--------|-------|
| H1 (hero) | Cal Sans | 128px | 400 | Background-clip text technique |
| H2 (section labels) | Inter | 14px | 400 | 20px line height |
| Body | Inter | 16px | 400 | 24px line height |
| Links | Inter | 14px | 400 | 20px line height |

Key rules:
- Cal Sans is used **only once** — the hero H1. Its personality is rationed.
- No negative tracking anywhere — Inter and Cal Sans are used at their natural spacing
- No weight variation above 400 — everything is regular weight. The scale disparity (128px vs 14px) does all the work.
- The jump from 128px to 14px is enormous and intentional — it forces a visual rhythm that nothing else could create
- Line height on the hero is 128px (1:1 ratio) — the heading is a block, not flowing text

---

## 4. Component Stylings

**Navigation**: Transparent background, Zinc-500 text. Links lighten to Zinc-400 on hover. No underlines. Focus rings use the browser's native blue (`rgb(55–59, 104, 161–164)`).

**Hero heading**: Background-clip text with white or near-white background color — creates a text knockout effect where the letter forms reveal the color/texture behind them. This is the defining component.

**Links (secondary)**: Muted grey with underline decoration (e.g., `a.underline`), hover lightens. Standard link behavior, no transforms or decorative effects.

**No cards, no buttons, no form elements detected**. The site is essentially navigation + hero text + minimal prose.

**Border radii**: None detected. No rounded corners — consistent with a raw, terminal aesthetic.

**Shadows**: None detected. Elevation is not a concept this design uses.

---

## 5. Layout Principles

- **Tailwind breakpoints**: 640, 768, 1024, 1280, 1536px — the full default set, though likely only a few are actually used
- **Body padding**: `0px` — no container padding at the body level
- **Max-width centering**: Not detectable from CSS data; likely managed through a Tailwind `max-w-*` wrapper inside `<main>`
- The 128px hero text dominates the above-fold on any desktop — layout serves to frame it
- Navigation is minimal: just a few text links, horizontally aligned, likely top-left

---

## 6. Depth & Elevation

There is no elevation system. chronark.com is deliberately flat in every dimension:

- No surface layers
- No background colors on any containers
- No box shadows
- No blur effects

The only perceived depth is the contrast between the white/transparent hero text and the absolute black background. Everything else exists on the same plane.

---

## 7. Do's and Don'ts

**Do:**
- Use Cal Sans exclusively for the hero display element — one use, full impact
- Use the background-clip text technique on the H1 for the knockout effect
- Keep the entire body in Zinc-500 (`rgb(113, 113, 122)`) at weight 400
- Let scale disparity (128px vs 14px) do all the visual work
- Use absolute black `rgb(0,0,0)` for the page background, nothing warmer

**Don't:**
- Use Cal Sans for anything other than the single hero heading
- Add surface backgrounds or cards — this design has no containers
- Add shadows or elevation
- Increase font weights above 400
- Add accent colors or decorative elements

---

## 8. Responsive Behavior

While the full Tailwind breakpoint set is present in the CSS (640/768/1024/1280/1536px), the actual responsive adaptations are minimal:

- **<768px**: The 128px hero likely scales down significantly — Cal Sans at full size would be unusable on mobile
- **≥768px**: Full desktop layout with the hero at or near 128px
- Navigation simplifies on mobile (possibly a hamburger menu or stacked links)

The sparse layout makes responsive adaptation straightforward — there's little to rearrange.

---

## 9. Agent Prompt Guide

When recreating or referencing chronark.com:

> "Design a minimal developer portfolio on pure black `#000000`. Hero: Cal Sans 128px/400 using background-clip text technique (white background, transparent color). All other text: Inter at Zinc-500 `rgb(113,113,122)`, hover to Zinc-400 `rgb(164,164,170)`. Two type sizes: 128px hero and 14–16px everything else, both at weight 400. No cards, no shadows, no surface colors, no rounded corners. Navigation is bare text links. The design philosophy is that scale contrast alone creates hierarchy."

---

*Generated by Sparkbites — extracted from live CSS analysis*
