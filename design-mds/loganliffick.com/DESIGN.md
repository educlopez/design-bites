# loganliffick.com — Design System

## 1. Visual Theme & Atmosphere

loganliffick.com inhabits the refined territory of the modern developer portfolio — clean, systematic, and visually literate without being ostentatious. Inter at modest weights carries all the typographic work, while a carefully graduated neutral scale (white through near-black, with precisely named tokens like `--text-strong` and `--text-soft`) signals a designer who thinks in systems. The background is off-white (`neutral-50`) rather than pure white, a small but meaningful decision that softens the contrast and gives the page warmth. Multi-layered shadows on key components add genuine depth. The overall feeling is of a well-maintained design system applied with restraint — confident, contemporary, and highly readable.

## 2. Color Palette & Roles

| Role | Token | Approximate Value | Usage |
|---|---|---|---|
| Page background | `--bg` | `neutral-50` (~`#fafafa`) | Canvas |
| Card / depth surface | `--bg-depth` | `white` | Elevated surfaces |
| Strong text | `--text-strong` | `neutral-900` (~`#171717`) | Headings, primary content |
| Soft text | `--text-soft` | `neutral-600` (~`#525252`) | Secondary labels, captions |
| Border | `--border` | `neutral-200` (~`#e5e5e5`) | Dividers, card edges |
| Marker | `--marker` | `neutral-300` (~`#d4d4d4`) | Visual accents, list markers |
| Base scale | `--base-100` to `--base-1000` | white → `neutral-950` | Systematic neutral ramp |

No colour accent extracted — the design is intentionally monochromatic. Any brand expression comes through typography and layout density rather than hue.

## 3. Typography Rules

**Primary typeface:** Inter (with Inter Fallback)  
**Code typeface:** System monospace stack (ui-monospace → Courier New)

- **H1:** Inter, 18px / 28px line-height / weight 500 — modest, content-first
- **Body (p):** Inter, 16px / 26px line-height / weight 400 — generous and readable
- **Code:** System monospace, 16px / 26px — matching body line-height for inline harmony
- No decorative sizes — nothing above 18px extracted
- No letter-spacing adjustments — Inter's optical defaults relied upon
- No text transforms — all-lowercase or title-case as authored

Inter at weight 500 for headings creates hierarchy through weight contrast alone, not size escalation. The heading size (18px) is barely larger than body (16px) — a deliberate signal that content matters more than hierarchy.

## 4. Component Stylings

- **Cards:** White (`--bg-depth`) background, `neutral-200` border, multi-layer soft shadow, `8px` border-radius
- **Navigation:** Transparent background, inheriting page colour
- **Code blocks:** System monospace, matching body line-height — no extracted syntax colours
- **Focus rings:** Inherited from browser or minimal system
- **Border-radius scale:** `4px` (small), `8px` (card), `16px` (larger card), `48px` (pill), `100%` (avatar)
- **Shadows:** Multi-layered, low-opacity: `rgba(0,0,0,0.06)` cascading through 4–5 layers — creates realistic depth without drama

## 5. Layout Principles

The token naming (`--bg`, `--bg-depth`, `--border`) implies a layered layout: a base canvas, elevated card surfaces, and bordered sections. The off-white background allows white cards to visually pop. Spacing is likely 8px-based — the system feels grid-conscious. Navigation is transparent, suggesting a sticky or inline nav that blends with the page.

## 6. Depth & Elevation

The shadow system is the most sophisticated of the five sites analysed:
- Multi-layer shadows at `rgba(0,0,0,0.06)` — subtle but unmistakable
- Two elevation levels: base page (`--bg`) and raised surface (`--bg-depth` = white)
- Border at `neutral-200` reinforces card edges alongside shadow
- Result: components feel physically present without feeling heavy

## 7. Do's and Don'ts

**Do:**
- Use the full neutral ramp from `--base-100` to `--base-1000` for hierarchy
- Apply multi-layer shadows to elevated components
- Keep Inter at weights 400 and 500 only
- Use `--bg-depth` white cards on `--bg` off-white canvas
- Keep heading sizes close to body (18px vs 16px) — hierarchy through weight

**Don't:**
- Introduce colour accents — this is a monochromatic system
- Use shadows larger than `8px` blur
- Scale headings above 24px
- Mix font weights beyond 400/500
- Add border-radius above 16px for content cards (use 48px only for avatars/pills)

## 8. Responsive Behavior

Breakpoints: 420px, 810px, 1200px. The layout likely shifts from multi-column (desktop) to single-column (mobile) for card grids. Typography may scale down slightly at mobile. The neutral-background card system works equally well at all widths. Navigation likely collapses to a menu at sub-420px.

## 9. Agent Prompt Guide

> Replicate loganliffick.com: off-white (`#fafafa`) canvas, white card surfaces with multi-layer `rgba(0,0,0,0.06)` shadows and `neutral-200` borders. Inter at 16px/26lh body (weight 400), 18px/28lh headings (weight 500). Monochromatic neutral palette — no colour accents. Border-radius 8px for cards. System monospace for code. `--text-strong` at `neutral-900`, `--text-soft` at `neutral-600`. Clean, systematic, depth through shadows not colour.

---
*Generated by Sparkbites — extracted from live CSS analysis*
