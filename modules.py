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

# Beschreibung (Beispiel)
# Name: "..."
# Beschreibung:
#   1. Welche Struktur hatte das Modul?
#      z. B. Vorlesung 1,5 h / Übung 1,5 h oder zusätzlich Praktika?
#   2. Welche Inhalte sind besonders wichtig und was eher Nebensächlich?
#   3. Warum ist das Modul für weiterführende Module wichtig oder nicht wichtig?
#   4. Prüfungsvorleistung:
#      Näheres: Was genau musste gemacht werden? (Inhalt, zeitlicher Aufwand etc.)

# Klausur:
#   Wie ist die Prüfungsleistung aufgebaut?
#   z. B. mündlich oder schriftlich
#   Wenn schriftlich:
#       - Rechnen / Theorie, wie ist der Aufbau?
#       - Wie viele Aufgaben gibt es?
#       - Wie viel Zeit steht zur Verfügung?
#   Wenn mündlich:
#       - Wie ist die Prüfung aufgebaut? 
#       - Was ist das Ziel in der Prüfung (z.B möglichst viele Fragen beantworten oder vielleicht eher die Fragen sehr ausführilich beantworten mit Zusatzinformationen)

# Tipps:
#   Wenn du das Modul nochmal beginnen würdest:
#       - Was würdest du vorher wissen wollen?
#       - Gibt es hilfreiche Bücher?
#       - Welche Vorleistungen sind besonders wichtig?
#       - Gibt es etwas, das man auf keinen Fall machen sollte?

