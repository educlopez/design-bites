# Kimera Corp — Design System Reference

## 1. Visual Theme & Atmosphere

Kimera Corp is a type foundry and branding studio, and its homepage is built like a shop window for its own typefaces — a dense masonry grid of typeface releases (Melange Grotesk, Waldenburg, Apparat), identity work (Souvenir, Transmoderna, Wastecare), and physical products (keychains, posters, a printed "Release Notes" publication), all sitting behind a functioning shopping cart. The signature move is that the site sets its own UI type — **Waldenburg** — as the body face across the entire interface, so browsing the catalogue is itself a live demo of the product. The palette stays almost entirely black-on-white, letting a tightly rationed set of accents (an electric blue, two greens, a brick red) do all the color work, usually as small UI flags rather than backgrounds. Typography runs unusually small and dense — 12px body copy, 9.6px paragraphs, a 6.6px uppercase button label — which reads less like an oversight and more like a foundry flexing that its type holds up at small, functional sizes with full OpenType feature sets (`calt`, `kern`, `liga`, `rclt`, `rlig`, `rvrn`) switched on. The overall tone is clinical, confident, and product-first: a studio selling craft through restraint.

---

## 2. Color Palette & Roles

**Foundation**
- `#fff` (`--white`) — page canvas, footer surface
- `#000` (`--black`) — body text, primary button background, cart container background
- `#eaeaea` (`--kimera-white`) — off-white UI surface (grid item cards, inverted button text/border)
- `#d6d6d6` (`--kimera-grey`) — secondary surface (`.kimera-button` fill)
- `#bcbcbc` (`--kimera-medium-grey`) — mid-tone UI grey
- `#4b4b4b` (`--kimera-dark-grey`) — dark UI grey, likely muted text/secondary labels

**Accents (functional, not decorative)**
- `#15abff` (`--kimera-blue`) — the one saturated brand accent; used on the cart-items counter badge
- `#48ec6c` (`--kimera-green`) / `#31c852` (`--kimera-green-dark`) — success/positive state pair
- `#c84531` (`--kimera-red`) — warning/error or destructive state

**Utility**
- `hsla(0,0%,59%,.4)` (`--kimera-filter-color`) — a translucent grey overlay, used for filter/dim treatments (likely category filters or disabled states)

**Roles observed**
- `body` — transparent background, black text and border (the page itself carries no explicit fill; white comes from the canvas beneath)
- `footer` — white background, black text
- `button` — black background, `#eaeaea` text and border (an inverted "stamp" treatment, similar in spirit to a dark pill on a light page)
- `span.cart-items-counter` — kimera-blue background, black text (the single spot of saturated color in the default chrome)

Surface luminance confirms a tight four-step ramp: pure white page-overlay (1.0) → `#eaeaea` grid-item-inner (0.918) → `#d6d6d6` kimera-button (0.839) → pure black shopping-cart container (0). Depth is built entirely from that grey ramp, not from color.

---

## 3. Typography Rules

One typeface family runs the entire interface: **Waldenburg**, falling back to `Arial, sans-serif`. Waldenburg is also one of the foundry's own commercial releases (sold on this same page as `/typefaces/waldenburg`) — the studio uses its own product as its UI font, which is the whole point of the site.

| Selector | Font | Size | Weight | Line-height | Tracking | Transform | Feature settings |
|---|---|---|---|---|---|---|---|
| `h4` | Waldenburg | 12px | 700 | 18px | normal | none | `"kern"` |
| `body` | Waldenburg | 12px | 400 | 18px | normal | none | `"kern"` |
| `a` | Waldenburg | 12px | 400 | 18px | normal | none | `"kern"` |
| `p` | Waldenburg | 9.6px | 400 | 14.4px | 0.192px | none | `"calt","kern","liga","rclt","rlig","rvrn"` |
| `button` | Waldenburg | 6.6px | 400 | 5.28px | 0.528px | **uppercase** | `"calt","kern","liga","rclt","rlig","rvrn"` |

