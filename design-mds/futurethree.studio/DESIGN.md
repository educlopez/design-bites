# Future Three — Design System Reference

## 1. Visual Theme & Atmosphere

Future Three presents itself as "A Creative Studio" that crafts "brands & digital experiences that seamlessly blend functionality with aesthetics," and the interface behaves like an editorial broadsheet that has been set in motion. A soft grey canvas (`rgb(241, 241, 241)`) alternates with full-bleed black sections (`rgb(0, 0, 0)`), so scrolling feels like turning between a printed page and a darkened screening room. Type does the heavy lifting: a Neue Haas Grotesk pair carries the interface, an Arizona-style serif appears at display size with extreme negative tracking, and a tiny uppercase mono handles labels. A single saturated red (`#f12a2d`) is declared as a token and held in reserve. The site is built on Webflow with GSAP, and a pair of custom easing curves (`cubic-bezier(.625,.05,0,1)` and `cubic-bezier(.32,.12,.2,1)`) suggests motion is a first-class part of the brand. Tone is confident, tightly typeset, and editorial rather than decorative.

---

## 2. Color Palette & Roles

**Foundation**
- `rgb(241, 241, 241)` / `#f1f1f1` — page canvas and contact panel (`--off-white`)
- `rgb(36, 32, 33)` / `#242021` — warm ink for links, button fills and input text (`--off-black`)
- `rgb(51, 51, 51)` — default body and main text colour
- `rgb(0, 0, 0)` — full-bleed section backgrounds and nav text (`--black`)
- `white` — `--white` token, and the thin `div.line` dividers at `rgb(255, 255, 255)`

**Accent**
- `#f12a2d` — signal red (`--red`), declared as a token and kept for emphasis only

**Form surfaces**
- `rgb(227, 227, 227)` — input background
- `rgb(204, 204, 204)` — input border
- `rgb(36, 32, 33)` — input text

**Inverted treatment**
- Buttons invert the page: `rgb(36, 32, 33)` background with `rgb(241, 241, 241)` text and border.
- The h1 is set in `rgb(241, 241, 241)`, which means it lives on the black sections, not on the grey canvas.

The system is bi-tonal at the frame level (grey and black), with warm off-black ink softening the harshness of pure black on light surfaces.

---

## 3. Typography Rules

Three families form a clear division of labour: a grotesk for the interface, a serif for dramatic display moments, and a mono for micro-labels.

**Typefaces**
- **Neue Haas Display** (as declared: `"Neuehaasdisplay Mediu"`, weight 500, and `"Neuehaasdisplay Roman"`, weight 400) — headings, links, paragraphs, form controls; Arial fallback
- **ABC Arizona Serif** (`Abcarizonaserif`, weight 300) — the single serif voice, used on h2
- **PP Supply Mono** (`Ppsupplymono-new`) — labels only

**Scale**

| Role   | Font                  | Size     | Weight | Line-height | Tracking    | Transform |
|--------|-----------------------|----------|--------|-------------|-------------|-----------|
| H1     | Neue Haas Medium      | 53.72px  | 500    | 50.49px     | -1.61px     | none      |
| H2     | ABC Arizona Serif     | 65.23px  | 300    | 52.18px     | -5.22px     | none      |
| H3     | Neue Haas Medium      | 21.10px  | 500    | 17.30px     | normal      | uppercase |
| H4     | Neue Haas Medium      | 15.35px  | 500    | 16.88px     | normal      | none      |
| Body   | Neue Haas Roman       | 15.35px  | 400    | 20px        | normal      | none      |
| P      | Neue Haas Medium      | 15.35px  | 500    | 16.88px     | -0.46px     | none      |
| Link   | Neue Haas Medium      | 34.53px  | 500    | 32.46px     | -1.04px     | none      |
| Button | Neue Haas Roman       | 15.35px  | 400    | 20px        | normal      | none      |
| Input  | Neue Haas Roman       | 15.35px  | 400    | 16.88px     | -0.46px     | none      |
| Label  | PP Supply Mono        | 9.59px   | 400    | 9.59px      | +0.48px     | uppercase |

**Principles**
- Line-height is set below the font size on most display roles (h1 53.7px on 50.5px, h2 65.2px on 52.2px), producing the tight, stacked headline look.
- The serif h2 carries tracking of -5.22px, about 8% of its size, an aggressive squeeze that turns a light serif into a graphic shape.
- Links are large (34.5px) and medium weight, so navigation reads as typography rather than UI.
- Labels drop to 9.6px mono, uppercase, with positive tracking, the only place tracking opens up.
- Sizes are fluid: `--size-font` is computed from `--size-container` (clamped between `992px` and `2560px` against a `1440` ideal and a `16` unit), so type scales with the viewport instead of jumping at breakpoints.

---

## 4. Component Stylings

