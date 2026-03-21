const data = {
  bachelor: {
    "Maschinenbau": {
      pflichtmodule: [
        "Mathe 1",
        "Mathe 2",
        "Mathe 3",
        "TM 1",
        "TM 2",
        "TM 3",
        "KL 1",
        "KL 2",
        "KL 3",
        "WT",
        "FL",
        "Informatik",
        "Messtechnik",
        "Regelungstechnik",
        "Thermo",
        "Strömung",
        "E-Technik"
      ],
      wahlmodule: {
        "Entwicklung und Konstruktion": [],
        "Energie- und Umwelttechnik": [],
        "Produktionstechnik und Logistik": [],
        "Regelungstechnik und Mechatronik": [],
        "Schiff- und Meerestechnik": [],
        "Sustainable Engineering": [],
        "Sonstige Module": []
      }
    },
    "Mechatronik": {
      pflichtmodule: [],
      wahlmodule: {}
    },
    "Biomedizinische Technik": {
      pflichtmodule: [],
      wahlmodule: {}
    },
    "Wirtschaftsingenieurwesen": {
      pflichtmodule: [],
      wahlmodule: {}
    }
  },
  master: {
    "Maschinenbau": {
      pflichtmodule: [],
      wahlmodule: {}
    },
    "Mechatronik": {
      pflichtmodule: [],
      wahlmodule: {}
    },
    "Biomedizinische Technik": {
      pflichtmodule: [],
      wahlmodule: {}
    },
    "Wirtschaftsingenieurwesen": {
      pflichtmodule: [],
      wahlmodule: {}
    },
    "Sustainable Engineering": {
      pflichtmodule: [],
      wahlmodule: {}
    }
  }
};

let currentDegree = "bachelor";
let currentProgram = "Maschinenbau";

const bachelorBtn = document.getElementById("bachelorBtn");
const masterBtn = document.getElementById("masterBtn");
const programButtons = document.getElementById("programButtons");
const detailTitle = document.getElementById("detailTitle");
const contentArea = document.getElementById("contentArea");

function renderProgramButtons() {
  programButtons.innerHTML = "";

  const programs = Object.keys(data[currentDegree]);

  if (!programs.includes(currentProgram)) {
    currentProgram = programs[0];
  }

  programs.forEach((program) => {
    const button = document.createElement("button");
    button.className = "program-btn";
    button.textContent = program;

    if (program === currentProgram) {
      button.classList.add("active");
    }

    button.addEventListener("click", () => {
      currentProgram = program;
      renderProgramButtons();
      renderContent();
      addAccordionEvents();
    });

    programButtons.appendChild(button);
  });
}

function createModuleList(modules, emptyText) {
  if (!modules || modules.length === 0) {
    return `<div class="placeholder">${emptyText}</div>`;
  }

  return `
    <ul class="module-list">
      ${modules
        .map(
          (modul) => `
            <li>
              <span class="module-name">${modul}</span>
            </li>
          `
        )
        .join("")}
    </ul>
  `;
}

function createWahlmoduleContent(wahlmodule) {
  const categories = Object.entries(wahlmodule || {});

  if (categories.length === 0) {
    return `<div class="placeholder">Für diesen Studiengang sind noch keine Wahlmodule eingetragen.</div>`;
  }

  return categories
    .map(
      ([categoryName, modules], index) => `
        <div class="sub-accordion">
          <button class="sub-accordion-header ${index === 0 ? "open" : ""}">
            <span>${categoryName}</span>
            <span class="accordion-icon">${index === 0 ? "−" : "+"}</span>
          </button>
          <div class="sub-accordion-content ${index === 0 ? "open" : ""}">
            ${createModuleList(
              modules,
              `Für "${categoryName}" sind noch keine Module eingetragen.`
            )}
          </div>
        </div>
      `
    )
    .join("");
}

function renderContent() {
  const degreeLabel = currentDegree === "bachelor" ? "Bachelor" : "Master";
  detailTitle.textContent = `${degreeLabel} - ${currentProgram}`;

  const currentData = data[currentDegree][currentProgram];

  contentArea.innerHTML = `
    <div class="accordion">
      <button class="accordion-header open">
        <span>Pflichtmodule</span>
        <span class="accordion-icon">−</span>
      </button>
      <div class="accordion-content open">
        ${createModuleList(
          currentData.pflichtmodule,
          `Für ${currentProgram} sind noch keine Pflichtmodule eingetragen.`
        )}
      </div>
    </div>

    <div class="accordion">
      <button class="accordion-header">
        <span>Wahlmodule</span>
        <span class="accordion-icon">+</span>
      </button>
      <div class="accordion-content">
        ${createWahlmoduleContent(currentData.wahlmodule)}
      </div>
    </div>
  `;
}

function addAccordionEvents() {
  const headers = document.querySelectorAll(".accordion-header, .sub-accordion-header");

  headers.forEach((header) => {
    header.addEventListener("click", () => {
      const content = header.nextElementSibling;
      const icon = header.querySelector(".accordion-icon");
      const isOpen = content.classList.contains("open");

      if (isOpen) {
        content.classList.remove("open");
        header.classList.remove("open");
        icon.textContent = "+";
      } else {
        content.classList.add("open");
        header.classList.add("open");
        icon.textContent = "−";
      }
    });
  });
}

function setDegree(degree) {
  currentDegree = degree;

  if (degree === "bachelor") {
    bachelorBtn.classList.add("active");
    masterBtn.classList.remove("active");
    currentProgram = "Maschinenbau";
  } else {
    masterBtn.classList.add("active");
    bachelorBtn.classList.remove("active");
    currentProgram = "Maschinenbau";
  }

  renderProgramButtons();
  renderContent();
  addAccordionEvents();
}

bachelorBtn.addEventListener("click", () => setDegree("bachelor"));
masterBtn.addEventListener("click", () => setDegree("master"));

renderProgramButtons();
renderContent();
addAccordionEvents();