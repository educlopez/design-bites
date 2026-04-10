# Dapper Agency — Design System

## 1. Visual Theme & Atmosphere

Dapper Agency operates at the intersection of Swiss clarity and playful energy. The base is a warm light grey (#f3f3f3) — not cold white, not cream, but a neutral that lets a vivid mint-green primary (#74f5a1) and unexpected electric purple secondary (#c35fff) pop with maximum contrast. The typeface pairing — Helvetica Now Display for display work and Helvetica Now Text for body — signals craft and precision. This is a design agency that takes typography seriously while using colour to show personality. The depth system uses a single generous shadow for elevation.

---

## 2. Color Palette & Roles

| Role | Value | Notes |
|------|-------|-------|
| Background | `#f3f3f3` | Warm light grey — not pure white |
| Dark surface | `#212121` | Near-black for reversed sections |
| Dark tint | `#191919` | Slightly deeper dark panel |
| Dark tint hover | `#292929` | Dark hover state |
| Primary accent | `#74f5a1` | Mint green — key CTAs, highlights |
| Primary dark | `#3c7c52` | Darker green for active/pressed |
| Primary light | `#d5fce3` | Pale mint for backgrounds/badges |
| Secondary accent | `#c35fff` | Electric purple — secondary calls to action |
| Border | `#eee` | Hairline borders |
| Muted text | `#919191` | Greyed-out / secondary copy |
| Light tint | `#ffffff` | Pure white for cards on grey |
| Light tint hover | `#e7e7e7` | Slightly darker on hover |
| Dialog bg | `#050505` | Almost black modal |

The dual accent system (mint + purple) provides flexibility for feature differentiation without introducing brand inconsistency.

---

## 3. Typography Rules

**Display typeface:** Helvetica Now Display — used for headlines.
**Text typeface:** Helvetica Now Text — used for UI labels and body.

| Level | Size | Weight | Line Height | Tracking |
|-------|------|--------|-------------|----------|
| h2 | 53px | 700 | 58.7px | -1.07px |
| h4 | 26.7px | 700 | 29.3px | — |
| h3 / labels | 13.3px | 700 | 17.3px | -0.4px |
| h1 (computed) | 16px | 700 | 19.2px | -0.16px |

- All weights are 700 — bold is the default register, not an emphasis state.
- Letter-spacing is negative throughout, even at smaller sizes (-0.4px at 13px).
- No text transforms — the boldness provides hierarchy without uppercase tricks.
- Font size uses em units (`--size-font: var(--unit-width)` with `--unit-width: 16px`) — the type scale is anchored to the root em.

---

## 4. Component Styling

- **Border radii:** Small (0.5em), medium (1em), large (1.5em) — a rounded system, in contrast to the sharp-edged typography.
- **Elevation shadow:** `rgba(0,0,0,0.3) 0px 32px 68px 0px` — a single large, soft drop shadow for floated UI panels.
- **Buttons:** Transparent background with white text — ghost style on dark backgrounds.
- **Textarea:** Dark background (#212121), light text (#f3f3f3) — reversed for form inputs.
- **Gap system:** xs=1em, default=1.5em, L=3em, XL=4.5em, eyebrow=2.5em — em-based, coherent.

---

## 5. Layout Principles

- Container max: 1920px, ideal: 1440px, min: 992px — a wide-screen-first design.
- Section padding: 12em (full), 9em (three-quarters), 6em (half) — generous spatial rhythm.
- Header padding: 12em — the nav breathes.
- Container padding: 3em on each side.
- The `--pixel` token is 3em — used for specific graphic/decorative sizing.
- Nav bar height: 7.5em — tall, prominent navigation.

---

## 6. Depth & Elevation

- One shadow tier: `0px 32px 68px 0px rgba(0,0,0,0.3)` — large blur, significant elevation for floating panels.
- No multi-tier shadow system. Surface depth is communicated through the light/dark colour alternation.
- The `--grow: 0.25em` token suggests micro hover-expand animations.

---

## 7. Do's and Don'ts

**Do:**
- Use mint green (#74f5a1) as the primary CTA colour — it's the brand's most distinctive trait.
- Pair rounded corners (1–1.5em) with bold typography for a playful-but-precise feel.
- Use em-based spacing to keep proportions fluid across zoom levels.
- Apply the single large shadow only to elevated floating panels.

**Don't:**
- Introduce thin (100–300) type weights — 700 is the only weight in this system.
- Use pure white (#ffffff) as the page background — the warm grey (#f3f3f3) is deliberate.
- Mix the mint and purple accents on the same component.
- Add multiple shadow tiers — one large shadow is the design intent.

---

## 8. Responsive Behavior

- Container width collapses from 1920px max through the ideal 1440px.
- Section padding tokens are halved/three-quartered for smaller contexts.
- Em-based spacing scales naturally with font-size adjustments.
- The nav bar height (7.5em) may need explicit overrides at mobile scale.

---

## 9. Agent Prompt Guide

> Build a design agency site using Dapper's aesthetic. Background is warm grey #f3f3f3, dark sections use #212121. Primary accent: mint #74f5a1. Secondary accent: purple #c35fff. Typeface: Helvetica Now Display (bold 700) for headlines, Helvetica Now Text for labels. All text at weight 700, negative letter-spacing. Border-radius: 0.5–1.5em (rounded system). Section padding 12em. One elevation shadow: rgba(0,0,0,0.3) 0 32px 68px. No gradients, no light shadows.

---

*Generated by Sparkbites — extracted from live CSS analysis*
