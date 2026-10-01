/* illuminz – Motion Graphics & Storyboarding: page interactions */
(() => {
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // ---- Mobile navigation ----
  const toggle = document.querySelector('.nav-toggle');
  const nav = document.getElementById('primary-nav');
  toggle.addEventListener('click', () => {
    const open = nav.classList.toggle('is-open');
    toggle.setAttribute('aria-expanded', open);
    toggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
  });
  nav.addEventListener('click', (e) => {
    if (e.target.closest('a')) {
      nav.classList.remove('is-open');
      toggle.setAttribute('aria-expanded', 'false');
    }
  });

  // ---- Header shadow once the page scrolls ----
  const header = document.querySelector('.site-header');
  const onScroll = () => header.classList.toggle('is-scrolled', window.scrollY > 8);
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  // ---- Hero load-in ----
  const hero = document.querySelector('.hero');
  requestAnimationFrame(() => requestAnimationFrame(() => hero.classList.add('is-ready')));

  // ---- Typing "mot" -> "motion" loop ----
  const typed = document.querySelector('.typed');
  const typedText = typed.querySelector('.typed-text');
  const word = typed.dataset.words;
  if (!reduceMotion) {
    const wait = (ms) => new Promise((r) => setTimeout(r, ms));
    const type = async () => {
      await wait(1400);
      for (;;) {
        typed.classList.add('is-typing');
        for (let i = typedText.textContent.length + 1; i <= word.length; i++) {
          typedText.textContent = word.slice(0, i);
          await wait(110);
        }
        typed.classList.remove('is-typing');
        await wait(2600);
        typed.classList.add('is-typing');
        for (let i = word.length - 1; i >= 3; i--) {
          typedText.textContent = word.slice(0, i);
          await wait(70);
        }
        typed.classList.remove('is-typing');
        await wait(900);
      }
    };
    type();
  } else {
    typedText.textContent = word;
  }

  // ---- Mouse parallax on hero shapes ----
  const shapes = [...document.querySelectorAll('.shape')];
  if (!reduceMotion && window.matchMedia('(pointer: fine)').matches) {
    let raf = 0, mx = 0, my = 0;
    hero.addEventListener('pointermove', (e) => {
      const r = hero.getBoundingClientRect();
      mx = (e.clientX - r.left) / r.width - 0.5;
      my = (e.clientY - r.top) / r.height - 0.5;
      if (!raf) raf = requestAnimationFrame(() => {
        shapes.forEach((el) => {
          const d = parseFloat(el.dataset.depth) || 0.5;
          el.style.transform = `translate3d(${mx * -40 * d}px, ${my * -40 * d}px, 0)`;
        });
        raf = 0;
      });
    });
    hero.addEventListener('pointerleave', () => shapes.forEach((el) => { el.style.transform = ''; }));
  }

  // ---- Scroll reveals ----
  const revealables = document.querySelectorAll('[data-reveal]');
  if ('IntersectionObserver' in window && !reduceMotion) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          entry.target.querySelectorAll('.swap').forEach((el) => el.classList.add('is-visible'));
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.18, rootMargin: '0px 0px -40px 0px' });
    revealables.forEach((el) => io.observe(el));
  } else {
    revealables.forEach((el) => el.classList.add('is-visible'));
    document.querySelectorAll('.swap').forEach((el) => el.classList.add('is-visible'));
  }

  // ---- Partner logos: duplicate the row so the mobile marquee loops seamlessly ----
  const logos = document.querySelector('.partner-logos');
  [...logos.children].forEach((li) => {
    const copy = li.cloneNode(true);
    copy.classList.add('dup');
    copy.setAttribute('aria-hidden', 'true');
    copy.querySelector('img').alt = '';
    logos.appendChild(copy);
  });
})();
