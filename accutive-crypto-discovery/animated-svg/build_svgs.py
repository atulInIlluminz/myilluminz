"""Generate self-contained animated SVGs for the Accutive cryptography discovery page.

Each SVG embeds its fonts (Latin subset, base64 woff2) and animates with CSS keyframes /
SMIL, so it plays in browsers, <img> tags, Webflow and WordPress with no other files.

Usage: python3 build_svgs.py <font-dir>
  <font-dir> must contain Poppins-500/600/700.woff2 and JetBrainsMono-400.woff2.
"""
import base64
import math
import os
import sys

FONT_DIR = sys.argv[1]
OUT = os.path.dirname(os.path.abspath(__file__))

C = dict(purple="#2d097d", light="#7f5fd9", btn="#6943c7", cyan="#14adff", ink="#0c022a",
         pill="#1c094a", pillb="#d2c0ff", ok="#3ddc97", warn="#ffb547", danger="#ff5c7a",
         lav="#f8f8fd", para="#4b4160", night="#0d0430")


def font_face(family, weight, file):
    data = base64.b64encode(open(os.path.join(FONT_DIR, file), "rb").read()).decode()
    return ("@font-face{font-family:'%s';font-weight:%s;font-style:normal;"
            "src:url(data:font/woff2;base64,%s) format('woff2');}" % (family, weight, data))


FONTS = {
    "p500": font_face("Poppins", 500, "Poppins-500.woff2"),
    "p600": font_face("Poppins", 600, "Poppins-600.woff2"),
    "p700": font_face("Poppins", 700, "Poppins-700.woff2"),
    "mono": font_face("JetBrains Mono", 400, "JetBrainsMono-400.woff2"),
}
BASE_CSS = (".p{font-family:Poppins,system-ui,sans-serif}"
            ".m{font-family:'JetBrains Mono',ui-monospace,monospace}"
            "@media (prefers-reduced-motion:reduce){*{animation:none!important}}")


def svg(name, w, h, title, body, css, fonts):
    style = "".join(FONTS[f] for f in fonts) + BASE_CSS + css
    doc = ('<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d" '
           'role="img" aria-label="%s"><title>%s</title><style>%s</style>%s</svg>\n'
           % (w, h, w, h, title, title, style, body))
    open(os.path.join(OUT, name), "w").write(doc)
    print("%-32s %6.1f KB" % (name, len(doc) / 1024))


def text_w(s, size, mono=False):
    """Rough advance width so pills/labels can be sized without a layout engine."""
    return len(s) * size * (0.6 if mono else 0.58)


def pct(x):
    return "%.2f%%" % x


# ---------------------------------------------------------------- 1. hero headline
def headline():
    words = ["Discover.", "Assess.", "Remediate.", "Automate."]
    # x, y (baseline) and approx width at 54px Poppins SemiBold
    pos = [(0, 54), (270, 54), (0, 118), (0, 182)]
    widths = [252, 210, 300, 285]
    T = 7.2  # seconds for a full cycle (1.8s per word)
    css, body = [], []
    for i, (w, (x, y)) in enumerate(zip(words, pos)):
        a, b = i * 25, (i + 1) * 25
        css.append("@keyframes w%d{0%%,%s{fill:#fff}%s,%s{fill:%s}%s,100%%{fill:#fff}}"
                   % (i, pct(max(a - .01, 0)), pct(a + 2), pct(b - 2), C["cyan"], pct(b)))
        css.append(".w%d{animation:w%d %ss infinite}" % (i, i, T))
        css.append("@keyframes u%d{0%%,%s{transform:scaleX(0)}%s,%s{transform:scaleX(1)}%s,100%%{transform:scaleX(0)}}"
                   % (i, pct(max(a - .01, 0)), pct(a + 4), pct(b - 3), pct(b)))
        css.append(".u%d{transform-box:fill-box;transform-origin:left;animation:u%d %ss infinite}" % (i, i, T))
        body.append('<text class="p w%d" x="%d" y="%d" font-size="54" font-weight="600" letter-spacing="-1.6" fill="#fff">%s</text>'
                    % (i, x, y, w))
        body.append('<rect class="u%d" x="%d" y="%d" width="%d" height="3" rx="1.5" fill="url(#ug)"/>' % (i, x + 2, y + 8, widths[i] - 10))
    defs = ('<defs><linearGradient id="ug"><stop offset="0" stop-color="%s"/><stop offset="1" stop-color="%s"/></linearGradient></defs>'
            % (C["cyan"], C["light"]))
    svg("hero-headline.svg", 520, 200, "Discover. Assess. Remediate. Automate.",
        defs + "".join(body), "".join(css), ["p600"])


