# haydenbleasel.com — Design System

## 1. Visual Theme & Atmosphere

Hayden Bleasel's personal site embodies a specific strain of minimalism: confident, typographic, and deliberately restrained. The canvas is pure white. The text is near-black. The margins are vast. Nothing competes for attention except the content itself.

What elevates this beyond generic minimalism is the typographic pairing. The h1 uses Instrument Serif — an elegant, slightly quirky display serif with character — at a modest 38px. Everything else runs on a geometric sans. This single serif/sans split does enormous work: the name or hero line becomes a human signature, while the surrounding interface recedes to pure utility. It's a designer's portfolio that doesn't shout; it holds space.

The color vocabulary is intentionally absent. No accent color was extracted. No brand hue asserts itself. The only color in the interactive states is a shift from medium-dark gray to near-black on hover — the gentlest possible signal that something is clickable. This is a design that trusts the reader.

---

## 2. Color Palette & Roles

**Backgrounds**
- Pure white `rgb(255, 255, 255)` — universal page background
- Neutral-100 `--secondary` — subtle secondary surface (hover states, code blocks)

**Text**
- Near-black `lab(2.75381 0 0)` ≈ `#060606` — headings, primary content
- Dark gray `lab(34.924 0 0)` ≈ `#4a4a4a` — body text, links at rest
- Muted `--muted: neutral-600` — captions, secondary labels

**Borders & Dividers**
- Neutral-200 `lab(90.952 0 0)` ≈ `#e5e5e5` — universal border color
- The same value appears consistently across all element borders

**Buttons**
- Near-black at 80% opacity `oklab(0.145 / 0.8)` — translucent dark fill
- White text on dark button
- Focus: opaque near-black

**Hover States**
- Links: `lab(34.924...)` (body gray) → `lab(2.75381...)` (near-black) — darkens without color change
- No underlines, no color, no background fill — pure value shift

What's absent: no accent color, no brand hue, no semantic colors (no green for success, no red for error). The palette is a grayscale system.

---

## 3. Typography Rules

**Instrument Serif** — hero/h1 only
- `38px` / `400` weight / `45.6px` line-height / `-0.24px` letter-spacing
- Used for the name or primary headline — where personality is needed
- Normal weight (not bold) — elegance over emphasis

**Sans (custom)** — the system font for everything else
- h2: `16px` / `500` / `24px` — medium weight section labels
- Body/paragraphs: `16px` / `400` / `26px` — slightly open line-height for readability
- Links: `16px` / `400` / `26px` — no visual differentiation from body other than context
- Buttons: `16px` / `400` / `24px`
- Inputs: `16px` / `400` / `26px`
- Letter-spacing: `-0.24px` globally — a subtle tightening applied to every element

The `-0.24px` letter-spacing is the system's quiet signature: it makes the sans feel more premium without being visibly compressed.

**What's absent:** no monospace, no bold body text, no uppercase labels, no size variation below 16px in the primary content hierarchy.

---

## 4. Component Stylings

**Navigation**
- Transparent background, no border, `24px` gap between items
- Links shift from body gray `lab(34.924...)` to near-black on hover — imperceptible on fast glance

**Buttons**
- Translucent near-black `oklab(0.145 / 0.8)` — feels like a dark glass button
- Pill-shaped via extreme border radius (`3.35544e+07px` — effectively `border-radius: 9999px`)
- White text
- Focus changes to fully opaque near-black — accessibility-friendly

**Content Links**
- No underline assumed, no background — pure typography
- Hover: color darkens from `#4a4a4a` to `#060606`

**Sections**
- `0px` padding, `24px` gap between internal elements — sections are tight containers
- Main layout: `128px 16px` padding, `0 304px` margin — creates a centered narrow column

**Borders**
- All borders: `lab(90.952 0 0)` ≈ `#e5e5e5` — neutral-200, consistently light
- `6px` radius on small components (non-pill elements)

---

## 5. Layout Principles

The layout is a study in generous whitespace and tight column control. The `main` element uses `margin: 0 304px` — a large fixed margin that creates an extremely narrow reading column at desktop. This is closer to a blog or long-form reading layout than a portfolio grid.

Combined with `padding: 128px 16px`, the content sits far from all edges. The vertical breathing room (128px top) is exceptional — the page opens with air before content appears. Sections have `24px` gap between them: not tight, not loose, just right for a vertical narrative flow.

Only one breakpoint at `600px` is visible in the extracted data — suggesting the design collapses cleanly at mobile with minimal intermediate states. The `304px` margin would need to collapse to `0` or `16px` at that breakpoint.

---

## 6. Depth & Elevation

There are no shadows. No extracted shadow values, no box-shadow tokens. The design achieves separation through whitespace, typography scale, and color steps alone.

No surface elevation, no card lift, no glass morphism. The one button has a translucent fill (`oklab(0.145 / 0.8)`) that creates implicit depth — it looks slightly like a glass layer over white — but this is the extent of dimensional play.

The `border: #e5e5e5` on elements does light work to separate sections. No inset shadows, no outer glows. The absence of elevation is itself the design statement: everything is on the same plane, readable, equal.

---

## 7. Do's and Don'ts

**Do:**
- Use pure white `#ffffff` as the only background — no off-whites, no gray
- Apply Instrument Serif exclusively to the primary name/hero heading
- Set `-0.24px` letter-spacing globally on the sans — it's the system's tonal signature
- Give the layout generous margins — the narrow reading column is intentional
- Keep hover states as value-only shifts: gray → near-black, no color
- Use `border-radius: 9999px` for pill buttons

**Don't:**
- Don't introduce an accent color — the monochromatic palette is the point
- Don't reduce the 128px top padding — the opening air is essential to the atmosphere
- Don't add shadows or elevation — the design is intentionally flat
- Don't use Instrument Serif below 32px — it reads as decoration, not signature, at small sizes
- Don't add border-bottom underlines to links — the color shift alone signals interactivity
- Don't add more than two type scales — the 38px + 16px system is complete

---

## 8. Responsive Behavior

A single breakpoint at `600px` is all that's needed — the layout is so simple that it requires minimal adjustment. At mobile, the `margin: 0 304px` on main collapses to full-width with `padding: 16px`. The `128px` top padding likely reduces to `64px` or `80px`.

The narrow reading column that feels generous at desktop becomes a natural full-width column at mobile — no content reflow needed. The single CTA button (pill shape) works at any width. Typography stays at `16px`; Instrument Serif at `38px` may scale to `28–32px` on mobile.

---

## 9. Agent Prompt Guide

Use this block when prompting an AI to generate UI in the style of haydenbleasel.com:

```
Design a minimal personal portfolio with pure white background (#ffffff) and no accent colors. Text hierarchy uses two values: near-black (#060606) for headings and #4a4a4a for body. Apply -0.24px letter-spacing globally. Hero heading uses Instrument Serif (or a similar editorial serif) at 38px/400 weight. All other text uses a geometric sans-serif (or system sans) at 16px. Layout is a centered narrow column with 128px vertical top padding and generous side margins. No shadows, no elevation, no card backgrounds. Borders are neutral-200 (#e5e5e5). Hover links darken from body gray to near-black — no color change. Primary button is a pill shape with translucent near-black fill and white text. One breakpoint at 600px. The design is about whitespace and typographic restraint.
```

---

*Generated by Sparkbites — extracted from live CSS analysis*
