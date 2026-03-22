document.addEventListener("DOMContentLoaded", function () {
  initHeaderSelects();
  initDetailsLabels();
});

function initHeaderSelects() {
  const wrapper = document.querySelector(".header-controls-dropdown");
  if (!wrapper) return;

  const degreeSelect = document.getElementById("degreeSelect");
  const programSelect = document.getElementById("programSelect");

  const baseUrl = wrapper.dataset.studiengaengeUrl;
  const lang = wrapper.dataset.lang;
  const currentView = wrapper.dataset.view;
  const currentSpecialization = wrapper.dataset.specialization;

  if (degreeSelect) {
    degreeSelect.addEventListener("change", function () {
      const url = new URL(baseUrl, window.location.origin);
      url.searchParams.set("degree", degreeSelect.value);
      url.searchParams.set("lang", lang);
      window.location.href = url.toString();
    });
  }

  if (programSelect) {
    programSelect.addEventListener("change", function () {
      const url = new URL(baseUrl, window.location.origin);
      url.searchParams.set("degree", degreeSelect.value);
      url.searchParams.set("program", programSelect.value);
      url.searchParams.set("lang", lang);

      if (currentView) {
        url.searchParams.set("view", currentView);
      }
      if (currentSpecialization) {
        url.searchParams.set("specialization", currentSpecialization);
      }

      window.location.href = url.toString();
    });
  }
}

function initDetailsLabels() {
  const detailsElements = document.querySelectorAll(".module-details");

  detailsElements.forEach((details) => {
    const label = details.querySelector(".details-label");
    if (!label) return;

    const openText = label.dataset.openText || "Mehr anzeigen";
    const closeText = label.dataset.closeText || "Weniger anzeigen";

    const updateText = () => {
      label.textContent = details.open ? closeText : openText;
    };

    details.addEventListener("toggle", updateText);
    updateText();
  });
}