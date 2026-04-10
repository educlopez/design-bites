# jonsbones.com — Design System

## 1. Visual Theme & Atmosphere

Jon's Bones is a direct-to-consumer e-commerce site selling pet products, and its design reads as warmly coastal — soft blues, dusty teals, and a dark slate that feels handcrafted rather than corporate. The visual identity occupies a middle ground between editorial illustration and clean commerce: headline typography in a serif (p22-mackinac-pro) conveys character and warmth, while body copy in proxima-nova keeps things readable and trustworthy.

The background is white but the emotional temperature is set by the palette — muted blue-greens that evoke calm, natural environments. Interactive elements like the add-to-cart button use a muted sky blue (`#7fBDDB`), deliberately understated for an e-commerce action. This is a shop that doesn't want to feel like a shop.

Built on Webflow. The layout and typography are Webflow-native with Adobe Fonts loaded server-side.

---

## 2. Color Palette & Roles

**Foundational neutrals:**

| Role | Value | Notes |
|------|-------|-------|
| Page background | `#ffffff` | Pure white |
| Primary text | `#394248` (dark-slate-grey) | Custom property, cool dark grey |
| Input placeholder | `#738189` | Lighter slate |

**Blues — the brand character:**

| Role | Value | Notes |
|------|-------|-------|
| Decorative light blue | `#c9d8e0` (light-grey token) | Background tints, muted borders |
| Cart checkout button | `#7fBDDB` | Muted sky — e-commerce CTA |
| Buy-now button | `#3898EC` | Brighter blue — urgency action |
| Blog section band | `#93b1c1` | Mid teal-blue content zone |
| Footer light background | `#f0f6fa` | Very pale blue-white |
| Nav transparent base | `rgba(133,160,175,0)` | Teal-tinted transparent |

**Functional / feedback:**

| Role | Value | Notes |
|------|-------|-------|
| Error state | `rgb(255,222,222)` | Pale red cart error |
| Dark action (add-to-bag) | `#394248` | Dark fill, matches primary text |
| Dividers | `#738189` | Slate divider lines |

The palette is cohesive: every blue and teal derives from the same blue-grey hue family. Even the footer and section backgrounds are variations of the same muted-blue-white. Nothing feels accidental.

---

## 3. Typography Rules

Two typefaces in a deliberate editorial pairing:

**Display: p22-mackinac-pro** (Adobe Fonts / Typekit)
- A warm, humanist serif with ink-trap details — evokes craft and care
- Used for h1 at large scale

**Body: proxima-nova** (Adobe Fonts / Typekit)
- A geometric-humanist sans — clean, modern, legible
- Used for all navigation, body, and UI text

| Role | Font | Size | Weight | Line Height |
|------|------|------|--------|-------------|
| H1 / hero | p22-mackinac-pro | 54.4px | 400 | 59.84px (1.1×) |
| Body / nav | proxima-nova | varies | 400 | normal |
| Dialog / UI | proxima-nova | 12.7px | 400 | 12.7px (1:1) |

The hero serif at 400 weight is unusual — it leans on the typeface's inherent personality rather than weight for impact. Mackinac at regular weight has strong optical character that makes bold unnecessary at display sizes.

Note: h1 is white (`#ffffff`) — it sits on a photographic or coloured hero background, not on the white page.

---

## 4. Component Stylings

**Add to Cart / Checkout button**
- Background: `#7fBDDB` (muted sky blue)
- Text: `#ffffff`
- Deliberately low-urgency colour for a considered purchase flow

**Buy Now button**
- Background: `#3898EC` (brighter blue)
- Text: `#ffffff`
- Higher visual priority than checkout

**Cart error state**
- Background: `rgb(255,222,222)` — pale blush red
- Text: `#394248` — slate body text

**Navigation**
- Transparent base (`rgba(133,160,175,0)`) — overlays hero imagery
- Text: `#394248` — slate

**Footer**
- Background: `#f0f6fa` — very pale blue-white
- Text: `#394248`
- Dividers: `#738189` (slate grey)

