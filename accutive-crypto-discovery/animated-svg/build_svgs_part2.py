"""Second half of the animated SVG set (imported by build_svgs.py)."""


def run(svg, text_w, pct, C):
    terminal(svg, pct, C)
    stack(svg, C)
    track(svg, C)
    flags(svg, text_w, C)
    scanner(svg, text_w, pct, C)


# ---------------------------------------------------------------- 5. remediation terminal
def terminal(svg, pct, C):
    rows = [("Legacy CA still issuing certs", "migrated to new CA hierarchy", "migrate CA"),
            ("API key exposed in pipeline config", "rotated &amp; moved to vault", "rotate key"),
            ("RSA-1024 / SHA-1 in billing app", "replaced with approved algorithms", "replace algorithm"),
            ("Orphaned shadow CA, no owner", "owner assigned, policy enforced", "governance"),
            ("Manual renewals, no alerting", "controls in place, gap closed", "controls")]
    W, T = 560, 8
    css, body = [], []
    body.append('<rect width="%d" height="420" rx="20" fill="%s" stroke="#a787ff" stroke-opacity=".3"/>' % (W, C["ink"]))
    body.append('<path d="M20 0h%d a20 20 0 0 1 20 20v28H0V20A20 20 0 0 1 20 0z" fill="#160744"/>' % (W - 40))
    for i, col in enumerate(["#ff5c7a", "#ffb547", "#3ddc97"]):
        body.append('<circle cx="%d" cy="24" r="5" fill="%s"/>' % (25 + i * 18, col))
    body.append('<text class="m" x="84" y="28" font-size="12" fill="#a99bd6">remediation-roadmap.run</text>')
    for i, (frm, to, lbl) in enumerate(rows):
        y = 64 + i * 64
        on = 10 + i * 12  # % of the loop at which this finding resolves
        css.append("@keyframes d%d{0%%,%s{opacity:0}%s,94%%{opacity:1}100%%{opacity:0}}" % (i, pct(on - .01), pct(on + 3)))
        css.append("@keyframes x%d{0%%,%s{opacity:1}%s,94%%{opacity:0}100%%{opacity:1}}" % (i, pct(on - .01), pct(on + 3)))
        css.append("@keyframes s%d{0%%,%s{transform:scaleX(0)}%s,94%%{transform:scaleX(1)}100%%{transform:scaleX(0)}}" % (i, pct(on - .01), pct(on + 4)))
        lw = len(lbl) * 6.6 + 16
        fw = len(frm) * 7.8
        # pending state
        body.append('<g style="animation:x%d %ss infinite"><circle cx="29" cy="%d" r="9" fill="#ff5c7a"/>'
                    '<text class="m" x="29" y="%d" text-anchor="middle" font-size="11" font-weight="700" fill="#fff">!</text>'
                    '<text class="m" x="52" y="%d" font-size="13" fill="#ff9bb0">%s</text>'
                    '<rect x="%d" y="%d" width="%.0f" height="20" rx="6" fill="#ff5c7a" fill-opacity=".15"/>'
                    '<text class="m" x="%.0f" y="%d" font-size="11" fill="#ff9bb0">%s</text></g>'
                    % (i, T, y + 19, y + 23, y + 23, frm, W - 20 - lw, y + 8, lw, W - 20 - lw + 8, y + 22, lbl))
        # resolved state
        body.append('<g style="animation:d%d %ss infinite"><circle cx="29" cy="%d" r="9" fill="#3ddc97"/>'
                    '<text class="m" x="29" y="%d" text-anchor="middle" font-size="11" fill="#fff">&#10003;</text>'
                    '<text class="m" x="52" y="%d" font-size="13" fill="#8f86b3">%s</text>'
                    '<text class="m" x="52" y="%d" font-size="13" fill="#3ddc97">&#8627; %s</text>'
                    '<rect x="%d" y="%d" width="%.0f" height="20" rx="6" fill="#3ddc97" fill-opacity=".15"/>'
                    '<text class="m" x="%.0f" y="%d" font-size="11" fill="#3ddc97">%s</text></g>'
                    % (i, T, y + 19, y + 23, y + 23, frm, y + 43, to, W - 20 - lw, y + 8, lw, W - 20 - lw + 8, y + 22, lbl))
        body.append('<rect x="52" y="%d" width="%.0f" height="1.6" fill="#8f86b3" style="transform-box:fill-box;transform-origin:left;animation:s%d %ss infinite"/>'
                    % (y + 18, fw, i, T))
        if i < len(rows) - 1:
            body.append('<line x1="20" x2="%d" y1="%d" y2="%d" stroke="#d2c0ff" stroke-opacity=".14" stroke-dasharray="4 4"/>' % (W - 20, y + 60, y + 60))
    body.append('<path d="M0 376h%d v24a20 20 0 0 1-20 20H20A20 20 0 0 1 0 400z" fill="#160744"/>' % W)
    body.append('<text class="m" x="20" y="402" font-size="12" fill="#a99bd6">findings resolved</text>')
    for k in range(6):
        start = 0 if k == 0 else 10 + (k - 1) * 12
        end = 94 if k == 5 else 10 + k * 12
        if k == 0:
            css.append("@keyframes c0{0%%,%s{opacity:1}%s,94%%{opacity:0}100%%{opacity:1}}" % (pct(end - .01), pct(end)))
        else:
            css.append("@keyframes c%d{0%%,%s{opacity:0}%s,%s{opacity:1}%s,100%%{opacity:0}}" % (k, pct(start - .01), pct(start), pct(end - .01), pct(end)))
        body.append('<text class="m" x="%d" y="402" text-anchor="end" font-size="12" fill="#3ddc97" style="animation:c%d %ss infinite">%d / 5</text>' % (W - 20, k, T, k))
    svg("remediation-terminal.svg", W, 420, "Remediation roadmap: findings resolved one by one", "".join(body), "".join(css), ["mono"])


