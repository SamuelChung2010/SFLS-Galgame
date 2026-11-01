'use strict';
(() => {
  const start = document.querySelector('#start-button');
  const frame = document.querySelector('#game-frame');
  const launch = document.querySelector('#launch-screen');
  const shell = document.querySelector('#player-shell');
  const help = document.querySelector('#help-dialog');
  const full = document.querySelector('#fullscreen-button');
  let started = false;
  start.addEventListener('click', () => {
    if (started) return;
    started = true;
    frame.src = frame.dataset.src;
    frame.hidden = false;
    launch.hidden = true;
    frame.focus();
  });
  document.querySelector('#help-button').addEventListener('click', () => help.showModal());
  document.querySelector('#close-help').addEventListener('click', () => help.close());
  help.addEventListener('click', event => {
    if (event.target !== help) return;
    const r = help.getBoundingClientRect();
    if (event.clientX < r.left || event.clientX > r.right || event.clientY < r.top || event.clientY > r.bottom) help.close();
  });
  // iPhone Safari may not expose element fullscreen; do not show an unusable control.
  if (document.fullscreenEnabled && shell.requestFullscreen) {
    full.hidden = false;
    full.addEventListener('click', async () => {
      try {
        if (document.fullscreenElement) await document.exitFullscreen();
        else await shell.requestFullscreen();
      } catch { full.textContent = '请横屏游玩'; }
    });
    document.addEventListener('fullscreenchange', () => {
      full.textContent = document.fullscreenElement ? '退出全屏' : '全屏';
    });
  }
})();