# ---------------------------------------------------------------- 2. discovery radar
ASSETS = [(20, 40, "TLS Certificates", 0), (62, 30, "Symmetric Keys", 0), (98, 42, "Hard-coded Secret", 1),
          (135, 30, "Internal CA", 0), (165, 42, "nShield HSM", 0), (205, 31, "RSA-1024", 1),
          (240, 43, "K8s Ingress", 0), (278, 32, "Self-signed Cert", 1), (312, 42, "Code Signing", 0),
          (350, 24, "Vault Tokens", 0)]


def radar():
    S, c, T = 520, 260, 6
    css, body = [], []
    defs = ('<defs><radialGradient id="bg" cx="50%" cy="35%" r="75%"><stop offset="0" stop-color="#3a2f7c"/>'
            '<stop offset=".5" stop-color="#1f1847"/><stop offset="1" stop-color="#030111"/></radialGradient>'
            '<linearGradient id="core" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#7f5fd9"/><stop offset="1" stop-color="#2d097d"/></linearGradient>'
            '<radialGradient id="sw" cx="0" cy="1" r="1"><stop offset="0" stop-color="#14adff" stop-opacity=".05"/><stop offset="1" stop-color="#14adff" stop-opacity=".35"/></radialGradient>'
            '<filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feDropShadow dx="0" dy="2" stdDeviation="4" flood-color="#5c36b2" flood-opacity=".9"/></filter></defs>')
    body.append('<rect width="%d" height="%d" rx="16" fill="url(#bg)"/>' % (S, S))
    for r, op, dash in [(235, .35, "4 8"), (175, .22, ""), (115, .18, "2 6")]:
        body.append('<circle cx="%d" cy="%d" r="%d" fill="none" stroke="#d2c0ff" stroke-opacity="%s"%s/>'
                    % (c, c, r, op, (' stroke-dasharray="%s"' % dash) if dash else ""))
    # sweep wedge: trailing 57deg behind a leading edge that starts pointing up
    R, a0 = 220, math.radians(-57)
    x0, y0 = c + R * math.sin(a0), c - R * math.cos(a0)
    body.append('<g><path d="M%d %d L%.1f %.1f A%d %d 0 0 1 %d %d Z" fill="#14adff" fill-opacity=".2"/>'
                '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="#14adff" stroke-opacity=".85" stroke-width="2"/>'
                '<animateTransform attributeName="transform" type="rotate" from="0 %d %d" to="360 %d %d" dur="%ss" repeatCount="indefinite"/></g>'
                % (c, c, x0, y0, R, R, c, c - R, c, c, c, c - R, c, c, c, c, T))
    # core hexagon
    pts = " ".join("%.1f,%.1f" % (c + 75 * math.cos(math.radians(60 * k - 90)), c + 75 * math.sin(math.radians(60 * k - 90))) for k in range(6))
    body.append('<polygon points="%s" fill="url(#core)" stroke="#d2c0ff"/>' % pts)
    # counter: one text per count, each visible in its time window
    times = sorted(a for a, *_ in ASSETS)
    for k in range(len(times) + 1):
        start = 0 if k == 0 else times[k - 1] / 360 * 100
        end = 100 if k == len(times) else times[k] / 360 * 100
        css.append("@keyframes n%d{0%%,%s{opacity:0}%s,%s{opacity:1}%s,100%%{opacity:0}}"
                   % (k, pct(max(start - .01, 0)), pct(start), pct(end - .01), pct(end)) if k else
                   "@keyframes n0{0%%,%s{opacity:1}%s,100%%{opacity:0}}" % (pct(end - .01), pct(end)))
        css.append(".n%d{animation:n%d %ss infinite}" % (k, k, T))
        body.append('<text class="p n%d" x="%d" y="%d" text-anchor="middle" font-size="26" font-weight="600" fill="#fff">%d</text>' % (k, c, c - 2, k))
    body.append('<text class="p" x="%d" y="%d" text-anchor="middle" font-size="10" font-weight="700" letter-spacing=".6" fill="#fff">ASSET TYPES FOUND</text>' % (c, c + 18))
    # pills: dim base + lit overlay that switches on when the beam passes
    for a, r, label, risk in ASSETS:
        w = text_w(label, 13) + 34
        rad, Rp = math.radians(a), r / 100 * S
        x = min(max(c + Rp * math.sin(rad) - w / 2, 12), S - w - 12)
        y = c - Rp * math.cos(rad) - 13
        on = a / 360 * 100
        k = "p%d" % a
        css.append("@keyframes %s{0%%,%s{opacity:0}%s,97%%{opacity:1}100%%{opacity:0}}" % (k, pct(on - .01), pct(on + .5)))
        dot = C["warn"] if risk else C["ok"]
        body.append('<g><rect x="%.1f" y="%.1f" width="%.1f" height="26" rx="13" fill="%s" fill-opacity=".7" stroke="#fff" stroke-opacity=".25"/>'
                    '<circle cx="%.1f" cy="%.1f" r="3.5" fill="#fff" fill-opacity=".3"/>'
                    '<text class="p" x="%.1f" y="%.1f" font-size="13" font-weight="500" fill="#fff" fill-opacity=".55">%s</text></g>'
                    % (x, y, w, C["pill"], x + 14, y + 13, x + 24, y + 17.5, label))
        body.append('<g style="animation:%s %ss infinite"><rect x="%.1f" y="%.1f" width="%.1f" height="26" rx="13" fill="%s" stroke="%s" filter="url(#glow)"/>'
                    '<circle cx="%.1f" cy="%.1f" r="3.5" fill="%s"/>'
                    '<text class="p" x="%.1f" y="%.1f" font-size="13" font-weight="500" fill="#fff">%s</text></g>'
                    % (k, T, x, y, w, C["pill"], C["pillb"], x + 14, y + 13, dot, x + 24, y + 17.5, label))
    body.append('<rect x="%d" y="%d" width="380" height="26" rx="13" fill="#0c022a" fill-opacity=".85" stroke="#d2c0ff" stroke-opacity=".3"/>' % (c - 190, S - 44))
    body.append('<text class="m" x="%d" y="%d" text-anchor="middle" font-size="11" fill="#cbb8ff">scan: cloud · on-prem · CI/CD · third-party</text>' % (c, S - 27))
    svg("discovery-radar.svg", S, S, "Cryptographic discovery radar", defs + "".join(body), "".join(css), ["p500", "p600", "p700", "mono"])


