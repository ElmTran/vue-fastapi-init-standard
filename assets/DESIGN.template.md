# Minimal Tool Design System

## 1. Visual Theme & Atmosphere

This product should feel like a calm personal tool, not a marketing site or a brand showcase. The interface is quiet, lightweight, and text-first. Visual hierarchy should come from spacing, alignment, typography, and a small number of neutral surfaces rather than oversized headlines, decorative gradients, or heavy chrome.

The reference temperament is close to a thoughtfully designed blog or note-taking app:

- restrained
- readable
- practical
- low-noise
- slightly warm rather than cold

The UI should help the user focus on tasks such as creating profiles, running interview sessions, and reviewing feedback. It should never compete with that content.

**Key characteristics**
- Soft warm page background instead of stark white
- Small-to-medium typography with strong readability
- Very light borders, used sparingly
- One muted accent color only
- Minimal shadows
- Generous whitespace
- Motion that is subtle and functional

## 2. Color Palette & Roles

### Primary surfaces
- **Page Background**: `#f5f1ea`
- **Raised Surface**: `rgba(255, 255, 255, 0.78)`
- **Strong Surface**: `rgba(255, 255, 255, 0.92)`

### Text
- **Primary Text**: `#171413`
- **Secondary Text**: `rgba(23, 20, 19, 0.72)`
- **Muted Text**: `rgba(23, 20, 19, 0.56)`

### Lines & Structure
- **Soft Border**: `rgba(18, 18, 18, 0.08)`
- **Standard Border**: `rgba(18, 18, 18, 0.14)`
- **Strong Border**: `rgba(18, 18, 18, 0.22)`

### Accent
- **Accent**: `#7a1f32`

Use the accent only for:
- links
- focus rings
- active indicators
- very small data highlights

Do not use the accent as a large background fill.

## 3. Typography Rules

### Font family
- **Body / UI**: `Inter, Segoe UI, Helvetica, Arial, sans-serif`
- **Optional Display / Editorial**: `Iowan Old Style, Palatino Linotype, Book Antiqua, Georgia, serif`
- **Code**: `SFMono-Regular, Consolas, Liberation Mono, Menlo, monospace`

### Typography hierarchy

| Role | Size | Weight | Line Height | Notes |
|------|------|--------|-------------|-------|
| Page Title | 28px-36px | 600 | 1.2 | Use sparingly |
| Section Title | 18px-22px | 600 | 1.3 | Default section heading |
| Card Title | 16px-18px | 600 | 1.35 | Most frequent heading size |
| Body | 14px-16px | 400 | 1.65-1.8 | Default reading size |
| Meta / Label | 12px-13px | 500 | 1.5 | Uppercase allowed only when useful |
| Small | 12px | 400 | 1.5 | Secondary details |

### Principles
- Prefer sans-serif for almost all UI text.
- Serif is optional and should be rare. If used, keep it limited to a few page titles or editorial moments.
- Avoid oversized hero typography.
- Avoid dense negative letter spacing.
- Let spacing create hierarchy before increasing font size.

## 4. Component Styling

### Buttons

**Primary**
- Dark text-on-dark fill or dark accent fill
- Medium height
- Rounded pill or soft rounded rectangle
- No glossy or dramatic treatment

**Secondary**
- Usually text-only or lightly outlined
- Border should be faint
- Hover should feel like a small state shift, not a visual transformation

### Cards & Containers
- Many sections can stay borderless
- When containment is needed, prefer a very light border
- Standard card radius: `10px` to `14px`
- Larger panels can use `16px`
- Shadows should be minimal or absent

### Inputs
- Clean, simple rectangles with soft radius
- Light border by default
- Stronger border or soft ring on focus
- No tinted backgrounds unless needed for hierarchy

### Navigation
- Compact
- Quiet
- Text-led
- Sticky is acceptable if it stays visually light

## 5. Layout Principles

### Overall structure
- Design like a tool dashboard or writing interface, not a landing page
- Keep the user near the task immediately
- Reduce decorative top matter
- Prefer direct content entry over dramatic hero sections

### Spacing
- Base spacing unit: `8px`
- Typical gaps: `8px`, `12px`, `16px`, `20px`, `24px`, `32px`
- Use whitespace deliberately to separate groups

### Containers
- Keep content width readable
- Avoid very wide full-bleed compositions unless they improve utility
- Prefer simple one-column or practical two-column layouts

## 6. Depth & Elevation

Depth should be subtle.

Preferred cues:
- background contrast
- whitespace
- thin borders
- slight hover background change

Avoid:
- large shadows
- thick outlines
- layered gradients
- glassmorphism-heavy effects

## 7. Motion

Motion should support orientation, not spectacle.

Recommended:
- page transition: gentle fade + 4px to 8px vertical movement
- hover: minor color or background change
- card hover: at most `translateY(-1px)` or `-2px`
- reveal animations: only if very subtle and not everywhere

Avoid:
- blur-heavy transitions
- scale-heavy transitions
- parallax
- decorative looping animations

## 8. Do's and Don'ts

### Do
- Keep titles modest in scale
- Use fewer borders, not more
- Use one accent color consistently
- Favor readable text blocks and calm spacing
- Make the product feel like a dependable utility
- Preserve mobile readability and compactness

### Don't
- Don't build a marketing-style hero
- Don't use oversized typography to force emphasis
- Don't stack many bordered cards inside many bordered cards unless structure really requires it
- Don't introduce multiple accent colors
- Don't rely on gradients or dark hero bands as a visual identity shortcut
- Don't over-animate route or panel transitions

## 9. Agent Prompt Guide

### Quick style reference
- "Use a calm, text-first tool UI."
- "Keep typography modest and readable."
- "Prefer light borders and soft warm neutrals."
- "Use one muted accent color only."
- "Avoid oversized hero sections and decorative gradients."

### Example component prompts
- "Design a profile list as a quiet utility view with small headings, muted metadata, and only light row separators."
- "Create a form with 14-16px body text, soft 12px radii, and very light borders."
- "Build a summary panel that feels like a note-taking interface rather than a product marketing card."
- "Add a page transition with only a light fade and small upward motion."

### Iteration guide
1. Remove visual noise before adding decoration.
2. Reduce font size before reducing content density.
3. Use spacing and alignment to solve hierarchy.
4. Add borders only where grouping is unclear without them.
5. Keep motion barely noticeable.
