from flask import Flask, render_template, request, redirect, url_for, flash
import json
import re
import os
from datetime import datetime

from chairs_data import CHAIRS
from modules import MODULES
from study_data import DATA, NICHT_TECHNISCHER_WAHLPFLICHTBEREICH

app = Flask(__name__)
app.secret_key = "mein_geheimer_schluessel"

RECIPIENT_EMAIL = "yadviga.vizhbovska@uni-rostock.de"
COMMENTS_FILE = os.environ.get("COMMENTS_FILE", "comments.json")

TRANSLATIONS = {
    "de": {
        "site_title": "Studienguide",
        "site_subtitle": "Orientierungshilfe eurer Fachschaft",
        "home_title": "Was möchtest du ansehen?",
        "home_subtitle": "Wähle den Bereich, den du öffnen möchtest.",
        "study_programs": "Studiengänge",
        "chairs": "Lehrstühle",
        "study_programs_desc": "Übersicht zu Studiengängen, Vertiefungen und Wahlbereichen.",
        "chairs_desc": "Übersicht der Lehrstühle und zugehörigen Fachbereiche.",
        "chairs_page_title": "Lehrstühle Übersicht",
        "chairs_page_text": "Hier kommt später die Übersicht der Lehrstühle hin.",
        "chair_modules_text": "Hier findest du später alle zugehörigen Module dieses Lehrstuhls.",
        "back_home": "Zurück zur Startseite",
        "back_chairs": "Zurück zu Lehrstühle",
        "degree": "Abschluss",
        "program": "Studiengang",
        "specializations": "Vertiefungsrichtungen",
        "other_areas": "Sonstige Bereiche",
        "non_technical_area": "Nicht technischer Wahlpflichtbereich",
        "mandatory_modules": "Pflichtmodule",
        "elective_modules": "Wahlmodule",
        "other_electives": "Sonstige Wahlmodule",
        "selected_modules": "Module der gewählten Vertiefungsrichtung.",
        "comment_write": "Kommentar schreiben",
        "comment": "Kommentar",
        "comment_placeholder": "Schreibe einen kurzen hilfreichen Kommentar...",
        "submit": "Absenden",
        "comments_existing": "Bisherige Kommentare",
        "comments_empty": "Noch keine Kommentare vorhanden.",
        "modules_empty": "Noch keine Module eingetragen.",
        "mandatory_empty": "Noch keine Pflichtmodule eingetragen.",
        "elective_empty": "Noch keine Wahlmodule eingetragen.",
        "other_electives_empty": "Noch keine sonstigen Wahlmodule eingetragen.",
        "specialization_empty": "Für diese Vertiefung sind noch keine Module eingetragen.",
        "show_more": "Mehr anzeigen",
        "module_description": "Modulbeschreibung",
        "mandatory_badge": "Pflichtmodul",
        "elective_badge": "Wahlmodul",
        "general_badge": "Übergreifend",
        "footer": "Studienguide der Fachschaft – zur Orientierung und als erste Übersicht gedacht."
    },
    "en": {
        "site_title": "Study Guide",
        "site_subtitle": "Orientation support from your student council",
        "home_title": "What would you like to view?",
        "home_subtitle": "Choose the section you want to open.",
        "study_programs": "Study programs",
        "chairs": "Chairs",
        "study_programs_desc": "Overview of degree programs, specializations and elective areas.",
        "chairs_desc": "Overview of chairs and associated subject areas.",
        "chairs_page_title": "Chairs Overview",
        "chairs_page_text": "The overview of chairs will be added here later.",
        "chair_modules_text": "Here you will later find all modules belonging to this chair.",
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
        "comment_write": "Write comment",
        "comment": "Comment",
        "comment_placeholder": "Write a short helpful comment...",
        "submit": "Submit",
        "comments_existing": "Existing comments",
        "comments_empty": "No comments yet.",
        "modules_empty": "No modules entered yet.",
        "mandatory_empty": "No mandatory modules entered yet.",
        "elective_empty": "No elective modules entered yet.",
        "other_electives_empty": "No other elective modules entered yet.",
        "specialization_empty": "No modules have been entered for this specialization yet.",
        "show_more": "Show more",
        "module_description": "Module description",
        "mandatory_badge": "Mandatory module",
        "elective_badge": "Elective module",
        "general_badge": "General",
        "footer": "Study guide from the student council – intended as orientation and a first overview."
    }
}


def get_lang_and_translations():
    lang = request.args.get("lang", "de")
    if lang not in TRANSLATIONS:
        lang = "de"
    return lang, TRANSLATIONS[lang]


