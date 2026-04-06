from flask import Flask, render_template, request, redirect, url_for, flash
import os

from chairs_data import CHAIRS
from modules import MODULES
from study_data import DATA, NICHT_TECHNISCHER_WAHLPFLICHTBEREICH

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-key-change-me")

TRANSLATIONS = {
    "de": {
        "site_title": "Studienguide",
        "site_subtitle": "Orientierungshilfe eurer Fachschaft",
        "home_intro": "Die Qual der Wahl – das kennen wir alle. An unserer Fakultät gibt es viele spannende Möglichkeiten. Gerade am Anfang ist es oft schwer einzuschätzen, was einen wirklich erwartet. Deshalb haben wir für euch zwei Übersichten zusammengestellt, die euch bei der Orientierung helfen sollen.",
        "home_disclaimer": "Die Modulbeschreibungen basieren auf den letzten Informationen, die uns vorlagen, und sind daher nicht immer vollständig oder aktuell. Wenn ihr eigene Erfahrungen mit Modulen teilen möchtet, schreibt uns gerne eine E-Mail an {email}. So helft ihr uns, die Seite gemeinsam aktuell zu halten.",
        "home_title": "Was möchtest du ansehen?",
        "home_subtitle": "Wähle den Bereich, den du öffnen möchtest.",
        "study_programs": "Studiengänge",
        "chairs": "Lehrstühle",
        "study_programs_desc": "Übersicht zu Studiengängen, Vertiefungen und Wahlbereichen.",
        "chairs_desc": "Übersicht der Lehrstühle und zugehörigen Fachbereiche.",
        "chairs_page_title": "Lehrstühle Übersicht",
        "chairs_page_text": "Hier findest du eine Übersicht der Lehrstühle nach Fachbereichen.",
        "chair_modules_text": "Zugehörige Module dieses Lehrstuhls.",
        "back_home": "Zurück zur Startseite",
        "back_chairs": "Zurück zu Lehrstühlen",
        "degree": "Abschluss",
        "program": "Studiengang",
        "specializations": "Vertiefungsrichtungen",
        "other_areas": "Sonstige Bereiche",
        "non_technical_area": "Nicht technischer Wahlpflichtbereich",
        "mandatory_modules": "Pflichtmodule",
        "elective_modules": "Wahlmodule",
        "other_electives": "Sonstige Wahlmodule",
        "selected_modules": "Module der gewählten Vertiefungsrichtung.",
        "show_more": "Mehr anzeigen",
        "show_less": "Weniger anzeigen",
        "module_name": "Name",
        "module_description": "Beschreibung",
        "module_exam": "Klausur",
        "module_tips": "Tipps",
        "module_experiences": "Erfahrungen",
        "no_exam_info": "Noch keine Informationen zur Klausur vorhanden.",
        "no_tips": "Noch keine Tipps vorhanden.",
        "no_experiences": "Noch keine Erfahrungen vorhanden.",
        "footer": "Studienguide der Fachschaft – zur Orientierung und als erste Übersicht gedacht.",
        "open_chair": "Lehrstuhl öffnen",
        "chair_modules": "Zugehörige Module",
        "no_chair_modules": "Für diesen Lehrstuhl sind noch keine Module hinterlegt.",
        "experience_title": "Erfahrungsberichte",
        "experience_hint": "Wenn ihr zu diesem Modul einen Erfahrungsbericht hinzufügen möchtet, schreibt uns bitte eine E-Mail mit euren Erfahrungen. Schreibt unbedingt das Semester dazu (z. B. SS24 oder WS25/26)."
    },
    "en": {
        "site_title": "Study Guide",
        "site_subtitle": "Orientation support from your student council",
        "home_title": "What would you like to view?",
        "home_subtitle": "Choose the section you want to open.",
        "home_intro": "Choosing the right path is never easy. Our faculty offers many exciting opportunities, but especially at the beginning it can be difficult to know what to expect. That is why we created two overviews to help you find your orientation.",
        "home_disclaimer": "Module descriptions are based on the latest information available to us and may therefore not always be complete or up to date. If you would like to share your experiences with modules, feel free to send us an email at {email}. This helps us keep the site updated together.",
        "study_programs": "Study programs",
        "chairs": "Chairs",
        "study_programs_desc": "Overview of degree programs, specializations and elective areas.",
        "chairs_desc": "Overview of chairs and associated subject areas.",
        "chairs_page_title": "Chairs Overview",
        "chairs_page_text": "Here you can find an overview of chairs grouped by subject areas.",
        "chair_modules_text": "Modules belonging to this chair.",
        "back_home": "Back to home",
        "back_chairs": "Back to chairs",
        "degree": "Degree",
        "program": "Study program",
        "specializations": "Specializations",
        "other_areas": "Other areas",
        "non_technical_area": "Non-technical elective area",
        "mandatory_modules": "Mandatory modules",
        "elective_modules": "Elective modules",
        "other_electives": "Other elective modules",
        "selected_modules": "Modules of the selected specialization.",
        "show_more": "Show more",
        "show_less": "Show less",
        "module_name": "Name",
        "module_description": "Description",
        "module_exam": "Exam",
        "module_tips": "Tips",
        "module_experiences": "Experiences",
        "no_exam_info": "No exam information available yet.",
        "no_tips": "No tips available yet.",
        "no_experiences": "No experiences available yet.",
        "footer": "Study guide from the student council – intended as orientation and a first overview.",
        "open_chair": "Open chair",
        "chair_modules": "Associated modules",
        "no_chair_modules": "No modules have been stored for this chair yet.",
        "experience_title": "Experience reports",
        "experience_hint": "If you would like to add an experience report for this module, please send us an email with your experiences. Please make sure to include the semester as well (e.g. SS24 or WS25/26)."
    }
}