# ---------------------------------------------------------------- 6. platform stack
def stack(svg, C):
    layers = [("PKI &amp; CLM", "#5b3bd0", "#2d097d"), ("KEYS &amp; SECRETS", "#6943c7", "#3b1797"),
              ("COMPLIANCE", "#7f5fd9", "#4b22b0"), ("HSM ROOT OF TRUST", "#a07bff", "#5b2fd1")]
    defs, body = [], ['<rect width="300" height="380" rx="16" fill="%s"/>' % C["night"]]
    css = "@keyframes fl{0%,100%{transform:translateY(0)}50%{transform:translateY(-8px)}}"
    for i, (label, a, b) in enumerate(layers):
        defs.append('<linearGradient id="g%d" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="%s"/><stop offset="1" stop-color="%s"/></linearGradient>' % (i, a, b))
        y = 20 + i * 70
        body.append('<g style="animation:fl 3.2s ease-in-out %.1fs infinite"><polygon points="150,%d 273,%d 150,%d 27,%d" fill="url(#g%d)"/>'
                    '<text class="p" x="150" y="%d" text-anchor="middle" font-size="11" font-weight="700" letter-spacing=".66" fill="#fff">%s</text></g>'
                    % (-i * 0.8, y, y + 51, y + 102, y + 51, i, y + 55, label))
    body.append('<rect x="88" y="336" width="124" height="26" rx="6" fill="%s"/>'
                '<text class="p" x="150" y="353" text-anchor="middle" font-size="11" font-weight="700" letter-spacing=".66" fill="#fff">ENTRUST PLATFORM</text>' % C["btn"])
    svg("platform-stack.svg", 300, 380, "Entrust platform layer stack", "<defs>%s</defs>%s" % ("".join(defs), "".join(body)), css, ["p700"])


