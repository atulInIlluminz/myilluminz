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

---

# Accutive Security – Cryptography, HSM Discovery, Inventory & Assessment

`accutive-crypto-discovery/index.html` (slug `/cryptography-hsm-discovery-inventory-assessment`), built from the
*Entrust Cryptography Discovery Page Wireframe* copy deck, with branding from the Accutive Figma file
(`9Pjpz90rOHQIFrNcmZLzBK`, "Homepage Final", 24 Sep). Self-contained: `acs.css`, `acs.js`, `assets/`. No build step.

**Brand tokens (from Figma):** Poppins; purple `#2d097d`, light purple `#7f5fd9`, button `#6943c7`, card lavender `#f8f8fd`,
heading `#202020`, paragraph `#4b4160`, hero highlight `#14adff`, footer `#150635`. The header, footer, pill buttons,
glass cards and CTA gradient match the homepage components. The logos were exported from the Figma file.

| Section | Creative treatment |
|---|---|
| Hero | The four verbs light up in turn; a radar sweep "discovers" crypto assets (risky ones glow amber) and counts them |
| Visibility gap | Ownership map (3 teams, no central owner, warning flags, stale spreadsheet); 41% / 38% ring stats count up |
| What discovery covers | 6 domains as accessible tabs; a scan console re-runs and reveals what gets discovered |
| Four clocks | 4 parallel glass cards, each with a ticking dial |
| Remediation | Terminal-style roadmap: findings get struck through and resolved one by one |
| Automation | 3 parallel cards on a looping dotted track |
| Platform | Isometric Entrust layer stack flanked by the 6 benefits; module list |
| Why Accutive | "2009" fills in on scroll; 3 credentials |
| Closing CTA | Figma CTA gradient with the "Every assessment includes" checklist |

Placeholder links (`#`) still need real URLs: the booking form, "View the full compliance timeline", the nav and the footer.
Reduced-motion users get a static version.
