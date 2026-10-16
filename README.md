# Fewer Thefts, More Violence: How Crime Changed in France (2016–2025)

Individual Student Project – Streamlit Dashboard (EFREI Paris, 2026)
Author: **Nathan CHEVAUCHE**

#EFREIDataStories2026

## The story

Ask people if crime is rising in France and most of them will say yes. The official numbers tell a more surprising story: **it depends on which crime you look at.** Between 2016 and 2025, recorded sexual violence rises by +155% while violent thefts without weapon fall by −48%. The app follows these two opposite curves.

- **Main question:** has crime really increased in France since 2016, and where?
- **Audience:** citizens, students and local decision makers who want facts instead of impressions.
- **Questions:**
  1. Which types of crime are rising and which are falling?
  2. Which regions and departments are the most affected?
  3. Can we trust these numbers?
- **Narrative pattern:** before/after change over time (2016 → 2025) + comparison of regions with a map and rankings.
- **Takeaway:** recorded violence against people is rising, most thefts are not, and part of the rise comes from victims reporting more.

## Storyboard

| Step | Chapter in the app | Headline | Content |
|---|---|---|---|
| Hook | Introduction | "It depends on which crime you look at" | Two opposite numbers (+155% / −48%), roadmap of the 4 chapters, caveat. |
| Context | About the data and the audience | – | Source, coverage, units, audience, how to use the filters. |
| Insight 1 | Chapter 1 · Thefts fall, violence rises | Computed: change of crimes against people vs property | "Scissor" chart by category (start year = 100) with events (#MeToo, Grenelle, lockdown, drug fines), change by indicator, zoom on the selected crime with KPIs. |
| Insight 2 | Chapter 2 · Not the same story everywhere | Computed: most affected region vs France, gap between departments | Bar chart by region, map by department, top / bottom 10. |
| Transparency | Chapter 3 · Can we trust these numbers? | "Mostly yes, but it measures what police record" | Missing values, duplicates, validation checks, limitations. |
| Implications | Chapter 4 · What it means | "Is crime rising? It depends." | Key numbers (computed from the data), implications, next steps. |

Each chapter ends with a short transition question that leads to the next one. The sentences in bold are computed from the data, so they change with the sidebar filters.

## Dataset

- **Name:** Bases statistiques communale, départementale et régionale de la délinquance enregistrée par la police et la gendarmerie nationales
- **Producer:** SSMSI (Ministry of the Interior)
- **Portal:** [data.gouv.fr](https://www.data.gouv.fr/datasets/bases-statistiques-communale-departementale-et-regionale-de-la-delinquance-enregistree-par-la-police-et-la-gendarmerie-nationales)
- **File used:** departmental file (DEP), July 2026 edition, years 2016–2025, 101 departments, 18 indicators
- **License:** Licence Ouverte / Open Licence v2.0
- **Map:** department boundaries from [france-geojson](https://github.com/gregoiredavid/france-geojson), built from IGN Admin Express (Licence Ouverte)
- **Code:** written for this course project, free to reuse for teaching

All links are in `dataset_link.txt`. A copy of the files is in `data/`. If the folder is empty, the app downloads the files automatically the first time (`fetch_and_cache()` in `utils/io.py`).

## Data work

**Cleaning**
- Columns renamed in English, codes read as text (to keep `01`, `2A`, `2B`, `971`…).
- Duplicates removed (there were none).
- The sub-indicators "Usage de stupéfiants (AFD)" and "(hors AFD)" are removed because their sum is exactly "Usage de stupéfiants" (checked), so keeping them would count the same cases twice.

**Validation checks** (shown in the app)
- Number of rows = departments × indicators × years (18,180).
- No missing values, no negative counts.
- The given rate per 1,000 is recomputed from count / population (count / homes for burglaries).
- Drug use total = AFD + non-AFD.

**Feature engineering**
- Department names joined from the GeoJSON (plus overseas departments), region names from the region code.
- Category for each indicator: crimes against people, crimes against property, fraud, drugs.
- Index by category (start year = 100) to compare trends of categories with very different sizes.
- Denominator `base` (population, or number of homes for burglaries) so rates can be recomputed after grouping by region or for all of France.
- Percentage change between the first and the last year of the selected period.

## App features

- **Sidebar filters:** indicator, year range, regions.
- **KPI header** under the title, linked to the filters: recorded cases, rate per 1,000, department with the highest rate.
- **Help texts** on the filters and KPIs to explain units and definitions.
- **Interactive charts with tooltips (Plotly):** scissor chart by category, bar chart of changes by indicator, line chart of the selected crime, bar chart by region, map by department, top / bottom 10 departments.
- **Annotations:** dotted lines for #MeToo (Oct 2017), the Grenelle on domestic violence (Sep 2019), the first lockdown (Mar 2020) and the fixed fine for drug use (Sep 2020), reference line at 100.
- **Data-driven headlines:** the bold sentences of each chapter are computed from the filtered data.
- **Data quality section:** missing values, duplicates, validation checks, limitations.
- **Accessibility:** each chart has a text description under it, all axes and units are labelled.
- **Performance:** data is loaded and cleaned once with `st.cache_data`.

## Project structure

```
app.py                  main page, sidebar filters
sections/
  intro.py              hook, roadmap, context, audience, caveats
  overview.py           chapter 1: scissor chart, change by indicator, KPIs, zoom
  deep_dives.py         chapter 2: regions, map, top / bottom 10 departments
  conclusions.py        chapters 3 and 4: data quality, insights, next steps
utils/
  io.py                 load_data(), fetch_and_cache(), source and license
  prep.py               cleaning, validation, aggregations
  viz.py                chart functions with a consistent style
data/                   cached CSV and GeoJSON
requirements.txt
dataset_link.txt
```

## How to run

Python 3.12 was used.

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows
source .venv/bin/activate       # macOS / Linux
pip install -r requirements.txt
streamlit run app.py
```

The app opens on http://localhost:8501. No sampling or randomness is used, so the results are always the same and no seed file is needed.

**Deployment:** push the folder to a GitHub repository, then on [Streamlit Community Cloud](https://share.streamlit.io) choose the repository and `app.py` as the main file.

## Key insights

- Between 2016 and 2025, crimes against people rise strongly: sexual violence +155%, domestic violence +126%, attempted murders +98%.
- Fraud with means of payment rises by +79%.
- Most thefts go down: violent thefts without weapon −48%, armed robberies −27%, vehicle thefts −24%, burglaries −15%.
- 2020 (lockdowns) lowered almost every indicator.
- Highest rates in 2025: sexual violence and fraud in Paris, domestic violence in Pas-de-Calais.

## Limitations

- These are **recorded** crimes: a rise can come from more complaints (for example for sexual and domestic violence) and not only from more crimes. No causal conclusion is made.
- Since 2020 drug use can be punished with a fixed fine (AFD), which changes how it is recorded.
- For 2024 and 2025 the rates use the 2023 INSEE population, Mayotte uses the 2017 census.
- Category lines add indicators with different units (victims, offences, vehicles), they only show trends.
- Rates of rare crimes (homicides) are unstable in small departments.
- The map only shows metropolitan France, overseas departments are in the bar charts.

## Ethics

- The data is aggregated by department: no personal data, no risk of re-identification.
- A high rate does not mean a territory is "dangerous": it also depends on reporting and police activity.
- No causal claims: events on the charts (#MeToo, Grenelle, lockdown, drug fines) are context, not proven causes.

## Links

- Deployed app: https://recorded-crime-france.streamlit.app
- GitHub repository: https://github.com/Neithennn/recorded-crime-france-dashboard
- Demo video: *to add*
