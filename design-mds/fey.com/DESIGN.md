# fey.com — Design Reference

## 1. Visual Theme & Atmosphere

Fey is a personal finance app with a design language that speaks to design-literate early adopters. The dark canvas (`#000000`) creates an immersive, premium feel reminiscent of native macOS dark interfaces. **Calibre** — a sharp, confident grotesque — is used exclusively across all type, giving the site a unified, controlled voice.

The color palette is rich and data-informed: coral/salmon reds for alerts, muted green for positive values, peach/amber for categories, bright blue for links and actions. This is the visual language of a financial dashboard translated to a marketing site — functional and evocative simultaneously.

## 2. Color Palette & Roles

| Role | Value | Notes |
|------|-------|-------|
| Background | `rgb(0, 0, 0)` | Pure black — deep dark mode |
| Body text | `rgb(255, 255, 255)` | Pure white |
| H1 text | `rgba(255,255,255,0.047)` | Near-invisible — display element only |
| H2 text | `rgba(255,255,255,0.5)` | 50% opacity — secondary display |
| Link / Action | `rgb(71, 159, 250)` | Bright blue |
| H3 / Positive | `rgb(255, 161, 108)` | Peach/salmon — category labels |
| CTA button | `rgb(230, 230, 230)` | Light gray pill |
| Data green | `rgb(78, 190, 150)` | 16% opacity background for positive values |
| Alert red | `rgb(255, 92, 92)` | Negative values / destructive |
| Accent pink | `rgb(231, 94, 206)` | Category tag accent |

**What's absent:** No warm whites, no off-black surfaces — the darkness is absolute. The glowing/transparent white headline (`rgba(255,255,255,0.047)`) is a bold pattern unique to this design.

## 3. Typography Rules

Calibre is the sole typeface — a single-family system with weight as the only variable.

| Element | Family | Size | Weight | Notes |
|---------|--------|------|--------|-------|
| H1 | Calibre | 54px | 600 | 100% line height — near-invisible fill |
| H2 | Calibre | 26px | 600 | 100% line height — 50% white opacity |
| H3 | Calibre | 18px | 700 | 130% line height |
| H4 | Calibre | 14px | 600 | 100% line height |
| Body | Calibre | 16px | 400 | 140% line height |
| Para | Calibre | 14px | 600 | 136% line height |

No letter-spacing variation — Calibre's inherent metrics are trusted as-is. The opacity trick on H1 (4.7% white) creates the appearance of enormous ghost type used as a background texture.

## 4. Component Stylings

- **Primary button:** Pill-shaped (99px radius), light gray (`rgb(230,230,230)`) on black
- **Tags/badges:** Rounded pill (999px), using data colors as fills with colored text
- **Cards:** Subtle dark surface (`rgba(230,230,230,0.08)`) — barely distinguishable from black
- **Inset buttons:** Complex layered inset shadow for 3D glass effect
- **Data rows:** Color-coded backgrounds at low opacity for category types
- **Circular elements:** 50% border-radius for avatars/icons

## 5. Layout Principles

- 17 breakpoints — extremely granular responsive tuning from 340px to 1440px
- Next.js application with styled-components (sc- class prefixes)
- Dense breakpoint set suggests a highly polished mobile-to-desktop progression
- Dashboard-like layouts with data rows and sidebar panels
- Ease curves defined as custom properties (`--ease-in`, `--ease-out`, `--ease-in-out`)

## 6. Depth & Elevation

Fey uses the most sophisticated shadow system in this collection:
- **Glow shadows:** `rgba(255,255,255,0.25) 0px 0px 14px` — soft white aura on dark elements
- **Glass inset buttons:** Multiple inset shadows (white 50% top, black 85% bottom, complex layering)
- **Card depth:** `rgba(0,0,0,0.12) 0px 30px 16px` — deep drop shadow for overlapping cards
- **Bottom border line:** `rgba(0,0,0,0.85) 0px 1px 0px` — subtle separator

## 7. Do's and Don'ts

**Do:**
- Use pure black backgrounds — no dark grays, no gradients
- Apply opacity variants of white for text hierarchy (100%, 50%, 5%)
- Use Calibre exclusively — weight variation handles all hierarchy
- Apply the glass-inset shadow technique for premium interactive elements
- Use data colors (green, red, peach) at low opacity as row backgrounds

**Don't:**
- Add warm tones — the palette is cool and dark
- Use sharp-cornered buttons — the system is pill-shaped throughout
- Mix typefaces — Calibre alone is intentional
- Use flat surfaces — depth through glows and inset shadows is core to the aesthetic

## 8. Responsive Behavior

- 17 breakpoints handle every device scenario from 340px to 1440px
- Dashboard panels stack vertically at mobile
- Typography scales smoothly — Calibre's metrics hold at all sizes
- Data rows and tables adapt to scrollable horizontal layouts on mobile

## 9. Agent Prompt Guide

> "Design in the style of fey.com: pure black canvas, Calibre grotesque exclusively at 600 weight for display. White text with opacity variants — 100% for body, 50% for secondary heads, 5% for ghost hero type. Data-colored badges (green, red, peach) at low opacity. Pill-shaped buttons (99px radius). Glass inset shadows for interactive elements. White glow aura shadows. No rounded corners below 4px except pills."

---

*Generated by Sparkbites — extracted from live CSS analysis*
