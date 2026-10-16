# Data Storytelling: Recorded Crime in France, 2016–2025

Individual Student Project – Streamlit Dashboard (EFREI Paris, 2026)
Author: **Nathan CHEVAUCHE**

#EFREIDataStories2026

## Topic and question

**Has crime really increased in France since 2016, and where?**

- **Audience:** citizens, students and local decision makers who want facts instead of impressions.
- **Questions:**
  1. Which types of crime are rising and which are falling?
  2. Which regions and departments are the most affected?
  3. What are the limits of these numbers?
- **Narrative pattern:** change over time (2016 → 2025) + comparison of regions with a map and rankings.

## Storyboard

| Step | Section in the app | Content |
|---|---|---|
| Hook | Why this matters | Crime is a big concern but the debate is based on impressions. |
| Context | Context / Audience and questions | Source, coverage, units, caveat "recorded ≠ real crime". |
| Analysis | 1. Overview | KPIs, trend of the selected indicator, change of all indicators. |
| Analysis | 2. Deep dive | Rate by region, map by department, top / bottom 10 departments. |
| Transparency | 3. Data Quality & Limitations | Missing values, duplicates, validation checks, limits. |
| Insights | 4. Key Insights & Next Steps | Takeaways, implications and next steps. |

## Dataset

- **Name:** Bases statistiques communale, départementale et régionale de la délinquance enregistrée par la police et la gendarmerie nationales
- **Producer:** SSMSI (Ministry of the Interior)
- **Portal:** [data.gouv.fr](https://www.data.gouv.fr/datasets/bases-statistiques-communale-departementale-et-regionale-de-la-delinquance-enregistree-par-la-police-et-la-gendarmerie-nationales)
- **File used:** departmental file (DEP), July 2026 edition, years 2016–2025, 101 departments, 18 indicators
- **License:** Licence Ouverte / Open Licence v2.0
- **Map:** department boundaries from [france-geojson](https://github.com/gregoiredavid/france-geojson)

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
- Denominator `base` (population, or number of homes for burglaries) so rates can be recomputed after grouping by region or for all of France.
- Percentage change between the first and the last year of the selected period.

## App features

- **Sidebar filters:** indicator, year range, regions.
- **KPIs** linked to the filters: recorded cases, rate per 1,000, department with the highest rate.
- **Interactive charts with tooltips (Plotly):** line chart with the 2020 lockdown band, bar chart of changes by indicator, bar chart by region, map by department, top / bottom 10 departments.
- **Data quality section:** missing values, duplicates, validation checks, limitations.
- **Accessibility:** each chart has a text description under it, all axes and units are labelled.
- **Performance:** data is loaded and cleaned once with `st.cache_data`.

## Project structure

```
app.py                  main page, sidebar filters
sections/
  intro.py              hook, context, audience, caveats
  overview.py           KPIs, trends over time, change by indicator
  deep_dives.py         regions, map, top / bottom 10 departments
  conclusions.py        data quality, insights, next steps
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

The app opens on http://localhost:8501.

**Deployment:** push the folder to a GitHub repository, then on [Streamlit Community Cloud](https://share.streamlit.io) choose the repository and `app.py` as the main file.

## Key insights

- Between 2016 and 2025, crimes against people rise strongly: sexual violence +155%, domestic violence +126%, attempted murders +98%.
- Fraud with means of payment rises by +79%.
- Most thefts go down: violent thefts without weapon −48%, armed robberies −28%, vehicle thefts −24%, burglaries −15%.
- 2020 (lockdowns) lowered almost every indicator.
- Paris has the highest rates for sexual violence and fraud, overseas departments for domestic violence.

## Limitations

- These are **recorded** crimes: a rise can come from more complaints (for example for sexual and domestic violence) and not only from more crimes. No causal conclusion is made.
- Since 2020 drug use can be punished with a fixed fine (AFD), which changes how it is recorded.
- For 2024 and 2025 the rates use the 2023 INSEE population, Mayotte uses the 2017 census.
- Rates of rare crimes (homicides) are unstable in small departments.
- The map only shows metropolitan France, overseas departments are in the bar charts.

## Links

- Demo video: *to add*
- Deployed app: *to add*
