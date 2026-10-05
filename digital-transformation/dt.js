/* illuminz – Digital Transformation page interactions */
(() => {
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const clamp = (v, a = 0, b = 1) => Math.min(b, Math.max(a, v));

  // ---- Mobile navigation ----
  const toggle = document.querySelector('.nav-toggle');
  const nav = document.getElementById('primary-nav');
  toggle.addEventListener('click', () => {
    const open = nav.classList.toggle('is-open');
    toggle.setAttribute('aria-expanded', open);
    toggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
  });
  nav.addEventListener('click', (e) => {
    if (e.target.closest('a')) { nav.classList.remove('is-open'); toggle.setAttribute('aria-expanded', 'false'); }
  });

  // ---- Hero load-in ----
  const hero = document.querySelector('.dt-hero');
  requestAnimationFrame(() => requestAnimationFrame(() => hero.classList.add('is-ready')));

  // ---- Seamless marquees: duplicate their contents ----
  const dupe = (track, fixAlt) => [...track.children].forEach((el) => {
    const c = el.cloneNode(true);
    c.setAttribute('aria-hidden', 'true');
    c.classList.add('dup');
    if (fixAlt) c.querySelectorAll('img').forEach((i) => { i.alt = ''; });
    track.appendChild(c);
  });
  dupe(document.querySelector('.mindset-track'));
  dupe(document.querySelector('.partner-logos'), true);

  // ---- Split the scrub paragraph into words ----
  const scrub = document.querySelector('[data-scrub]');
  scrub.innerHTML = scrub.textContent.trim().split(/\s+/).map((w) =>
    `<span class="w${/survival|thrives/.test(w) ? ' accent' : ''}">${w}</span>`).join(' ');
  const words = [...scrub.querySelectorAll('.w')];

  // ---- KPI counters ----
  const runCounter = (el) => {
    const to = +el.dataset.to;
    const from = el.dataset.from ? +el.dataset.from : null;
    const start = performance.now();
    const dur = 1600;
    const tick = (now) => {
      const t = clamp((now - start) / dur);
      const e = 1 - Math.pow(1 - t, 3);
      el.textContent = from !== null ? `${Math.round(from * e)}–${Math.round(to * e)}` : `${Math.round(to * e)}`;
      if (t < 1) requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
  };

  // ---- Scroll reveals ----
  const revealables = document.querySelectorAll('[data-reveal]');
  const reveal = (el) => {
    el.classList.add('is-visible');
    if (!reduceMotion) el.querySelectorAll('.count').forEach(runCounter);
  };
  if ('IntersectionObserver' in window && !reduceMotion) {
    const io = new IntersectionObserver((entries) => entries.forEach((en) => {
      if (en.isIntersecting) { reveal(en.target); io.unobserve(en.target); }
    }), { threshold: 0.15, rootMargin: '0px 0px -40px 0px' });
    revealables.forEach((el) => io.observe(el));
  } else {
    revealables.forEach((el) => el.classList.add('is-visible'));
  }

  // ---- Engagement panels ----
  const panels = [...document.querySelectorAll('.panel')];
  const activate = (p) => panels.forEach((x) => {
    x.classList.toggle('is-active', x === p);
    x.setAttribute('aria-expanded', x === p);
  });
  panels.forEach((p) => {
    p.addEventListener('click', () => activate(p));
    p.addEventListener('focus', () => activate(p));
    p.addEventListener('mouseenter', () => { if (window.matchMedia('(hover: hover)').matches) activate(p); });
  });

  // ---- Bento spotlight follows the pointer ----
  document.querySelectorAll('.bento-card').forEach((card) => {
    card.addEventListener('pointermove', (e) => {
      const r = card.getBoundingClientRect();
      card.style.setProperty('--mx', `${e.clientX - r.left}px`);
      card.style.setProperty('--my', `${e.clientY - r.top}px`);
    });
  });

  // ---- Scroll-driven effects ----
  const header = document.querySelector('.site-header');
  const progressBar = document.querySelector('.scroll-progress span');
  const cards = [...document.querySelectorAll('.stack-card')];
  const stickyMQ = window.matchMedia('(min-width: 900px) and (min-height: 700px)');
  const vSection = document.querySelector('.verticals');
  const vViewport = vSection.querySelector('.verticals-viewport');
  const vTrack = vSection.querySelector('.verticals-track');
  const vCount = vSection.querySelector('.verticals-count');
  const vMeter = vSection.querySelector('.meter');
  const vCards = vTrack.children.length;
  const pinMQ = window.matchMedia('(min-width: 1000px) and (min-height: 640px)');
  const stepsWrap = document.querySelector('.steps-wrap');
  const stepsLine = stepsWrap.querySelector('.steps-line');
  const steps = [...stepsWrap.querySelectorAll('.step')];

  let travel = 0;
  const measure = () => {
    if (pinMQ.matches) {
      travel = Math.max(0, vTrack.scrollWidth - vViewport.clientWidth);
      vSection.style.setProperty('--pin-h', `${travel + window.innerHeight}px`);
    } else {
      travel = 0;
      vSection.style.removeProperty('--pin-h');
      vTrack.style.removeProperty('--tx');
    }
  };

  const setVerticalIndex = (p) => {
    const idx = Math.min(vCards, Math.floor(p * vCards) + 1);
    vCount.textContent = String(idx).padStart(2, '0');
    vMeter.style.setProperty('--vp', Math.max(1 / vCards, p));
  };
  vViewport.addEventListener('scroll', () => {
    if (pinMQ.matches) return;
    const max = vViewport.scrollWidth - vViewport.clientWidth;
    setVerticalIndex(max > 0 ? vViewport.scrollLeft / max : 0);
  }, { passive: true });

  const update = () => {
    const vh = window.innerHeight;
    const y = window.scrollY;
    header.classList.toggle('is-scrolled', y > 8);
    const docH = document.documentElement.scrollHeight - vh;
    progressBar.style.setProperty('--p', docH > 0 ? y / docH : 0);

    // Words light up as the paragraph scrolls through the viewport
    const sr = scrub.getBoundingClientRect();
    const sp = reduceMotion ? 1 : clamp((vh * 0.85 - sr.top) / (sr.height + vh * 0.35));
    const lit = Math.round(sp * words.length);
    words.forEach((w, i) => w.classList.toggle('on', i < lit));

    // Stacking cards: earlier cards shrink and dim as the next one slides over
    if (stickyMQ.matches && !reduceMotion) {
      cards.forEach((card, i) => {
        const next = cards[i + 1];
        if (!next) return;
        const nr = next.getBoundingClientRect();
        const top = parseFloat(getComputedStyle(next).top) || 0;
        const p = clamp(1 - (nr.top - top) / card.offsetHeight);
        card.style.setProperty('--scale', (1 - 0.05 * p).toFixed(4));
        card.style.setProperty('--dim', (1 - 0.1 * p).toFixed(4));
      });
    } else {
      cards.forEach((c) => { c.style.removeProperty('--scale'); c.style.removeProperty('--dim'); });
    }

    // Verticals: vertical scroll drives horizontal travel
    if (pinMQ.matches && travel > 0) {
      const r = vSection.getBoundingClientRect();
      const p = clamp(-r.top / (vSection.offsetHeight - vh));
      vTrack.style.setProperty('--tx', `${-p * travel}px`);
      setVerticalIndex(p);
    }

    // Process line draws down; steps switch on as the line reaches them
    const wr = stepsWrap.getBoundingClientRect();
    const mid = vh * 0.6;
    const lp = clamp((mid - wr.top) / wr.height);
    stepsLine.style.setProperty('--lp', lp);
    steps.forEach((s) => {
      const dot = s.querySelector('.step-dot').getBoundingClientRect();
      s.classList.toggle('is-on', reduceMotion || dot.top + dot.height / 2 < mid);
    });
  };

  let ticking = false;
  const onScroll = () => {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(() => { update(); ticking = false; });
  };
  measure();
  update();
  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', () => { measure(); update(); });
  window.addEventListener('load', () => { measure(); update(); });
})();