**Buttons**
- Background `rgb(36, 32, 33)`, text and border `rgb(241, 241, 241)`
- 15.35px Neue Haas Roman, weight 400, line-height 20px

**Links**
- Transparent background, ink `rgb(36, 32, 33)` text
- 34.53px medium weight with -1.04px tracking, which makes primary navigation (Studio, Work, Contact) a typographic gesture

**Inputs and textarea**
- Background `rgb(227, 227, 227)`, border `rgb(204, 204, 204)`, text `rgb(36, 32, 33)`
- 15.35px Neue Haas Roman with -0.46px tracking
- Contact form fields are Your Name, Company Name, Email Address and Your Message, with a Submit action and inline success and error messages

**Labels**
- PP Supply Mono, 9.59px, uppercase, +0.48px tracking

**Border radius**
- `3.83693px` — a hairline softening, the only radius extracted

**Shadows**
- None detected.

**Interactive states**
- No hover or focus states were captured; interaction is expressed through GSAP-driven motion and the two easing curves.

---

## 5. Layout Principles

- `body` and `main` reset padding and margin to `0px`, so sections run edge to edge and spacing is owned by the sections themselves.
- The layout is container-driven: width is `clamp(992px, 100vw, 2560px)` against a 1440 reference, and a root `16` unit scales proportionally.
- Sections alternate between grey (`rgb(241, 241, 241)`) and black (`rgb(0, 0, 0)`) bands.
- Thin `div.line` rules, in white and in `rgb(36, 32, 33)`, divide content within sections.
- Content structure on the live site is numbered and editorial: a featured work block, an About block, a footer with address, phone, email, a local-time clock and language toggle.
- Breakpoints at **479 / 767 / 768 / 991**, the standard Webflow set.

---

## 6. Depth & Elevation

Depth is flat. No `box-shadow` was extracted. The layering cues are:
- **Surface swap** — `rgb(241, 241, 241)` panels (the `contact-inner` block, luminance 0.945) against `rgb(0, 0, 0)` sections (luminance 0).
- **Ink vs paper** — `rgb(36, 32, 33)` (luminance 0.131) separates dark controls and dividers from pure black.
- **Motion** — GSAP and the custom easings supply the sense of layering during transitions, not static elevation.

---

## 7. Do's and Don'ts

**Do**
- Alternate `rgb(241, 241, 241)` and `rgb(0, 0, 0)` sections for rhythm.
- Pair a medium-weight grotesk with one light serif at display size, and squeeze the serif hard (-5.22px at 65px).
- Keep display line-heights below the font size for stacked headlines.
- Use PP Supply Mono at under 10px, uppercase, for labels.
- Use `rgb(36, 32, 33)` rather than pure black for ink on light surfaces.
- Reserve `#f12a2d` for rare emphasis.
- Use `cubic-bezier(.625,.05,0,1)` for primary motion and `cubic-bezier(.32,.12,.2,1)` for softer movement.

**Don't**
- Don't add drop shadows; the system has none.
- Don't use the serif for body or UI text; it appears only at display size.
- Don't use bold weights; headings top out at 500.
- Don't round corners beyond roughly `4px`.
- Don't spread the red across UI chrome.

---

## 8. Responsive Behavior

Four breakpoints at **479, 767, 768 and 991** follow Webflow's defaults. Typography is the real responsive mechanism: font sizes derive from a container variable clamped between `992px` and `2560px`, so type grows and shrinks proportionally with the viewport rather than at fixed steps. Below the 992px container floor the layout falls to the Webflow breakpoints. The footer content (address, phone, email, language switch, local time) stacks as an information block on the live site.

---

## 9. Agent Prompt Guide

> Build a UI that matches Future Three's design language.

Use a light grey canvas `rgb(241, 241, 241)` alternating with full-bleed black `rgb(0, 0, 0)` sections, and warm ink `rgb(36, 32, 33)` for links and buttons on light surfaces. Set interface type in **Neue Haas Display** (medium 500 for headings, links and paragraphs, roman 400 for body, buttons and inputs) at around 15.35px body size. Make h1 about 53.7px with -1.6px tracking and line-height slightly below the size. Set h2 in **ABC Arizona Serif** weight 300 at about 65px with -5.2px tracking. Make navigation links large, around 34.5px medium with -1px tracking. Labels use **PP Supply Mono** at 9.6px, uppercase, +0.48px tracking. Buttons are `rgb(36, 32, 33)` with `rgb(241, 241, 241)` text and border. Inputs sit on `rgb(227, 227, 227)` with an `rgb(204, 204, 204)` border. Use a `3.8px` radius and no shadows. Keep `#f12a2d` as a rare accent. Drive motion with `cubic-bezier(.625,.05,0,1)` and scale type fluidly from a clamped container width. Let the typography and the grey-black rhythm carry the identity.

---

*Generated by Sparkbites — extracted from live CSS analysis*
