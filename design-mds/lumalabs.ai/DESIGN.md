# Luma — Design System Reference

## 1. Visual Theme & Atmosphere

Luma's homepage stages an inverted composition: the top two-thirds of the viewport is a dark-video hero with a dotted-grid texture running down the right edge, and the bottom third resolves into a crisp white editorial canvas. The headline — "Creative agents that make you prolific" — sits in a custom **Graphik** display at 52px with aggressive negative tracking (`-2.6px`), announcing the product through typography rather than through illustration or product imagery. The chromatic system is radically binary: `oklch(100%)` pure white for the page, `oklch(14.5%)` near-black for the dark frames. A pill-shaped "Sign In" button in the top-right and a pill-shaped "Try Luma" CTA on the video panel are the only rounded chrome; everything else is rectilinear with generous 24px card radii. The vibe is precise, corporate-editorial, confident — a product page that reads like the Apple of AI video: restrained palette, huge type, carefully tuned OKLCH neutrals, and the whole hero animated as a video that plays above a bone-white content shelf.

---

## 2. Color Palette & Roles

Luma's tokens are expressed in **OKLCH** — a perceptually uniform color space — which is itself a design signal. The values are precise and deliberate:

**Foundation (OKLCH)**
- `oklch(100% 0 0)` — `--background` / `--card` / `--popover` (pure white)
- `oklch(14.5% 0 0)` — `--foreground` / `--card-foreground` / `--popover-foreground` (near-black ink)
- `oklch(98.5% 0 0)` — `--primary-foreground` / `--destructive-foreground` (off-white button ink)
- `oklch(20.5% 0 0)` — `--secondary-foreground` / `--accent-foreground` (mid-dark secondary text)
- `oklch(97% 0 0)` — `--muted` / `--accent` (whisper-gray surface)
- `oklch(55.6% 0 0)` — `--muted-foreground` (mid-gray helper text)
- `oklch(92.2% 0 0)` — `--border` (hairline gray)
- `oklch(75% 0 0)` — `--input` (input border)
- `oklch(70.8% 0 0)` — `--ring` (focus ring)

**Destructive / error**
- `oklch(57.7% 0.245 27.325)` — the only chromatic token in the whole system. A single saturated red-orange (~`#e5483d`) reserved for destructive actions. Note the `0.245` chroma — a deliberate, high-saturation value compared to the near-zero chroma of every other token.

**Actual applied colors (RGB equivalents in rendered state)**
- `rgb(255, 255, 255)` — body bg
- `rgb(0, 0, 0)` — body text / nav bg (dark nav against white page)
- `rgb(0, 0, 0)` with white text — nav inversion

The system is intentionally **chromatic-free at rest**. Only the destructive token has hue; every other surface is a pure grayscale step. This is a rare move — most design systems keep at least a brand hue in their tokens — and it signals that Luma expects the *content* (video, generated imagery) to supply all color, and the chrome to stay completely out of the way.

---

## 3. Typography Rules

**Typefaces**
- **Graphik** (self-hosted, obfuscated class name `__graphik_7126cf`) — the entire editorial voice. Weights 400 (body/links/buttons) and 500 (display).
- System fallback stack via `__graphik_Fallback_7126cf`

**Scale**

| Role | Font | Size | Weight | Line-height | Tracking | Transform |
|------|------|------|--------|-------------|----------|-----------|
| H1 / P (display) | Graphik | 52px | 500 | 65px / 62.4px | −2.6px / −2.08px | none |
| H2 | Graphik | 48px | 500 | 57.6px | −1.44px | none |
| H3 | Graphik | 32px | 500 | 38.4px | −1.28px | none |
| Body / A / Button | Graphik | 16px | 400 | 24px | −0.4px | none |