# Erfahrungen:
#   1. Wann hast du das Modul belegt? (z. B. WS 2025/2026, SS 2024)
#   2. Was war besonders gut?
#   3. Was war nicht so gut?
#   4. Wie gut war die Vorbereitung auf die Klausur?
#   5. Wie passt die Note zu deinem Lernaufwand?
#   6. Würdest du das Modul im Nachhinein wieder wählen / empfehlen?

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
    "advanced_analysis_of_marine_structures": {
        "name": "Advanced Analysis of Marine Structures",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "advanced_analysis_offshore_systems": {
        "name": "Advanced Analysis of Offshore Systems",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
        },  
    "aerodynamik_hydrodynamik": {
        "name": "Aerodynamik und Hydrodynamik",
        "beschreibung": "Vorlesung 1,5 h und Übung 1,5 h. Zusätzlich gibt es einen freiwilligen Tagesausflug nach Laage. Dieses Modul ist eine Art Grundlagen in Richtung Potentialtheorie, Überschallgebiete, Verdichtungsstoß Profiltheorie und Grenzschichten. Man kann die Inhalte auch später für das Modul Numerische Strömungsmechanik gut gebrauchen. Es gibt keine Prüfungsvorleistung.",
        "klausur": "Mündliche Prüfung. Man muss einerseits die Fragen richtig beantworten, andererseits im Fragenkatalog weit kommen (d. h. viele Fragen beantworten).",
        "tipps": [
            "Vorlesungen besuchen (es werden genau diese Inhalte in der Prüfung abgefragt).",
            "Nehmt die Exkursion nach Laage unbedingt mit."
        ],
        "erfahrungen": [
            {
                "semester": "WS24/25",
                "bericht": "Ich fand, das war eines der besten Module im Studium. Die Exkursion war super. Die Prüfung war fair, aber es gibt schon viel zu lernen und zu verstehen. Ich würde mir mehr solche Module wünschen."
            }
        ]
    },
    "advanced_cpu_design": {
        "name": "Advanced CPU Design",
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
    "anatomie_und_physiologie": {
        "name": "Anatomie und Physiologie der Biomedizinischen Technik",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "angewandte_biomechanik": {
        "name": "Angewandte Biomechanik",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "angewandte_biofluidmechanik_medizintechnik": {
        "name": "Angewandte Biomfluidmechanik für Medizintechnik",
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
    "ausgewaehlte_anwendung_regelungstechnik": {
        "name": "Ausgewählte Anwendungen der Regelungstechnik",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "ausgewaehlte_fertigungsverfahren": {
        "name": "Ausgewählte Fertigungsverfahren",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "ausgewaehlte_kapitel_der_biomedizinischen_technik": {
        "name": "Ausgewählte Kapitel der Biomedizinischen Technik",
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
    "automobile_produktion": {
        "name": "Automobile Produktion",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "balance": {
        "name": "BALANCE - Einführung in interdisziplineres Denken",
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
    "bild_videoverarbeitung_und_codierung": {
        "name": "Bild-/Videverarbeitung und Codierung",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "biofilm_medizin_technik": {
        "name": "Biofilm in Medizin und Technik",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "biomaterialieneinsatz_und_prüfung": {
        "name": "Biomaterialieneinsatz und -prüfung",
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
    "biomedizinische_technik": {
        "name": "Biomedizinische Technik",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
     "bruch_schaedigungmechanik": {
        "name": "Bruch- und Schädigungsmechanik",
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
    "cfd_fuer_schiffshydrodynamik": {
        "name": "CFD für Schiffshydrodynamik",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "cfd_maritime_engineering": {
        "name": "CFD in Maritime Engineering",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
        },
    "coding_of_finite_elements": {
        "name": "Coding of Finite Elements",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "compact_modeling_large_scale_dynamical_system": {
        "name": "Compact Modeling of Large Scale Dynamical Systems",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
        },
    "composite_material_design": {
        "name": "Composite Material Design",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
        },
    "computational_modelling_of_biomaterials_and_their_interaction_with_tissue": {
        "name": "Computational modelling of biomaterials and their interaction with tissue",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "computational_methods_in_fluid_dynamics": {
        "name": "Computational Methods in Fluid Dynamics",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "computer_aided_design": {
        "name": "Computer Aided Design",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "computerorientierte_mathematik_algorithmen_strukturen": {
        "name": "Computerorientierte Mathematik, Algorithmen und Strukturen",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "continuum_mechanics": {
        "name": "Continuum Mechanics",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "data_driven_methods_in_signal_processing": {
        "name": "Data-Driven Methods in Signal Processing",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "deep_learning": {
        "name": "Deep Learning",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "deep_sea_technology_underwater_applications": {
        "name": "Deep-Sea Technology and Practical Applications of Underwater Technology",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "deskriptive_statistik*": {
        "name": "Deskriptive Statistik*",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "design_offshore_aquaculture_systems": {
        "name": "Design of Offshore Aquaculture Systems",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "design_offshore_systems": {
        "name": "Design of Offshore Systems",
        "beschreibung": "Decription incoming",
        "klausur": "No informations",
        "tipps": [],
        "erfahrungen": []
    },
    "design_underwater_systems": {
        "name": "Design of Underwater Systems",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "dienstleistungsmarketing": {
        "name": "Dienstleistungsmarketing",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "digitale_datenuebertragung": {
        "name": "Digitale Datenübertragung",
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
    "digitale_signalverarbeitung": {
        "name": "Digitale Signalverarbeitung",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "deutsch_a11": {
        "name": "Deutsch A1.1",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "deutsch_a12": {
        "name": "Deutsch A1.2",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "dynamic_behavior_ac_mashine": {
        "name": "Dynamic Behavior of AC Machines",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "dynamics_multibody_systems": {
        "name": "Dynamics of Multibody Systems",
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
    "dynamik_von_schiffen_und_offshore_strukturen": {
        "name": "Dynamik von Schiffen und Offshore Strukturen",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "echtzeitsysteme": {
        "name": "Echtzeitsysteme",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "einfuehrung_betriebswirtschaftsliche_steuerlehre": {
        "name": "Einführung in die betriebswirtschaftsliche Steuerlehre",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "einfuehrung_betriebswirtschaftslehre": {
        "name": "Einführung in die Betriebswirtschaftslehre",
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
    "einfuehrung_data_science": {
        "name": "Einführung in die Data Science in Materialwissenschafte und Ingenieurwesen",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "einfuehrung_digitale_umrichtersteuerung": {
        "name": "Einführung in die digitale Umrichtersteuerung",
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
    "einfuehrung_wirtschaftsrecht": {
        "name": "Einführung ins Wirtschaftsrecht",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "eingebettete_multi_prozessor_systeme": {
        "name": "Eingebettete Multi-Prozessor-Systeme",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "elektrische_fahrzeugantriebe": {
        "name": "Elektrische Fahrzeugantriebe",
        "beschreibung": "Grundlagen der Elektrotechnik für Maschinenbauer.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "elektrotechnik": {
        "name": "Einführung im die Elektrotechnik für Maschinenbau",
        "beschreibung": "Das Modul umfassen drei mal 45-minütige Vorlesungen als auch Übungen, welche sich von zwei Lehrpersonen geteilt werden: Elektrotechnik und elektrische Maschinen. Hier lernt man die Grundlagen zum Thema Strom, Spannung, Widerstand, als auch Magnetismus, Stromkreise und verschiedenen Maschinen, welche man beschreiben und berechnen muss. Als Klausurvorleistung muss man die Kurzfragentest vor jedem „Praktikum“ bestehen, als auch ein Protokoll des jeweiligen Versuches anfertigen, welche aus dem Deckblatt, einer Hausaufgabe, Berechnungen von Messwerten, Zeichnungen von Diagrammen und einer Auswertung bestehen.",
        "klausur": "Die Klausur ist schriftlich mit Rechen- und Theorieaufgaben. Es kommen Teile aus dem Bereich Elektrotechnik und Rechenaufgaben aus dem Bereich elektrische Maschinen. Die Klausur orientiert sich sehr stark an der letzten Übung und der Konsultation.",
        "tipps": [
            "Unbedingt die Konsultation und die Übungen besuchen, da hier Aufgaben gerechnet werden, die sehr ähnlich sind zu den Klausuraufgaben.",
            "Bei den Praktika eine klare Aufgabenverteilung in der Gruppe haben, damit man direkt schnell loslegen kann, da man nur eine Woche für das Protokoll Zeit hat.",
            "In der ersten Vorlesung wird der Ablaufplan veröffentlicht. Manchmal hat man zwei Vorlesungen in der Woche, mal eine Übung, mal ein Praktikum.",
            "Anfang Januar wechselt die Lehrperson und kündigt eigene Termine an.",
        ],
        "erfahrungen": [
            {
                "semester": "WS24/25",
                "bericht": "Bei Dr. Schaeper kann man bei Nichtbestehen der Testate diese beliebig oft wiederholen. Bei Sänger nur zwei Mal "
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
    "endoprothetik_und_orthopaedische_chirurgie": {
        "name": "Endoprothetik und Orthopädische Chirurgie",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "englisch_fachkommunikation_el_technik_info_c11":{
        "name": "Englisch Fachkommunikation Elektrotechnik/Informationstechnik C1.1 GER",
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
    "englisch_fachkommunikation_wiwi_c11": {
        "name": "Englisch Fachkommunikation Wirtschaftswissenschaften C1.1 GER",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },"englisch_fachkommunikation_wiwi_c12": {
        "name": "Englisch Fachkommunikation Wirtschaftswissenschaften C1.2 GER",
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
    "entwerfen_von_schiffen": {
        "name": "Entwerfen von Schiffen",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "erfolgsfaktoren_beruflicher_selbstaendigkeit": {
        "name": "Erfolgsfaktoren beruflicher Selbstständigkeit",
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
    "essentials_ocean_science_and_sustainable_ocean_use": {
        "name": "Essentials of Ocean Science and Sustainable Ocean Use",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "experimental_methods_maritime_engineering": {
        "name": "Experimental Methods in Maritime Engineering",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },  
    "experimentelle_stroemungsmechanik": {
        "name": "Experimentelle Strömungsmechanik",
        "beschreibung": " Das Modul teilt sich in zwei Phasen: Zuerst gibt es 8 Wochen lang eine 2-stündige Vorlesung (120 min). Diese wird komplett an der Tafel geschrieben, das heißt, man muss alles mitschreiben. Der Dozent lädt auf nette Nachfrage aber auch die einzelnen Videos aus der Coronazeit hoch. Danach folgen 6 Wochen mit Versuchen: Es findet jede Woche ein Versuch statt, der meistens 1 bis 1,5 Stunden dauert. Man arbeitet in Gruppen und trägt sich dafür irgendwann ein. Es werden unterschiedliche experimentelle Messmethoden behandelt, wie zum Beispiel PIV, LDA usw. Prüfungsvorleistung sind die Protokolle. Jede Gruppe muss zu jedem Versuch jeweils ein Protokoll abgeben. Wenn man 6 Mitglieder in der Gruppe hat, gibt jede Person ein Protokoll ab. Wenn es nur 3 Personen sind, schreibt jede Person zwei Protokolle usw.",
        "klausur": "Mündliche Prüfung: 30 Minuten. Es werden meistens Fragen zu den experimentellen Verfahren aus den Versuchen gestellt. Jedoch sollte man alles lernen, man weiß nie.",
        "tipps": [
            	"Versuche sind essenziell.",
                "Fotografiert alles bei den Versuchen ab.",
                "Schreibt euch auf, was ihr bei den Versuchen macht und warum."
        ],
        "erfahrungen": [
            {
            "semester":"WS25/26",
            "bericht":"Bis jetzt eines der schwersten Module im Studium da man nicht wusste genau, was man lernen soll und in welchem Ausmaß. Es war sehr, sehr viel Stoff, teilweise auch mit vielen veralteten Experimenten. Der Stoff, der in den Vorlesungen vermittelt wurde, war sehr mathelastig, was in der Prüfung leider nur wenig gebracht hat, da dort eher Verständnisfragen gestellt wurden und sehr viel in die Tiefe gefragt wurde. Die Versuche sind aber super und haben total Spaß gemacht. Diese würde ich allen empfehlen, besonders das MRI und PIV."
            }
        ]
    },
    "experimenteller_leichtbau": {
        "name": "Experimenteller Leichtbau",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },

    "fabrikplanung": {
        "name": "Fabrikplanung und Automatisierung",
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
    "fehlerdiagnose_und_fehlertoleranz_in_technischen_systemen": {
        "name": "Fehlerdiagnose und Fehlertoleranz in technischen Systemen",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "fertigungslehre": {
        "name": "Fertigungslehre",
        "beschreibung": "Das Modul umfassen 90-minütige Vorlesungen, als auch fünf Übungen. Hier lernt man die verschiedenen Herstellungs- und Weiterverarbeitungsmöglichkeiten von Werkstoffen. Also der Weg von „Wie schaffe ich meinen Stahl“ über „Mit welchen Werkzeugen und Methoden, kann ich den Stahl verändern“ bis „Welche Eigenschaften soll der Stahl haben“. Als Prüfungsvorleistung müssen vier der fünf Kurzfragentest am Anfang jede Übung erfolgreich bestanden werden.",
        "klausur": "Die Klausur ist schriftlich. Es dürfen zwei Seiten Spicker (laut unseren letzen Information, prüft das aber bitte!) mit in die Klausur genommen werden, wobei diese am besten komplett ausgenutzt werden sollten, da Theorie, Skizzen und Diagramme abgefragt werden.",
        "tipps": [
            "Die Spickzettel sollten rechtzeitig angefangen werden, da sehr viel Stoff, inklusive Zeichnungen zusammengefasst werden muss.",
            "Jedes Jahr wird ein Exkurs in das Stahlwerk Salzgitter angeboten, wo man sich den theoretischen Stoff in der Praxis anschauen kann."
        ],
        "erfahrungen": []
    },
    "fertigungsmittel": {
        "name": "Fertigungsmittel",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "festigkeitsoptimiertes_bruchsicheres": {
        "name": "Festigkeitsoptimiertes und bruchsicheres Gestalten",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "fluid_dynamik": {
        "name": "Fluid Dynamik",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "finanzbuchhaltung": {
        "name": "Finanzbuchhaltung",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "finanzierung_investition": {
        "name": "Finanzierung und Investition 1",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "finanzierung_investition_2": {
        "name": "Finanzierung und Investition 2",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "finite_element_analysis_composite_structures": {
        "name": "Finite Element Analysis of Composite Structures",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "finite_elemente_analyse_verbundwerkstoffstrukturen": {
        "name": "Finite-Elemente-Analyse von Verbundwerkstoffstrukturen",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "fortgeschrittene_elektronik_schaltkreisentwurf": {
        "name": "Fortgeschrittene Elektronik und Schaltkreisentwurf",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "geraetetechnik": {
        "name": "Gerätetechnik",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "geraetetechnik_und_sensorik_in_der_biomedizinischen_technik": {
        "name": "Gerätetechnik und Sensorik in der Biomedizinischen Technik",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "geregelte_elektrische_antriebe": {
        "name": "Geregelte Elektrische Antriebe",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "gewaesserregelung_kuesten_hochwasserschutz": {
        "name": "Gewässerregelung, Küten- und Hochwasseschutz",
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
    "grundlagen_angewandten_muskuloskelettalen_biomechanik_orthopaedietechnik": {
        "name": "Grundlagen der angewandten muskulo-skelettalen Biomechanik und Orthopädietechnik",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "grundlagen_automatisierung": {
        "name": "Grundlagen der Automatisierung",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "grundlagen_bevölkerungsökonomik": {
        "name": "Grundlagen der Bevölkerungsökonomik",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "grundlagen_chemie": {
        "name": "Grundlagen der Chemie",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "grundlagen_controlling": {
        "name": "Grundlagen des Controllings",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "grundlagen_elektronik": {
        "name": "Grundlagen der Elektronik 1",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "grundlagen_fuegetechnik": {
        "name": "Grundlagen der Fügetechnik",
        "beschreibung": "Es sind immer zwei 1,5h Veranstaltungen pro Woche. Übung wird nur bei Bedarf abgehalten (z.B. Verspannungsschaubild! geht hin! spart Lernzeit). Es gibt auch noch 2-3 freiwillige Exkursionen in Fraunhofer-nahe Betriebe (z.B.EEW, Nordex, Liebherr). Behandelt werden, mehr oder weniger, die Grundlagen aller gängigen Fügeverfahren. Jeder Themenbereich wird von einem jeweiligen Dozenten des Fraunhofer IGP abgehalten (Kleben, Schrauben, Nieten, Schweißen). Klebtechnik wird sehr ausführlich behandelt (mind. 4 Vorlesungen). Mechanische Verbindungstechnik (Schrauben) schließt Wissenslücken der KL-Module. Umformtechnisches Fügen (Nieten) und Schweißtechnik werden auch behandelt, ist aber nicht im Fokus. Insgesamt das Module bildet eine gute Basis für weiterführende Module Richtung Leichtbau und Fertigungstechnik im Master, sind jedoch nicht zwingend notwendig. Es gibt keine Prüfungsvorleistung",
        "klausur": "Mündlich, 30min. Es werden drei Themengebiete abgefragt, in jedem Fall Klebtechnik! Geprüft werdet ihr, in der Regel, von euren Dozenten",
        "tipps": [
            "geht zu den Übungen. Wenn das Thema Schrauben geprüft wird, müsst ihr das Verspannungsschaubild aus dem FF kennen, was ihr nach der Übung könnt. ",
            "Schwänzt nicht zu viele Vorlesungen. Eure Dozenten werden eure Prüfer sein. Je besser ihr euch kennt, desto entspannter wird die Mündliche.",
            "Wenn ihr euch durch die Veranstaltungen schleift, habt ihr die Chance mit sehr wenig Lern- und Freizeitaufwand eine sehr gute Note zu ergattern."
        ],
        "erfahrungen": [
            {
                "semester": "WS24/25",
                "bericht": "Vorteil: derZeitaufwand zu Prüfunslesitung ist sehr gering. Nachteil: Themengebiete können sehr trocken werden. Vertretungsdozent mussten sehr oft einspringen, ohne genug Zeit die Folien vorbereiten zu können. Sonst gilt die Letzte Vorlesung als Konsultation. Wenn ihr keine Fragen habt, wird nichts beantwortet. Das Modul würde nicht unbedingt weiterempfehlen, da es oft Trocken werden kann. Anderseits kann man gut Kontakte in der regionalen Industrie aufbauen."
            }
        ]
    },
    "grundlagen_hydromechanik_schiffen_offshore": {
        "name": "Grundlagen der Hydromechanik von Schiffen und Offshore-Strukturen",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "grundlagen_materiner_stoffkreislaeufe": {
        "name": "Grundlagen der Materialflusstechnik",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "grundlagen_materialflusstechnik": {
        "name": "Grundlagen mariner Stoffkreisläufe",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "grundlagen_schiffstechnik": {
        "name": "Grundlagen der Schiffstechnik",
        "beschreibung": "Ein 90-minütige Vorlesung und Übungsvorlesung. Man beschäftigt sich mit der allgemeinen Einteilung von Schiffen (nach Gruppen), außerdem mit dem Entwurfsprozess. Die Schwimmstabilität wird in den letzten Vorlesungen ebenfalls zu einem wichtigen Thema. In der Übung geht es eher um etwas Praktisches und nicht nur um Rechenübungen, obwohl man auch ein bisschen rechnen muss. Prüfungsvorleistung sind 4 Belege: 1. Rechnen, 2. Modellieren, 3. Rechnen mit Software, 4. Dokumentation abgeben",
        "klausur": "Mündliche Prüfung: an sich fragen die genau das was in der Vorlesungen besprochen wurde.",
        "tipps": [
        ],
        "erfahrungen": [
            {
                "semester": "SS25",
                "bericht": "Ich fand das Modul sehr gut, sowohl die Struktur als auch die Inhalte und alles, was man dabei gelernt hat. Der Umgang mit der Software Rhinoceros 3D war ebenfalls eine wertvolle Erfahrung für später. Ich habe viel gelernt. Die Prüfung war allerdings recht knackig; man musste schon ordentlich lernen."
            }
        ]
    },
    "grundlagen_statistik": {
        "name": "Grundlagen der Statistik",
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
    "grundzüge_dienstleistungsmanagement": {
        "name": "Grundzüge des Dienstleistungsmanagements",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "grundzüge_moderner_oekonomie": {
        "name": "Grundzüge der modernen Ökonomie",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "hochintegrierte": {
        "name": "Hochintegrierte [wie heist das]",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "hochtemperaturelektronik": {
        "name": "Hochtemperaturelektronik - Konstruktion und Fertigung",
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
    "ideenfindung_entwicklung": {
        "name": "Ideenfindung und -entwicklung",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "implantattechnologie": {
        "name": "Implantattechnologie",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "industrial_engineering": {
        "name": "Industrial Engineering",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "informatik": {
        "name": "Informatik 1: Einführung in die Programmierung",
        "beschreibung": "Einführung in informatische Grundlagen und technische Anwendungen.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "informatik_wissenschaft_gesellschaft": {
        "name": "Informatik - Wissenschaft und Gesellschaft",
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
    "introduction_applied_programming_cpp": {
        "name": "Introduction to Applied Programming in C++",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "introduction_data_science_materials": {
        "name": "Introduction to Data Science in Materials Science and Engineering",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "ip_management_in_der_medizintechnik": {
        "name": "IP-Management in der Medizintechnik",
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
    "kanalcodierung": {
        "name": "Kanalcodierung",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "kardiovakulaere_implantate": {
        "name": "Kardiovaskuläre Implantate",
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
    "kolben_stroemungsmaschinen": {
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
        "beschreibung": "Das Modul geht über zwei Semester und besteht aus 90-minütigen Vorlesungen und Übungen, wobei ein Tutorium nur in der ersten Hälfte vorgesehen ist. Hier lernt man wie Bauteile in technischen Zeichnungen erkennt, zeichnet, modelliert, deren Ausmaße und Festigkeit berechnet und nachweist. Das Hauptaugenmerk liegt hierbei auf den Berechnungen. Die Klausurvorleistung beinhalten Handzeichnungen, Online-Fragetest, 3D-Modellierungen, und Berechnungen.",
        "klausur": "Die Klausur findet erst im 3.ten Semester statt und umfasst zwei mal drei Teile: jeweils einen Theorie-, einen Zeichen- und einen Rechenteil pro Semester (Kl2 im SS und Kl3 im WS). Es ist möglich, dass bald die Klausur zusammengefasst wird und nicht mehr 2 mal 3 Teile hat sondern, nur 3 Große Teile sind.",
        "tipps": [
            "Unbedingt die Übungen und Tutorien besuchen, da dies die Grundlagen der Belege sind und dort Fragen beantwortet werden können.",
            "Die Belege sollte man rechtzeitig anfangen, da sie teilweise recht umfangreich sind und, je perfektionistischer man ist, auch gut über mehr als 10 Stunden gehen können. Vor allem der letzte „Komplexbeleg“ ist sehr kompliziert und zeitaufwendig.",
            "Die Onlinetests nicht auf den letzten Drücker machen, da vor allem die Rechentest aufwendig sind.",
        ],
        "erfahrungen": [
            {
            "semester": "WS24/25",
            "bericht": "Für die Belege und die Klausur habe ich mir das Tabellenbuch Metall besorgt, da hier viele Ausschnitte aus wichtigen Normen sind, welche man oft benötigt. Die Vorlesung habe ich nicht regelmäßig besucht, da ich mit den Folien allein besser klargekommen bin. Wenn man früh anfängt für die Klausur zu lernen, und sich Mühe beim Spickerschreiben gibt, ist die Klausur sehr gut machbar "
            }
        ],
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
    "kosten_leistungsrechnung": {
        "name": " Kosten- und Leistungsrechnung (KLR)",
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
    "labor_werkstofftechnik": {
        "name": "Laborpraktikum Werkstofftechnik",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "labor_thermodynamik_stroemungsmaschinen_und_verbrennungsmotoren": {
        "name": "Laborpraktikum Thermodynamik, Strömungsmaschinen und Verbrennungsmotoren",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "labor_werkstofftechnik": {
        "name": "Laborpraktikum Werkstofftechnik",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "large_engines_energy_converters_fuels": {
        "name": "Large Engines, Energy Converters and Fuels for Climate Neutral Marine Applications",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "leckstabilitaet_und_kentersicherheit": {
        "name": "Leckstabilität und Kentersicherheit",
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
    "leistungshalbleiter": {
        "name": "Leistungshalbleiter",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "logistik": {
        "name": "Logistik und Kreislaufwirtschaft",
        "beschreibung": "Es geht um Logistik und Kreislaufwirtschaft in der industriellen Anwendung. Prof. Sender gibt sehr viele praxisnahe Beispiele.",
        "klausur": "Bisher keine genauen Infos zur Prüfungsform eingetragen.",
        "tipps": [
            "Begriffe und Modelle früh lernen.",
            "Praxisbeispiele mit den theoretischen Inhalten verknüpfen."
        ],
        "erfahrungen": [
            {
                "semester": "WS24/25",
                "bericht": "Inhaltlich spannend wegen der Praxisnähe, aber an manchen Stellen recht trocken."
            }
        ]
    },
    "management_entwicklungsteams_projekten": {
        "name": "Management von Entwicklungsteams und Projekten",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "maritime_graphics": {
        "name": "Maritime Graphics",
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
    "maritime_sensorik": {
        "name": "Maritime Sensorik",
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
        "name": "Mathematik 1: Grundlagen und eindimensionale Analysis",
        "beschreibung": "Das Modul beinhaltet eine 3 mal 45-minütige Vorlesung als auch 90-minütige Übungen und Tutorien. Hier lernt man die ersten mathematischen Grundlagen, die auf der Schulmathematik aufbauen und im Laufe des Studiums gebraucht werden: Von Mengenlehre und was Reihen sind, über imaginäre Zahlen, bis hin zu Integralen, Ableitungen und Differentialgleichungen. Als Klausurvorleistung müssen wöchentliche Hausaufgaben abgegeben werden, wo man mindestens 50% der möglichen Punkte erreichen muss.",
        "klausur": "Schriftliche Klausur: Bei Prof. Wagner ist die Klausur sehr ähnlich zur Probeklausur. Echt sehr ähnlich. Bei Dr. Just: Die Klausur ist schriftlich und besteht aus einem Kurzrechenteil, wo nur die Antworten zählen, und einem Teil, wo größere Aufgaben mit mehreren Unteraufgaben gestellt werden und Lösungswege abgefragt werden.",
        "tipps": [
            "Geht unbedingt zu der ersten Vorlesung, da erklären die Profs immer was genau zu beachten ist und wie alles aufgebaut ist. Jedes Jahr kann etwas neues dazu kommen, was hier noch nicht steht.",
            "Macht die Serien ordentlich und schreibt euch das gut auf (mit einem guten System). Ihr werdet im Studium noch weiter darauf zurückgreifen. ",
            "Falls ihr die Klausur nicht schreiben wollt, macht trotzdem die Zulassung. Ihr werdet euch ärgern, wenn ihr das nicht vorher fertig macht.",
            "Die wöchentlichen Aufgabenserien gründlich bearbeiten und in den Übungen mitmachen, sodass man den Stoff versteht.",
            "o	Nehmt euch Zeit die Übungsserien zu bearbeiten, da sie teilweise sehr aufwendig sein können und man ein paar Stunden vor den Aufgaben sitzt."
        ],
        "erfahrungen": [
            {
                "semester": "WS24/25",
                "bericht":  "Bei Dr. Just wurde die Klausur als open book geschrieben, sodass man sämtliche Vorlesungs- und Übungsmaterialien mit in die Prüfung nehmen durfte. Das mehrfache Rechnen der Probeklausur und wiederholen der Übungsaufgaben hat mir sehr geholfen in der Klausur."
            }
        ]
    },
    "mathematik_2": {
        "name": "Mathematik 2: Lineare Algera und Geometrie",
        "beschreibung": "Vertiefung mathematischer Methoden mit Fokus auf Analysis und lineare Algebra.",
        "klausur": "Die Klausur ist schriftlich und besteht aus einem Kurzrechenteil, wo nur die Antworten zählen, und einem Teil, wo größere Aufgaben mit mehreren Unteraufgaben gestellt werden und Lösungswege abgefragt werden.",
        "tipps": [],
        "erfahrungen": [
            {
                "semester": "WS24/25",
                "bericht":  "Bei Dr. Just wurde die Klausur als open book geschrieben, sodass man sämtliche Vorlesungs- und Übungsmaterialien mit in die Prüfung nehmen durfte. Das mehrfache Rechnen der Probeklausur und wiederholen der Übungsaufgaben hat mir sehr geholfen in der Klausur."
            }
        ]
    },
    "mathematik_3": {
        "name": "Mathematik 3: Differenzialgleichungen und mehrdimensionale Analysis",
        "beschreibung": "Weiterführende mathematische Verfahren für technische Problemstellungen.",
        "klausur": "Die Klausur ist schriftlich und besteht aus einem Kurzrechenteil, wo nur die Antworten zählen, und einem Teil, wo größere Aufgaben mit mehreren Unteraufgaben gestellt werden und Lösungswege abgefragt werden",
        "tipps": [],
        "erfahrungen": [
            {
                "semester": "WS24/25",
                "bericht":  "Bei Dr. Just wurde die Klausur als open book geschrieben, sodass man sämtliche Vorlesungs- und Übungsmaterialien mit in die Prüfung nehmen durfte. Das mehrfache Rechnen der Probeklausur und wiederholen der Übungsaufgaben hat mir sehr geholfen in der Klausur."
            }
        ]
    },
    "mathematische_modelle_in_der_schiffstheorie": {
        "name": "Mathematische Modelle in der Schiffstheorie",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "medizinische_grundlagen": {
        "name": "Medizinische Grundlagen für Studierende der Biomedizintechnik: Labordiagnostik, Pathologie, Mikrobiologie, Abwehsysteme",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "medizinische_technologie_bildgebende_verfahren": {
        "name": "Medizinische Technologie / Bildgebende Verfahren",
        "beschreibung": "Beschreibung folgt.",
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
    "meeresforschungstechnik": {
        "name": "Meeresforschungstechnik",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "messtechnik": {
        "name": "Grundlagen der Messtechnik",
        "beschreibung": "Grundlagen technischer Messverfahren und Auswertung.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "messtechnik_analoge_schaltungen": {
        "name": "Messtechnik und Analoge Schaltungen",
        "beschreibung": "Grundlagen technischer Messverfahren und Auswertung.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "metallic_engineering_materials": {
        "name": "Metallic Engineering Materials",
        "beschreibung": "Beschreibung folgt.",
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
    "mikrosystemtechnologie": {
        "name": "Mikrosystemtechnologie",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "mikrotechnologie_aktore_sensoren": {
        "name": "Mikrotechnologie - Aktoren und Sensoren",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "mobilkommunikation": {
        "name": "Mobilkommunikation",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "modellbildung_simulation_technischer_systeme": {
        "name": "Modellierung und Simulation technischer Systeme",
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
    "modellierung_und_simulation_der_turbulenz": {
        "name": "Modellierung und Simulation der Turbulenz",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "modelling_turbulent_flows": {
        "name": "Modelling and Simulation of Turbulent Flows",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "modeling_symulation_mechatronic_systems": {
        "name": "Modeling and Simulation of Mechatronic Systems",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "moderne_methoden_regelungstechnik": {
        "name": "Moderne Methoden der Regelungstechnik",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "moderne_physik_ingenieurwissenschaften": {
        "name": "Moderne Physik für Ingenieurwissenschaften",
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
    "navigation_control_autonomy_systems": {
        "name": "Navigation, Control and Vehicle Autonomy of Maritime Systems",
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
    "numerical_and_experimental_hydroacoustics": {
        "name": "Numerical and Experimental Hydroacoustics",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "numerical_fluid_mechanics_turbulent_flows": {
        "name": "Numerical Fluid Mechanics and Turbulent Flows",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "numerik_fuer_ingenieurwissenschaften": {
        "name": "Numerik für Ingenieurwissenschaften",
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
    "beschreibung": "Typisches Modul mit 1,5 h Übung und 1,5 h Vorlesung. Inhaltlich geht es hauptsächlich um numerische Simulationen von Strömungen. Behandelt werden der gesamte Ablauf von der Formulierung des physikalischen Problems über die räumliche und zeitliche Diskretisierung bis hin zur Aufstellung und Lösung des Gleichungssystems. Ein besonderer Schwerpunkt liegt auf der Finite-Differenzen- und der Finite-Volumen-Methode. Zusätzlich werden die Ansätze RANS, DNS und LES miteinander verglichen und ein erster Einblick in turbulente Strömungen gegeben. Das Modul bietet eine sehr gute Grundlage, um spätere Simulationsprogramme und deren Aufbau besser zu verstehen.",
    "klausur": "Mündliche Prüfung. Im Wesentlichen werden die Inhalte der Vorlesung systematisch durchgegangen. Der Fokus liegt darauf, den gesamten Prozess einer Strömungssimulation erklären zu können, vom physikalischen Problem bis zur numerischen Lösung. Typisch für die Prüfung bei Grundmann ist, im Fragenkatalog möglichst weit zu kommen und die Fragen ausführlich sowie verständlich zu beantworten. Es gibt keine Prüfungsvorleistung.",
    "tipps": [
        "Die Übungen zu Vorwärts-, Rückwärts- und ähnlichen numerischen Verfahren sind sehr hilfreich.",
        "Unbedingt die Konsultationen von Hüttmann nutzen, besonders wenn bereits konkrete Fragen gesammelt wurden.",
        "Die Vorlesungen regelmäßig besuchen, da die Prüfung sehr nah an den dort erklärten Inhalten orientiert ist."
    ],
    "erfahrungen": [
        {
            "semester": "WS24/25",
            "bericht": "Sehr cooles Modul, definitiv nicht eines der leichtesten, aber wenn man Interesse an dem Thema hat, macht es wirklich Spaß. Die Dozenten sind super engagiert und sehr studentennah. Die mündliche Prüfung war total angenehm. Durch die entspannte Art der beiden war die Aufregung schnell weg. Insgesamt war die Note genau wie erwartet, und das Verhältnis von Aufwand zu Ergebnis war wirklich gut."
            }
    ]
},
    "open_space": {
        "name": "Open Space",
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
    "ocean_renewable_energies": {
        "name": "Ocean Renewable Energies",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "ocean_research_technologies": {
        "name": "Ocean Research Technologies",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "ocean_waves": {
        "name": "Ocean Waves",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "personlawirtschaftslehre_organisationen": {
        "name": "Personalwirtschaftslehre und Verhalten Organisationen",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "polymere_als_biomaterialien": {
        "name": "Polymere als Biomaterialien",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "power_system_control_protection": {
        "name": "Power System Control and Protection",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "power_system_dynamic_stability_control": {
        "name": "Power System Dynamic Stability and Control",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "principle_analysis_of_marine_structures": {
        "name": "Principle Analysis of Marine Structures",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "principles_of_energy_technology_systems_and_applications_in_maritime_context": {
        "name": "Principles of energy technology: systems & applications in maritime context",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "principles_of_marine_fluid_mechanics": {
        "name": "Principles of marine fluid mechanics",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "produktionsplanung_steuerung": {
        "name": "Produktionsplanung und -steuerung",
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
    "project_seminar_power_electronics": {
        "name": "Project Seminar Power Electronics",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "projektseminar_entwurf_simulation_elektronischer_baugruppen": {
        "name": "Projektseminar Entwurf und Simulation elektronischer Baugruppen",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "propellertheorie": {
        "name": "Propellertheorie",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "prozessautomation_robotik": {
        "name": "Prozessautomation und Robotik",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "prozessmesstechnik": {
        "name": "Prozessmesstechnik",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "python_data_analysis": {
        "name": "Python for data analysis and visualization",
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
    "radio_navigation_and_radar": {
        "name": "Radio Navigation and Radar",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "reasoning_under_uncertainty": {
        "name": "Reasoning under Unsertainty",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "rechnerarchitekturen_fuer_deep_learning_anwendungen": {
        "name": "Rechnerarchitekturen für Deep Learning Anwendungen",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "rechnergestuetzte_entwicklungsmethoden_in_der_schiffs_und_meerestechnik": {
        "name": "Rechnergestützte Entwicklungsmethoden in der Schiffs- und Meerestechnik",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "rechnetgestützter_reglerentwurf": {
        "name": "Rechnergestützter Reglerentwurf",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "regelungstechnik": {
        "name": "Systemdynamik und Regelungstechnik",
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
    "renewable_energy_grid_connection_controller_design_grid_code_requirements": {
        "name": "Renewable Energy: Grid Connection, Controller Design and Grid Code Requirements",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "renewable_energy_sources": {
        "name": "Renewable Energy Sources",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "resistance_propulsion": {
        "name": "Resistance and Propulsion",
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
    "robust_control": {
        "name": "Robust Control ans State Estimation",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "robuste_regelung_zustandsschaetzung": {
        "name": "Robuste Regelung und Zustandsschätzung",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "safety_maritime_systems": {
        "name": "Safety of Marine Systems",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "sailing_theory": {
        "name": "Sailing Theory",
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
     "sea_loads_on_offshore_structures_emship": {
        "name": "Sea loads on Offshore structures",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "seakeeping_manoeuvring": {
        "name": "Seakeeping and Manoeuvring",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "selected_topics_for_the_analysis_of_marine_structures": {
        "name": "Selected Topics for the Analysis of Marine Structures",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "sensorik": {
        "name": "Sensorik",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "seminar_stroemungs_und_windenergietechnik": {
        "name": "Seminar Strömungs- und Windenergietechnik",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "ship_design": {
        "name": "Ship design",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "ship_life_cycle_digitalization": {
        "name": "Ship Life Cycle Digitalization",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "signal_systemtheorie": {
        "name": "Signal- und Systemtheorie",
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
    "steuerungstechnik": {
        "name": "Steuerungstechnik",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "strategisches_marketing": {
        "name": "Strategisches Marketing",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "stochastik": {
        "name": "Stochastik für Ingenieurwissenschaften",
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
    "structural_design_marine_structures": {
        "name": "Structural Design of Marine Structures",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "structural_durability": {
        "name": "Structural Durability",
        "beschreibung": "Beschreibung folgt.",
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
    "team_project_emship": {
        "name": "Team Project EMship",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "technical_production_processes_ships": {
        "name": "Technical Production Processes of Maritime Structures and Ships",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "technical_fluids_sustainable_maritime": {
        "name": "Technical Fluids for Sustainable Maritime Applications",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "technische_darstellungslehre": {
        "name": "Technische Darstellunglehre",
        "beschreibung": "Das Modul umfassen 90-minütige Vorlesungen, Übung und Tutorien, wo man die Grundlagen des technischen Zeichnens, als auch die Zeichnung von Gegenständen in verschiedenen Ansichten lernt. Von „Wie halte ich den Bleistift richtig“ bis „Wie stelle ich zwei sich schneidende Körper da“. Als Klausurvorleistung müssen handgezeichnete Belege, als auch am PC erstellte 3D- Modelle, angefertigt werden.",
        "klausur": "Die Klausur ist schriftlich und umfasst einen Theorie- und auch meist zwei Zeichenteile",
        "tipps": [
            "Unbedingt die Übungen und Tutorien besuchen, da dies die Grundlagen der Belege sind und dort Fragen beantwortet werden können.",
            "Die Belege sollte man rechtzeitig anfangen, da sie teilweise recht umfangreich sind und, je perfektionistischer man ist, auch gut über mehr als 10 Stunden gehen können."
            "Die Theorie und die Tutorien zu den CAD-Programmen sind Grundlage für das Modul Konstruktionslehre."
        ],
        "erfahrungen": []
    },
    "technische_dokumentation": {
        "name": "Technische Dokumentation",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "technische_optik": {
        "name": "Technische Optik",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "technische_mechanik_1": {
        "name": "Technische Mechanik 1: Statik",
        "beschreibung": "Das Modul umfassen 90-minütige Vorlesungen, Übung und Tutorien, wo man die Grundlage vieler anderen Module lernt: Von der Definition einer Kraft, über die Bestimmung von Schwerpunkten eines Körpers bis hin zum Verhalten von Lagern und Stäben unter Belastung. Hierbei wird viel auf der Schulmathematik und Physik aufgebaut. Als Klausurvorleistung muss man einer der beiden kleineren Probeklausuren bestehen.",
        "klausur": "Schriftliche Klausur. Ähnlich vom Aufbau wie die Probeklausuren, vom Umfang drei bis vier Aufgaben.",
        "tipps": [
            "Die Übungen helfen beim Verständnis, da dort die Aufgaben vorgerechnet werden, während man in den Tutorien die Aufgaben selbstständig bearbeitet und den Stoff verinnerlicht.",
            "Unbedingt zu beiden Probeklausuren gehen, da etwas ähnliches auch in der Klausur drankommen könnte."
        ],
        "erfahrungen": []
    },
    "technische_mechanik_2": {
        "name": "Technische Mechanik 2: Festigkeitslehre",
        "beschreibung": "Das Modul umfassen 90-minütige Vorlesungen, Übung und Tutorien, welches auf das Modul Technische Mechanik 1 aufbaut. Hier kommt zu der Frage, welche Kräfte auf das System wirken auch die Frage, wie und ab wann sich das System unter der Belastung verändert, verbiegt und knickt. Als Klausurvorleistung muss man einer der beiden kleineren Probeklausuren bestehen.",
        "klausur": "Schriftliche Klausur. Ähnlich vom Aufbau wie die Probeklausuren, vom Umfang drei bis vier Aufgaben.",
        "tipps": [
            "Die Übungen helfen beim Verständnis, da dort die Aufgaben vorgerechnet werden, während man in den Tutorien die Aufgaben selbstständig bearbeitet und den Stoff verinnerlicht.",
            "Unbedingt zu beiden Probeklausuren gehen, da etwas ähnliches auch in der Klausur drankommen könnte."
        ],
        "erfahrungen": []
    },
    "technische_mechanik_3": {
        "name": "Technische Mechanik 3: Dynamik",
        "beschreibung": "Das Modul umfassen 90-minütige Vorlesungen, Übung und Tutorien, welches auf das Modul Technische Mechanik 2 aufbaut. Hier fangen die Systeme an sich zu bewegen und man erlernt die Beschreibung von Bahnenbewegungen, Stößen und Schwingungen. Als Klausurvorleistung muss man einer der beiden kleineren Probeklausuren bestehen.",
        "klausur": "Schriftliche Klausur. Ähnlich vom Aufbau wie die Probeklausuren, vom Umfang drei bis vier Aufgaben.",
        "tipps": [
            "Die Übungen helfen beim Verständnis, da dort die Aufgaben vorgerechnet werden, während man in den Tutorien die Aufgaben selbstständig bearbeitet und den Stoff verinnerlicht.",
            "Unbedingt zu beiden Probeklausuren gehen, da etwas ähnliches auch in der Klausur drankommen könnte."
        ],
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
    "theorie_und_entwerfen_schwimmender_und_gegruendeter_offshore_systeme": {
        "name": "Theorie und Entwerfen schwimmender und gegründeter Offshore-Systeme",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "theorie_und_entwerfen_von_unterwassersystemen": {
        "name": "Theorie und Entwerfen von Unterwassersystemen",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": [
            {
                "semester": "",
                "bericht": ""
            }
        ]
    },
    "thermodynamics_of_energy_and_environmental_processes": {
        "name": "Thermodynamics of Energy and Environmental Processes",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": [
            {
                "semester": "",
                "bericht": ""
            }
        ]
    },
    "thermodynamik": {
        "name": "Technische Thermodynamik 1",
        "beschreibung": "Das Modul umfassen 90-minütige Vorlesungen und Übungen. Hier lernt man welche Energieformen es gibt, wie man Systeme und Kreisläufe mit diesen beschreibt und mithilfe der Hauptsätze berechnet. Es gibt zwar keine Klausurvorleistung, doch sollte man das Modul deshalb nicht auf die leichte Schulter nehmen.",
        "klausur": "Die Klausur ist schriftlich und beinhaltet einen Theorieteil, wo Kurzfragen beantwortet werden, und einen Rechenteil, der aus ca. drei Aufgaben besteht. Die lehrstuhleigene Formelsammlung darf mitgenommen werden.",
        "tipps": [
            "Lerne mit der Formelsammlung umzugehen, da dies viel Zeit in der Klausur spart.",
            "Unbedingt die Vorlesungen besuchen, da die Tafelbilder nicht mit in den Foliensatz übernommen werden und viele Erklärungen mit Beispielen im spontanen Dialog mit dem Professor entstehen.",
            "Unbedingt die Altklausuren angucken, da viele der Theoriefragen wiederverwendet werden und manche nicht ganz so ausführlich in der Vorlesung besprochen werden."

        ],
        "erfahrungen": [
            {
                "semester": "",
                "bericht": ""
            }
        ]
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
    "umrichterregelung_erneubare_energien": {
        "name": "Umrichterregelung für Erneuerbare Energien",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "umweltverfahrenstechnik": {
        "name": "Umweltverfahrenstechnik",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "unternehmensrechnung_controlling_finanzierung": {
        "name": "Unternehmensrechnung, Controlling und Finanzierung",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "ultimate_strength_assessment_of_marine_structures": {
        "name": "Ultimate Strength Assessment of Marine Structures",
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
    "verbundwerkstoffdesign": {
        "name": "Verbundwerkstoffdesign",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "vernetzte_produktion_und_logistik": {
        "name": "Vernetzte Produktion und Logistik",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "verteilte_eingebettete_systeme": {
        "name": "Verteilte eingebettete Systeme",
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
        "name": "Werkstofftechnik 1",
        "beschreibung": "Das Modul geht über zwei Semester, wobei das erste Semester aus 90-minütigen Vorlesungen und allen zwei Wochen stattfindenden Übungen und das zweite aus Laborpraktika besteht. Hier lernt man welche verschiedenen Werkstoffe es gibt, wie sie chemisch aufgebaut sind und wie man sie behandeln kann, um die Eigenschaften des Endprodukts nach belieben zu verändern. Als Klausurvorleistung müssen die Laborpraktika bestanden werden, welche aus einer Fragerunde und einer kleinen Demonstration der verschiedenen Untersuchungsmethoden von Werkstoffen bestehen.",
        "klausur": "Die Klausur ist schriftlich. Die Probeklausuren helfen sehr, da einige Fragen der Klausur wiederverwendet werden.",
        "tipps": [
            "Unbedingt die Vorlesungen besuchen, da mit Tafelbildern gearbeitet wird, welche nicht auf den Folien übernommen wird.",
            "Wenn die Vorlesungsvideos aus der Corona-Zeit bereitgestellt werden: unbedingt mit denen lernen, da in der Klausur sehr genau auf die Wortwahl und die Definitionen geachtet wird.",
            "Gut auf die Laborpraktika vorbereiten, da man hier genau ausgefragt werden kann.",
        ],
        "erfahrungen": []
    },
    "werkstofftechnik_2": {
        "name": "Werkstofftechnik 2: Erweiterte Grundlagen",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "widerstand_und_propulsion": {
        "name": "Widerstand und Propulsion",
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
    },
    "x_ray": {
        "name": "X-ray techniques for materials characterisation",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
    "zuverlaessigkeit_und_testbarkeit_elektronischer_systeme": {
        "name": "Zuverlässigkeit und Testbarkeit elektronischer Systeme",
        "beschreibung": "Beschreibung folgt.",
        "klausur": "Noch keine Informationen zur Klausur vorhanden.",
        "tipps": [],
        "erfahrungen": []
    },
}

MODULES = normalize_modules(RAW_MODULES)