def get_lang_and_translations():
    lang = request.args.get("lang", "de")
    if lang not in TRANSLATIONS:
        lang = "de"
    return lang, TRANSLATIONS[lang]


def get_programs_for_degree(degree):
    return list(DATA[degree].keys())


def with_module_defaults(module):
    return {
        "name": module.get("name", "Unbekanntes Modul"),
        "beschreibung": module.get("beschreibung", "Keine Beschreibung vorhanden."),
        "klausur": module.get("klausur", "Noch keine Informationen zur Klausur vorhanden."),
        "tipps": module.get("tipps", []),
        "erfahrungen": module.get("erfahrungen", [])
    }


def resolve_modules(module_ids):
    resolved = []
    for module_id in module_ids:
        if module_id in MODULES:
            resolved.append(with_module_defaults(MODULES[module_id]))
        else:
            resolved.append(with_module_defaults({
                "name": module_id,
                "beschreibung": "Modul nicht gefunden."
            }))
    return resolved


def split_modules_by_degree(module_ids):
    bachelor_modules = []
    master_modules = []

    for module_id in module_ids:
        module = with_module_defaults(MODULES.get(module_id, {
            "name": module_id,
            "beschreibung": "Modul nicht gefunden."
        }))

        found_in_bachelor = False
        found_in_master = False

        for degree, programs in DATA.items():
            for program_name, program_data in programs.items():
                for key, value in program_data.items():
                    if key in ["pflichtmodule", "wahlmodule", "sonstige_wahlmodule"]:
                        if isinstance(value, list) and module_id in value:
                            if degree == "Bachelor":
                                found_in_bachelor = True
                            elif degree == "Master":
                                found_in_master = True

                    elif key == "vertiefungen" and isinstance(value, dict):
                        for vert_name, module_list in value.items():
                            if module_id in module_list:
                                if degree == "Bachelor":
                                    found_in_bachelor = True
                                elif degree == "Master":
                                    found_in_master = True

        if found_in_bachelor:
            bachelor_modules.append(module)

        if found_in_master:
            master_modules.append(module)

        if not found_in_bachelor and not found_in_master:
            bachelor_modules.append(module)

    return bachelor_modules, master_modules


def resolve_program_data(program_data):
    resolved = {}

    for key, value in program_data.items():
        if key in ["pflichtmodule", "wahlmodule", "sonstige_wahlmodule"]:
            resolved[key] = resolve_modules(value)
        elif key == "vertiefungen":
            resolved[key] = {}
            if isinstance(value, dict):
                for vert_name, module_ids in value.items():
                    resolved[key][vert_name] = resolve_modules(module_ids)
        else:
            resolved[key] = value

    return resolved


def get_resolved_data():
    resolved_data = {}

    for degree, programs in DATA.items():
        resolved_data[degree] = {}
        for program_name, program_data in programs.items():
            resolved_data[degree][program_name] = resolve_program_data(program_data)

    return resolved_data


