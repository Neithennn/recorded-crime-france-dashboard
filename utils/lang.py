import streamlit as st

TEXT = {
    "en": {
        "program": "Program",
        "year": "Year",
        "course": "Course",
        "professor": "Professor",
        "title": "Fewer Thefts, More Violence: How Crime Changed in France (2016–2025)",
        "source": "Source: {source} — {portal} — {license}",
        "filters": "Filters",
        "indicator": "Indicator",
        "indicator_help": "Type of crime. Each indicator has its own unit (victims, offences, vehicles, people charged).",
        "years": "Year range",
        "years_help": "Changes are computed between the first and the last year of the range.",
        "region": "Region",
        "region_help": "Leave empty to keep all of France.",
        "per_homes": "per 1,000 homes",
        "per_inhabitants": "per 1,000 inhabitants",
        "Crimes against people": "Crimes against people",
        "Crimes against property": "Crimes against property",
        "Fraud": "Fraud",
        "Drugs": "Drugs",
        "selection": "Your selection: {indicator} · {start}–{end} · {scope}",
        "all_france": "all of France",
        "kpi_cases": "Recorded cases in {end}",
        "kpi_rate": "Rate in {end}",
        "kpi_rate_help": "Recorded cases {label}",
        "kpi_top": "Highest rate in {end}",
        "kpi_top_help": "Rate {label}",
        "hook": "Ask people if crime is rising in France and most of them will say yes. "
        "The official numbers tell a more surprising story: **it depends on which crime you look at.**",
        "hook_help": "Change in recorded cases, all of France",
        "roadmap": "Two numbers going in opposite directions. This dashboard follows them in four chapters:\n"
        "1. **Thefts fall, violence rises**: which crimes go up and which go down?\n"
        "2. **Not the same story everywhere**: which regions and departments are the most affected?\n"
        "3. **Can we trust these numbers?**: data quality and limits.\n"
        "4. **What it means**: takeaways and next steps.",
        "dataset": "**Dataset:** [{name}]({url}), {portal}, {license}",
        "about_title": "About the data and the audience",
        "about": "- **Source:** SSMSI, the statistical service of the Ministry of the Interior, published on data.gouv.fr.\n"
        "- **Coverage:** crimes recorded by the police and gendarmerie, 101 departments, 16 indicators, 2016–2025.\n"
        "- **Units:** each indicator has its own unit (victims, offences, vehicles, people charged) and a rate per "
        "1,000 inhabitants (per 1,000 homes for burglaries).\n"
        "- **Audience:** citizens, students and local decision makers who want facts instead of impressions.\n"
        "- **How to use it:** the sidebar filters change every chart and every sentence written in bold.",
        "caveat": "Keep in mind: this is **recorded** crime, not real crime. A rise can come from more crimes, "
        "but also from more victims filing a complaint or from changes in how police record offences.",
        "ch1_title": "Chapter 1 · Thefts fall, violence rises",
        "ch1_headline": "**Between {start} and {end}, recorded crimes against people changed by {people:+.0f}%, "
        "while crimes against property changed by {prop:+.0f}%.**",
        "ch1_text": "On the national view, the red line starts to climb after #MeToo at the end of 2017, stops during the 2020 "
        "lockdown and then rises even faster from 2021, after the Grenelle on domestic violence. Fraud and drug cases "
        "also go up. On the other side, the blue line of thefts and damage falls in 2020 and never comes back to its "
        "2016 level.",
        "scissor_alt": "Line chart of recorded cases for the four categories of crime, with {start} set to 100. "
        "Dotted lines mark #MeToo, the Grenelle on domestic violence, the first lockdown and the fixed fine for drug use.",
        "ch1_drive": "Which crimes drive the gap?",
        "ch1_top3": "**The three biggest increases are: {top3}.**",
        "change_alt": "Horizontal bar chart of the percentage change in recorded cases for each indicator between {start} "
        "and {end}, coloured by category. Bars on the right of the grey line are increases, bars on the left are decreases.",
        "zoom_title": "Zoom on one crime: {indicator}",
        "zoom_headline": "**{indicator}: {change:+.0f}% recorded cases between {start} and {end}, the highest rate is "
        "reached in {peak}.** Choose another crime in the sidebar to follow its own story.",
        "line_title": "{indicator}: rate {label}",
        "line_alt": "Line chart of the yearly rate of {indicator} {label} from {start} to {end}, "
        "with the same dotted event lines as the chart above.",
        "ch1_transition": "*These are national numbers. But is it the same story everywhere? →*",
        "year_axis": "Year",
        "cases": "Recorded cases",
        "category": "Category",
        "indicator_axis": "Indicator",
        "change_axis": "Change (%)",
        "index_axis": "Index ({start} = 100)",
        "scissor_title": "Recorded cases by category ({start} = 100)",
        "change_title": "Change in recorded cases, {start} → {end}",
        "rate_axis": "Rate {label}",
        "region_axis": "Region",
        "department_axis": "Department",
        "ev_metoo": "#MeToo",
        "ev_grenelle": "Domestic violence Grenelle",
        "ev_lockdown": "1st lockdown",
        "ev_afd": "Fixed fine for drug use",
        "ch2_title": "Chapter 2 · Not the same story everywhere",
        "ch2_headline": "**In {end}, {region} has the highest rate of {indicator} ({rate:.2f} {label}), "
        "against {france:.2f} for all of France.**",
        "compare_regions": "Compare regions",
        "region_title": "{indicator} by region in {end}",
        "region_alt": "Horizontal bar chart of the rate of {indicator} {label} for each region in {end}, "
        "sorted from lowest to highest.",
        "map_view": "Map view",
        "map_ratio": "**At department level, {top} ({top_rate:.2f}) has {ratio:.1f} times the rate of "
        "{bottom} ({bottom_rate:.2f}).**",
        "map_top": "**At department level, {top} has the highest rate ({top_rate:.2f}).**",
        "map_title": "{indicator} by department in {end}",
        "map_alt": "Map of metropolitan France where each department is coloured by its rate of {indicator} {label} "
        "in {end}. Darker means higher. Overseas departments are not on the map but are in the other charts.",
        "top_bottom": "Top and bottom 10 departments",
        "highest": "Highest {n} in {end}",
        "lowest": "Lowest {n} in {end}",
        "highest_alt": "Bar chart of the {n} departments with the highest rate of {indicator} in {end}.",
        "lowest_alt": "Bar chart of the {n} departments with the lowest rate of {indicator} in {end}.",
        "ch2_transition": "*Before drawing conclusions, one question remains: can we trust these numbers? →*",
        "ch3_title": "Chapter 3 · Can we trust these numbers?",
        "ch3_headline": "**Mostly yes: the file is complete and consistent. But it measures what the police record, "
        "not all the crimes that happen.**",
        "missing_title": "**Missing values per column**",
        "missing_col": "Missing values",
        "duplicates": "Duplicate rows",
        "checks_title": "**Validation checks**",
        "check_col": "Check",
        "result_col": "Result",
        "check_rows": "Rows = departments x indicators x years",
        "check_negative": "No negative counts",
        "check_rate": "Rate per 1,000 matches count / population",
        "check_drugs": "Drug use = AFD + non-AFD",
        "max_error": "max error = {value:.6f}",
        "max_gap": "max gap = {value:.0f}",
        "limits": "- **Recorded crime ≠ real crime.** Only crimes reported to or found by the police are counted.\n"
        "- **Changes in recording.** Since 2020, drug use can be punished with a fixed fine (AFD). "
        "The two sub-indicators (AFD / non-AFD) were removed to avoid counting the same cases twice, "
        "only the total \"Usage de stupéfiants\" is kept.\n"
        "- **Population.** For {years} the rates use an older INSEE population, so the rates of the last years are "
        "slightly overestimated. Mayotte always uses the 2017 census.\n"
        "- **Categories.** The category lines of chapter 1 add indicators with different units (victims, offences, "
        "vehicles), they only show trends, not exact totals.\n"
        "- **Small departments.** Rare crimes (homicides) give unstable rates when the population is small.\n"
        "- **Map.** The GeoJSON only contains metropolitan France, overseas departments are only shown in the bar charts.\n"
        "- **Ethics.** The data is aggregated by department, so no person can be identified. A high rate does not mean "
        "that a territory is \"dangerous\": it also depends on how often victims report and on police activity.",
        "ch4_title": "Chapter 4 · What it means",
        "ch4_headline": "**So, is crime rising in France? Recorded violence against people is, most thefts are not, "
        "and part of the rise comes from victims speaking up more.**",
        "insights": "- Between {start} and {end}, **crimes against people rise strongly**: sexual violence {sexual:+.0f}%, "
        "domestic violence {domestic:+.0f}%, attempted murders {attempts:+.0f}%.\n"
        "- **Fraud** with means of payment also rises: {fraud:+.0f}%.\n"
        "- **Most thefts go down**: violent thefts without weapon {violent:+.0f}%, armed robberies {armed:+.0f}%, "
        "vehicle thefts {vehicles:+.0f}%, burglaries {burglaries:+.0f}%.\n"
        "- 2020 is a clear break: the lockdown lowered almost every indicator.\n"
        "- Highest rates in {end}: sexual violence in {top_sexual}, fraud in {top_fraud}, domestic violence in {top_domestic}.",
        "implications": "**Implications:** according to the SSMSI, part of the rise of sexual and domestic violence comes "
        "from more victims filing a complaint. These numbers do not prove alone that there is more violence, but they show "
        "a growing need for victim support and for police trained to receive these complaints.\n\n"
        "**Next steps:** compare with the victimisation survey (Vécu et ressenti en matière de sécurité) to separate "
        "real crime from reporting, and go down to the city level with the communal file of the same dataset.",
    },
    "fr": {
        "program": "Programme",
        "year": "Année",
        "course": "Cours",
        "professor": "Professeur",
        "title": "Moins de vols, plus de violences : comment la délinquance a évolué en France (2016–2025)",
        "source": "Source : {source} — {portal} — {license}",
        "filters": "Filtres",
        "indicator": "Indicateur",
        "indicator_help": "Type de délit. Chaque indicateur a sa propre unité (victimes, infractions, véhicules, mis en cause).",
        "years": "Période",
        "years_help": "Les évolutions sont calculées entre la première et la dernière année de la période.",
        "region": "Région",
        "region_help": "Laisser vide pour garder toute la France.",
        "per_homes": "pour 1 000 logements",
        "per_inhabitants": "pour 1 000 habitants",
        "Crimes against people": "Atteintes aux personnes",
        "Crimes against property": "Atteintes aux biens",
        "Fraud": "Escroqueries",
        "Drugs": "Stupéfiants",
        "selection": "Votre sélection : {indicator} · {start}–{end} · {scope}",
        "all_france": "toute la France",
        "kpi_cases": "Faits enregistrés en {end}",
        "kpi_rate": "Taux en {end}",
        "kpi_rate_help": "Faits enregistrés {label}",
        "kpi_top": "Taux le plus élevé en {end}",
        "kpi_top_help": "Taux {label}",
        "hook": "Demandez aux Français si la délinquance augmente et la plupart répondront oui. "
        "Les chiffres officiels racontent une histoire plus surprenante : **tout dépend du délit que l'on regarde.**",
        "hook_help": "Évolution des faits enregistrés, toute la France",
        "roadmap": "Deux chiffres qui vont dans des directions opposées. Ce tableau de bord les suit en quatre chapitres :\n"
        "1. **Les vols baissent, les violences augmentent** : quels délits montent et lesquels baissent ?\n"
        "2. **Pas la même histoire partout** : quelles régions et quels départements sont les plus touchés ?\n"
        "3. **Peut-on faire confiance à ces chiffres ?** : qualité des données et limites.\n"
        "4. **Ce que ça veut dire** : conclusions et suites possibles.",
        "dataset": "**Jeu de données :** [{name}]({url}), {portal}, {license}",
        "about_title": "À propos des données et du public",
        "about": "- **Source :** le SSMSI, service statistique du ministère de l'Intérieur, publié sur data.gouv.fr.\n"
        "- **Périmètre :** faits enregistrés par la police et la gendarmerie, 101 départements, 16 indicateurs, 2016–2025.\n"
        "- **Unités :** chaque indicateur a sa propre unité (victimes, infractions, véhicules, mis en cause) et un taux "
        "pour 1 000 habitants (pour 1 000 logements pour les cambriolages).\n"
        "- **Public :** citoyens, étudiants et élus locaux qui veulent des faits plutôt que des impressions.\n"
        "- **Utilisation :** les filtres de la barre latérale changent chaque graphique et chaque phrase en gras.",
        "caveat": "À garder en tête : ce sont des faits **enregistrés**, pas la délinquance réelle. Une hausse peut venir "
        "de plus de délits, mais aussi de plus de victimes qui portent plainte ou d'un changement dans la façon "
        "d'enregistrer les faits.",
        "ch1_title": "Chapitre 1 · Les vols baissent, les violences augmentent",
        "ch1_headline": "**Entre {start} et {end}, les atteintes aux personnes enregistrées ont évolué de {people:+.0f} %, "
        "alors que les atteintes aux biens ont évolué de {prop:+.0f} %.**",
        "ch1_text": "Au niveau national, la ligne rouge commence à monter après #MeToo fin 2017, s'arrête pendant le "
        "confinement de 2020, puis monte encore plus vite à partir de 2021, après le Grenelle des violences conjugales. "
        "Les escroqueries et les affaires de stupéfiants augmentent aussi. De l'autre côté, la ligne bleue des vols et "
        "dégradations chute en 2020 et ne revient jamais à son niveau de 2016.",
        "scissor_alt": "Graphique en courbes des faits enregistrés pour les quatre catégories, avec {start} ramené à 100. "
        "Les lignes en pointillés marquent #MeToo, le Grenelle des violences conjugales, le premier confinement et "
        "l'amende forfaitaire pour usage de stupéfiants.",
        "ch1_drive": "Quels délits creusent l'écart ?",
        "ch1_top3": "**Les trois plus fortes hausses : {top3}.**",
        "change_alt": "Graphique en barres horizontales de l'évolution en % des faits enregistrés pour chaque indicateur "
        "entre {start} et {end}, coloré par catégorie. Les barres à droite de la ligne grise sont des hausses, celles à "
        "gauche des baisses.",
        "zoom_title": "Zoom sur un délit : {indicator}",
        "zoom_headline": "**{indicator} : {change:+.0f} % de faits enregistrés entre {start} et {end}, le taux le plus "
        "élevé est atteint en {peak}.** Choisissez un autre délit dans la barre latérale pour suivre son histoire.",
        "line_title": "{indicator} : taux {label}",
        "line_alt": "Graphique en courbe du taux annuel de {indicator} {label} de {start} à {end}, "
        "avec les mêmes lignes d'événements que le graphique précédent.",
        "ch1_transition": "*Ce sont des chiffres nationaux. Mais est-ce la même histoire partout ? →*",
        "year_axis": "Année",
        "cases": "Faits enregistrés",
        "category": "Catégorie",
        "indicator_axis": "Indicateur",
        "change_axis": "Évolution (%)",
        "index_axis": "Indice ({start} = 100)",
        "scissor_title": "Faits enregistrés par catégorie ({start} = 100)",
        "change_title": "Évolution des faits enregistrés, {start} → {end}",
        "rate_axis": "Taux {label}",
        "region_axis": "Région",
        "department_axis": "Département",
        "ev_metoo": "#MeToo",
        "ev_grenelle": "Grenelle des violences conjugales",
        "ev_lockdown": "1er confinement",
        "ev_afd": "Amende forfaitaire stupéfiants",
        "ch2_title": "Chapitre 2 · Pas la même histoire partout",
        "ch2_headline": "**En {end}, {region} a le taux le plus élevé pour {indicator} ({rate:.2f} {label}), "
        "contre {france:.2f} pour toute la France.**",
        "compare_regions": "Comparaison des régions",
        "region_title": "{indicator} par région en {end}",
        "region_alt": "Graphique en barres horizontales du taux de {indicator} {label} pour chaque région en {end}, "
        "trié du plus faible au plus élevé.",
        "map_view": "Carte",
        "map_ratio": "**À l'échelle des départements, {top} ({top_rate:.2f}) a un taux {ratio:.1f} fois plus élevé que "
        "{bottom} ({bottom_rate:.2f}).**",
        "map_top": "**À l'échelle des départements, {top} a le taux le plus élevé ({top_rate:.2f}).**",
        "map_title": "{indicator} par département en {end}",
        "map_alt": "Carte de la France métropolitaine où chaque département est coloré selon son taux de {indicator} "
        "{label} en {end}. Plus c'est foncé, plus c'est élevé. Les départements d'outre-mer ne sont pas sur la carte "
        "mais sont dans les autres graphiques.",
        "top_bottom": "Les 10 départements les plus et les moins touchés",
        "highest": "Les {n} plus élevés en {end}",
        "lowest": "Les {n} plus faibles en {end}",
        "highest_alt": "Graphique en barres des {n} départements avec le taux de {indicator} le plus élevé en {end}.",
        "lowest_alt": "Graphique en barres des {n} départements avec le taux de {indicator} le plus faible en {end}.",
        "ch2_transition": "*Avant de conclure, une question reste : peut-on faire confiance à ces chiffres ? →*",
        "ch3_title": "Chapitre 3 · Peut-on faire confiance à ces chiffres ?",
        "ch3_headline": "**Plutôt oui : le fichier est complet et cohérent. Mais il mesure ce que la police enregistre, "
        "pas tous les délits commis.**",
        "missing_title": "**Valeurs manquantes par colonne**",
        "missing_col": "Valeurs manquantes",
        "duplicates": "Lignes en double",
        "checks_title": "**Contrôles de validation**",
        "check_col": "Contrôle",
        "result_col": "Résultat",
        "check_rows": "Lignes = départements x indicateurs x années",
        "check_negative": "Aucune valeur négative",
        "check_rate": "Taux pour 1 000 = nombre / population",
        "check_drugs": "Usage de stupéfiants = AFD + hors AFD",
        "max_error": "erreur max = {value:.6f}",
        "max_gap": "écart max = {value:.0f}",
        "limits": "- **Faits enregistrés ≠ délinquance réelle.** Seuls les faits signalés à la police ou constatés par "
        "elle sont comptés.\n"
        "- **Changements d'enregistrement.** Depuis 2020, l'usage de stupéfiants peut être puni d'une amende forfaitaire "
        "(AFD). Les deux sous-indicateurs (AFD / hors AFD) ont été retirés pour ne pas compter deux fois les mêmes faits, "
        "seul le total \"Usage de stupéfiants\" est gardé.\n"
        "- **Population.** Pour {years}, les taux utilisent une population INSEE plus ancienne, donc les taux des "
        "dernières années sont un peu surestimés. Mayotte utilise toujours le recensement de 2017.\n"
        "- **Catégories.** Les courbes par catégorie du chapitre 1 additionnent des indicateurs aux unités différentes "
        "(victimes, infractions, véhicules), elles montrent seulement des tendances.\n"
        "- **Petits départements.** Les délits rares (homicides) donnent des taux instables quand la population est faible.\n"
        "- **Carte.** Le GeoJSON ne contient que la France métropolitaine, les départements d'outre-mer sont seulement "
        "dans les graphiques en barres.\n"
        "- **Éthique.** Les données sont agrégées par département, donc personne ne peut être identifié. Un taux élevé "
        "ne veut pas dire qu'un territoire est \"dangereux\" : il dépend aussi de la fréquence des plaintes et de "
        "l'activité de la police.",
        "ch4_title": "Chapitre 4 · Ce que ça veut dire",
        "ch4_headline": "**Alors, la délinquance augmente-t-elle en France ? Les violences enregistrées contre les "
        "personnes, oui. La plupart des vols, non. Et une partie de la hausse vient de victimes qui parlent davantage.**",
        "insights": "- Entre {start} et {end}, **les atteintes aux personnes augmentent fortement** : violences sexuelles "
        "{sexual:+.0f} %, violences intrafamiliales {domestic:+.0f} %, tentatives d'homicide {attempts:+.0f} %.\n"
        "- **Les escroqueries** aux moyens de paiement augmentent aussi : {fraud:+.0f} %.\n"
        "- **La plupart des vols baissent** : vols violents sans arme {violent:+.0f} %, vols avec armes {armed:+.0f} %, "
        "vols de véhicules {vehicles:+.0f} %, cambriolages {burglaries:+.0f} %.\n"
        "- 2020 marque une rupture nette : le confinement a fait baisser presque tous les indicateurs.\n"
        "- Taux les plus élevés en {end} : violences sexuelles ({top_sexual}), escroqueries ({top_fraud}), "
        "violences intrafamiliales ({top_domestic}).",
        "implications": "**Conséquences :** selon le SSMSI, une partie de la hausse des violences sexuelles et "
        "intrafamiliales vient de victimes qui portent plus souvent plainte. Ces chiffres ne prouvent donc pas à eux "
        "seuls qu'il y a plus de violences, mais ils montrent un besoin croissant d'accompagnement des victimes et de "
        "policiers formés pour recevoir ces plaintes.\n\n"
        "**Suites possibles :** comparer avec l'enquête de victimation (Vécu et ressenti en matière de sécurité) pour "
        "séparer la délinquance réelle des plaintes, et descendre au niveau des communes avec le fichier communal du "
        "même jeu de données.",
    },
}


def t(key, **kwargs):
    lang = st.session_state.get("lang", "en")
    return TEXT[lang][key].format(**kwargs)