# ---------------------------------------------------------------- 3. stat rings
def ring(value, caption):
    T, circ = 6, 2 * math.pi * 40
    off = circ * (1 - value / 100)
    css = ("@keyframes fill{0%%,8%%{stroke-dashoffset:%.1f}38%%,88%%{stroke-dashoffset:%.1f}100%%{stroke-dashoffset:%.1f}}"
           ".bar{stroke-dasharray:%.1f;animation:fill %ss cubic-bezier(.22,.8,.2,1) infinite}"
           "@keyframes num{0%%,20%%{opacity:0}34%%,88%%{opacity:1}100%%{opacity:0}}.num{animation:num %ss infinite}"
           % (circ, off, circ, circ, T, T))
    lines, line = [], ""
    for word in caption.split():
        if text_w(line + " " + word, 14) > 216 and line:
            lines.append(line); line = word
        else:
            line = (line + " " + word).strip()
    lines.append(line)
    cap = "".join('<tspan x="22" dy="%d">%s</tspan>' % (0 if i == 0 else 20, l) for i, l in enumerate(lines))
    body = ('<defs><linearGradient id="rg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#2d097d"/><stop offset="1" stop-color="#7f5fd9"/></linearGradient></defs>'
            '<rect width="260" height="190" rx="14" fill="%s" stroke="#7f5fd9" stroke-opacity=".14"/>'
            '<circle cx="66" cy="66" r="40" fill="none" stroke="#2d097d" stroke-opacity=".08" stroke-width="8"/>'
            '<circle class="bar" cx="66" cy="66" r="40" fill="none" stroke="url(#rg)" stroke-width="8" stroke-linecap="round" transform="rotate(-90 66 66)"/>'
            '<text class="p num" x="66" y="74" text-anchor="middle" font-size="22" font-weight="600" fill="%s">%d%%</text>'
            '<text class="p" x="22" y="140" font-size="14" font-weight="500" fill="%s">%s</text>'
            % (C["lav"], C["purple"], value, C["para"], cap))
    svg("stat-ring-%d.svg" % value, 260, 190, "%d%% %s" % (value, caption), body, css, ["p500", "p600"])


# ---------------------------------------------------------------- 4. clock dial
def clock():
    body = ('<circle cx="32" cy="32" r="31" fill="%s" stroke="%s" stroke-width="2"/>'
            '<circle cx="32" cy="32" r="25" fill="none" stroke="#cbb8ff" stroke-opacity=".35" stroke-dasharray="3 3"/>'
            '<rect x="30.8" y="17" width="2.4" height="15" rx="1.2" fill="#fff">'
            '<animateTransform attributeName="transform" type="rotate" from="0 32 32" to="360 32 32" dur="48s" repeatCount="indefinite"/></rect>'
            '<rect x="30.8" y="10" width="2.4" height="22" rx="1.2" fill="%s">'
            '<animateTransform attributeName="transform" type="rotate" from="0 32 32" to="360 32 32" dur="4s" repeatCount="indefinite"/></rect>'
            '<circle cx="32" cy="32" r="3" fill="#fff"/>' % (C["ink"], C["light"], C["cyan"]))
    svg("clock-dial.svg", 64, 64, "Ticking readiness clock", body, "", [])


if __name__ == "__main__":
    headline()
    radar()
    ring(41, "name poor cryptographic visibility their top readiness barrier")
    ring(38, "are actively preparing for post-quantum")
    clock()
    import build_svgs_part2  # noqa: E402  (terminal, stack, track, flags, scanner)
    build_svgs_part2.run(svg, text_w, pct, C)
