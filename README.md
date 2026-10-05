# illuminz – Motion Graphics & Storyboarding page

Responsive, animated HTML/CSS/JS build of the Figma frame
"Motion Graphics & Storyboarding" (file `CaqZS7uG0azSppZmNogWj1`, node `11687:23265`).

Open `index.html` in a browser. No build step or dependencies.

| File | Purpose |
|---|---|
| `index.html` | Semantic markup for every section |
| `styles.css` | Mobile-first styles, design tokens, animations |
| `script.js` | Menu, typing effect, scroll reveals, hero parallax, logo marquee |
| `assets/` | Images exported from the Figma file |

## Animations
- **Hero:** text slides in on load, "mot" types out to "motion" and back, 3D shapes float and follow the mouse.
- **Dark section:** "inform" / "connect" wipe in with an underline sweep; timeline clips slide along their tracks while a playhead scrubs across.
- **Service cards:** heading, copy, tags and illustration reveal in sequence on scroll.
- **Tools:** icons bob gently. **Why It Works:** pills fade up in sequence and lift on hover.
- **CTA:** background slowly drifts. **Footer:** "We're Hiring" pulses; partner logos scroll as a marquee on smaller screens.
- Everything turns off for visitors with *reduce motion* enabled.

## Fonts
The design uses **Graphik** (commercial). If you have a licence, add it with `@font-face` and it will be used
automatically; otherwise the page falls back to Inter. Tool labels use "Metal" in Figma, with Instrument Serif as the fallback.

## Breakpoints
640px (badge shows), 900px (service text goes two-column), 1024px (full nav), 1100px (4 pills, 4-column footer).

---

# Digital Transformation page

`digital-transformation/index.html`, built from the copy in *Digital Transformation (illuminz website).docx*.
It reuses `../styles.css` (tokens, header, footer, reveals) and `../assets/`, plus its own `dt.css` and `dt.js`.

| Section | Scroll / layout idea |
|---|---|
| Hero | "Re-" words with a cycling pastel highlighter; modules (Cloud, AI, APIs, Data…) orbit a "digital core" |
| Mindset band | Tilted lilac marquee with the "mindset shift" lines |
| Transform Beyond Technology | Dark section; the statement lights up word by word as you scroll; 5 bento cards fill with pastel on hover; "IT project" gets struck through |
| Offerings | 6 sticky cards that stack and shrink as you scroll, each with its own animated illustration |
| Emerging tech | Bento grid with pointer-following spotlight and small animated visuals |
| Built for Every Vertical | Pinned section: scrolling down slides 7 industry cards sideways (swipe on mobile) |
| Process | A line draws down the page and lights up each step |
| Engagement models | Expanding panels (hover/click/focus) plus a Security & IP strip |
| Outcomes | KPI tiles with count-up numbers, filling bars and a "days → minutes" flip |
| CTA | Blue gradient with drifting pastel glows |

Reduced-motion users get a static version. Pinned and sticky effects only switch on when the viewport is large enough.
