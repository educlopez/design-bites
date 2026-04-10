# zmh.org — Design System

## 1. Visual Theme & Atmosphere

WordPress-built portfolio or organization site using a bold violet brand color against clean white. The design leans on WordPress block editor conventions with a structured, institutional feel.

**Mood:** institutional, clean, WordPress-conventional, bold accent

The visual language is refined without being austere — custom typefaces carry the personality while structural clarity does the heavy lifting. A structured token system underpins every color decision.

---

## 2. Color Palette & Roles

**Design tokens found:** 19 color custom properties

**Named Tokens (excerpt)**
- `--wp-block-synced-color`: `#7a00df`
- `--wp-editor-canvas-background`: `#ddd`
- `--wp-admin-theme-color`: `#007cba`
- `--wp-admin-theme-color-darker-10`: `#006ba1`
- `--wp-admin-theme-color-darker-20`: `#005a87`
- `--wp--preset--color--black`: `#000000`
- `--wp--preset--color--cyan-bluish-gray`: `#abb8c3`
- `--wp--preset--color--white`: `#ffffff`
- `--wp--preset--color--pale-pink`: `#f78da7`
- `--wp--preset--color--vivid-red`: `#cf2e2e`
- `--wp--preset--color--luminous-vivid-orange`: `#ff6900`
- `--wp--preset--color--luminous-vivid-amber`: `#fcb900`

**Palette philosophy:** Controlled neutrals with a single accent that carries all interactivity signals.

---

## 3. Typography Rules

- **h1**: Merriweather / 24px / wt 550 / lh 34.8px
- **h2**: Merriweather / 13px / wt 700 / tracking 1px / lh 18.85px / uppercase
- **body**: Lucida Grande / 12.8px / wt 400 / lh 21.76px
- **p**: Lucida Grande / 14.8px / wt 400 / lh 25.16px
- **a**: Lucida Grande / 12.8px / wt 400 / lh 21.76px
- **button**: Arial / 13.3333px / wt 400
- **input**: Lucida Grande / 12.8px / wt 400 / lh 19.2px
- **[role="dialog"]**: Lucida Grande / 16px / wt 400 / lh 27.2px
- **label**: Lucida Grande / 10px / wt 400 / lh 17px

**Custom typefaces:** Merriweather, Lucida Grande

**Typography philosophy:** Two-typeface system: display and body voices serve distinct roles without fighting for dominance.


**Headline scale:** h1 at 24px, h2 at 13px — restrained sizing — hierarchy through weight and spacing rather than scale.

---

## 4. Component Stylings

**Border radius:** No border-radius — sharp edges throughout.


**Shadows:** Shadows are absent — depth through color and spacing alone.

- Component data limited — apply global radius and color rules consistently.

---

## 5. Layout Principles





**Layout philosophy:** Content-first layout — sections breathe independently; no fixed grid forces awkward compositions.

Spacing cadence: Fluid spacing tokens via `clamp()` — scales smoothly between breakpoints without abrupt jumps.

---

## 6. Depth & Elevation

**Flat design** — no box shadows. Depth communicates through:
- Background color contrast between sections
- Border lines as separators
- Typography weight shifts
- Proximity and whitespace

This is an intentional choice: shadows would add visual noise to a carefully restrained palette.

---

## 7. Do's and Don'ts

**Do:**
- Respect the established spacing rhythm — every element should feel intentional
- Use only the defined typefaces (Merriweather, Lucida Grande) — system fonts will break the brand voice
- Keep all edges sharp — border-radius destroys the visual discipline
- Keep elevation flat — adding shadows would contradict the design language

**Don't:**
- Apply dark mode as an afterthought — it requires its own color decisions
- Use accent colors for decoration — they are reserved for interactive signals only
- Mix more than two typeface families — typographic chaos undermines brand clarity
- Add gradient backgrounds unless they exist in the design system
- Use stock UI component defaults (e.g., Bootstrap/MUI) without full restyling

---

## 8. Responsive Behavior

**Headline scale:**
- Desktop: 24px
- Suggest mobile: 13px–16px

**Body text:** 12.8px — standard; consider 15px on mobile for comfort



**Layout breakpoints:** Standard: stack multi-column sections to single column; reduce headline size; maintain horizontal padding of at least 16px.

**Navigation:** Apply standard mobile nav pattern: fixed header, collapsible menu.

---

## 9. Agent Prompt Guide

When asked to create UI in the style of **zmh.org**, instruct the agent:

```
Design in the style of zmh.org: institutional, clean, WordPress-conventional, bold accent.
Use clean backgrounds with high contrast text.
Primary typeface: Merriweather, body: Lucida Grande.
Sharp corners on all elements — no border-radius.
No shadows — flat design.
Accent color: #7a00df — use only for interactive elements.
Generous whitespace. Typography drives hierarchy.
Avoid: generic card components, gradient backgrounds, icon-heavy layouts, rounded pill buttons.
```

**Key design signals to reference:**
- Custom font: Merriweather — load via CDN if reproducing
- Shadow-free — use border or background contrast for separation
- Zero border-radius — rectangular everything
- Color temperature: Neutral with controlled accent

---

*Generated by Sparkbites — extracted from live CSS analysis*
