function toggleElement(id, className) {
  document.getElementById(id).classList.toggle(className);
}

window.onclick = function (event) {
  if (!event.target.matches(".dropButton")) {
    const dropdowns = document.getElementsByClassName("dropdown-content");
    for (let i = 0; i < dropdowns.length; i++) {
      const openDropdown = dropdowns[i];
      if (openDropdown.classList.contains("show")) {
        openDropdown.classList.remove("show");
      }
    }
  }
};

