# abjt.dev — Design System

## 1. Visual Theme & Atmosphere

abjt.dev is a developer portfolio built on Next.js and Tailwind CSS that achieves something rare: a dark theme that feels warm rather than cold. The background is not pure black but a dark warm brown-black (`rgb(19, 18, 16)`) — barely perceptible, but it shifts the entire mood from the sterile "dark mode default" toward something more like aged paper or studio leather. The typography pairing — GeistSans for structure, GeistMono for content — signals that this is a developer's space, not a designer's. Code and prose coexist deliberately. Surface elevations are shallow and warm, and the only decorative flourish is a whisper-thin translucent overlay (`rgba(255,255,255,0.024)`) that suggests a glass-morphism hint without fully committing. The design is confident in what it omits: no accent colour, no gradients, no imagery-based depth.

## 2. Color Palette & Roles

| Role | Value | Usage |
|---|---|---|
| Page background | `rgb(19, 18, 16)` | Body canvas — warm near-black |
| Elevated surface | `rgb(38, 37, 36)` | Cards, panels (neutral-200) |
| Sunken surface | `rgb(19, 18, 16)` | Flush with page (neutral-50 maps same) |
| Ghost surface | `rgba(255, 255, 255, 0.024)` | Barely-visible glass layer |
| Primary text | `rgb(250, 249, 247)` | Body, headings — warm off-white |
| Muted text | `rgb(163, 162, 160)` | Nav links, secondary labels (default) |
| Active text | `rgb(250, 249, 247)` | Nav links on hover/focus |
| Border | `rgb(229, 231, 235)` | Subtle structural lines |
| Focus ring | `rgb(250, 249, 247)` 1px solid | Keyboard focus indicator |

The palette is a study in near-neutrals: background, text, and surfaces are all within a narrow warm-grey band. No accent colour exists — hierarchy comes entirely from opacity and luminance steps. The warm off-white text (`#FAF9F7`) against the warm black background avoids the harshness of pure `#FFFFFF` on `#000000`.

## 3. Typography Rules

The dual-font system is the defining typographic statement: **GeistSans** handles structural and navigational text, while **GeistMono** is used for body paragraphs and content — inverting the conventional hierarchy where monospace is reserved for code snippets.

| Element | Font | Size | Weight | Line Height | Tracking |
|---|---|---|---|---|---|
| h1 | GeistSans | 16px | 400 | 24px (1.5) | normal |
| body / a / button | GeistSans | 16px | 400 | 24px (1.5) | normal |
| p (content) | GeistMono | 14px | 500 | 20px (1.43) | normal |

Using monospace for prose is a deliberate identity choice — it signals technical literacy, suggests terminal-adjacent aesthetics, and creates a consistent reading texture across code and copy. The slightly heavier weight (500) on `GeistMono` paragraphs compensates for monospace's lower apparent weight at small sizes.

## 4. Component Styling

**Buttons**: Transparent background with `rgba(0,0,0,0)`, warm off-white text. Styled via a `bg-gradient-to-tl` class — a gradient is likely applied in Tailwind utilities even if the computed value shows transparent. Border radius: 9999px (fully pill-shaped). Focus ring is a 1px `rgb(250, 249, 247)` solid outline — matching the text colour, not a browser default blue.

**Nav links**: Default state in muted warm grey (`rgb(163,162,160)`), transitioning to full warm white (`rgb(250,249,247)`) on hover and focus. No background change, no underline — opacity and colour shift only. Clean and non-disruptive.

**Cards / panels**: Two surface levels separated by ~0.075 luminance — barely distinguishable in isolation but perceptible in context. Border radius 11px for panels; 9999px reserved for pill buttons only.

**Ghost layer**: The `rgba(255,255,255,0.024)` surface — 2.4% white — likely a subtle highlight on an absolute-positioned element, possibly a hero image overlay or card shimmer effect.

## 5. Layout Principles

Standard Tailwind breakpoint ladder: 640 / 768 / 1024 / 1280 / 1536px. The `main` element carries a top padding of 108px — a fixed-height nav offset, suggesting a sticky navigation bar approximately 64–72px tall with additional breathing room. This generous top offset anchors the hero section well below the fold-fold, giving navigation visual clarity. Content is left-flush within a constrained max-width container. The design is clearly single-column on mobile, expanding to a wider reading column at 768px+.

## 6. Depth & Elevation

Depth is minimal and warm. Three functional layers:

- `rgb(19, 18, 16)` — luminance 0.071 — base canvas
- `rgb(38, 37, 36)` — luminance 0.146 — elevated panels (+0.075)
- `rgba(255,255,255,0.024)` — luminance ~1.0 at near-zero opacity — ghost shimmer

One actual shadow: `rgb(0,0,0) 0px 1px 2px 0px` — a hairline bottom shadow, barely 2px, used for micro-separation on small interactive elements. No spread, no blur radius — essentially the thinnest possible elevation signal. This restraint keeps the interface flat while still providing tactile separation where needed.

## 7. Do's and Don'ts

**Do:**
- Use `rgb(19, 18, 16)` (not `#000`) for dark backgrounds — the warmth is the differentiator
- Reserve GeistMono for prose content to maintain the developer-identity aesthetic
- Use the muted-to-active colour transition (`#A3A2A0` → `#FAF9F7`) for all interactive state changes
- Keep border radii binary: 11px for panels, 9999px for pill buttons — no mixing
- Maintain the 108px main top-padding for sticky nav clearance

**Don't:**
- Introduce an accent colour — the monochrome warmth is the brand
- Use pure black (`#000000`) or pure white (`#FFFFFF`) — the warmth of the near-neutrals is deliberate
- Apply shadows larger than 2px — the near-flat system would be violated
- Use GeistSans for body paragraphs — the mono/sans inversion is intentional
- Add hover background fills on nav items — colour-only transitions keep the nav weightless

## 8. Responsive Behavior

Standard Tailwind five-point breakpoint system (640 / 768 / 1024 / 1280 / 1536px). Mobile-first with the critical layout shift at 768px where two-column or wider reading widths likely activate. The 108px main padding is fixed regardless of viewport — on mobile this could feel heavy; a responsive `pt-16 md:pt-[108px]` pattern would be appropriate. The nav is likely sticky/fixed given the offset, collapsing to a hamburger or minimal icon at small viewports.

## 9. Agent Prompt Guide

> "Design in the style of abjt.dev: warm near-black background `rgb(19,18,16)`, warm off-white text `rgb(250,249,247)`, GeistSans for UI/navigation, GeistMono at weight 500 for body paragraphs, no accent colour, muted grey `rgb(163,162,160)` for secondary nav that transitions to full white on hover, pill buttons (9999px radius) with transparent backgrounds, card panels at `rgb(38,37,36)` with 11px radius, hairline 2px shadows only, 108px main content offset for sticky nav, standard Tailwind breakpoints. Warm, developer-coded, monochromatic."

---

*Generated by Sparkbites — extracted from live CSS analysis*
