# wojtek.im — Design System

## 1. Visual Theme & Atmosphere

Wojtek.im is a personal portfolio built with the aesthetic vocabulary of a developer who designs — not a designer who codes. The canvas is pure black. The accent is a wide-gamut P3 mint-green (`color(display-p3 0 0.92 0.67)`) that sits outside sRGB's reach, making it feel more luminous on capable screens than any hex code could achieve. The overall mood is terminal-meets-refined: monospaced type for headlines, a geometric humanist for body, dark surfaces with surgical precision borders. This site is confident enough to have no decorative elements whatsoever — the typography and a single green accent carry everything.

Social platform colours (`--color-twitter: #1da1f2`, `--color-instagram: #e736ba`, `--color-farcaster: #9559ff`, `--color-friends: #ffa722`) appear as named tokens, suggesting links to external profiles rendered in their native brand colours.

---

## 2. Color Palette & Roles

### Foundation (Dark Mode)
| Role | Value | Usage |
|---|---|---|
| Canvas | `#000000` | Page background |
| Elevated surface | `#333333` | Cards, inset panels |
| Subtle muted | `#0f0f0f` | Button backgrounds (`--color-button`) |
| Border | `#262626` (`--color-border`) | All structural dividers |

### Text
| Role | Value | Usage |
|---|---|---|
| Primary | `#ffffff` | Headlines, primary content |
| Body | `#a8a8a8` (`--color-body`) | Body copy, descriptions |
| Dark body | `#545454` (`--color-body-dark`) | H2, supporting labels |
| Darker | `#333333` (`--color-body-darker`) | Tertiary text |

### Accent
| Role | Value | Usage |
|---|---|---|
| Signature green | `color(display-p3 0 0.92 0.67)` ≈ `#00eb9b` | Buttons, interactive links, focus rings — the only accent |
| Warning orange | `#fe8600` | Alerts, warnings |
| Visited purple | `#6e5aff` | Visited link state |

### Social Brand Tokens
- Friends amber: `#ffa722`
- Twitter blue: `#1da1f2`
- Instagram pink: `#e736ba`
- Peace yellow: `#fdc900`
- Farcaster purple: `#9559ff`

---

## 3. Typography Rules

Wojtek.im deploys a sharp two-font split: **Proto Mono** for all display and narrative text, **Basier Circle Regular** for all UI chrome.

| Selector | Font | Size | Weight | Line Height |
|---|---|---|---|---|
| H1 | Proto Mono | 24px | 400 | 32px |
| H2 | Proto Mono | 14px | 400 | 20px |
| H3 | Proto Mono | 14px | 400 | 20px |
| Paragraph | Proto Mono | 24px | 400 | 32px |
| Body | Basier Circle | 16px | 400 | 24px |
| Buttons/Links | Basier Circle | 16px | 400 | 24px |

The decision to use a monospaced face (Proto Mono) for headlines and body paragraphs is the site's defining typographic gesture. It creates a coding-notebook quality — precise, unhurried, deeply personal. Basier Circle handles UI interactions cleanly without competing. Notably, no bold weights appear anywhere: the entire site runs at weight 400, using size contrast and colour alone to create hierarchy.

---

## 4. Component Styling

**Interactive elements** use a distinctive hover mechanic: box-shadow transitions from `rgb(38,38,38) 0 0 0 1px` (subtle dark ring) to `color(display-p3 0 0.92 0.67) 0 0 0 2px` (wide-gamut green ring). The ring expands in both weight and colour saturation on hover — a single, elegant micro-interaction.

**Links with text-link-hover** use a skew transform on hover: `matrix(0.979, 0, -0.109, 1, 0, 0)` with a black background that grows from 0 to a 4px shadow box — creating a kinetic underline/highlight effect that italicises and backgrounds the text simultaneously.

**Border radii**: `6px`, `8px`, `12px`, `16px` — no sharp corners, no pill shapes. Medium-rounded throughout.

**Shadows** are structural ring-style, not ambient drops. Three shadow values in use, all zero-blur ring compositions.

---

## 5. Layout Principles

The main content area has an unusual fixed-margin approach: `margin: 0 292px` — a hard 292px gutter on both sides, creating a tight centered column. Combined with `padding: 24px 24px 48px`, content sits in a deliberate, narrow reading lane. This suggests a single-column essay/portfolio layout reminiscent of personal writing sites. No CSS grid or flex gaps are exposed at the macro level; layout appears to be sequential vertical flow.

---

## 6. Depth & Elevation

Depth is entirely achieved through ring shadows and colour contrast, not ambient elevation. Two levels exist:
1. **Base** — black canvas (`#000000`)
2. **Raised** — `#333333` card surfaces

The green ring appears on interaction, creating a third visual plane that signals "active." There are no blurred drop shadows anywhere; the aesthetic is deliberately flat with sharp-edged divisions.

---

## 7. Do's and Don'ts

**Do:**
- Use `color(display-p3 0 0.92 0.67)` for the accent — the wide-gamut P3 value is intentional and should not be substituted with a hex fallback on capable displays
- Apply the skew-transform hover to inline text links (the site's most distinctive micro-interaction)
- Keep all weights at 400 — hierarchy comes from font-family switching and size, never weight
- Respect the `#262626` border token for all dividers; thicker or lighter borders break the system

**Don't:**
- Use Proto Mono below 14px — it becomes illegible at small sizes
- Introduce any warm or light background surfaces; the entire system lives on black/very-dark
- Add ambient drop shadows — ring shadows only
- Deviate from the single green accent; the restraint is the point

---

## 8. Responsive Behavior

No explicit breakpoint data was captured. The fixed 292px side margins suggest a primarily desktop-targeted layout that would need explicit mobile overrides — likely collapsing to standard 24px gutters below ~768px. The monospaced text at 24px/32px would reflow naturally on narrower viewports.

---

## 9. Agent Prompt Guide

> Build a personal portfolio page in the style of wojtek.im. Pure black background (`#000000`). Primary text white, body copy in `#a8a8a8`. Single accent: `color(display-p3 0 0.92 0.67)` (wide-gamut mint green). Headlines use a monospaced font (Proto Mono or similar) at 24px/400 weight with 32px line-height. Body UI uses a geometric humanist (Basier Circle or similar) at 16px/400. All interactive elements animate from a `#262626` 1px ring to a 2px green ring on hover. Use a narrow centered column (max ~600px). No bold weights, no drop shadows, no decorative elements. Social links rendered in their respective brand colours.

---

*Generated by Sparkbites — extracted from live CSS analysis*
