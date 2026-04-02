document.addEventListener("DOMContentLoaded", function () {
  initHeaderSelects();
  initDetailsLabels();
});

function initHeaderSelects() {
  const wrapper = document.querySelector(".header-controls-dropdown");
  if (!wrapper) return;

  const degreeSelect = document.getElementById("degreeSelect");
  const programSelect = document.getElementById("programSelect");

  if (!degreeSelect && !programSelect) return;

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

      if (degreeSelect) {
        url.searchParams.set("degree", degreeSelect.value);
      }

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
  const detailElements = document.querySelectorAll(".module-details");

  detailElements.forEach((detail) => {
    detail.addEventListener("toggle", function () {
      const summary = detail.querySelector("summary");
      if (!summary) return;

      if (detail.open) {
        summary.setAttribute("data-open", "true");
      } else {
        summary.setAttribute("data-open", "false");
      }
    });
  });
}