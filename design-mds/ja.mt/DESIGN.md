# ja.mt — Design Language

## 1. Visual Theme & Atmosphere

ja.mt is a personal site of warm restraint — a Framer-built portfolio using an analog paper palette instead of the typical dark or white canvas. The background is a faded terracotta parchment (`rgb(245, 234, 221)`), and its secondary surface deepens slightly to a muted blush (`rgb(221, 202, 191)`). The visual mood is handmade and tactile without being fussy — the digital equivalent of a well-used sketchbook. The body typeface, **Exposure Italic Trial**, is a display-calibre italic at 20px body size — an unusual and bold choice that gives all prose a calligraphic lean. This is a site that feels personal rather than professional in the corporate sense.

## 2. Color Palette & Roles

| Role | Value | Usage |
|---|---|---|
| Base background | `rgb(245, 234, 221)` — parchment | Body, primary surface |
| Secondary surface | `rgb(221, 202, 191)` — blush tan | Accent panels, cards |
| Text | `rgb(0, 0, 0)` — black | All body copy |
| Link / interactive | `rgb(0, 0, 238)` — browser blue | Anchor elements |
| Link overlay bg | `rgba(255, 87, 87, 0)` — transparent coral | Background color defined but invisible |

The palette is warm and monochromatic — two tones of the same sandy hue. Black text on warm parchment reads like ink on paper. The browser-default blue for links is kept as-is, a deliberate vernacular signal. The defined-but-transparent coral (`rgba(255,87,87,0)`) on links hints at a potential hover state colour that never fires — a ghost of intention.

**What's absent:** No dark surfaces, no cool tones, no gradients, no shadows, no border-radius.

## 3. Typography Rules

**Exposure Italic Trial −10** is the primary typeface — a trial optical variant tuned for smaller sizes (the −10 designation typically indicates tighter spacing/ink trap adjustments). Using an italic-only trial font as the body typeface is a distinctive choice that makes every paragraph feel like a personal note.

| Element | Family | Size | Weight | Line-height |
|---|---|---|---|---|
| Body / p | Exposure Italic Trial −10 | 20px | 400 | 34px (1.7) |
| Navigation / links | sans-serif (system) | 12px | 400 | normal |

The 1.7 line-height on body text is generous — text breathes like handwriting in a journal. Navigation uses a plain system sans as a deliberate contrast: functional vs. expressive. No heading typography was captured, suggesting either a single-level hierarchy or headings using the same Exposure family.

**What's absent:** No bold weight, no letter-spacing, no text transforms, no display-size type (above 20px in captured data).

## 4. Component Styling

- **Framer architecture:** Absolutely positioned components with Framer Motion for transitions.
- **No border-radius** — all surfaces are sharp-cornered, like cut paper.
- **No shadows** — elevation is purely tonal (parchment vs. blush).
- **Links:** Browser-default blue with the transparent coral background — hover states likely handled by Framer Motion rather than CSS.
- **Focus:** Default browser outline (`rgb(0, 95, 204) auto 1px`) — no custom focus styling.
- **Single breakpoint at 464px** — a lean two-state responsive model (mobile / everything else).

## 5. Layout Principles

- Framer canvas layout; no flow-based grid detected.
- A single breakpoint at 464px is unusually minimal — suggesting the design is primarily desktop with a simple mobile reflow.
- No spacing data beyond body `padding: 0` — layout rhythm is encoded in Framer component positions.
- The warm surfaces invite close, intimate composition rather than wide-margin editorial space.

## 6. Depth & Elevation

Two tonal surfaces — parchment (luminance 0.925) and blush (luminance 0.81) — create the only depth layer. No shadows, no blur. The ~11% luminance difference between the two surfaces is subtle but sufficient to define sections from backgrounds without any border or shadow. It reads as paper layering.

## 7. Do's and Don'ts

**Do:**
- Use `rgb(245, 234, 221)` as the base and `rgb(221, 202, 191)` as the inset/panel surface.
- Let Exposure Italic carry the personality of body copy — don't override with regular weight.
- Keep line-height at 1.7 for body text; the spaciousness is central to the reading feel.
- Leave links in browser-default blue — the vernacular contrast is intentional.

**Don't:**
- Introduce dark backgrounds or cool grays — this design lives entirely in warm analog tones.
- Add border-radius or shadows; the paper metaphor depends on flat, cut surfaces.
- Use bold weights or uppercase transforms — the voice is soft and handwritten.
- Over-engineer the responsive model; one breakpoint at 464px is purposefully simple.

## 8. Responsive Behavior

With only one breakpoint at 464px, the design operates in two states: narrow mobile (below 464px) and everything wider. The Framer canvas reflows from its desktop composition to a stacked single-column view. The italic body text and warm palette hold their character at all widths; no typography rescaling was captured, suggesting copy volume is intentionally short.

## 9. Agent Prompt Guide

> Build a personal portfolio in the style of ja.mt: warm parchment background (`rgb(245,234,221)`), blush panel surface (`rgb(221,202,191)`), black body text. Primary typeface is an expressive italic (like Exposure Italic or a similar calligraphic font) at 20px/34px line-height. Navigation in plain system sans at 12px. No border-radius, no shadows. Browser-default blue for links. Framer/absolute-position layout with a single breakpoint at 464px. The mood is intimate, analog, and journal-like — not corporate.

---

*Generated by Sparkbites — extracted from live CSS analysis*
