# rascalsbaby.com — Design System

## 1. Visual Theme & Atmosphere

Rascalsbaby.com is a baby and children's product brand that has made a clear design choice: trust through sophistication, not through pastels. Where most baby brands reach for soft pinks and sky blues, this site grounds itself in a deep teal-green (`#003A48`) that reads as authoritative and natural simultaneously — evoking organic materials, clean nurseries, and confident parenting rather than nursery-rhyme naivety. White provides the light, airy canvas that balances the deep footer and nav accents.

The personality lives in two accent colors: a warm lavender-purple (`#9574DF`) for primary CTAs and a seafoam mint (`#5ED2BD`) for links and secondary interactions. Together they form a playful-but-elevated duo that gives the brand its warmth without surrendering its credibility. The design says: these are premium products for parents who research.

---

## 2. Color Palette & Roles

**Surfaces**
- `#FFFFFF` — Page canvas and card backgrounds
- `#CFf1EB` (`rgb(207, 241, 235)`) — Mint-wash accent surface (absolute-positioned highlights, decorative panels)
- `#003A48` — Deep teal; footer, sticky nav, and dark section backgrounds

**Text**
- `#003A48` — Primary body text (the brand's anchor color carries into typography)
- `#FFFFFF` — Text on dark surfaces (nav, footer, inputs)
- `rgb(229, 231, 235)` — Default border color throughout (Tailwind's `gray-200`)

**Brand Accents**
- `#9574DF` — Lavender purple; primary buttons and CTAs (`button`, `button.group`)
- `#5ED2BD` — Seafoam mint; link color and interactive highlights

**Interactive States**
- Link default: `#5ED2BD`
- Link hover: `#FFFFFF` — links turn white on hover, implying they live on the dark teal surface
- Input fields: `rgba(255,255,255,0.1)` background with white border — ghost input on dark backgrounds

---

## 3. Typography Rules

Rascalsbaby.com employs a deliberate two-font system that separates display personality from body legibility:

**Sofia Pro** (display/headings) — A geometric sans with friendly curves. Headings use weight 400 at 40px with `-0.5px` letter-spacing — soft and approachable without being childlike. The light tracking keeps it refined.

**DM Sans** (body/captions) — A low-contrast humanist sans at 16–18px. Heavier weights (500–600) appear at larger sizes while smaller captions stay at 500. DM Sans is an excellent legibility workhorse for product descriptions and navigation.

- **h1**: Sofia Pro / 40px / 400 / `letter-spacing: -0.5px`
- **body**: DM Sans / 18px / 400 / `line-height: 28px`
- **figcaption**: DM Sans / 16px / 500

No uppercase labels or decorative text transforms are used. The typography system is readable-first, personality-second.

---

## 4. Component Stylings

**Primary buttons**: Solid lavender-purple (`#9574DF`) fill, white text, with the site's rounded approach. Full pill-style rounding (`9999px`) also used alongside moderate `8–10px` and `16px` radii — different components use different radii based on context.

**Border radii spectrum**: `8px` (default), `10px`, `16px` (larger cards/panels), `9999px` (pill buttons and tags), and one asymmetric value `0px 8px 8px 0px` suggesting a connected-input pattern.

**Navigation**: Transparent (`rgba(0,0,0,0)`) above the fold, transitions to the deep teal (`#003A48`) on scroll via the `div.fixed` surface. Nav text is white regardless of state.

**Footer**: Solid `#003A48` with white text — a strong closing anchor that mirrors the nav treatment.

**No shadows detected** — the site achieves visual hierarchy through color blocking rather than elevation.

---

## 5. Layout Principles

Rascalsbaby.com uses a multi-breakpoint responsive ladder: 430, 540, 1024, 1280, 1440, and 1740px — a wide-screen optimized scale that extends to 1740px, suggesting large-display product photography is a priority.

The main layout appears section-based with full-width color blocks. The `--header-height` CSS variable (`8.5rem` default, `7.625rem` at large breakpoints) is explicitly tracked — suggesting a sticky header that adjusts its footprint across sizes.

The Next.js + Tailwind stack drives a utility-first grid, with sections likely using full-bleed backgrounds and constrained inner content columns.

---

## 6. Depth & Elevation

No box shadows are present in the extracted data. The site uses color contrast as its primary depth mechanism: white surfaces sit "above" the deep teal panels and footer through brightness contrast. The `#CFf1EB` mint-wash panels create a soft mid-layer between white and teal.

Interactive elements (buttons, cards) likely use scale transforms or opacity shifts rather than shadow on hover, consistent with the shadow-free approach.

---

## 7. Do's and Don'ts

**Do**
- Use `#003A48` teal for all dark sections, footers, and sticky chrome
- Reserve `#9574DF` lavender exclusively for primary actions
- Use `#5ED2BD` mint for text links and secondary interactions only
- Extend to 1440–1740px with full-bleed product imagery
- Keep Sofia Pro for display text, DM Sans for everything functional

**Don't**
- Use pastels, primary-color baby palettes, or nursery-rhyme aesthetics
- Mix lavender and mint in the same interactive element
- Add box shadows — use color contrast for depth
- Use pure black text — `#003A48` is the darkest readable tone in this system

---

## 8. Responsive Behavior

The six-breakpoint scale (430 → 540 → 1024 → 1280 → 1440 → 1740px) spans mobile-small through ultra-wide. At 430px (covering many modern phones), layout likely stacks into a single column. The jump to 1024px suggests a two-column product grid appears at tablet-landscape. The 1740px breakpoint exists to serve large photography without layout breaking.

The `--header-height-lg` variable (`7.625rem`) is marginally smaller than the default `8.5rem`, suggesting the header compresses slightly at desktop widths — common for sticky header behavior.

---

## 9. Agent Prompt Guide

> "Design in the style of rascalsbaby.com: deep ocean teal `#003A48` as the anchor dark tone, white as the primary canvas, lavender-purple `#9574DF` for CTAs, seafoam mint `#5ED2BD` for links. Two-font system: Sofia Pro for display headings (weight 400, slight negative tracking), DM Sans for body. No shadows — use full-bleed color blocks for depth. Sophisticated, natural, and elevated — premium baby products for discerning parents."

---

*Generated by Sparkbites — extracted from live CSS analysis*
