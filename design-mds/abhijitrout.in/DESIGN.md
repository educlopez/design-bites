# abhijitrout.in — Design System

## 1. Visual Theme & Atmosphere

abhijitrout.in is a personal portfolio built in Framer that wears its craft tools visibly. The palette is almost brutally simple: pure white canvas, true black type, with two surface variants providing the only tonal relief. What makes it distinctive is not any single design decision but the combination of aggressive restraint with high-radius pill shapes — the tension between razor-sharp typography and extremely soft, almost bubble-like border radii (30px and 60px) creates an approachable, designer-playful personality. The browser-default hyperlink blue (`rgb(0, 0, 238)`) is kept intentionally, functioning as a self-aware nod to the raw web — either ironic minimalism or deliberate anti-polish. No shadows. No gradients. Framer Motion adds animation without decorative complexity.

## 2. Color Palette & Roles

| Role | Value | Usage |
|---|---|---|
| Page background | `rgb(255, 255, 255)` | Body canvas |
| Off-white surface | `rgb(246, 246, 243)` | Warm card/section backgrounds |
| Mid-grey surface | `rgb(184, 184, 184)` | Dividers, muted elements |
| Dark surface / inversion | `rgb(0, 0, 0)` | Black accent panels |
| Primary text | `rgb(0, 0, 0)` | All body copy |
| Muted text (hover) | `rgb(184, 184, 184)` | Link hover — text fades to grey |
| Link / interactive | `rgb(0, 0, 238)` | Hyperlinks (browser default blue) |
| Button background | `rgb(59, 59, 62)` | Dark charcoal button fill |
| Border | `rgb(0, 0, 0)` | Hard black borders |

The colour story is pure black-and-white with one warm-grey surface (`#F6F6F3`) for softness and the browser-default link blue as a deliberate raw-web reference. Notably absent: any custom brand colour, any tint, any gradient.

## 3. Typography Rules

The site uses **Geist** — Vercel's open-source humanist sans-serif — for body paragraphs, paired with a bare `sans-serif` fallback for most other elements. This creates a subtle hierarchy: Geist-set content is the authored voice; everything else defers to the browser default.

| Element | Font | Size | Weight | Line Height | Tracking |
|---|---|---|---|---|---|
| body / a / button | `sans-serif` (system) | 12px | 400 | normal | normal |
| p | Geist | 14px | 400 | 16.8px (1.2) | −0.42px |

The tight letter-spacing on paragraphs (−0.42px at 14px) is subtle but intentional — it compresses Geist slightly, giving prose a crisp, almost journalistic quality. The 12px base for non-paragraph elements suggests UI chrome is deliberately small and recessive, letting content breathe. No heading typography was detected — headings either use images or are styled via Framer's canvas rather than semantic HTML.

## 4. Component Styling

**Buttons**: Charcoal (`rgb(59, 59, 62)`) background, 12px system font. No hover state captured. Border radius at 3px — uniquely minimal compared to the pill shapes used elsewhere, suggesting buttons are intentionally boxy and utilitarian against the organic roundness of cards.

**Links**: Default browser blue (`rgb(0,0,238)`) with hard black borders — browsers' default link underline behaviour likely retained. Hover state changes text to `rgb(184, 184, 184)` — a cool fade rather than an underline toggle.

**Cards / panels**: Two warm surface levels — `rgb(246,246,243)` (nearly white) and `rgb(184,184,184)` (mid-grey) — plus a pure black inversion panel. Border radii of 30px and 60px give cards a pronounced pill quality, softening what would otherwise be a very hard-edged layout.

**Framer classes**: Component IDs like `framer-51BfY`, `framer-9lsero` confirm Framer-generated markup — no custom component naming system.

## 5. Layout Principles

Framer-generated layout with three breakpoints: ~810px (tablet) and ~1200px (desktop), plus a 2160px cap for ultrawide. The 809.98 / 810 pair is a Framer pattern — two near-identical values defining the exact tablet boundary. Section padding is compact (10px), footer padding is generous (40px), suggesting a design where the footer is treated as a distinct "chapter" rather than an afterthought. Overall layout density is low — the small font sizes and generous whitespace (via Framer's auto layout) create a calm, open feel.

## 6. Depth & Elevation

No shadows at all. Depth is created entirely through surface colour contrast:

- `rgb(255, 255, 255)` — page canvas
- `rgb(246, 246, 243)` — luminance 0.963 — warm lift
- `rgb(184, 184, 184)` — luminance 0.722 — mid element
- `rgb(0, 0, 0)` — luminance 0 — maximum contrast inversion

The absence of shadows is philosophically consistent: depth here comes from tonal steps, not simulated light. The black panel (`rgb(0,0,0)`) creates the strongest visual anchor on the page purely by contrast.

## 7. Do's and Don'ts

**Do:**
- Use the warm off-white (`#F6F6F3`) for card backgrounds — never pure white on white
- Keep the browser-default blue for links — it's a design choice, not an oversight
- Apply large border radii (30–60px) on card containers for the signature pill softness
- Use Framer Motion for subtle enter animations — keep them short and purposeful
- Let font size hierarchy do the work: 12px chrome, 14px content

**Don't:**
- Introduce custom brand colours — the raw-web aesthetic depends on the absence of branded hues
- Add shadows or glows — the flat luminance system is the whole depth strategy
- Use Geist on UI elements (nav, buttons) — reserve it for authored content paragraphs only
- Increase font sizes beyond 14px for body — the small-scale typesetting is deliberate
- Round button corners (keep them at 3px) — contrasting with the soft cards is intentional

## 8. Responsive Behavior

Three primary breakpoints: ≤809.98px (mobile), 810–1199.98px (tablet), ≥1200px (desktop), with a 2160px wide-screen boundary. Framer auto-layout manages column reflow. The extremely tight mobile breakpoint boundary (809.98 vs 810) is Framer's precision — don't try to replicate this manually. Footer padding increases at larger sizes (40px), suggesting the footer layout expands horizontally at desktop widths.

## 9. Agent Prompt Guide

> "Design in the style of abhijitrout.in: pure white canvas, true black type, Geist font at 14px with −0.42px tracking for body content, 12px system sans-serif for UI chrome, no custom accent colour (use browser-default blue `#0000EE` for links), charcoal buttons (`#3B3B3E`) with 3px radius, soft pill cards with 30–60px border radius, warm off-white surface `#F6F6F3`, no shadows, hover states via colour fade to grey `#B8B8B8`, Framer Motion for entry animations. Intentionally raw, anti-decorative, typographically restrained."

---

*Generated by Sparkbites — extracted from live CSS analysis*