**Blog content band**
- Background: `#93b1c1` — mid teal-blue
- Text: `#394248` — ensures contrast on the mid-tone surface

---

## 5. Layout Principles

Built on Webflow with Webflow Commerce (`w-commerce` classes). The layout follows Webflow's standard grid conventions.

- Navigation is full-width, transparent overlay on hero
- Content sections alternate between white and tinted blue backgrounds for rhythm
- The blog text wrapper uses a coloured band (`#93b1c1`) for editorial sectioning
- Footer is clearly delineated with `#f0f6fa` background

No custom grid token system detected. Spacing is managed through Webflow's layout tools. The site uses natural sectioning rather than a mathematical spacing scale.

---

## 6. Depth & Elevation

Depth is handled through background colour banding rather than shadows:

- Hero: full-bleed image with overlaid white h1 text
- Content: white sections
- Blog band: `#93b1c1` tinted section
- Footer: `#f0f6fa` pale blue

No `box-shadow` or `filter: drop-shadow` detected on primary UI elements. The cart/modal overlay may use standard Webflow dialog shadows, but no custom shadow system exists.

The add-to-bag animation element uses `#394248` — a dark filled overlay — suggesting a temporary feedback animation rather than a persistent elevated surface.

---

## 7. Do's and Don'ts

**Do:**
- Pair p22-mackinac-pro (serif, 400) with proxima-nova for display + body contrast
- Keep e-commerce CTAs in muted blues — this site is not aggressive about conversion
- Use the teal-blue family (`#c9d8e0`, `#93b1c1`, `#7fBDDB`) for all branded colour
- Let the transparent nav overlay photography — keep it unobstructed
- Use white text on h1 / hero — it's always placed over image backgrounds

**Don't:**
- Use p22-mackinac-pro for body text — it's purely a display/hero typeface
- Introduce warm colours (orange, red, yellow) — they clash with the cool coastal palette
- Make the buy button more prominent than necessary — the understated UX is intentional
- Add box-shadows to cards or product tiles — the design is flat and surface-neutral
- Use dark backgrounds; this is a light-on-white system with blue accent surfaces

---

## 8. Responsive Behavior

Built on Webflow — responsive behaviour is managed through Webflow's breakpoint system:

Standard Webflow breakpoints:
- **Desktop**: 992px+
- **Tablet**: 768px–991px
- **Mobile landscape**: 480px–767px
- **Mobile portrait**: below 480px

The transparent navigation will collapse to a Webflow hamburger menu pattern on mobile. The 54.4px hero serif scales down at smaller viewports. Product grid (Webflow Commerce) reflows from multi-column to single-column. The cart checkout/buy-now buttons are adequately sized for touch at their current dimensions.

---

## 9. Agent Prompt Guide

**Quick reference:**
- Background: `#ffffff`, surfaces: `#f0f6fa` (footer), `#93b1c1` (editorial band)
- Primary text: `#394248` (slate)
- Blues: `#c9d8e0` (light), `#7fBDDB` (CTA), `#3898EC` (buy now)
- Fonts: p22-mackinac-pro (display/serif) + proxima-nova (body/UI)
- Hero h1: white on image background, 54.4px / 400

**Prompt to replicate this aesthetic:**
> "Design a pet product e-commerce page with a coastal, editorial feel. White background with muted teal-blue accents (`#7fBDDB`, `#c9d8e0`). Primary text in dark slate `#394248`. Hero heading in a warm serif (p22-mackinac-pro or equivalent) at large size / regular weight in white over a hero image. Body copy in a geometric sans (proxima-nova). CTAs in muted blue — not high-urgency. Teal band `#93b1c1` for editorial sections."

**Prompt to extend a component:**
> "Add a product card for jonsbones.com. White background. Product name in proxima-nova `#394248`. Price in `#738189`. Add-to-cart button background `#7fBDDB`, white text. No shadow. Light border or no border. Footer area: `#f0f6fa` background."

---

*Generated by Sparkbites — extracted from live CSS analysis*
