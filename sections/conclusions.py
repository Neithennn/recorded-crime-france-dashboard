import streamlit as st

from utils.prep import change_by_indicator


def top_department(df, indicator, year):
    rows = df[(df["indicator"] == indicator) & (df["year"] == year)]
    return rows.loc[rows["rate"].idxmax(), "department"]


def show(df, quality):
    st.header("Chapter 3 · Can we trust these numbers?")
    st.markdown(
        "**Mostly yes: the file is complete and consistent. But it measures what the police record, "
        "not all the crimes that happen.**"
    )

    c1, c2 = st.columns([1, 2])
    with c1:
        st.markdown("**Missing values per column**")
        st.dataframe(quality["missing"])
        st.metric("Duplicate rows", quality["duplicates"])
    with c2:
        st.markdown("**Validation checks**")
        st.dataframe(quality["checks"], hide_index=True)

    st.info(
        "- **Recorded crime ≠ real crime.** Only crimes reported to or found by the police are counted.\n"
        "- **Changes in recording.** Since 2020, drug use can be punished with a fixed fine (AFD). "
        "The two sub-indicators (AFD / non-AFD) were removed to avoid counting the same cases twice, "
        "only the total \"Usage de stupéfiants\" is kept.\n"
        f"- **Population.** For {', '.join(str(y) for y in quality['old_population'])} the rates use an older INSEE population, "
        "so the rates of the last years are slightly overestimated. Mayotte always uses the 2017 census.\n"
        "- **Categories.** The category lines of chapter 1 add indicators with different units (victims, offences, vehicles), "
        "they only show trends, not exact totals.\n"
        "- **Small departments.** Rare crimes (homicides) give unstable rates when the population is small.\n"
        "- **Map.** The GeoJSON only contains metropolitan France, overseas departments are only shown in the bar charts."
    )

    start, end = int(df["year"].min()), int(df["year"].max())
    changes = change_by_indicator(df, start, end).set_index("indicator")["change"]
    attempts = changes["Tentatives d'homicide"]

    st.header("Chapter 4 · What it means")
    st.markdown(
        "**So, is crime rising in France? Recorded violence against people is, most thefts are not, "
        "and part of the rise comes from victims speaking up more.**"
    )
    st.success(
        f"- Between {start} and {end}, **crimes against people rise strongly**: sexual violence "
        f"{changes['Violences sexuelles']:+.0f}%, domestic violence {changes['Violences physiques intrafamiliales']:+.0f}%, "
        f"attempted murders {attempts:+.0f}%.\n"
        f"- **Fraud** with means of payment also rises: {changes['Escroqueries et fraudes aux moyens de paiement']:+.0f}%.\n"
        f"- **Most thefts go down**: violent thefts without weapon {changes['Vols violents sans arme']:+.0f}%, "
        f"armed robberies {changes['Vols avec armes']:+.0f}%, vehicle thefts {changes['Vols de véhicule']:+.0f}%, "
        f"burglaries {changes['Cambriolages de logement']:+.0f}%.\n"
        "- 2020 is a clear break: the lockdown lowered almost every indicator.\n"
        f"- Highest rates in {end}: sexual violence in {top_department(df, 'Violences sexuelles', end)}, "
        f"fraud in {top_department(df, 'Escroqueries et fraudes aux moyens de paiement', end)}, "
        f"domestic violence in {top_department(df, 'Violences physiques intrafamiliales', end)}."
    )
    st.markdown(
        "**Implications:** according to the SSMSI, part of the rise of sexual and domestic violence comes from more victims "
        "filing a complaint. These numbers do not prove alone that there is more violence, but they show a growing need "
        "for victim support and for police trained to receive these complaints.\n\n"
        "**Next steps:** compare with the victimisation survey (Vécu et ressenti en matière de sécurité) to separate "
        "real crime from reporting, and go down to the city level with the communal file of the same dataset."
    )