def get_default_view(degree, program):
    program_data = DATA[degree][program]

    if "pflichtmodule" in program_data and isinstance(program_data["pflichtmodule"], list):
        return "pflichtmodule"

    if (
        "vertiefungen" in program_data
        and isinstance(program_data["vertiefungen"], dict)
        and program_data["vertiefungen"]
    ):
        return "vertiefungen"

    if "wahlmodule" in program_data:
        return "wahlmodule"

    if "sonstige_wahlmodule" in program_data:
        return "sonstige_wahlmodule"

    return "nichttechnischer_wahlpflichtbereich"


def get_default_specialization(degree, program):
    program_data = DATA[degree][program]
    if (
        "vertiefungen" in program_data
        and isinstance(program_data["vertiefungen"], dict)
        and program_data["vertiefungen"]
    ):
        return list(program_data["vertiefungen"].keys())[0]
    return None


def get_all_chairs():
    chairs = []

    for chair_id, chair in CHAIRS.items():
        chairs.append({
            "id": chair_id,
            "name": chair["name"],
            "modules_count": len(chair.get("modules", []))
        })

    return sorted(chairs, key=lambda x: x["name"].lower())


@app.route("/")
def home():
    lang, t = get_lang_and_translations()
    return render_template("home.html", lang=lang, t=t)


@app.route("/lehrstuehle")
def lehrstuehle():
    lang, t = get_lang_and_translations()
    chairs = get_all_chairs()

    return render_template(
        "lehrstuehle.html",
        lang=lang,
        t=t,
        chairs=chairs
    )

@app.route("/lehrstuehle/<chair_id>")
def lehrstuhl_detail(chair_id):
    lang, t = get_lang_and_translations()

    if chair_id not in CHAIRS:
        flash("Lehrstuhl nicht gefunden.", "error")
        return redirect(url_for("lehrstuehle", lang=lang))

    chair = CHAIRS[chair_id]
    bachelor_modules, master_modules = split_modules_by_degree(chair["modules"])

    return render_template(
        "lehrstuhl_detail.html",
        lang=lang,
        t=t,
        chair=chair,
        chair_id=chair_id,
        bachelor_modules=bachelor_modules,
        master_modules=master_modules
    )


@app.route("/studiengaenge")
def studiengaenge():
    lang, t = get_lang_and_translations()
    resolved_data = get_resolved_data()

    degree = request.args.get("degree", "Bachelor")
    if degree not in resolved_data:
        degree = "Bachelor"

    programs = get_programs_for_degree(degree)

    program = request.args.get("program", programs[0])
    if program not in resolved_data[degree]:
        program = programs[0]

    program_raw_data = DATA[degree][program]
    nichttechnisch_ids = program_raw_data.get(
        "nichttechnischer_wahlpflichtbereich",
        NICHT_TECHNISCHER_WAHLPFLICHTBEREICH
    )
    resolved_nichttechnisch = resolve_modules(nichttechnisch_ids)

    program_data = resolved_data[degree][program]
    view = request.args.get("view", get_default_view(degree, program))

    allowed_views = ["nichttechnischer_wahlpflichtbereich"]

    if "pflichtmodule" in program_data:
        allowed_views.append("pflichtmodule")
    if "vertiefungen" in program_data:
        allowed_views.append("vertiefungen")
    if "sonstige_wahlmodule" in program_data:
        allowed_views.append("sonstige_wahlmodule")
    if "wahlmodule" in program_data:
        allowed_views.append("wahlmodule")

    if view not in allowed_views:
        view = get_default_view(degree, program)

    current_specialization = request.args.get("specialization")
    if view == "vertiefungen" and isinstance(program_data.get("vertiefungen"), dict):
        if current_specialization not in program_data["vertiefungen"]:
            current_specialization = get_default_specialization(degree, program)
    else:
        current_specialization = None

    return render_template(
        "index.html",
        data=resolved_data,
        current_degree=degree,
        current_program=program,
        current_view=view,
        current_specialization=current_specialization,
        programs=programs,
        nichttechnischer_wahlpflichtbereich=resolved_nichttechnisch,
        lang=lang,
        t=t
    )


if __name__ == "__main__":
    app.run(debug=True)