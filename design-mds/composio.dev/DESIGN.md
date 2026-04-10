# composio.dev — Design System

## 1. Visual Theme & Atmosphere

composio.dev is a developer-tools landing page with an ambitious visual split personality: a pure white main content area anchored by a dark, almost theatrical hero section. The header and above-fold live in near-black territory (`rgb(15, 15, 15)` footer, dark backgrounds throughout), while the body transitions to white for documentation-style content. This creates a dramatic first impression that resolves into a clean, readable product page.

The design personality is **developer-confident** — it speaks the language of terminals and code. Section labels use JetBrains Mono in uppercase with wide tracking, signaling to developers that this is their native environment. The main display typeface is ABC Diatype, a geometric sans with character, used for the hero at an oversized 64px. The combination communicates: built by developers, designed with intention.

Unique theatrical details — macOS-style window chrome (red/yellow/green traffic light dots), a warm tan/sandstone accent (`rgb(196, 149, 106)`), and electric-blue interactive elements — separate composio.dev from generic SaaS templates.

---

## 2. Color Palette & Roles

**Structural**:
- Body/light canvas: `oklch(100% 0 0)` — pure white
- Primary text: `oklch(14.5% 0 0)` — near-black
- Border / input: `oklch(92.2% 0 0)` — light grey
- Muted foreground: `oklch(55.6% 0 0)` — medium grey
- Footer background: `rgb(15, 15, 15)` — very dark, near black

**Surface stack** (light to dark):
- `rgb(255, 255, 255)` — base white
- `rgb(246, 246, 246)` — subtle off-white
- `rgb(232, 232, 232)` — inactive surface
- `rgb(42, 42, 42)` — dark card (chat bubble, code block)
- `rgb(30, 30, 30)` — panel background
- `rgb(26, 26, 26)` — elevated dark panel
- `rgb(20, 20, 20)` — deep dark
- `rgb(15, 15, 15)` — footer / deepest surface

**Accent / interactive**:
- Primary blue: `rgba(0, 137, 255, 0.08)` background + `rgb(0, 137, 255)` border — ghost button treatment
- Cyan variant: `rgba(0, 255, 255, 0.12)` + `rgb(0, 150, 255)` — alternate interactive element
- Tan/sandstone: `rgb(196, 149, 106)` — decorative warm accent, chat avatar or illustration element
- Header text on dark: `rgb(255, 255, 255)`
- Section labels (H2 on dark): `oklab(0.999994... / 0.6)` — white at 60% opacity

**Window chrome** (decorative):
- Red: `rgb(255, 95, 87)` — macOS close button
- Yellow: `rgb(254, 188, 46)` — macOS minimize button
- Green: `rgb(40, 200, 64)` — macOS maximize button

---

## 3. Typography Rules

The site runs a **dual-family system**: ABC Diatype for all display and prose, JetBrains Mono for section labels and code.

| Role | Typeface | Size | Weight | Notes |
|------|----------|------|--------|-------|
| H1 / Hero | ABC Diatype | 64px | 400 | 55.68px line height (0.87×) |
| H2 (section label) | JetBrains Mono | 14px | 400 | Uppercase, 0.7px tracking |
| H3 (card title) | ABC Diatype | 28px | 400 | 33.6px line height |
| Body | ABC Diatype | 16px | 400 | 24px line height |
| Buttons / links | ABC Diatype | 16px | 400 | Standard |
| Code inline | JetBrains Mono | 11px | 400 | 17.6px line height |
| Code block | JetBrains Mono | 9px | 400 | Very compact |

Key rules:
- H1 line height is **subtighter than the cap height** (55.68/64 = 0.87) — an intentional display typography choice that creates a tightly packed headline
- Section labels (H2) are uppercase monospaced — this is the only use of uppercase on the site
- ABC Diatype at weight 400 throughout — no weight variation, scale and typeface switching carry all hierarchy
- JetBrains Mono's 0.7px tracking on section labels is a subtle but important detail that opens up the monospace for better readability at display sizes

---

## 4. Component Stylings

**Navigation (dark)**: Transparent background on dark, white text, 8px padding. Links appear without visible hover states (none detected in interactive states).

**Ghost buttons**: `rgba(0, 137, 255, 0.08)` fill with `rgb(0, 137, 255)` border — a frosted-glass effect in blue. Rounded at `--radius: 0.625rem` (10px).

