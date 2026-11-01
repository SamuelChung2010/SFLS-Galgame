'use strict';
(() => {
  const menuButton = document.querySelector('.menu-toggle');
  const mobileNav = document.querySelector('#mobile-nav');
  function closeMenu(returnFocus = false) {
    mobileNav.hidden = true;
    menuButton.setAttribute('aria-expanded', 'false');
    menuButton.setAttribute('aria-label', '打开导航菜单');
    if (returnFocus) menuButton.focus();
  }
  menuButton.addEventListener('click', () => {
    const open = menuButton.getAttribute('aria-expanded') !== 'true';
    mobileNav.hidden = !open;
    menuButton.setAttribute('aria-expanded', String(open));
    menuButton.setAttribute('aria-label', open ? '关闭导航菜单' : '打开导航菜单');
  });
  mobileNav.querySelectorAll('a').forEach(link => link.addEventListener('click', () => closeMenu()));
  document.addEventListener('click', event => {
    if (!mobileNav.hidden && !event.target.closest('.site-header')) closeMenu();
  });
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && !mobileNav.hidden) closeMenu(true);
  });
  const desktopMedia = window.matchMedia('(min-width: 801px)');
  const resetMenu = event => { if (event.matches) closeMenu(); };
  if (desktopMedia.addEventListener) desktopMedia.addEventListener('change', resetMenu);
  else desktopMedia.addListener(resetMenu);

  const tabs = [...document.querySelectorAll('.chapter-tab')];
  const panels = [...document.querySelectorAll('.chapter-panel')];
  function activateChapter(index, focus = false) {
    tabs.forEach((tab, i) => {
      const active = i === index;
      tab.classList.toggle('active', active);
      tab.setAttribute('aria-selected', String(active));
      tab.tabIndex = active ? 0 : -1;
      panels[i].hidden = !active;
    });
    if (focus) tabs[index].focus();
  }
  tabs.forEach((tab, index) => {
    tab.addEventListener('click', () => activateChapter(index));
    tab.addEventListener('keydown', event => {
      let next;
      if (event.key === 'ArrowRight' || event.key === 'ArrowDown') next = (index + 1) % tabs.length;
      else if (event.key === 'ArrowLeft' || event.key === 'ArrowUp') next = (index + tabs.length - 1) % tabs.length;
      else if (event.key === 'Home') next = 0;
      else if (event.key === 'End') next = tabs.length - 1;
      if (next !== undefined) { event.preventDefault(); activateChapter(next, true); }
    });
  });

  // Display names and profiles confirmed by the project owner.
  const characters = {
  "daomeixiong": {
    "name": "倒霉熊",
    "mark": "熊",
    "subtitle": "同学 · 旧识",
    "description": "开朗热情，朋友不少。初中时就与你同年级，如今在新校园里再次碰面，那份熟悉感也跟着回来了。",
    "identity": "同学 · 初中同年级的旧识",
    "keywords": "开朗 / 热情 / 好相处",
    "connection": "搬进宿舍时再次碰面的同学",
    "background": "#e5ebd7"
  },
  "qiwenchang": {
    "name": "齐文昌",
    "mark": "齐",
    "subtitle": "同桌",
    "description": "有些内向的同桌。起初话不算多，聊到共同感兴趣的话题时，才发现彼此很合拍。",
    "identity": "同学 · 同桌",
    "keywords": "内向 / 兴趣相投 / 同桌",
    "connection": "在教室里逐渐熟悉的同桌",
    "background": "#dce7ed"
  },
  "xiaodeng": {
    "name": "小邓",
    "mark": "邓",
    "subtitle": "同学 · 走读生",
    "description": "性格喜感，喜欢整活。和他一起探索校园，平常的日常也多了几分热闹。",
    "identity": "同学 · 走读生",
    "keywords": "整活 / 喜感 / 校园探索",
    "connection": "带你一起探索校园的同伴",
    "background": "#eddfcf"
  },
  "wanglihao": {
    "name": "王力豪",
    "mark": "豪",
    "subtitle": "舍友",
    "description": "表面很“豪”的舍友，言谈间总带着几分排场。相处下来就会发现，他本性不坏。",
    "identity": "舍友",
    "keywords": "表面豪 / 本性不坏 / 宿舍日常",
    "connection": "一起住进新宿舍的舍友",
    "background": "#e9e0cb"
  },
  "lige": {
    "name": "李哥",
    "mark": "李",
    "subtitle": "舍友",
    "description": "喜欢宝可梦，也喜欢动漫。聊起这些共同的兴趣，宿舍里总能多出一些话题。",
    "identity": "舍友 · 宝可梦爱好者",
    "keywords": "宝可梦 / 动漫 / 舍友",
    "connection": "宿舍日常里的同伴",
    "background": "#dedfeb"
  },
  "heyunze": {
    "name": "何云泽 Alexios",
    "mark": "何",
    "subtitle": "国际书院新生",
    "description": "时而抽象，时而正经。喜欢足球，也有着让人印象深刻的反差感。",
    "identity": "国际书院新生",
    "keywords": "足球 / 时而抽象 / 时而正经",
    "connection": "在操场上相遇的同伴",
    "background": "#e0e9d3"
  }
};
  const dialog = document.querySelector('#character-dialog');
  let dialogTrigger = null;
  document.querySelectorAll('[data-character]').forEach(card => card.addEventListener('click', () => {
    const key = card.dataset.character;
    const character = characters[key];
    if (!character) return;
    dialogTrigger = card;
    dialog.style.setProperty('--character-bg', character.background);
    dialog.querySelector('.dialog-letter').textContent = character.mark;
    document.querySelector('#dialog-title').textContent = character.name;
    document.querySelector('#dialog-subtitle').textContent = character.subtitle;
    document.querySelector('#dialog-description').textContent = character.description;
    const facts = dialog.querySelector('.dialog-facts');
    facts.replaceChildren();
    [['身份', character.identity], ['关键词', character.keywords], ['相遇', character.connection]].forEach(([label, value]) => {
      const term = document.createElement('dt');
      const description = document.createElement('dd');
      term.textContent = label;
      description.textContent = value;
      facts.append(term, description);
    });
    dialog.showModal();
    document.body.classList.add('modal-open');
    dialog.querySelector('.dialog-close').focus();
  }));
  dialog.querySelector('.dialog-close').addEventListener('click', () => dialog.close());
  dialog.addEventListener('click', event => {
    if (event.target !== dialog) return;
    const bounds = dialog.getBoundingClientRect();
    if (event.clientX < bounds.left || event.clientX > bounds.right || event.clientY < bounds.top || event.clientY > bounds.bottom) dialog.close();
  });
  dialog.addEventListener('close', () => {
    document.body.classList.remove('modal-open');
    if (dialogTrigger) dialogTrigger.focus({ preventScroll: true });
  });

  // Content stays visible when JavaScript or IntersectionObserver is unavailable.
  if ('IntersectionObserver' in window) {
    const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (!reducedMotion) {
      document.documentElement.classList.add('motion-ready');
      const revealObserver = new IntersectionObserver(entries => {
        entries.forEach(entry => {
          if (entry.isIntersecting) { entry.target.classList.add('visible'); revealObserver.unobserve(entry.target); }
        });
      }, { threshold: 0.05 });
      document.querySelectorAll('.reveal').forEach(element => revealObserver.observe(element));
    }
    const navLinks = [...document.querySelectorAll('.desktop-nav a')];
    const sectionObserver = new IntersectionObserver(entries => {
      const visible = entries.filter(entry => entry.isIntersecting).sort((a, b) => b.intersectionRatio - a.intersectionRatio);
      if (!visible.length) return;
      navLinks.forEach(link => {
        if (link.hash === `#${visible[0].target.id}`) link.setAttribute('aria-current', 'location');
        else link.removeAttribute('aria-current');
      });
    }, { rootMargin: '-15% 0px -50% 0px', threshold: 0 });
    document.querySelectorAll('main section[id]').forEach(section => sectionObserver.observe(section));
  }
})();