# ---------------------------------------------------------------- 7. automation track
def track(svg, C):
    W = 900
    body = ('<line x1="0" x2="%d" y1="12" y2="12" stroke="%s" stroke-opacity=".45" stroke-width="2" stroke-dasharray="8 8"/>'
            '<g><circle cx="0" cy="12" r="11" fill="%s" fill-opacity=".2"/><circle cx="0" cy="12" r="5" fill="%s"/>'
            '<animateTransform attributeName="transform" type="translate" from="0 0" to="%d 0" dur="5s" repeatCount="indefinite"/></g>'
            % (W, C["light"], C["light"], C["light"], W))
    svg("automation-loop.svg", W, 24, "Continuous automation loop", body, "", [])


# ---------------------------------------------------------------- 8. warning flags
def flags(svg, text_w, C):
    labels = ["self-signed", "forgotten CA", "hard-coded secret", "SHA-1"]
    css = ("@keyframes bl{0%,100%{opacity:1;transform:translateY(0)}50%{opacity:.55;transform:translateY(-4px)}}"
           ".f{animation:bl 4s ease-in-out infinite}")
    body, x = [], 4
    for i, l in enumerate(labels):
        w = text_w(l, 11, True) + 38
        body.append('<g class="f" style="animation-delay:-%ds"><rect x="%.0f" y="10" width="%.0f" height="24" rx="6" fill="#fff" stroke="#ff5c7a" stroke-opacity=".4"/>'
                    '<circle cx="%.0f" cy="22" r="7" fill="#ff5c7a"/><text class="p" x="%.0f" y="26" text-anchor="middle" font-size="10" font-weight="700" fill="#fff">!</text>'
                    '<text class="m" x="%.0f" y="26" font-size="11" fill="#9b1d3a">%s</text></g>'
                    % (i, x, w, x + 16, x + 16, x + 28, l))
        x += w + 14
    svg("warning-flags.svg", int(x), 44, "Visibility gap warning flags", "".join(body), css, ["p700", "mono"])


