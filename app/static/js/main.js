document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("search-form");
  form.addEventListener("submit", () => {
    const button = form.querySelector("button");
    button.textContent = "Searching...";
    button.disabled = true;
  });
});