**Principles**
- **Negative tracking scales with size.** −2.6px at 52px, −1.44px at 48px, −1.28px at 32px, −0.4px at 16px — a consistent ~−5% letter-spacing across the ramp. This is Graphik's signature density trick: tight headlines that compress horizontally so the condensed display weight can breathe vertically.
- **Two weights only: 400 and 500.** No 300, 600, or 700. Semibold 500 for display, regular 400 for everything else. Hierarchy is driven by size, not weight.
- **P (paragraph) is 52px.** In the extracted data, `<p>` renders at 52px with weight 500 and negative tracking — meaning the primary lead paragraph is typographically *indistinguishable from h1*. This is the editorial "pull quote as hero" pattern: the prose IS the headline.
- **Body at 16/24 with −0.4px.** Even body copy gets the Graphik tracking treatment — −0.4px keeps the type dense and crisp, matching the display treatment at a smaller scale.

**What's absent:** no italic, no display alternate face, no serif. Graphik + two weights is the entire typographic system.

---

## 4. Component Stylings

**Primary button pill** — e.g. "Sign In", "Try Luma"
- Background: white pill on dark hero / black pill on white shelf (contextual inversion)
- Border-radius: `3.35544e+07px` — this is the CSS parser's interpretation of a very large px number (likely `border-radius: 100vmax` or `9999px` being computed against a container size). Effectively: **full capsule**.
- Text: Graphik 16px/24 weight 400, `−0.4px` tracking
- No shadow, no transform, no hover changes detected in the extracted data — focus is the only interactive state surfaced (native `rgb(0, 95, 204) auto 1px`)

**Cards / content surfaces**
- Border-radius: `24px` — a generous but not pill corner, used on video wrappers and feature cards
- Background: `oklch(100% 0 0)` white on the light shelf; `rgb(0, 0, 0)` on dark sections
- Border: `oklch(92.2% 0 0)` — a 92% lightness hairline that reads as the faintest of lines against white

**Links / nav items** ("Product", "Pricing", "Enterprise", "News", "Join Us")
- Transparent background, `rgb(255, 255, 255)` text (on the dark nav bar)
- Class `.typo-label` suggests a semantic class system for small-cap type — exact label treatment not in the extracted data
- No hover state detected — navigation is feedback-free until focus
- Focus ring: `rgb(0, 95, 204) auto 1px` (browser default)

**Inputs**
- Border: `oklch(75% 0 0)` — slightly darker than `--border` to signal an editable affordance

**Shadows** — none in the extracted system. Depth is binary (dark hero above, white shelf below).

---

## 5. Layout Principles

- **Video-hero over content-shelf.** The hero occupies roughly the top 70% of the first viewport and plays video with the headline overlaid in the lower-left; below the fold a clean white section houses copy, cards, and product features.
- **Sticky dark nav bar.** The navigation bar is `rgb(0, 0, 0)` with white text — it sits against the dark hero without a visible transition. On scroll, the bar presumably holds the dark treatment as the page transitions to white (a deliberate "masthead" strategy rather than a chameleon nav).
- **Section padding: `0 32px`.** Global horizontal rails at 32px keep content pulled in from the viewport edges.
- **Footer padding: `0 32px 160px` with `gap: 80px`.** The footer ends with deep breathing room — 160px below content — treating the page close as an editorial margin, not a flush cutoff.
- No breakpoints are extracted — the layout almost certainly uses container queries or `clamp()`-based scaling given the OKLCH token system and the modern Tailwind CSS stack.

**Detected stacks**: Next.js + Tailwind CSS — consistent with the OKLCH token usage and the obfuscated Graphik class names.

---

## 6. Depth & Elevation

Depth is **binary**: a dark hero video pane sits above a pure-white content pane. There is no gradient between them; the transition is a hard edge. Within each pane:

- On the dark side: a subtle dotted-grid texture (visible in the screenshot on the right edge) provides the only sub-pane depth cue. No shadows.
- On the light side: cards sit on the white canvas with `oklch(92.2% 0 0)` hairline borders — luminance 0.92 against 1.00, so the separation is barely perceptible but legibly carded.

**No `box-shadow` values in the extracted data.** Elevation is achieved through contrast of luminance, not through shadow — and the dark/light hard edge between hero and shelf is the entire depth system of the page.

---