# ---------------------------------------------------------------- 9. discovery scanner (auto-cycling)
def scanner(svg, text_w, pct, C):
    domains = [("Certificates", ["Public and Private TLS", "Client", "Code Signing", "Document Signing", "Expiry and Validity Periods", "Issuing CAs", "Ownership"]),
               ("Keys", ["Symmetric and Asymmetric", "Length", "Algorithm", "Location", "Age", "Rotation History"]),
               ("Secrets", ["API Keys", "Tokens", "Credentials in Vaults", "Pipelines", "App Configs"]),
               ("PKI", ["Internal and External CA Hierarchies", "Orphaned and Shadow CAs", "Trust Store Contents", "Policy Config"]),
               ("Crypto Libraries", ["Algorithms and Versions in Use", "Across Every Application", "Across Every Endpoint"]),
               ("Infrastructure", ["HSMs", "Vaults", "Load Balancers", "Cloud-Native Cert Services", "Kubernetes Ingress"])]
    W, H, n, T = 960, 440, 6, 24
    span = 100 / n
    css, body = [], []
    body.append('<defs><radialGradient id="cg" cx="100%" cy="0" r="120%"><stop offset="0" stop-color="#3a1e8f"/><stop offset=".45" stop-color="#1c0752"/><stop offset="1" stop-color="#0c022a"/></radialGradient>'
                '<linearGradient id="pg"><stop offset="0" stop-color="#14adff"/><stop offset="1" stop-color="#7f5fd9"/></linearGradient></defs>')
    body.append('<rect width="%d" height="%d" rx="20" fill="#fafaff"/>' % (W, H))
    # active-tab highlight steps down the list
    steps = "".join("%s,%s{transform:translateY(%dpx)}" % (pct(i * span + .5), pct((i + 1) * span - .01), i * 66) for i in range(n))
    css.append("@keyframes hi{0%%{transform:translateY(0)}%s100%%{transform:translateY(0)}}" % steps)
    body.append('<rect x="24" y="24" width="280" height="64" rx="12" fill="#fff" stroke="#7f5fd9" stroke-opacity=".35" style="animation:hi %ss infinite"/>' % T)
    for i, (name, _) in enumerate(domains):
        y = 24 + i * 66
        a, b = i * span, (i + 1) * span
        css.append("@keyframes t%d{0%%,%s{fill:#3e0eb7;fill-opacity:.08}%s,%s{fill:%s;fill-opacity:1}%s,100%%{fill:#3e0eb7;fill-opacity:.08}}"
                   % (i, pct(max(a - .01, 0)), pct(a + .5), pct(b - .5), C["purple"], pct(b)))
        body.append('<rect x="38" y="%d" width="44" height="44" rx="10" style="animation:t%d %ss infinite"/>' % (y + 10, i, T))
        body.append('<rect x="52" y="%d" width="16" height="16" rx="3" fill="none" stroke="#fff" stroke-width="1.7" stroke-opacity=".9"/>' % (y + 24))
        body.append('<text class="p" x="96" y="%d" font-size="16" font-weight="500" fill="#202020">%s</text>' % (y + 37, name))
    cx, cw = W - 612 - 24, 612
    body.append('<rect x="%d" y="24" width="%d" height="%d" rx="20" fill="url(#cg)" stroke="#a787ff" stroke-opacity=".35"/>' % (cx, cw, H - 48))
    for i, col in enumerate(["#ff5c7a", "#ffb547", "#3ddc97"]):
        body.append('<circle cx="%d" cy="57" r="5" fill="%s"/>' % (cx + 31 + i * 18, col))
    body.append('<text class="m" x="%d" y="61" font-size="12" fill="#a99bd6">accutive://discovery — what gets discovered</text>' % (cx + 90))
    body.append('<rect x="%d" y="136" width="560" height="4" rx="2" fill="#fff" fill-opacity=".1"/>' % (cx + 26))
    for i, (name, items) in enumerate(domains):
        a, b = i * span, (i + 1) * span
        css.append("@keyframes v%d{0%%,%s{opacity:0}%s,%s{opacity:1}%s,100%%{opacity:0}}" % (i, pct(max(a - .01, 0)), pct(a + .3), pct(b - .4), pct(b)))
        css.append("@keyframes g%d{0%%,%s{transform:scaleX(0)}%s,100%%{transform:scaleX(1)}}" % (i, pct(a), pct(a + span * .25)))
        g = ['<g style="animation:v%d %ss infinite">' % (i, T)]
        g.append('<text class="p" x="%d" y="112" font-size="26" font-weight="600" fill="#fff">%s</text>' % (cx + 26, name))
        g.append('<rect x="%d" y="136" width="560" height="4" rx="2" fill="url(#pg)" style="transform-box:fill-box;transform-origin:left;animation:g%d %ss infinite"/>' % (cx + 26, i, T))
        x, y = cx + 26, 160
        for j, it in enumerate(items):
            w = text_w(it, 14) + 42
            if x + w > cx + 586:
                x, y = cx + 26, y + 46
            on = a + span * (.2 + j * .06)
            css.append("@keyframes c%d_%d{0%%,%s{opacity:0}%s,100%%{opacity:1}}" % (i, j, pct(on), pct(on + 1.2)))
            g.append('<g style="animation:c%d_%d %ss infinite"><rect x="%.0f" y="%d" width="%.0f" height="36" rx="18" fill="#fff" fill-opacity=".06" stroke="#d2c0ff" stroke-opacity=".3"/>'
                     '<circle cx="%.0f" cy="%d" r="3" fill="#3ddc97"/><text class="p" x="%.0f" y="%d" font-size="14" font-weight="500" fill="#eaeaea">%s</text></g>'
                     % (i, j, T, x, y, w, x + 18, y + 18, x + 28, y + 23, it))
            x += w + 10
        g.append('</g>')
        body.append("".join(g))
    body.append('<text class="m" x="%d" y="%d" font-size="12" fill="#a99bd6">scope: on-prem · multi-cloud · hybrid · third-party</text>' % (cx + 26, H - 50))
    svg("discovery-scanner.svg", W, H, "What discovery covers: six domains scanned in turn", "".join(body), "".join(css), ["p500", "p600", "mono"])
