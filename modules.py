def normalize_modules(modules_dict):
    normalized = {}
    for module_id, module in modules_dict.items():
        normalized[module_id] = {
            "name": module.get("name", module_id),
            "beschreibung": module.get("beschreibung", "Keine Beschreibung vorhanden."),
            "klausur": module.get("klausur", "Noch keine Informationen zur Klausur vorhanden."),
            "tipps": module.get("tipps", []),
            "erfahrungen": module.get("erfahrungen", [])
        }
    return normalized


RAW_MODULES = {
    "aktive_systeme_kraftfahrzeug": {
        "name": "Aktive Systeme im Kraftfahrzeug",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "additive_fertigungsverfahren": {
        "name": "Additive Fertigungsverfahren",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "aerodynamik_hydrodynamik": {
        "name": "Aerodynamik und Hydrodynamik",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "alternative_antriebssysteme": {
        "name": "Alternative Antriebssysteme",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "angewandte_stroemungsmechanik": {
        "name": "Angewandte Strömungsmechanik in Natur und Technik",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "angewandte_stroemungssimulation": {
        "name": "Angewandte Strömungssimulation",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "anlagenwirtschaft": {
        "name": "Anlagenwirtschaft",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "antriebstechnik": {
        "name": "Antriebstechnik",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "antriebssteuerung": {
        "name": "Antriebssteuerung",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "automatisierung_fertigung_montage": {
        "name": "Automatisierung in Fertigung und Montage",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "aufladung_verbrennungsmotor": {
        "name": "Aufladung des Verbrennungsmotors",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "ausgewaehlte_themen_logistik": {
        "name": "Ausgewählte Themen der Logistik",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "betriebsfestigkeit": {
        "name": "Betriebsfestigkeit",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "biomaterialien_maschinenbau": {
        "name": "Biomaterialien für Maschinenbau",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "blue_engineering": {
        "name": "Blue Engineering - Nachhaltigkeit im Ingenieurwesen",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "cad": {
        "name": "Computer Aided Design (CAD)",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "digitale_regelung": {
        "name": "Digitale Regelung",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "dynamik_kraftfahrzeuge": {
        "name": "Dynamik von Kraftfahrzeugen",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "dynamik_mehrkoerpersysteme": {
        "name": "Dynamik von Mehrkörpersystemen",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "einfuehrung_cpp": {
        "name": "Einführung in die angewandte C++ Programmierung",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "einfuehrung_meerestechnik": {
        "name": "Einführung in die Meerestechnik",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "elektrotechnik": {
        "name": "Elektrotechnik",
        "beschreibung": "Grundlagen der Elektrotechnik für Maschinenbauer.",
        "klausur": "Schriftliche Klausur mit Rechen- und Theorieaufgaben.",
        "tipps": [
            "Altklausuren rechnen.",
            "Schaltungen und Grundgesetze wirklich verstehen.",
            "Nicht nur lesen, sondern Aufgaben aktiv rechnen."
        ],
        "erfahrungen": [
            {
                "semester": "SS25",
                "text": "Mit regelmäßigem Üben ist das Modul machbar. Kurz vor der Klausur alles auf einmal zu lernen war eher schwierig."
            }
        ]
    },
    "elektrotechnik_1": {
        "name": "Elektrotechnik 1",
        "beschreibung": "Grundlagen der Elektrotechnik für Maschinenbauer.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "elektrotechnik_2": {
        "name": "Elektrotechnik 2",
        "beschreibung": "Grundlagen der Elektrotechnik für Maschinenbauer.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "elektrotechnik_3": {
        "name": "Elektrotechnik 3",
        "beschreibung": "Grundlagen der Elektrotechnik für Maschinenbauer.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "elastische_mehrkoerpersysteme": {
        "name": "Elastische Mehrkörpersysteme",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "englisch_fachkommunikation_ing_c12": {
        "name": "Englisch Fachkommunikation Ingenieurwissenschaften C1.2 GER",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "englisch_fachkommunikation_maschinenbau_c11": {
        "name": "Englisch Fachkommunikation Maschinenbau C1.1 GER",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "energietechnik": {
        "name": "Energietechnik",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "entwerfen_antriebe": {
        "name": "Entwerfen von Antrieben",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "ermuedungsrisse": {
        "name": "Ermüdungsrisse",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "experimentelle_stroemungsmechanik": {
        "name": "Experimentelle Strömungsmechanik",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "experimenteller_leichtbau": {
        "name": "Experimenteller Leichtbau",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "fabrikplanung": {
        "name": "Fabrikplanung",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "fahrzeugantriebe": {
        "name": "Fahrzeugantriebe",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "fertigungslehre": {
        "name": "Fertigungslehre",
        "beschreibung": "Grundlagen des Fachgebiets laut Studienplan.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "fertigungsmittel": {
        "name": "Fertigungsmittel",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "festigkeitsoptimiertes_gestalten": {
        "name": "Festigkeitsoptimiertes und bruchsicheres Gestalten",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "gewerbliche_schutzrechte": {
        "name": "Gewerbliche Schutzrechte",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "grossmotoren_schiff": {
        "name": "Großmotoren für Schiffsanwendungen – Grundlagen und Zukunftstrends",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "grundlagen_akustik": {
        "name": "Grundlagen der Akustik",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "grundlagen_fuegetechnik": {
        "name": "Grundlagen der Fügetechnik",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "grundlagen_hydromechanik_schiffen_offshore": {
        "name": "Grundlagen der Hydromechanik von Schiffen und Offshore-Strukturen",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "grundlagen_materialflusstechnik": {
        "name": "Grundlagen der Materialflusstechnik",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "grundlagen_schiffstechnik": {
        "name": "Grundlagen der Schiffstechnik",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "grundlagen_stroemungsmaschinen_windturbinen": {
        "name": "Grundlagen der Strömungsmaschinen und Windturbinen",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "hydraulik_pneumatik": {
        "name": "Hydraulik und Pneumatik",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "hydraulische_stroemungsmaschinen": {
        "name": "Hydraulische Strömungsmaschinen",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "informatik": {
        "name": "Informatik",
        "beschreibung": "Einführung in informatische Grundlagen und technische Anwendungen.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "intralogistik": {
        "name": "Intralogistik",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "kaelte_klimatechnik": {
        "name": "Kälte- und Klimatechnik",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "klimaneutrale_kraftstoffe": {
        "name": "Klimaneutrale Kraftstoffe",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "klebtechnik": {
        "name": "Klebtechnik",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "kolben_stroemungsmaschinen_energiemaschinen": {
        "name": "Kolben- und Strömungsmaschinen / Energiemaschinen",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "komponenten_mechatronischer_systeme": {
        "name": "Komponenten mechatronischer Systeme",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "konstruktion_windenergieanlagen": {
        "name": "Konstruktion von Windenergieanlagen",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "konstruktionslehre": {
        "name": "Konstruktionslehre",
        "beschreibung": "Weiterführende Inhalte der Konstruktionslehre.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "konstruktionsmethodik": {
        "name": "Konstruktionsmethodik",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "kraft_schmierstoffe_co2": {
        "name": "Kraft- und Schmierstoffe – von der fossilen Basis zur CO₂-Neutralität",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "labor_schiffs_meerestechnik": {
        "name": "Labor: Schiffs- und Meerestechnik",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "labor_thermische_maschinen": {
        "name": "Laborpraktikum: Thermische Maschinen - Effizienz und Umwelt",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "labor_vertiefung_werkstofftechnik": {
        "name": "Laborpraktikum Vertiefungsrichtung Werkstofftechnik",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "leichtbau_grundlagen": {
        "name": "Grundlagen des Leichtbaus",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "leichtbaukonstruktion": {
        "name": "Leichtbaukonstruktion",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "leichtbauwerkstoffe": {
        "name": "Leichtbauwerkstoffe",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "logistik": {
        "name": "Logistik",
        "beschreibung": "Es geht um Logistik und Kreislaufwirtschaft in der industriellen Anwendung. Prof. Sender gibt sehr viele praxisnahe Beispiele. Jedoch kann die Vorlesung einem sehr trocken erscheinen, wenn man nicht so sehr auf theoretische Inhalte steht.",
        "klausur": "Bisher keine genauen Infos zur Prüfungsform eingetragen.",
        "tipps": [
            "Begriffe und Modelle früh lernen.",
            "Praxisbeispiele mit den theoretischen Inhalten verknüpfen."
        ],
        "erfahrungen": [
            {
                "semester": "WS24/25",
                "text": "Inhaltlich spannend wegen der Praxisnähe, aber an manchen Stellen recht trocken."
            }
        ]
    },
    "logistik_kreislaufwirtschaft": {
        "name": "Logistik und Kreislaufwirtschaft",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "management_entwicklungsteams_projekten": {
        "name": "Management von Entwicklungsteams und Projekten",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "maritime_logistik": {
        "name": "Maritime Logistik",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "maschinendynamik": {
        "name": "Maschinendynamik",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "mathematik_1": {
        "name": "Mathematik 1",
        "beschreibung": "Grundlagen der Mathematik für ingenieurwissenschaftliche Anwendungen.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "mathematik_2": {
        "name": "Mathematik 2",
        "beschreibung": "Vertiefung mathematischer Methoden mit Fokus auf Analysis und lineare Algebra.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "mathematik_3": {
        "name": "Mathematik 3",
        "beschreibung": "Weiterführende mathematische Verfahren für technische Problemstellungen.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "mehrstoffthermodynamik": {
        "name": "Mehrstoffthermodynamik",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "messtechnik": {
        "name": "Messtechnik",
        "beschreibung": "Grundlagen technischer Messverfahren und Auswertung.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "metallische_konstruktionswerkstoffe": {
        "name": "Metallische Konstruktionswerkstoffe / Wärmebehandlung",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "mikrofluidik": {
        "name": "Mikrofluidik",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "modellierung_abgasnachbehandlung": {
        "name": "Modellierung und Simulation von Abgasnachbehandlungskomponenten",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "modellierung_turbulenz": {
        "name": "Modellierung und Simulation der Turbulenz",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "moderne_windenergieanlagen": {
        "name": "Moderne Windenergieanlagen",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "motor_energiemanagement": {
        "name": "Motor- und Energiemanagement für Fahrzeugantriebe",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "motorthermodynamik": {
        "name": "Motorthermodynamik",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "nachhaltige_werkstoffauswahl": {
        "name": "Nachhaltige Werkstoffauswahl und Produktentwicklung",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "nanomaterialien": {
        "name": "Nanomaterialien",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "nichtlineare_regelungssysteme": {
        "name": "Nichtlineare Regelungssysteme",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "nichtmetallische_werkstoffe": {
        "name": "Nichtmetallische Konstruktionswerkstoffe",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "nichtnewtonsche_fluidmechanik": {
        "name": "Nichtnewtonsche Fluidmechanik",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "numerik_stochastik_ing": {
        "name": "Numerik und Stochastik für Ingenieurwissenschaften",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "numerische_stroemungsmechanik": {
        "name": "Numerische Strömungsmechanik und turbulente Strömungen",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "optimierungsmethoden_mechatronik": {
        "name": "Optimierungsmethoden in der Mechatronik",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "produktionsplanung_steuerung_pps": {
        "name": "Produktionsplanung und -steuerung (PPS)",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "produktionswirtschaft": {
        "name": "Produktionswirtschaft",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "projekt_additive_fertigung": {
        "name": "Projekt Additive Fertigung",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "projekt_antriebssysteme_embedded_systems": {
        "name": "Projekt Antriebssysteme und Embedded Systems",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "projekt_konstruktionslehre": {
        "name": "Projekt Konstruktionslehre",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "projekt_produktentwicklung": {
        "name": "Projekt Produktentwicklung",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "qualitaetsmanagement": {
        "name": "Qualitätsmanagement",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "regelungstechnik": {
        "name": "Regelungstechnik",
        "beschreibung": "Einführung in Regelkreise, Systeme und deren Verhalten.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "regelungsorientierte_modellbildung_mechatronik": {
        "name": "Regelungsorientierte Modellbildung in der Mechatronik",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "regelungssysteme_zustandsraum": {
        "name": "Regelungssysteme im Zustandsraum",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "regenerative_energietechnik": {
        "name": "Regenerative Energietechnik",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "robotertechnik": {
        "name": "Robotertechnik",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "robuste_regelung": {
        "name": "Robuste Regelung und Zustandsschätzung",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "schadensanalyse_sicherheitsrelevanter_produkte": {
        "name": "Schadensanalyse sicherheitsrelevanter Produkte",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "schiffs_offshorekonstruktionen": {
        "name": "Schiffs- und Offshorekonstruktionen",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "schiffsfertigungstechnik": {
        "name": "Schiffsfertigungstechnik - Betrieb von Werften",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "schweisskonstruktion": {
        "name": "Schweißkonstruktion",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "schweissmetallurgie": {
        "name": "Schweißmetallurgie",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "schweisstechnologie": {
        "name": "Schweißtechnologie",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "simulation_werkstofftechnik": {
        "name": "Simulation in der Werkstofftechnik",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "stroemungsmechanik_grundlagen": {
        "name": "Grundlagen der Strömungsmechanik",
        "beschreibung": "Grundlagen der Strömungsmechanik und technische Anwendungen.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "strukturmechanik_fem_1": {
        "name": "Strukturmechanik und FEM 1: Grundlagen",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "strukturmechanik_fem_2": {
        "name": "Strukturmechanik und FEM 2: Erweiterte Grundlagen",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "supply_chain_management": {
        "name": "Supply Chain Management",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "technische_darstellungslehre": {
        "name": "Technische Darstellunglehre",
        "beschreibung": "Grundlagen der Konstruktionslehre.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "technische_dokumentation": {
        "name": "Technische Dokumentation",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "technische_mechanik_1": {
        "name": "Technische Mechanik 1",
        "beschreibung": "Einführung in die Technische Mechanik mit Statik und Grundprinzipien.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "technische_mechanik_2": {
        "name": "Technische Mechanik 2",
        "beschreibung": "Aufbau auf TM 1 mit weiterführenden mechanischen Zusammenhängen.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "technische_mechanik_3": {
        "name": "Technische Mechanik 3",
        "beschreibung": "Vertiefung technischer Mechanik mit anspruchsvolleren Anwendungen.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "technische_schwingungslehre": {
        "name": "Technische Schwingungslehre",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "technische_thermodynamik_2": {
        "name": "Technische Thermodynamik 2",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "technologien_meeresenergienutzung": {
        "name": "Technologien zur Meeresenergienutzung",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "theorie_offshore_systeme": {
        "name": "Theorie und Entwerfen schwimmender und gegründeter Offshore-Systeme",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "thermodynamik": {
        "name": "Thermodynamik",
        "beschreibung": "Grundlagen der Thermodynamik für Maschinenbau.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "thermodynamik_umweltprozesse": {
        "name": "Thermodynamik von Energie- und umwelttechnischen Prozessen",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "thermodynamik_verbrennung": {
        "name": "Thermodynamik der Verbrennung",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "thermische_stroemungsmaschinen": {
        "name": "Thermische Strömungsmaschinen",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "turbulenzmodellierung": {
        "name": "Modellierung und Simulation der Turbulenz",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "umformtechnisches_fuegen": {
        "name": "Umformtechnisches / Mechanisches Fügen",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "verbrennungsmotoren_1": {
        "name": "Verbrennungsmotoren 1: Konstruktionsgrundlagen emissionsarmer Verbrennungsmotoren",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "verbrennungsmotoren_2": {
        "name": "Verbrennungsmotoren 2: Brennverfahren, Abgasreinigung und Kraftstoffe für die Energiewende",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "verbrennungsmotoren_3": {
        "name": "Verbrennungsmotoren 3: Entwicklungsmethoden für Brennverfahren und Abgasreinigung",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "verbrennungsmotoren_4": {
        "name": "Verbrennungsmotoren 4: Zukunftsstrategien für klimaneutrale Mobilität",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "waerme_stoffuebertragung": {
        "name": "Wärme- und Stoffübertragung",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "werkstoffanalytik": {
        "name": "Werkstoffanalytik",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "werkstofftechnik": {
        "name": "Werkstofftechnik",
        "beschreibung": "Werkstofftechnische Grundlagen und Eigenschaften technischer Materialien.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "werkstofftechnik_2": {
        "name": "Werkstofftechnik 2: Erweiterte Grundlagen",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "windenergie_simulation": {
        "name": "Simulation von Windenergieanlagen - Einführung und praktische Anwendung",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "windenergietechnik": {
        "name": "Windenergietechnik",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    }
}

MODULES = normalize_modules(RAW_MODULES)