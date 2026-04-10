# itiskul.com — Design Language

## 1. Visual Theme & Atmosphere

ITISKUL is a Wix-powered brand with a pop-art energy that refuses neutrality. Three vivid accent colors — periwinkle purple, electric lime, and bubblegum pink — sit against a white ground, creating the kind of chromatic confidence more often seen in fashion editorials than design portfolios. The uppercase Neue Power Ultra typeface brings industrial weight; the bright palette brings irreverence. The combination reads as a brand that knows exactly what it is: loud, joyful, and intentional. This is not an "also dark mode" website — it is maximalist daylight.

## 2. Color Palette & Roles

| Role | Value | Usage |
|---|---|---|
| Background | `rgb(255, 255, 255)` — white | Page canvas, buttons |
| Primary text | `rgb(28, 28, 28)` — near-black | h1, body copy |
| Accent Purple | `rgb(163, 172, 255)` — periwinkle | Section backgrounds, tags |
| Accent Lime | `rgb(225, 255, 0)` — electric yellow-green | Section backgrounds, CTAs |
| Accent Pink | `rgb(255, 176, 227)` — bubblegum | Section backgrounds, highlights |
| Interactive blue | `rgb(17, 109, 255)` — vivid blue | Button text, links on white |
| h2 inverse | `rgb(255, 255, 255)` — white | Headings on colored surfaces |

The three accent colors function as section skin colors — each panel wears one hue. They never mix in the same surface. The white-and-near-black base is the neutral container; accents are the personality.

**What's absent:** No dark mode, no grays, no gradients, no drop-shadows (except a 0px stub), no border-radius.

## 3. Typography Rules

**Neue Power Trial Ultra** is the dominant display font, delivered via Wix's webfont pipeline. It is always uppercase, heavy, and wide — built for impact.

| Element | Family | Size | Weight | Transform |
|---|---|---|---|---|
| h1 | Neue Power Trial Ultra | ~49.8px | 400 (Ultra cut) | `uppercase` |
| h2 | Neue Power Trial Ultra | 24px | 400 (Ultra cut) | uppercase implied |
| Body / p | Wix system sans | ~14px | 400 | none |

The `textTransform: uppercase` on h1 is baked into the type rule — all display text shouts. The relatively small h2 at 24px keeps section labels readable without competing with hero text. Body text is set in Wix's default sans, suggesting the brand energy lives in headings rather than long-form copy.

Wix custom properties (`--wst-font-style-h6`, `--wst-font-style-body-large`) indicate a token system underlying the presentation.

**What's absent:** No serif, no italic, no tracking adjustments, no mixed weight families.

## 4. Component Styling

- **Buttons:** White background with `rgb(17, 109, 255)` text and matching border — an outlined style on white surfaces.
- **Section panels:** The three accent hues (`rgb(163,172,255)`, `rgb(225,255,0)`, `rgb(255,176,227)`) apply as full-background colored sections.
- **Shadow stub:** A `0px 0px 0px 0px` shadow declaration exists — no actual elevation rendered, but the intent for depth is architectured in.
- **Borders:** 1px solid near-black (`rgb(28,28,28)`) on lime and pink surfaces; absent on purple (transparent border noted).
- **No rounded corners** — all edges are squared.

## 5. Layout Principles

- Three breakpoints: 320px (mobile base), 750px (tablet), 1000px (desktop).
- Sections use zero padding/margin defaults — spacing is set at the content component level via Wix's block editor.
- The Wix architecture imposes a fixed-width block model; layout composition is visual rather than CSS-grid.
- Accent-colored sections likely alternate in sequence, creating a rhythm of purple → lime → pink (or similar) as the user scrolls.

## 6. Depth & Elevation

Flat by design. The shadow declaration is zeroed out — no elevation system is active. Depth comes from chromatic contrast: a lime section next to a white section reads as "popping" through hue contrast alone. The `rgb(0,0,0)` border on colored sections adds a graphic outline quality, reinforcing the flat illustration aesthetic.

## 7. Do's and Don'ts

**Do:**
- Apply accent colors as full-section backgrounds, never as partial fills or gradients.
- Keep Neue Power in uppercase at all display sizes — lowercase would break the brand voice.
- Use the vivid blue (`rgb(17,109,255)`) only for interactive elements (buttons, links) on neutral surfaces.
- Pair black borders with colored panels for the graphic, illustrated look.

**Don't:**
- Mix two accent colors in the same section or component.
- Add border-radius — rounded corners would soften a design that is deliberately hard-edged.
- Use the accent palette for body text — it lives in backgrounds, not prose.
- Introduce shadows or blur; the flatness is not an oversight.

## 8. Responsive Behavior

At 750px and below, the block layout likely collapses to single-column stacks. The 49.8px uppercase h1 scales down at mobile, but Neue Power Ultra's extreme weight means it holds visual impact even at reduced sizes. The three-color section rhythm likely persists across breakpoints. At 320px (defined explicitly), the design has a deliberate small-phone layout separate from the tablet view.

## 9. Agent Prompt Guide

> Build a brand site in the style of itiskul.com: white background, near-black text (`rgb(28,28,28)`). Full-section accent panels in periwinkle `rgb(163,172,255)`, lime `rgb(225,255,0)`, and bubblegum pink `rgb(255,176,227)` — one color per section, never mixed. Headlines in Neue Power Ultra (or similar ultra-heavy display font) at uppercase. No border-radius, no shadows. Buttons are outlined: white fill, `rgb(17,109,255)` text and border. Sections have black 1px borders on colored panels. Three breakpoints: 320, 750, 1000px.

---

*Generated by Sparkbites — extracted from live CSS analysis*
