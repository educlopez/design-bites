# expensive.toys — Design Language

## 1. Visual Theme & Atmosphere

expensive.toys is an act of deliberate anachronism. In a landscape of smooth, flat, system-font interfaces, it commits fully to Windows 95 / early web aesthetics — rendered through a modern Next.js codebase. The body background is a flat grey (`rgb(207, 207, 207)`) that unmistakably evokes the Windows desktop. Buttons have the classic bevelled 3D appearance via asymmetric border coloring. The font is `ms_sans_serif` — the original Windows interface font, recreated for the web.

This is not "inspired by" retro design; it is a precise reconstruction. Every detail — the bevelled borders, the grey palette, the `arial` heading font — is a reference to a specific era of computing. The design philosophy is: the medium is the message. A site called "expensive.toys" sells premium digital goods through the visual language of the earliest consumer software.

The result is simultaneously ironic and affectionate, nostalgic and functional.

## 2. Color Palette & Roles

**Background System**
- `rgb(207, 207, 207)` — Page body; the classic Windows 95 desktop grey
- `rgb(198, 198, 198)` — Elevated surface / content area; slightly darker than body, the standard "window" grey
- `rgb(198, 198, 198)` — Button face; same as surface, consistent with Windows control rendering

**Accent / Highlights**
- `rgb(222, 173, 37)` — Gold/amber; used on featured product cards or price tags. In the Windows palette context, this reads as an "attention" color — bright against grey.
- `rgb(137, 176, 168)` — Muted teal-green footer; evokes the Windows-era teal screen color, creating a section separator with period-authentic character.

**Text**
- `rgb(0, 0, 0)` — Pure black; the only text color
- `rgb(10, 10, 10)` — Near-black for nav links; effectively identical

**Borders (bevelled system)**
Windows 3D effect via asymmetric border coloring:
- Light edges: `rgb(254, 254, 254)` (bottom-right) — the lit face
- Dark edges: `rgb(132, 133, 132)` (top-left) — the shadow face
- Footer uses `rgb(162, 199, 192)` light / `rgb(5, 6, 8)` dark for a teal-tinted bevel

This four-sided border asymmetry is the technical mechanism behind every element that looks "raised" or "sunken" on this site.

**Absent:** No CSS custom properties, no design tokens, no shadows. The entire depth system is border-based.

## 3. Typography Rules

**ms_sans_serif** — The Windows system font, used for all body text, paragraphs, links, and buttons. This is not a generic system font fallback — it is a specific named font (likely loaded as a webfont that mimics the original bitmap typeface). At 16px / 400 weight, it renders with the characteristic chunky, low-resolution feel of early Windows interfaces.

**Arial** — H1 only. Arial was the standard heading font in Windows-era documents. At 40px / 700 / 60px line-height, it creates display-sized headlines with the intentional bluntness of the era.

**Scale**
| Role | Font | Size | Weight | Line Height |
|------|------|------|--------|-------------|
| H1 | Arial | 40px | 700 | 60px |
| Body | ms_sans_serif | 16px | 400 | 24px |
| Button | ms_sans_serif | 18px | 400 | normal |

No letter-spacing adjustments — the fonts are used straight, as they would have appeared on a 1995 monitor. No ligatures, no font features. The rawness is the style.

## 4. Component Stylings

**Buttons**
`rgb(198, 198, 198)` fill, black text, asymmetric bevel borders. The Windows button: exactly as it appeared in the Start menu era. No border-radius (none declared in the data — this is a zero-radius design). On hover, no color change is captured — interaction may be handled through the bevel border reversal (light edges become dark, dark become light) which simulates a "pressed" state.

**Product / Feature Cards**
Gold/amber fill (`rgb(222, 173, 37)`) with the same bevel border system. In the Windows context this creates "highlighted" or "selected" tile appearance.

**Footer**
`rgb(137, 176, 168)` background with teal-tinted bevel borders (`rgb(162, 199, 192)` top-left, `rgb(5, 6, 8)` bottom-right). Functions as a taskbar or status-bar analog — a distinct chrome element below the main content.

**Navigation**
Transparent background, near-black text. Links retain the raw browser-default blue (`rgb(0, 0, 238)`) — a browser default that here feels entirely at home in the retro context.

## 5. Layout Principles

Built on Next.js with a six-breakpoint responsive system: 460 / 510 / 678 / 796 / 1050 / 1176px. This unusually granular breakpoint set suggests careful adaptation of a fixed-width Windows-style layout to fluid screen widths — each breakpoint likely adjusts column counts or element sizes to maintain the gridded, window-pane feel.

Footer padding is `16px 0px` — compact, like a taskbar. No section-level padding data suggests spacing is handled within components directly.

No max-width declaration at the body level; the Windows desktop metaphor extends edge-to-edge.

## 6. Depth & Elevation

Zero box-shadows. All elevation is achieved through the Windows 3D border technique:

**Raised element:** Top and left borders `rgb(254, 254, 254)` (light), bottom and right borders `rgb(132, 133, 132)` (dark). Simulates light coming from top-left.

**Sunken element:** Reverse the border assignment. Top and left go dark, bottom and right go light.

This technique creates physically accurate simulated 3D depth using only 2 CSS properties. The system requires no `box-shadow`, no `filter`, no opacity layering — just four border values.

## 7. Do's and Don'ts

**Do**
- Use `rgb(207, 207, 207)` for the page body; this specific grey is the Windows 95 desktop
- Apply the four-sided asymmetric border system for all raised/sunken elements
- Use `ms_sans_serif` for all UI text; `Arial` only for H1 display text
- Keep border-radius at zero — rounded corners break the period aesthetic
- Use the gold/amber for featured highlights; the teal footer as a chrome separator

**Don't**
- Add box-shadows — the bevel system is the elevation mechanism
- Introduce smooth gradients or blur effects; these are anachronistic
- Use modern typefaces alongside the Windows fonts
- Apply hover color transitions — the interaction model is border-state-based
- Add CSS custom properties or design tokens; the design intentionally has none

## 8. Responsive Behavior

Six breakpoints (460 / 510 / 678 / 796 / 1050 / 1176px) allow careful step-down of the Windows-grid aesthetic across screen sizes. At mobile widths, the design likely collapses to a single column while maintaining the grey-and-bevel visual language. The font sizes (16px body, 40px H1) hold across breakpoints — legibility at small sizes is a feature, not a problem, for the `ms_sans_serif` bitmap-style rendering.

## 9. Agent Prompt Guide

> Build a UI in the style of expensive.toys: Windows 95 aesthetic. Page body is `rgb(207, 207, 207)` flat grey. All elements use asymmetric four-sided borders for 3D bevel effect — top/left borders `rgb(254, 254, 254)` (raised light) and bottom/right `rgb(132, 133, 132)` (raised shadow). Font is `ms_sans_serif` at 16px for body, `Arial` at 40px/700 for H1. Zero border-radius everywhere. Gold `rgb(222, 173, 37)` for featured elements. Teal `rgb(137, 176, 168)` for footer. No box-shadows, no gradients, no CSS custom properties. Pure Windows 3.1–95 reconstruction in a modern stack.

---

*Generated by Sparkbites — extracted from live CSS analysis*
