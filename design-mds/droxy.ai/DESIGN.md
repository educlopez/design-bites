# Droxy AI — Design System

## 1. Visual Theme & Atmosphere

Droxy AI builds with softness and approachability — a near-white background (#f6f7f8) rather than pure white, pastel card surfaces, and Inter Display as the typographic backbone. It is the opposite of the aggressive dark AI aesthetic: this product wants to feel friendly, trustworthy, and accessible. The card palette reads like a children's colour wheel of gentle pastels — warm yellow, sage green, lavender, and dusty teal — each assigned to a feature or product area. Shadows are cool blue-tinted rather than neutral black, anchoring the elevation system in the same cool-soft tone as the overall palette.

---

## 2. Color Palette & Roles

| Role | Value | Notes |
|------|-------|-------|
| Page background | `#f6f7f8` | Warm off-white |
| Primary text | `rgb(37,37,37)` | Near-black, neutral |
| Section heading | `rgb(37,37,37)` | Same near-black |
| Slate grey surface | `rgb(100,113,126)` | Muted blue-grey card |
| Warm yellow card | `rgb(251,235,192)` | Pastel sand |
| Sage green card | `rgb(217,234,201)` | Soft green |
| Lavender card | `rgb(227,201,234)` | Soft purple |
| Teal-blue card | `rgb(214,233,235)` | Pale teal |
| Default link | `rgb(0,0,238)` | Browser-default (likely unstyled) |

The pastel card system assigns one colour per product feature/panel — used as full background fills on card components, not as accent highlights. Cool-tinted shadows reinforce the gentle, non-aggressive tone.

---

## 3. Typography Rules

**Primary typeface:** Inter Display SemiBold (for headings), Inter Display (for body).

| Level | Size | Weight | Line Height | Tracking |
|-------|------|--------|-------------|----------|
| h2 | 48px | 400 (SemiBold face) | 54px | -1.92px |
| h3 | 32px | 600 | 40px | -0.32px |
| p / body | 14px | 400 | — | — |
| Base body | 12px | 400 | normal | normal |

- Inter Display SemiBold is the face for h2 — the weight is baked into the font name, so CSS weight is 400 relative to that subfamily.
- h3 at weight 600 with Inter Display (regular face) is the secondary heading level.
- Negative tracking at large sizes (-1.92px at 48px) — strong compression typical of modern SaaS headings.
- No monospace, no display novelty — this is pure Inter through and through.

---

## 4. Component Styling

- **Pastel cards:** Full-colour fill backgrounds in the pastel palette — rounded (border-radius inferred from Framer).
- **Shadow system (cool-tinted):**
  - Default card: `rgb(220,224,229) 0 0 0 1px, rgba(201,219,234,0.32) 0 7.65px 19.14px -5.74px, rgba(12,73,134,0.04) 0 -4px 8px inset`
  - Elevated card: `rgba(201,219,234,0.32) 0 7.65px 19.14px -5.74px, rgba(12,73,134,0.04) 0 3.83px 8px inset`
- The blue-tinted shadows (rgba(12,73,134,0.04) — dark navy at 4% opacity for inset) is subtle but consistent with the cool palette.
- 1px border ring in light grey (rgb(220,224,229)) before the blur shadow — crisp edge before soft glow.
- Links default to browser blue — likely not customised in this tool/utility context.

---

## 5. Layout Principles

- Body padding is 0 — content fills to edge, components control their own padding.
- No section-level spacing tokens — Framer absolute positioning handles layout.
- The layout appears card-grid based, with each feature in its own pastel panel.

---

## 6. Depth & Elevation

- Cool-tinted shadow system — all shadows have a blue-grey quality rather than neutral black.
- 1px border ring in light grey before the blur shadow — a crisp edge before the soft glow.
- Inset shadow adds a subtle concavity to cards — they appear pressed slightly into the surface.
- No dramatic depth — the elevation is whisper-soft, in keeping with the friendly aesthetic.

---

## 7. Do's and Don'ts

**Do:**
- Assign one pastel to each feature area — the colour communicates category, not state.
- Use cool-tinted shadows exclusively — warm shadows would fight the palette.
- Apply Inter Display SemiBold at -1.92px tracking for all primary headings.
- Include the 1px grey border ring with every elevated card.

**Don't:**
- Use high-contrast or saturated accent colours — this palette is intentionally muted.
- Mix multiple pastels in a single component.
- Use dark backgrounds or dark mode — the design is explicitly light and airy.
- Add harsh black drop shadows — only cool-tinted soft shadows.

---

## 8. Responsive Behavior

- Framer-built — absolute positioning requires explicit breakpoints at mobile.
- Pastel card grid should reflow to single-column at mobile.
- The compact body text (12–14px) needs minimum 16px on mobile to comply with accessibility norms.
- Off-white background (#f6f7f8) avoids the glare of pure white on high-brightness screens.

---

## 9. Agent Prompt Guide

> Build a friendly AI SaaS interface using Droxy's soft aesthetic. Background #f6f7f8. Text rgb(37,37,37). Typeface: Inter Display SemiBold for h2 at 48px/-1.92px tracking, Inter Display 600 for h3 at 32px/-0.32px tracking. Four pastel card surfaces: warm yellow rgb(251,235,192), sage rgb(217,234,201), lavender rgb(227,201,234), teal rgb(214,233,235). Cool-tinted shadows with 1px rgb(220,224,229) border ring. No dark backgrounds, no saturated accents, no warm shadows.

---

*Generated by Sparkbites — extracted from live CSS analysis*