**Principles**
- Hierarchy is carried almost entirely by weight (400 vs 700) and by size shifts inside a very small type scale — the whole system lives under 12px at the base tier, with `p` and `button` dropping even smaller.
- `body`/`h4`/`a` run the lean `"kern"`-only feature set; `p` and `button` switch on the full contextual set (`calt`, `liga`, `rclt`, `rlig`, `rvrn`) — the richer OpenType treatment is reserved for reading copy and interactive labels, where ligatures and contextual alternates matter most.
- Buttons are the only uppercase, tracked text in the system (`0.528px` letter-spacing at 6.6px) — a micro-label treatment, not a heading treatment.
- Positive tracking scales inversely with size: `p` gets `0.192px` at 9.6px, `button` gets `0.528px` at 6.6px — smaller text is opened up more to stay legible.

---

## 4. Component Stylings

**Buttons (default `button` element)**
- Black background, `#eaeaea` text and matching `#eaeaea` border — an inverted stamp, same logic as an ink-on-paper pill
- Text set 6.6px uppercase Waldenburg with 0.528px tracking — a genuinely tiny, badge-like button label

**`.kimera-button`**
- Fills with `--kimera-grey` (`#d6d6d6`), radius driven by `--kimera-button-border-radius: 2em` — a fully pill-shaped, size-relative radius (scales with the button's own font-size rather than a fixed pixel value)

**Grid item cards (`.grid-item-inner`)**
- `#eaeaea` surface — the off-white card tier that separates catalogue tiles from the pure-white page canvas

**Cart badge (`.cart-items-counter`)**
- `--kimera-blue` (`#15abff`) fill with black text — the only moment the brand accent appears as a filled chip rather than a line or state color

**Shopping cart container**
- Pure black (`#000`) inner surface — the deepest point on the luminance ramp, reserved for the cart drawer/panel

**Radius system**
- General radius token: `--kimera-border-radius: 0.7rem` (renders at `13.2px` in the extracted DOM, implying a non-16px root size)
- Button-specific radius: `--kimera-button-border-radius: 2em` — pill shape, relative to element font-size
- No shadows detected anywhere in the extracted system

---

## 5. Layout Principles

- Grid gaps are explicit and small: `--kimera-grid-gap: 8px` (column) and `--kimera-grid-row-gap: 14px` (row) — a tighter horizontal rhythm than vertical, typical of a masonry/tile catalogue where cards need to breathe more vertically than horizontally.
- `--kimera-side-padding: 1.25rem` sets the outer page margin; `header` padding (`4px 15px`) and `footer` padding (`2.4px 15px, 4px` bottom) are both far shallower than the side padding, keeping chrome thin so the product grid dominates the viewport.
- `--kimera-small-gap: max(4px, min(0.333em, 8px))` is a genuinely fluid spacing token — it scales with the element's own font-size (`0.333em`) but is clamped between 4px and 8px, so tiny UI clusters (badges, icon+label pairs) never collapse or overflow regardless of local type size.
- `body` and `main` are fully reset (0 padding, 0 margin) — all spacing is delegated to `header`, `footer`, and the grid gap tokens rather than the document flow.
- Breakpoint set — `480 / 767–768 / 769 / 1023–1024` — reads as three real tiers (mobile / tablet / desktop) expressed as paired max-width/min-width queries, a standard Nuxt/CSS-modules pattern rather than anything bespoke.

---

## 6. Depth & Elevation

Depth is a pure greyscale ramp, with zero shadows in the extracted system:

| Surface | Color | Luminance |
|---|---|---|
| `div.page-overlay` | `#fff` | 1.0 |
| `div.grid-item-inner` | `#eaeaea` | 0.918 |
| `div.kimera-button` | `#d6d6d6` | 0.839 |
| `div.shopping-cart-inner-container` | `#000` | 0.0 |

Each tier is a small, deliberate step down from white — page overlay, then card surface, then button fill — before the system jumps all the way to black for the cart drawer. That jump (0.839 → 0.0) is the only dramatic contrast move in the whole ramp, which makes the cart panel feel like a distinct, weightier layer rather than another card in the stack. `--kimera-filter-color: hsla(0,0%,59%,.4)` is the one non-opaque token — a translucent mid-grey scrim, presumably for filter dropdowns or dimmed/inactive states.

---

## 7. Do's and Don'ts

**Do**
- Set body copy in Waldenburg at 12px/18px line-height with `"kern"` only — reserve the fuller OpenType feature set (`calt`, `liga`, `rclt`, `rlig`, `rvrn`) for `p` and `button` text specifically.
- Keep buttons small, uppercase, and tightly tracked (6.6px, 0.528px letter-spacing) — treat them as labels, not headlines.
- Build depth from the grey ramp (`#fff` → `#eaeaea` → `#d6d6d6` → `#000`), not from shadows.
- Reserve `--kimera-blue` for functional badges (cart counters, active states) rather than large fills.
- Use the `2em` pill radius only on button-class elements; keep the `0.7rem` radius for general cards/containers.
- Let the small, clamped gap token (`max(4px, min(0.333em, 8px))`) handle tight inline clusters so they scale with local type size without breaking.

**Don't**
- Don't introduce a second typeface — the entire system, including the tiniest UI labels, runs on Waldenburg.
- Don't add box-shadows for elevation; none exist in the source system, and the greyscale-ramp approach is the whole point.
- Don't blow out the accent colors (blue, greens, red) into backgrounds or large surfaces — they're state/badge colors, not brand wallpaper.
- Don't use a fixed pixel radius on buttons — the `2em` token is intentionally relative to the button's own type size.
- Don't loosen the header/footer padding to match the side padding — chrome stays thin on purpose so grid content reads as the main event.

---

## 8. Responsive Behavior

Breakpoints cluster at **480, 767/768, and 769/1023/1024** — effectively three tiers (mobile, tablet, desktop) expressed through paired max-width/min-width queries rather than a single clean set, consistent with a component-scoped Nuxt build. The fluid `--kimera-small-gap` token (`max(4px, min(0.333em, 8px))`) is the clearest responsive signal in the token set: spacing that tracks local font-size but never drops below 4px or exceeds 8px, so compact UI groupings stay legible from the smallest to the largest tier without a media query of their own.

---

## 9. Agent Prompt Guide

> Build a UI that matches Kimera Corp's design language.

Use **Waldenburg** (fallback `Arial, sans-serif`) as the only typeface, site-wide — this is a type-foundry product page, so the UI font is itself the exhibit. Run body/nav/link text at 12px/18px line-height with `"kern"`-only features; drop paragraph copy to 9.6px/14.4px with `0.192px` tracking and the full OpenType feature set (`calt`, `kern`, `liga`, `rclt`, `rlig`, `rvrn`) switched on; set buttons at a tiny 6.6px, uppercase, `0.528px` tracking, with the same full feature set. Keep weight binary — 400 for everything except `h4` at 700 — and let size and case carry hierarchy. Base the palette on black text on a white canvas (`#000` / `#fff`), with `#eaeaea` for card surfaces, `#d6d6d6` for secondary button fills, and pure black for the deepest panel (a cart drawer or modal). Reserve `#15abff` for small functional badges only (like a cart counter), and hold `#48ec6c`/`#31c852` and `#c84531` back as success/error state colors, not decoration. Radius: `0.7rem` on general containers, a fully relative `2em` pill on button-class elements. No shadows — depth comes purely from the white → `#eaeaea` → `#d6d6d6` → black luminance ramp. Grid gaps stay tight (8px columns, 14px rows), side padding at `1.25rem`, and header/footer padding kept shallow (4–15px range) so a dense product grid dominates the page.

---

*Generated by Sparkbites — extracted from live CSS analysis*
