# Animated SVGs: Cryptography Discovery page

Self-contained animated SVGs: fonts are embedded, and motion uses CSS keyframes / SMIL. They play in any browser,
in `<img>` tags, and in Webflow / WordPress. **Figma shows them as still images.** For motion in Figma, use the
prototype on page `15 - Crypto Discovery (Animated)` of the Accutive file.

| File | Animation | Loop |
|---|---|---|
| `hero-headline.svg` | Cyan highlight + underline steps through Discover / Assess / Remediate / Automate | 7.2s |
| `discovery-radar.svg` | Beam sweeps; asset pills light up as it passes (risky ones amber); counter climbs | 6s |
| `stat-ring-41.svg`, `stat-ring-38.svg` | Ring fills to the value, holds, resets | 6s |
| `warning-flags.svg` | Visibility-gap flags pulse | 4s |
| `discovery-scanner.svg` | Six domains scanned in turn; chips appear one by one | 24s |
| `clock-dial.svg` | Ticking readiness clock | 4s |
| `remediation-terminal.svg` | Findings struck through and resolved one by one, counter 0→5 | 8s |
| `automation-loop.svg` | Dot travels along the automation track | 5s |
| `platform-stack.svg` | Entrust platform layers float | 3.2s |

All of them stop moving for visitors with *reduce motion* turned on.

Regenerate with `python3 build_svgs.py <font-dir>`. `<font-dir>` must hold `Poppins-500/600/700.woff2` and
`JetBrainsMono-400.woff2` (Latin subset from Google Fonts).