def load_comments():
    if not os.path.exists(COMMENTS_FILE):
        return []
    try:
        with open(COMMENTS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []


def save_comment(comment):
    comments = load_comments()
    comments.append(comment)
    with open(COMMENTS_FILE, "w", encoding="utf-8") as f:
        json.dump(comments, f, ensure_ascii=False, indent=2)

def save_all_comments(comments):
    with open(COMMENTS_FILE, "w", encoding="utf-8") as f:
        json.dump(comments, f, ensure_ascii=False, indent=2)


def get_next_comment_id():
    comments = load_comments()
    if not comments:
        return 1
    existing_ids = [comment.get("id", 0) for comment in comments]
    return max(existing_ids) + 1


def get_approved_comments():
    comments = load_comments()
    return [comment for comment in comments if comment.get("status") == "freigegeben"]


def is_valid_semester(semester):
    return bool(re.match(r"^(WS\d{2}/\d{2}|SS\d{2})$", semester))
def get_programs_for_degree(degree):
    return list(DATA[degree].keys())


def resolve_modules(module_ids):
    resolved = []
    for module_id in module_ids:
        if module_id in MODULES:
            resolved.append(MODULES[module_id])
        else:
            resolved.append({
                "name": module_id,
                "beschreibung": "Modul nicht gefunden."
            })
    return resolved


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


@app.route("/")
def home():
    lang, t = get_lang_and_translations()
    return render_template("home.html", lang=lang, t=t)


@app.route("/lehrstuehle")
def lehrstuehle():
    lang, t = get_lang_and_translations()

    grouped_chairs = {}
    for chair_id, chair in CHAIRS.items():
        group = chair["group"]
        if group not in grouped_chairs:
            grouped_chairs[group] = []
        grouped_chairs[group].append({
            "id": chair_id,
            "name": chair["name"]
        })

    return render_template(
        "lehrstuehle.html",
        lang=lang,
        t=t,
        grouped_chairs=grouped_chairs
    )


@app.route("/lehrstuehle/<chair_id>")
def lehrstuhl_detail(chair_id):
    lang, t = get_lang_and_translations()

    if chair_id not in CHAIRS:
        return "Nicht gefunden", 404

    chair = CHAIRS[chair_id]
    modules = resolve_modules(chair["modules"])

    return render_template(
        "lehrstuhl_detail.html",
        lang=lang,
        t=t,
        chair=chair,
        modules=modules,
        chair_id=chair_id
    )


@app.route("/studiengaenge")
def studiengaenge():
    lang, t = get_lang_and_translations()
    comments = get_approved_comments()
    resolved_data = get_resolved_data()
    resolved_nichttechnisch = resolve_modules(NICHT_TECHNISCHER_WAHLPFLICHTBEREICH)

    degree = request.args.get("degree", "Bachelor")
    if degree not in resolved_data:
        degree = "Bachelor"

    programs = get_programs_for_degree(degree)

    program = request.args.get("program", programs[0])
    if program not in resolved_data[degree]:
        program = programs[0]

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
        comments=comments,
        current_degree=degree,
        current_program=program,
        current_view=view,
        current_specialization=current_specialization,
        programs=programs,
        nichttechnischer_wahlpflichtbereich=resolved_nichttechnisch,
        lang=lang,
        t=t
    )


@app.route("/comment", methods=["POST"])
def comment():
    degree = request.form.get("degree", "Bachelor")
    program = request.form.get("program", "Maschinenbau")
    view = request.form.get("view", "vertiefungen")
    specialization = request.form.get("specialization", "")
    lang = request.form.get("lang", "de")

    modulname = request.form.get("modulname", "").strip()
    kommentar = request.form.get("kommentar", "").strip()
    semester = request.form.get("semester", "").strip().upper()

    if not modulname or not kommentar or not semester:
        flash("Bitte Modulname, Kommentar und Semester ausfüllen.", "error")
        return redirect(url_for(
            "studiengaenge",
            degree=degree,
            program=program,
            view=view,
            specialization=specialization,
            lang=lang
        ))

    if not is_valid_semester(semester):
        flash("Bitte ein gültiges Semester angeben, z. B. WS24/25 oder SS23.", "error")
        return redirect(url_for(
            "studiengaenge",
            degree=degree,
            program=program,
            view=view,
            specialization=specialization,
            lang=lang
        ))

    save_comment({
        "id": get_next_comment_id(),
        "modulname": modulname,
        "kommentar": kommentar,
        "semester": semester,
        "zeitpunkt": datetime.now().strftime("%d.%m.%Y %H:%M"),
        "recipient": RECIPIENT_EMAIL,
        "status": "wartet auf Prüfung"
    })

    flash("Dein Kommentar wurde gespeichert und wartet auf Freigabe.", "success")

    return redirect(url_for(
        "studiengaenge",
        degree=degree,
        program=program,
        view=view,
        specialization=specialization,
        lang=lang
    ))

@app.route("/admin/comments")
def admin_comments():
    comments = load_comments()
    wartende_kommentare = [c for c in comments if c.get("status") == "wartet auf Prüfung"]
    freigegebene_kommentare = [c for c in comments if c.get("status") == "freigegeben"]

    return render_template(
        "admin_comments.html",
        wartende_kommentare=wartende_kommentare,
        freigegebene_kommentare=freigegebene_kommentare
    )


@app.route("/admin/comments/freigeben/<int:comment_id>", methods=["POST"])
def comment_freigeben(comment_id):
    comments = load_comments()

    for comment in comments:
        if comment.get("id") == comment_id:
            comment["status"] = "freigegeben"
            break

    save_all_comments(comments)
    flash("Kommentar wurde freigegeben.", "success")
    return redirect(url_for("admin_comments"))


@app.route("/admin/comments/loeschen/<int:comment_id>", methods=["POST"])
def comment_loeschen(comment_id):
    comments = load_comments()
    comments = [comment for comment in comments if comment.get("id") != comment_id]

    save_all_comments(comments)
    flash("Kommentar wurde gelöscht.", "success")
    return redirect(url_for("admin_comments"))

if __name__ == "__main__":
    app.run(debug=True)