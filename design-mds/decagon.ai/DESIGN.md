# DESIGN.md — decagon.ai

## 1. Visual Theme & Atmosphere

Decagon presents an AI enterprise product through a palette that is simultaneously neutral and quietly expressive. The base is a cool off-white (`#f4f4f5`), avoiding both clinical pure-white and dark-mode conventions. A violet-purple accent (`#6b5cff`) carries brand identity through CTAs and borders. What distinguishes Decagon visually is a case study palette inset into the otherwise neutral page — displaying client brand colors (navy, lime green, violet, amber, deep plum) as named swatches. The site uses GSAP for smooth scroll-driven transitions, giving it a sense of controlled kinetic energy beneath the calm surface. FK Grotesk Neue, the chosen typeface, is corporate-modern without being generic — slightly geometric, slightly editorial.

---

## 2. Color Palette & Roles

### Foundation
- **Off-White** (`rgb(244, 244, 245)` = `#f4f4f5`): The universal page background. Slightly cool, clearly intentional — not white, not gray.
- **Near-Black** (`rgb(17, 17, 17)` = `#111111`): Footer surface. Maximum contrast anchor.
- **Dark Text** (`rgb(19, 19, 19)` = `#131313`): Primary text color across all headings and body.

### Brand Accent
- **Violet** (`rgb(111, 92, 255)` = `#6b5cff`): Primary brand accent. Used on link borders, CTAs, and interactive highlights. Sits between indigo and purple — distinctly tech-forward without being a standard blue.

### Interactive / UI
- **Pure White** (`rgb(255, 255, 255)`): Card surfaces, nav backgrounds, announcement bars.
- **Muted Gray** (`rgb(107, 107, 118)` = `#6b6b76`): Input placeholder and secondary text.
- **Progress Gray** (`rgb(224, 225, 224)`): Tab progress bar track background.
- **Tab Active** (`rgb(232, 232, 232)`): Inactive tab indicator fill.

### Case Study Brand Colors (decorative swatches)
- **Navy** (`rgb(47, 74, 115)`): Client case study swatch
- **Lime Green** (`rgb(88, 204, 2)`): Client case study swatch
- **Amber** (`rgb(255, 173, 21)`): Client case study swatch
- **Dark Plum** (`rgb(79, 45, 61)`): Client case study swatch

These are client brand colors displayed in a case study grid — they are not Decagon's own palette and should not be used outside that context.

---

## 3. Typography Rules

**FK Grotesk Neue**: The sole typeface. A contemporary geometric grotesque, licensed from Fontwerk. All text — display, body, labels, nav — is set in this single family.

Scale:
- **Hero**: 68.8px / 68.8px (1:1 line-height), weight 500 — tight leading creates dense, impactful headlines
- **Section head**: 40px / 44px, weight 400 — open, readable subheadings
- **Labels/Nav**: 14–16px, weight 500 — consistent medium-weight for UI copy
- **Body**: 15–16px, weight 400, line-height ~24px
- **Small UI**: 13–14px, weight 400–500

The 68.8px / 68.8px hero setting (equal font size and line-height) is a specific stylistic choice — no extra leading, headlines sit tightly stacked. Custom properties `--_typography---font-family--body` confirm the typeface is systematically applied.

No serif, no monospace, no system fonts. Single-family discipline throughout.

---

## 4. Component Styling

- **Primary Button**: Dark background with white text. Border radius from 80px (pill) to 800px — all buttons are pill-shaped.
- **Announcement Banner**: Transparent background, white text. Hover: text fades to 52% opacity white — a subtle dimming rather than a color change.
- **Links**: Violet border (`#6b5cff`) on anchor elements. CTAs lean on the violet identity.
- **Cards**: White surface (`#fff`) on the off-white page — one step of contrast. Single shadow: `rgba(0,0,0,0.1) 0px 4px 8px 0px`.
- **Input fields**: Transparent background, gray placeholder text, no visible border on default state.
- **Tab / Progress**: Progress bar track in light gray, fills dynamically — indicates a timed or scroll-driven section transition.
- **Border Radius**: 80px and 800px for pill shapes, 20px for standard cards, 8px for small components, 100% for circular avatars.

---

## 5. Layout Principles

Webflow powers the layout with GSAP scroll animations. The extensive breakpoint list (26 values, from 371px to 1920px) reflects Webflow's fine-grained responsive system — essentially continuous responsive control rather than a few snap points. The case study grid, progress-tab section, and announcement bar suggest a classic marketing site structure: hero → social proof → product features → case studies → CTA. Max content width likely around 1200–1440px with generous left/right padding.

---

## 6. Depth & Elevation

One shadow in the system: `rgba(0,0,0,0.1) 0px 4px 8px 0px` on card elements. This is the only depth signal. Everything else is flat. The off-white background provides a ground that makes white cards feel naturally elevated without additional shadow. GSAP handles perceived depth through scroll-parallax and entrance animations.

---

## 7. Do's and Don'ts

**Do:**
- Use FK Grotesk Neue exclusively. The brand is built on single-typeface discipline.
- Keep the hero at tight line-height (1:1 ratio at large sizes).
- Apply violet (`#6b5cff`) to CTAs and interactive link borders only — one accent, used consistently.
- Render all buttons as pill shapes (radius 80–800px). No square or mildly-rounded buttons.
- Use case study swatches only in the case study grid context — never as brand colors.

**Don't:**
- Use the case study brand colors (navy, lime, amber, plum) outside their swatch context.
- Add heavy shadow systems. One subtle card shadow is the ceiling.
- Introduce a second typeface — the single-family discipline is the identity.
- Use pure black as a background. The footer is `#111`, never `#000`.
- Set hero headlines above weight 500 — the design relies on medium weight at large sizes.

---

## 8. Responsive Behavior

Webflow's 26 breakpoints enable highly granular control from 371px (small phones) to 1920px (wide screen). The hero 68.8px headline will scale down significantly at mobile — expect 32–40px at 375px. Pill buttons remain pill-shaped at all sizes. The announcement bar collapses or hides on small screens. Tab/progress sections likely convert to vertical accordion on mobile. Off-white background persists across all breakpoints.

---

## 9. Agent Prompt Guide

> Build an AI enterprise landing page matching decagon.ai: off-white background (`#f4f4f5`), near-black text (`#131313`), near-black footer (`#111111`). FK Grotesk Neue weight 500 for hero at 68.8px with 1:1 line-height, weight 400 for body. Violet accent (`#6b5cff`) on CTAs and link borders. All buttons pill-shaped (radius 80px+). White cards with single shadow: `rgba(0,0,0,0.1) 0px 4px 8px 0px`. One typeface, flat surfaces, GSAP scroll animations.

---

*Generated by Sparkbites — extracted from live CSS analysis*
