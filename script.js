// Keep navigation usable when JavaScript is unavailable.
const menu = document.querySelector('.menu-toggle');
const nav = document.querySelector('#primary-nav');
if (menu && nav) {
  const mobile = window.matchMedia('(max-width: 900px)');
  const setOpen = (open) => {
    menu.setAttribute('aria-expanded', String(open));
    nav.dataset.collapsed = String(!open);
  };
  const syncLayout = () => {
    menu.hidden = !mobile.matches;
    setOpen(!mobile.matches);
  };
  syncLayout();
  mobile.addEventListener('change', syncLayout);
  menu.addEventListener('click', () => setOpen(menu.getAttribute('aria-expanded') !== 'true'));
  nav.addEventListener('click', (event) => {
    if (mobile.matches && event.target.closest('a')) setOpen(false);
  });
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && mobile.matches && menu.getAttribute('aria-expanded') === 'true') {
      setOpen(false);
      menu.focus();
    }
  });
}
document.querySelectorAll('[data-year]').forEach((element) => {
  element.textContent = new Date().getFullYear();
});
