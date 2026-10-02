# Appllama Loader Buttons — Design System Reference

## 1. Visual Theme & Atmosphere

"25 Unique Loading Button Animations" by Appllama is a single-purpose showcase, and the page is designed to disappear behind its subject. A flat light-gray canvas (`#f0f0f0`) and near-black ink (`#191919`) hold a grid of glassy loading buttons, each labeled with a verb such as "Gathering" or "Focusing." The buttons are the only dimensional objects on the page: translucent white pills with layered inset highlights and soft long shadows, like frosted glass pebbles. Around them, the page is quiet and editorial, with a large Georgia headline set tight and small system-ui labels. A "Pause motion" control and a closing "More experiments are coming" block with maker profile cards complete the tone: craft-first, personal, and calm.

---

## 2. Color Palette & Roles

Declared as CSS variables:
- `--page: #f0f0f0` — canvas
- `--ink: #191919` — text and borders
- `--muted: rgba(25, 25, 25, 0.52)` — secondary text, footer, idle controls
- `--hairline: rgba(25, 25, 25, 0.12)` — dividers and card edges

**Button glass**
- `rgba(255, 255, 255, 0.55)` — button fill
- `rgba(255, 255, 255, 0.9)` — button border
- `rgba(255, 255, 255, 0.46)` — profile-card hover fill

There are no accent hues. The only color on the page is neutral gray, white and ink; the browser-default link blue (`rgb(0, 0, 238)`) shows up in the extraction on the brand link but is an unstyled fallback, not part of the palette.

---

## 3. Typography Rules

| Role   | Font                  | Size    | Weight | Line-height | Tracking  | Transform |
|--------|-----------------------|---------|--------|-------------|-----------|-----------|
| H1     | Georgia, Times serif  | 59.2px  | 400    | 54.464px    | -3.4336px | none      |
| H2     | system-ui             | 12px    | 500    | normal      | 1.32px    | uppercase |
| H3     | system-ui             | 12px    | 500    | normal      | -0.12px   | none      |
| Body   | system-ui             | 16px    | 400    | normal      | normal    | none      |
| P      | system-ui             | 12px    | 500    | normal      | 1.32px    | uppercase |
| Button | system-ui             | 12px    | 400    | normal      | normal    | none      |

**Principles**
- The H1 is set with line-height below its font-size (54px on 59px) and heavy negative tracking (-3.43px, about -5.8%): tight, magazine-like.
- Everything else is small system-ui at 12px, with uppercase 1.32px-tracked eyebrows for section labels.
- The serif/system pairing needs no webfont, which keeps the page fast.

---

## 4. Component Stylings

**Loader buttons** (the hero component)
- Fill `rgba(255, 255, 255, 0.55)`, border `rgba(255, 255, 255, 0.9)`, text `rgb(25, 25, 25)`, 12px system-ui
- Full pill radius (`9999px`)
- Shadow stack: inset white highlight (`0 1px 4px`), inset lower white glow (`0 -4px 4px`), inset gray ambient (`0 0 14px`), then two outer drops (`0 11px 28px` at 7% black and `0 23px 31px` at 5% black)
- Hover on some buttons scales to 0.975; focus shows a 2px outline at 58% ink

**Motion control ("Play motion" / "Pause motion")**
- Transparent, muted `rgba(25, 25, 25, 0.52)` text; hover darkens to full ink `rgb(25, 25, 25)`; focus a 2px 24% ink outline

**Profile cards**
- Transparent with ink text; hover adds `rgba(255, 255, 255, 0.46)` fill and a `0 1px 0` inset white highlight

**Border radius**
- `9999px` pills, `20px` cards, `50%` avatars and loaders.

---

## 5. Layout Principles

- Side margins of `24px` on header, sections and footer.
- Header padding `84px 0 88px`; sections end with `96px` bottom padding: generous vertical rhythm so each animation has breathing room.
- Breakpoints at **410, 690, 1050**.
- Animated examples are laid out as a grid of equal cells, each with a small 12px label.

---

## 6. Depth & Elevation

Depth is concentrated entirely in the buttons. The inset highlight plus inset glow makes each pill look like a convex, back-lit glass surface, while two long, low-opacity outer shadows (28px and 31px blurs) lift it off the gray canvas. The rest of the page stays flat, separated only by `rgba(25, 25, 25, 0.12)` hairlines.

---

## 7. Do's and Don'ts

**Do**
- Keep the canvas `#f0f0f0` and ink `#191919`; vary only opacity for hierarchy.
- Give the hero component the full five-layer glass shadow.
- Use ease-out-quart timing (`cubic-bezier(0.25, 1, 0.5, 1)`) for motion.
- Provide a visible pause/play control for animations.
- Label each demo with a short verb.

**Don't**
- Don't add accent colors; the animations are the interest.
- Don't put the glass shadow on non-interactive page chrome.
- Don't loosen the H1 tracking or raise its line-height.
- Don't leave links as default blue.

---

## 8. Responsive Behavior

Breakpoints at **410, 690 and 1050px**. The 24px side margins hold at every width, and the system-ui type scale (12 to 16px) is constant. Only the H1 and the grid of examples need to flex between phone, tablet and desktop columns.

---

## 9. Agent Prompt Guide

> Build a UI that matches Appllama Loader Buttons' design language.

Use a `#f0f0f0` canvas with `#191919` ink; set secondary text to `rgba(25, 25, 25, 0.52)` and dividers to `rgba(25, 25, 25, 0.12)`. Headline in Georgia at about 59px, weight 400, line-height 54px, letter-spacing -3.43px. All other text in system-ui 12px (uppercase eyebrows at weight 500 and 1.32px tracking, 16px body). Build buttons as 9999px pills with `rgba(255, 255, 255, 0.55)` fill, `rgba(255, 255, 255, 0.9)` border, and the glass shadow: `inset 0 1px 4px rgba(255,255,255,.667), inset 0 -4px 4px rgba(255,255,255,.85), inset 0 0 14px rgba(229,229,229,.55), 0 11px 28px rgba(0,0,0,.07), 0 23px 31px rgba(0,0,0,.05)`. Scale to 0.975 on press or hover, use `cubic-bezier(0.25, 1, 0.5, 1)`, and always include a Pause motion control. 24px side margins, 84px header and 96px section spacing.

---

*Generated by Sparkbites — extracted from live CSS analysis*
