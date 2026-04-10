# nevflynn.com — Design System

## 1. Visual Theme & Atmosphere

Nev Flynn's personal site leans into the aesthetic of a dark-mode developer portfolio with creative warmth layered on top. The base is near-black — almost ink — with a background of `rgb(13, 17, 23)`, reminiscent of GitHub's dark theme, grounding the page in a technical seriousness. Against this deep canvas, a custom display typeface (Moranga Bold) injects personality: rounded, confident, editorial. The result is a personal brand that reads as "engineer with taste" — structured but not sterile, expressive but restrained. There are no decorative gradients, no hero imagery demanding attention; the typography does the visual work. The density is comfortable, the whitespace intentional.

## 2. Color Palette & Roles

| Role | Value | Usage |
|---|---|---|
| Page Background | `rgb(13, 17, 23)` | Base canvas — near-black with a slight blue undertone |
| Primary Text | `rgb(208, 215, 222)` (inferred) | Body copy and paragraphs against dark bg |
| Outline / Focus | `rgb(0, 0, 0) none` | Buttons inherit a zero-opacity outline by default |
| Interactive Ink | system default | Links and buttons use inherited context |

No custom CSS properties were defined — the palette is handled at the browser/framework level. Colors are implicit rather than tokenized. This is a minimal system by design.

**What's absent:** No accent color. No semantic error/success states. No gradient. The restraint is intentional — a monochromatic dark field where content is the only color.

## 3. Typography Rules

Two type families define the entire voice of the site:

- **Display: Moranga Bold** — Used exclusively for `h2` headings. A custom typeface with rounded character forms that contrast sharply with the technical stack fallback. `24px / 32px`, weight 400 (the Bold is baked into the font name itself). Normal letter-spacing.
- **Body: System UI stack** — `-apple-system, system-ui, Segoe UI, Roboto, Oxygen, Ubuntu, Cantarell, Fira Sans, Droid Sans, Helvetica Neue, sans-serif` — The browser's native sans-serif. `16px` body. Zero custom OpenType features.

| Selector | Family | Size | Weight | Line Height |
|---|---|---|---|---|
| `h2` | Moranga Bold | 24px | 400 | 32px |
| `body` | System UI | 16px | 400 | — |

**Design intent:** Moranga Bold is used sparingly at a single heading level. Every other text element inherits the system stack. This contrast — one expressive typeface versus pure utility — is the entire typographic strategy.

## 4. Component Stylings

**Buttons:** Outlined with `rgb(0, 0, 0) none 0px` outline (effectively no visible ring). Padding suggests standard interactive sizing. No box-shadow. Background likely inherits or is transparent.

**Subscribe form:** A newsletter subscribe button exists (`newsletter__subscribebutton`). Styled simply — no elaborate state styling in the extracted CSS. Functionality over decoration.

**Map/Lockdown toggle:** Interactive map elements (`map__marker`, `bio__lockdownbutton`) suggest a location-based interactive section. These appear as custom components with their own scoped class names rather than a shared design system.

**Navigation:** No dedicated nav styling extracted — likely minimal or integrated into the body layout.

## 5. Layout Principles

- **Spacing:** References to `25px` and `71961px` (likely a large z-index or transform value) and standard `padding/margin` suggest a relaxed, content-first layout.
- **Grid:** No explicit grid tokens. Layout appears single-column or narrow-centered, typical of a personal portfolio.
- **Whitespace philosophy:** Generous. The dark background means negative space reads as atmosphere rather than emptiness.
- **No layout framework tokens** detected — custom spacing throughout.

## 6. Depth & Elevation

No box-shadows or elevation tokens are defined. The dark background itself creates depth through contrast — content floats on the dark surface rather than being layered with shadows. Depth is achieved chromatically, not through light simulation.

## 7. Do's and Don'ts

**Do:**
- Use Moranga Bold only for primary headings — never body copy
- Respect the near-black background as the defining visual signature
- Keep the color count low; add accent only via content (images, links)
- Match the system UI stack for all non-heading text

**Don't:**
- Don't introduce bright background colors or hero gradients
- Don't add decorative borders or dividers unless truly necessary
- Don't use Moranga Bold below `20px` — it's a display face
- Don't tokenize colors prematurely; this site works without a token system

## 8. Responsive Behavior

No explicit breakpoints were found in the extracted CSS. The system-UI font stack naturally handles text rendering across all devices. `16px` base body size meets minimum legibility standards. The personal portfolio format suggests a single-column flow that adapts gracefully without explicit grid breakpoints. Touch targets on buttons inherit browser defaults.

## 9. Agent Prompt Guide

**Quick reference:**
- Background: `rgb(13, 17, 23)`
- Display type: `"Moranga Bold"` at 24px/32px for h2
- Body type: System UI stack at 16px
- No accent color — keep it monochromatic

**Prompt starters:**
- *"Dark personal portfolio, near-black background `rgb(13, 17, 23)`, Moranga Bold display headings, system-UI body text, no shadows, content-first layout."*
- *"Minimal dark site: ink background, one expressive display font for h2, everything else in native system sans-serif. No color accents."*

---

*Generated by Sparkbites — extracted from live CSS analysis*
