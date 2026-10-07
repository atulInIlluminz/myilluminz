/* Accutive – Cryptography Discovery page interactions */
(function () {
  "use strict";
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };

  /* ---------- Header: mobile menu + shadow on scroll ---------- */
  var header = $(".site-header"), nav = $(".nav"), toggle = $(".nav-toggle");
  toggle.addEventListener("click", function () {
    var open = nav.classList.toggle("open");
    toggle.setAttribute("aria-expanded", open);
    toggle.setAttribute("aria-label", open ? "Close menu" : "Open menu");
  });
  var onScroll = function () { header.classList.toggle("scrolled", window.scrollY > 8); };
  window.addEventListener("scroll", onScroll, { passive: true }); onScroll();

  /* ---------- Count-up helper ---------- */
  function countUp(el, to, ms) {
    if (reduce) { el.textContent = to; return; }
    var t0 = performance.now();
    (function step(t) {
      var p = Math.min(1, (t - t0) / ms), e = 1 - Math.pow(1 - p, 3);
      el.textContent = Math.round(to * e);
      if (p < 1) requestAnimationFrame(step);
    })(t0);
  }

  /* ---------- Hero: cycle highlight through the four verbs ---------- */
  var words = $$("[data-cycle] .w"), wi = 0;
  if (words.length) {
    words[0].classList.add("on");
    if (!reduce) setInterval(function () {
      words[wi].classList.remove("on");
      wi = (wi + 1) % words.length;
      words[wi].classList.add("on");
    }, 1800);
  }

  /* ---------- Hero radar: place assets, light them up as the beam passes ---------- */
  var radar = $("[data-radar]");
  if (radar) {
    var place = function () {
      var k = window.innerWidth < 560 ? 0.78 : 1; // pull pills inward on phones so they stay on screen
      assets.forEach(function (o) {
        var r = o.r * k, rad = o.a * Math.PI / 180;
        o.el.style.left = (50 + r * Math.sin(rad)) + "%";
        o.el.style.top = (50 - r * Math.cos(rad)) + "%";
      });
    };
    var assets = $$(".asset", radar).map(function (el) {
      return { el: el, a: +el.dataset.a, r: +el.dataset.r };
    });
    place();
    window.addEventListener("resize", place);
    var live = $("[data-count-live]", radar), riskEl = $("[data-risk]", radar);
    var sweep = $(".sweep", radar);
    var found = 0, risk = 0;
    var mark = function (o) {
      if (o.el.classList.contains("found")) return;
      o.el.classList.add("found"); found++;
      if (o.el.classList.contains("risk")) risk++;
      live.textContent = found;
      riskEl.textContent = risk;
    };
    if (reduce) {
      assets.forEach(mark);
    } else {
      sweep.style.animation = "none";
      var t0 = performance.now(), PERIOD = 6000, last = 0;
      (function frame(t) {
        var ang = ((t - t0) / PERIOD * 360) % 360;
        sweep.style.transform = "rotate(" + ang + "deg)";
        assets.forEach(function (o) {
          var passed = ang >= o.a && (last <= o.a || ang < last);
          if (passed) mark(o);
        });
        last = ang;
        requestAnimationFrame(frame);
      })(t0);
    }
  }

  /* ---------- Reveal on scroll + one-shot section effects ---------- */
  var fire = {
    ring: function (el) {
      var pct = +el.dataset.ring, bar = $(".bar", el), C = 2 * Math.PI * 40;
      bar.style.strokeDashoffset = C * (1 - pct / 100);
      countUp($("[data-count]", el), pct, 1600);
    },
    fixes: function (el) {
      var rows = $$(".fix", el), out = $("[data-fixed]", el);
      rows.forEach(function (row, i) {
        setTimeout(function () { row.classList.add("done"); $(".st", row).textContent = "\u2713"; out.textContent = i + 1; }, reduce ? 0 : 600 + i * 700);
      });
    },
    year: function (el) { el.classList.add("in"); }
  };
  var targets = $$(".reveal, [data-ring], [data-fixes], [data-year]");
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        var el = en.target;
        el.classList.add("in");
        if (el.dataset.ring) fire.ring(el);
        if (el.hasAttribute("data-fixes")) fire.fixes(el);
        if (el.hasAttribute("data-year")) fire.year(el);
        io.unobserve(el);
      });
    }, { threshold: 0.25, rootMargin: "0px 0px -40px 0px" });
    targets.forEach(function (el) { io.observe(el); });
  } else {
    targets.forEach(function (el) {
      el.classList.add("in");
      if (el.dataset.ring) fire.ring(el);
      if (el.hasAttribute("data-fixes")) fire.fixes(el);
    });
  }

  /* ---------- Discovery coverage: accessible tabs that "re-scan" ---------- */
  var tabs = $$(".domain-btn"), consoleEl = $("[data-console]");
  function select(tab, focus) {
    tabs.forEach(function (t) {
      var on = t === tab;
      t.setAttribute("aria-selected", on);
      t.tabIndex = on ? 0 : -1;
      document.getElementById(t.getAttribute("aria-controls")).hidden = !on;
    });
    if (focus) tab.focus();
    consoleEl.classList.remove("scanning");
    void consoleEl.offsetWidth; // restart CSS animations
    consoleEl.classList.add("scanning");
  }
  tabs.forEach(function (tab, i) {
    tab.addEventListener("click", function () { select(tab); });
    tab.addEventListener("keydown", function (e) {
      var k = e.key, n = tabs.length, j = null;
      if (k === "ArrowDown" || k === "ArrowRight") j = (i + 1) % n;
      if (k === "ArrowUp" || k === "ArrowLeft") j = (i - 1 + n) % n;
      if (k === "Home") j = 0;
      if (k === "End") j = n - 1;
      if (j !== null) { e.preventDefault(); select(tabs[j], true); }
    });
  });
})();
