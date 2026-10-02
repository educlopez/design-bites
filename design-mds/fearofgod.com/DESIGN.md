# Fear of God — Design System Reference

## 1. Visual Theme & Atmosphere

The Fear of God official store (Shopify, Spain storefront) is a luxury-fashion catalogue disguised as a web shop: a white canvas, black type, and almost no ornament, so the product photography and the brand name do all the work. The typographic signature is a pairing of Optima, a humanist flared sans associated with quiet luxury, for the headline and paragraph voice, and HelveticaNeueLTPro Condensed for navigation, labels and body, set in uppercase with generous tracking. The result feels like a printed lookbook: restrained, wide-spaced, and deliberately minimal. Collections such as "Essentials Fall 2026" are featured as full links rather than decorated banners.

---

## 2. Color Palette & Roles

**Foundation**
- `rgb(255, 255, 255)` — page canvas
- `rgb(0, 0, 0)` — text, borders, header
- `rgb(105, 105, 105)` — h3 secondary gray

**Neutral surfaces**
- `rgb(248, 248, 248)` — grouped content panels
- `rgb(244, 244, 244)` — footer-logo strip
- `rgba(0, 0, 0, 0.5)` — modal dark filter

**Consent/UI utility (OneTrust cookie panel, not brand)**
- `rgb(39, 69, 92)`, `rgb(70, 130, 84)`, `rgb(56, 96, 190)` — slate, green and blue seen only in the cookie banner controls
- `rgb(249, 255, 250)` — opt-out signal tint

The brand itself is strictly black and white. Color only appears in third-party consent chrome.

---

## 3. Typography Rules

| Role   | Font                         | Size | Weight | Line-height | Tracking | Transform |
|--------|------------------------------|------|--------|-------------|----------|-----------|
| H1     | Optima                       | 32px | 400    | 32px        | normal   | none      |
| H2     | HelveticaNeueLTPro-Cn        | 11px | 400    | 16.5px      | 1.1px    | uppercase |
| H3     | HelveticaNeueLTPro-Cn        | 16px | 700    | 20.8px      | normal   | none      |
| H4     | HelveticaNeueLTPro-Cn        | 14px | 700    | 21px        | normal   | none      |
| Body   | HelveticaNeueLTPro-Cn        | 14px | 400    | 22.4px      | 0.7px    | none      |
| P      | Optima                       | 14px | 400    | 16.8px      | normal   | none      |
| Link   | HelveticaNeueLTPro-Cn        | 14px | 400    | 22.4px      | 0.7px    | uppercase |
| Button | HelveticaNeueLTPro-Cn        | 14px | 400    | 14px        | 1.8px    | uppercase |
| Input  | Optima                       | 16px | 400    | 19.2px      | normal   | uppercase |

**Principles**
- Two voices: Optima for the editorial headline and paragraph text, condensed Helvetica for everything functional.
- Links, buttons and H2 labels are uppercase and tracked out (0.7px to 1.8px); wide spacing on a condensed face gives the luxury feel.
- Bold (700) is reserved for H3/H4; everything else is 400.
- Fallbacks are Gill Sans and Helvetica/Arial.

---

## 4. Component Stylings

**Links and navigation**
- Uppercase condensed 14px, 0.7px tracking, black on white
- Skip-to-content link gains a white fill and a 2.8px white ring on focus

**Buttons**
- Uppercase 14px, 1.8px tracking, transparent background by default

**Inputs**
- Optima 16px, uppercase

**Border radius**
- `2px`, `17px`, `50px`, `50%` — near-square for most UI, round for icon buttons and toggles.

**Shadows**
- `rgba(0, 0, 0, 0.15) 0px 4px 20px 0px` — soft lifted shadow for floating panels
- 1px inset black ring used as an outline treatment

**Hover tokens (theme variables)**
- `--hover-lift-amount: 4px`, `--hover-scale-amount: 1.03`, `--hover-subtle-zoom-amount: 1.015`, with `0.25s ease-out` timing.

---

## 5. Layout Principles

- Page widths: narrow `90rem`, normal `120rem`, wide `150rem`; content widths 36 / 42 / 46rem.
- Sidebar width `25rem`; section heights small `15rem`, medium `25rem`, large `35rem`, so imagery is given tall, cinematic blocks.
- Left-aligned text by default.
- Body, main, header and footer have zero padding; spacing is set inside sections and image blocks.
- A very dense set of breakpoints (320 up to 1600) reflects the Shopify theme's heavy responsive tuning.

---

## 6. Depth & Elevation

Mostly flat. The surface ladder is white `rgb(255, 255, 255)` to `rgb(248, 248, 248)` to `rgb(244, 244, 244)`. Elevation is added only with the single soft shadow (`0 4px 20px` at 15% black) and the 50% black modal backdrop. Interaction depth comes from the hover lift (4px) and zoom (1.015 to 1.03) tokens with `0.25s` ease-out; submenus open over `0.36s` with `cubic-bezier(.25, .1, .25, 1)`, and surfaces transition over `0.3s`.

---

## 7. Do's and Don'ts

**Do**
- Keep the page white and the type black.
- Pair Optima (headlines, paragraphs) with a condensed Helvetica (UI).
- Track out uppercase labels (0.7px to 1.8px).
- Let photography occupy tall section blocks.
- Use subtle hover lift and zoom with ease-out timing.

**Don't**
- Don't add brand colors; color belongs to product imagery.
- Don't use heavy shadows or large radii on content.
- Don't bold body copy; reserve 700 for small sub-headings.
- Don't set long text in uppercase.

---

## 8. Responsive Behavior

Over 30 breakpoints from 320px to 1600px, with key steps near 480, 600, 768, 900, 1024, 1200 and 1440. Content widths are capped by named page-width tokens (90 / 120 / 150rem), so very wide screens keep a controlled measure while the sidebar stays at `25rem`. Type sizes stay compact (11 to 16px).

---

## 9. Agent Prompt Guide

> Build a UI that matches Fear of God's design language.

Use a white canvas and black text, with gray `rgb(105, 105, 105)` only for secondary headings. Set the main headline and paragraphs in **Optima** (32px headline, 14px paragraph, weight 400) and all navigation, labels, buttons and body in **HelveticaNeueLTPro-Cn**: 14px with 0.7px tracking, uppercase links, uppercase buttons with 1.8px tracking, 11px uppercase labels with 1.1px tracking. Use bold 700 only on 14-16px sub-headings. Keep radii at `2px` for UI and `50%` for round controls. Use a single soft shadow (`0 4px 20px rgba(0, 0, 0, 0.15)`) for floating panels, a 4px hover lift with `0.25s ease-out`, and tall full-bleed imagery blocks (15 / 25 / 35rem). No brand colors; let the product carry the color.

---

*Generated by Sparkbites — extracted from live CSS analysis*
