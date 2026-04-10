# jasper.ai — Design System

## 1. Visual Theme & Atmosphere

Jasper.ai is one of the more typographically ambitious AI-product sites: it pairs a custom serif **Feature** (headings) with a custom grotesque **ABC ROM** (body), both at font-weight 450 — a non-standard value between Regular and Medium. Built on Webflow with GSAP animations, the design avoids the dark-mode arms race of its competitors entirely, opting for a white-primary palette with a deep navy `rgb(0, 6, 61)` as the brand ink and an assertive coral-orange `rgb(250, 64, 40)` as the action color. The atmosphere is authoritative and warm — editorial in the mode of a considered brand magazine, with a candy-bright supporting palette of pastels used as section accents.

## 2. Color Palette & Roles

**Foundation**
- `rgb(255, 255, 255)` — primary canvas
- `rgb(0, 6, 61)` — brand text and ink color; deep navy with a hint of indigo

**Action / Brand**
- `rgb(250, 64, 40)` — primary CTA; coral-orange; links; buttons
- `rgb(0, 17, 167)` — secondary action background; pure electric blue for dark sections
- `rgb(0, 11, 61)` — alt dark CTA button background

**Pastel section accents** (section background swatches)
- `rgb(230, 255, 217)` — mint green section
- `rgb(255, 232, 226)` — blush pink section
- `rgb(255, 247, 245)` — near-white warm wash
- `rgb(255, 251, 183)` — pale yellow (eyebrow labels)

**Navigation menu accents** (pill backgrounds)
- `rgb(206, 235, 255)` — light blue
- `rgb(255, 179, 163)` — light salmon
- `rgb(210, 255, 193)` — light mint
- `rgb(255, 179, 222)` — light pink
- `rgb(255, 246, 125)` — light yellow

**Button secondaries**
- `rgb(129, 203, 255)` — light blue secondary button
- `rgb(150, 255, 111)` — bright green secondary button

## 3. Typography Rules

Feature serif for all display and Feature-family heading roles; ABC ROM grotesque for all UI, body, and interactive text. Both at the non-standard weight 450 — softer than medium, firmer than regular.

| Role | Font | Size | Weight | Letter-spacing | Notes |
|---|---|---|---|---|---|
| H1 | Feature | 73.83px | 450 | -2.21px | lh 73.83px — 1:1 ratio |
| H3 / P (large) | Feature | 38px | 450 | -0.76px | lh 38px |
| H2 | Feature | 24px | 450 | normal | lh 26.4px |
| Body | ABC ROM | 16px | 450 | -0.16px | lh 22.4px |
| Links / buttons | ABC ROM | 16px | 450 | normal | — |
| Labels | ABC ROM | 16px | 500 | -0.32px | `<label>` elements |
| Inputs | ABC ROM | 16px | 450 | -0.32px | Form elements |

The 73.83px H1 with a 1:1 line-height echoes the tight editorial headlines of magazine culture. Feature's serif character at display scale conveys gravitas; ABC ROM keeps the UI readable and contemporary.

## 4. Component Stylings

**Primary CTA buttons** — Coral-orange `rgb(250, 64, 40)` fill with white text. Alt: deep navy `rgb(0, 6, 61)` fill with white text. Border radius: `0.5rem` (8px) for small, `1rem` (16px) for standard, `100vw` for pill/round variants.

**Secondary buttons** — Light blue `rgb(129, 203, 255)` or green `rgb(150, 255, 111)` — pastel-toned, high contrast on white.

**Navigation pills** — Pastel-colored menu category pills (each category gets its own pastel: blue for one product area, salmon for another, etc.).

**Section backgrounds** — Full-bleed pastel washes per section (`mint`, `blush`, `yellow`) create a color-coded content architecture.

**Eyebrow labels** — Yellow `rgb(255, 251, 183)` background pill with navy text introduces each section category.

No shadows on structural elements. Minimal decoration — the color architecture carries all the hierarchy.

## 5. Layout Principles

Rich responsive system: 11 breakpoints from `360px` to `1920px`. This is a fully fluid Webflow layout with named spacing tokens using `clamp()`: `--_spacing---section-space--main` scales from `4rem` at narrow to `7rem` at wide. Column margin system (`--column-margin--5`, `--column-margin--6`) suggests a named grid layer. Small radii `2px` and `4px` suggest a tight micro-spacing system for inline elements.

Custom properties use a Webflow variable naming convention (`--_theme---`, `--_typography---`, `--_spacing---`).

## 6. Depth & Elevation

Extremely flat. No shadows detected. Depth is created entirely through:
- **Color contrast**: navy text on white, coral on white
- **Section color bands**: pastel sections stack as visual layers
- **Typography scale**: Feature serif at 73px vs ABC ROM at 16px creates hierarchy through presence

The `border-radius: 100vw` pill shape on CTAs creates a visual softness that implies accessibility and approachability rather than depth.

## 7. Do's and Don'ts

**Do**
- Use Feature serif for all headings; the serif/grotesque split is the brand's typographic identity
- Apply font-weight 450 throughout — it's non-standard and must be explicitly declared
- Color-code navigation categories with distinct pastels
- Use pastel section backgrounds as a visual rhythm tool — each section earns its own hue

**Don't**
- Switch to a dark background — Jasper.ai is explicitly white-primary, unlike its AI contemporaries
- Round CTAs beyond `100vw` pill or `1rem` standard; the radius system has three specific stops
- Use the coral `rgb(250, 64, 40)` for anything other than primary actions and links
- Apply Feature serif to body text — it belongs only at heading scale

## 8. Responsive Behavior

11 breakpoints from `360px` to `1920px`. The clamp-based spacing system ensures smooth transitions. Feature serif headlines likely scale down with the typography clamp system. Pastel section backgrounds remain full-bleed at all widths. The navigation pill system likely collapses to a hamburger below 768px. The 1920px upper breakpoint means the layout has a maximum-width container that doesn't expand beyond large monitor sizes.

## 9. Agent Prompt Guide

> Build a white-primary AI marketing site in the style of jasper.ai. Deep navy `rgb(0, 6, 61)` as brand text color. Feature serif at 73px/450 weight with 1:1 line-height for hero; ABC ROM at 16px/450 for body. Coral CTA buttons `rgb(250, 64, 40)` with `border-radius: 1rem`. Section backgrounds in pastels: mint `rgb(230, 255, 217)`, blush `rgb(255, 232, 226)`, yellow wash `rgb(255, 251, 183)`. Navigation uses colored pill menus, each category with its own pastel. No shadows. Webflow-style clamp spacing tokens. 11 breakpoints from 360px to 1920px.

---

*Generated by Sparkbites — extracted from live CSS analysis*