## 7. Do's and Don'ts

**Do**
- Use **OKLCH** for every token. Luma's restraint is only credible because the neutrals are perceptually tuned — RGB grayscale breaks the tonal math.
- Pick **Graphik** (or equivalent: Söhne, Neue Haas Grotesk, Helvetica Now Display) as the single typeface. Ship 400 and 500 only.
- Apply negative tracking scaled to ~−5% of font-size across the whole ramp — including body.
- Invert chrome based on context: dark hero → white pill, white shelf → black pill. The capsule shape is constant; the inversion does the visual work.
- Reserve chroma for destructive/error states only. `oklch(57.7% 0.245 27.325)` is the only saturated hue in the system.
- Use `24px` card radii and full-capsule button radii (`border-radius: 9999px` or `100vmax`) — nothing in between.
- Treat paragraphs as potential hero type. Luma's `<p>` at 52px is a deliberate flattening of h1/p into a single editorial voice.

**Don't**
- Don't introduce a brand accent color. The token system doesn't have one; adding one breaks the editorial neutrality.
- Don't use drop-shadows — the system has none, and adding them would undermine the hard hero/shelf edge.
- Don't use a third font-weight. 400 + 500 is the full palette; 300 looks anemic in Graphik and 600+ breaks the display-over-text hierarchy.
- Don't soften the hero-to-shelf transition with a gradient. The hard edge is load-bearing.
- Don't use positive letter-spacing on display type — the whole look depends on tight, dense headlines.
- Don't place the nav over the hero without explicit dark styling — letting it "adapt" to the hero will blur Luma's masthead posture.

---

## 8. Responsive Behavior

No breakpoints are extracted — Luma is using a modern Next.js + Tailwind CSS v4 setup with OKLCH tokens, which typically means responsive scaling happens via `clamp()`, container queries, or Tailwind utility breakpoints (`sm/md/lg/xl/2xl`) rather than explicit `@media` rules captured in stylesheets. The practical behavior: the 52px h1 likely scales down to ~36–40px on tablet and ~28–32px on mobile via `clamp(...)`, keeping the negative tracking proportional. The hero video maintains aspect ratio while the shelf expands upward to fill the shorter viewport. Section padding of `0 32px` compresses to `0 16px` or `0 20px` on narrow screens. The key responsive invariant: the dark-hero-over-light-shelf composition must survive every breakpoint — collapsing to a single scroll column but never abandoning the binary contrast.

---

## 9. Agent Prompt Guide

> Build a UI that matches Luma's design language.

Use **OKLCH** color tokens: page bg `oklch(100% 0 0)`, foreground `oklch(14.5% 0 0)`, border `oklch(92.2% 0 0)`, muted `oklch(97% 0 0)`, ring `oklch(70.8% 0 0)`. Reserve chroma for destructive states only: `oklch(57.7% 0.245 27.325)` is the one allowed hue. Typography: **Graphik** (or Söhne/Neue Haas) at weights **400 and 500 only**. Display (H1, H2, H3, hero P) is weight 500 with negative tracking scaled to ~−5% of font-size (e.g. 52px → −2.6px, 48px → −1.44px, 32px → −1.28px). Body is 16/24 with `−0.4px` tracking at weight 400. Layout: a dark hero pane (`rgb(0, 0, 0)` bg with video + dotted grid texture) sits directly above a pure-white content shelf — **hard edge, no gradient**. Nav bar is dark (`rgb(0, 0, 0)` bg, white text) and stays dark through the transition. Primary CTA is a **full capsule pill** that inverts based on context: white pill with black text on dark surfaces, black pill with white text on light surfaces. Cards get `24px` radius. No box-shadows anywhere — depth is binary luminance contrast. Keep section padding at `0 32px`; footer padding at `0 32px 160px` with `gap: 80px` so the page ends with generous editorial breathing room. Let Graphik and the OKLCH neutrals carry the entire brand — no illustrations, no colored icons, no decorative chrome.

---

*Generated by Sparkbites — extracted from live CSS analysis*
