// Smooth scroll from hero buttons
document.querySelectorAll(".hero-option").forEach((btn) => {
  btn.addEventListener("click", () => {
    const targetSelector = btn.getAttribute("data-target");
    const target = document.querySelector(targetSelector);
    if (target) {
      target.scrollIntoView({ behavior: "smooth", block: "start" });
    }
  });
});

// Set current year in footer
const yearSpan = document.getElementById("year");
if (yearSpan) {
  yearSpan.textContent = new Date().getFullYear();
}