**Terminal/code window**: The macOS window chrome (traffic light dots) sits atop a dark surface (`rgb(26, 26, 26)`) — a decorative container mimicking a code editor or terminal. Code blocks inside use JetBrains Mono at 9px.

**Chat interface mockup**: Uses dark surfaces (`rgb(42, 42, 42)`) for message bubbles, the tan accent (`rgb(196, 149, 106)`) for one participant's avatar/indicator.

**Shadows**:
- Large: `rgba(0,0,0,0.25) 0px 25px 50px -12px` — dramatic depth for hero cards
- Medium: `rgba(0,0,0,0.5) 0px 8px 32px` — dark cards, high opacity
- Flat offset: `rgba(0,0,0,0.15) 4px 4px 0px 0px` — retro/constructive offset shadow

**Border radius**: Uniformly 4px everywhere (from CSS data) — notably small, creating crisp, sharp-cornered elements. The `--radius: 0.625rem` token suggests some shadcn components may use 10px, but the dominant extracted value is 4px.

---

## 5. Layout Principles

- **No breakpoints detected** in CSS data — possibly uses container queries or Tailwind's arbitrary values for responsive behavior
- Header is compact: `padding: 8px` — minimal nav bar
- Main and section elements have `padding: 0px` — spacing entirely managed by child utilities
- The above-fold dark-to-light transition is achieved through section background colors, not the page canvas
- Content density is high in the dark hero area; the light content section is more spacious

---

## 6. Depth & Elevation

composio.dev uses the most complex elevation system in this collection:

**Light side** (content area):
- White base → `rgb(246,246,246)` off-white → `rgb(232,232,232)` inactive
- Shadows: large spread `0px 25px 50px -12px` for feature cards

**Dark side** (hero/footer):
- Four-step dark scale: `rgb(30)` → `rgb(26)` → `rgb(20)` → `rgb(15)` at the deepest
- Dark card shadows: `rgba(0,0,0,0.5) 0px 8px 32px` — high opacity creates dramatic lift

**Offset shadow**: `rgba(0,0,0,0.15) 4px 4px 0px 0px` — a flat constructivist offset used on specific decorative elements, adding a retro feel.

---

## 7. Do's and Don'ts

**Do:**
- Use ABC Diatype at 64px with tight line-height (0.87×) for hero display
- Use JetBrains Mono uppercase with 0.7px tracking for section labels
- Maintain the dark-hero / light-content two-zone structure
- Use `rgba(0, 137, 255, 0.08)` ghost buttons with solid blue border
- Include the macOS window chrome as a decorative element on code/terminal mockups
- Apply the tan accent `rgb(196, 149, 106)` sparingly as a warm contrast element

**Don't:**
- Break the dual typeface system — no third face
- Increase font weights above 400 — scale and typeface variation carry hierarchy
- Use saturated colors outside the defined blue accents and traffic light dots
- Use large border radii — keep corners at 4–10px, not pill-shaped
- Use shadows smaller than 8px spread on dark surfaces — they need weight

---

## 8. Responsive Behavior

No breakpoints were detected in the CSS extraction, which may indicate:
- The site uses Tailwind's inline responsive utilities without generating media query declarations at the root level
- Or container queries are used for the component-level adaptation

From structural inference:
- The dark hero section likely goes full-width/full-viewport on all sizes
- The terminal/code mockup probably collapses or scrolls horizontally on mobile
- Navigation bar likely compresses with a hamburger menu below ~768px

---

## 9. Agent Prompt Guide

When recreating or referencing composio.dev:

> "Design a developer-tools landing page with a dark hero (`rgb(15,15,15)` → `rgb(26,26,26)` surface stack) transitioning to a pure white content area. Display: ABC Diatype 64px/400 at 0.87× line height. Section labels: JetBrains Mono 14px uppercase/0.7px tracking. Both typefaces at weight 400 only. Ghost buttons: `rgba(0,137,255,0.08)` fill + `rgb(0,137,255)` border. Decorative macOS chrome dots (red/yellow/green). Warm tan accent `rgb(196,149,106)`. 4px border radius. Two shadow types: large dark-side spread (`rgba(0,0,0,0.5) 0px 8px 32px`) and flat constructivist offset (`4px 4px 0px 0px`)."

---

*Generated by Sparkbites — extracted from live CSS analysis*
