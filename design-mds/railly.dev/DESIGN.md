# railly.dev — Design System

## 1. Visual Theme & Atmosphere

Railly.dev is a developer portfolio stripped to its essential signal. The design philosophy is deliberate minimalism — not the kind born from laziness, but from confidence. The near-white background (`#FDFDFC`, just a whisker off pure white) and near-black text (`#111111`) create maximum contrast with zero visual noise. There are no gradients, no illustrative decorations, no color accents in the content layer. The only departure from monochrome is a sticky dark element — a bar, nav, or code surface — rendered in `#111111` that anchors the page visually.

The atmosphere communicates: "the work speaks for itself." This is a portfolio designed for developers reading developers. Typography does all the heavy lifting.

---

## 2. Color Palette & Roles

**Surfaces**
- `#FDFDFC` — Page background (near-white with imperceptible warm cast)
- `#111111` — Sticky/pinned surface (dark bar, likely navigation or code block)

**Text**
- `#111111` — Primary body text and borders (near-black, maximally legible)
- `#525252` — Secondary text (h2, subheadings, metadata) — a neutral mid-grey
- `#FDFDFC` — Text on dark surfaces (button labels, inverted contexts)

**Interactive**
- No accent color detected for links or CTAs in the default state
- Hover on buttons uses `opacity: 0.6` — fade rather than color shift
- Focus states use browser-default `rgb(0, 95, 204)` blue outline — accessibility maintained without custom styling

**Notable absence**: There is no brand accent color. The palette is intentionally achromatic. Any color in the visual experience comes from project screenshots or external content.

---

## 3. Typography Rules

The single typeface is **IBM Plex Sans** — IBM's open-source humanist grotesque. The choice is meaningful: it signals a developer/technical background while retaining warmth through its slightly humanist letter forms. It is not the flashy choice — it is the considered one.

- **h1**: 18px / weight 500 / `letter-spacing: -0.45px` — deliberately modest header size; this is a personal site, not a landing page
- **h2**: 14px / weight 400 — subdued section labeling, nearly body-sized
- **body / p**: 15–16px / weight 400 — comfortable reading size
- **inputs**: 16px — prevents iOS zoom, a developer detail worth noting

The tight negative letter-spacing on h1 (`-0.45px`) is the only typographic refinement visible. Everything else is left at optical defaults. No text transforms, no uppercase labels, no decorative weight contrasts. The scale is deliberately compressed — headings don't shout, they state.

---

## 4. Component Stylings

**Buttons**: Transparent background with near-white text on dark surfaces. Interaction feedback is purely opacity-based (`opacity: 0.6` on hover) — no color shifts, no shadows, no transforms. This is austere by design.

**Subscribe button**: Solid `#111111` fill with `#FDFDFC` text — the only filled button, used for the primary CTA. The inversion of the base palette makes it immediately identifiable.

**Border radii**: `6px` primary, `4px` secondary — subtly rounded, not pill-shaped. Sharp but not harsh.

**Code/pre surfaces**: The sticky `#111111` surface likely serves double duty as a code display area or terminal-like element.

No cards, no modals, no complex component patterns detected. The site is compositionally simple: text, a few interactive elements, and possibly project cards built from the same minimal palette.

---

## 5. Layout Principles

Main content uses `padding: 96px 24px 32px` — generous top padding (likely clearing a fixed navigation bar) with conservative side margins. This creates a tall, narrow reading column suited to focused content consumption.

No breakpoints were detected in the CSS extraction — likely the layout is a single fluid column that scales naturally, or breakpoints are handled purely through Tailwind utility classes. The Astro + Tailwind stack confirms a utility-first approach where responsive behavior lives in markup rather than media query declarations.

The header is transparent and overlaid — the content starts directly at the viewport top with padding compensation.

---

## 6. Depth & Elevation

Depth is completely absent by conventional measures: no box shadows detected anywhere. The only elevation signal is the sticky dark surface, which creates contrast-based depth — a dark plane pinned above the lighter page. This is 2D-first design; the third dimension is not invited.

Even interactive states avoid shadow. Focus outlines are browser-default thin strokes. The site feels like a printed page rather than a layered interface.

---

## 7. Do's and Don'ts

**Do**
- Keep the palette achromatic — color belongs to content, not chrome
- Use IBM Plex Sans exclusively; its character is the brand
- Let opacity handle hover states rather than color changes
- Keep border-radius conservative: 4–6px only
- Trust whitespace — generous padding is a feature, not waste

**Don't**
- Introduce accent colors in navigation or UI chrome
- Scale up font sizes dramatically — the compressed type scale is intentional
- Add box shadows or card lift effects
- Use uppercase or tracked-out letter-spacing for labels

---

## 8. Responsive Behavior

No explicit CSS breakpoints were extracted, suggesting the layout is a single-column fluid design. The 24px side padding at all sizes provides minimum breathing room. The Tailwind approach likely uses `sm:`, `md:` utilities inline, but the design probably doesn't fundamentally restructure across breakpoints — it's a single-column document at every size.

Sticky navigation (the `#111111` surface) likely collapses gracefully at mobile widths given the site's minimal complexity.

---

## 9. Agent Prompt Guide

> "Design in the style of railly.dev: achromatic palette — near-white `#FDFDFC` background, near-black `#111111` text and surfaces. IBM Plex Sans as sole typeface, modestly sized. No accent colors, no shadows, no decorative elements. Hover states use opacity fade only. Border-radius capped at 6px. The design communicates through confident emptiness — let content and whitespace do the work."

---

*Generated by Sparkbites — extracted from live CSS analysis*
