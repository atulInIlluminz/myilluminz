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
