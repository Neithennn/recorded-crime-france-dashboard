import streamlit as st


def show(quality):
    st.header("3. Data Quality & Limitations")

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
        "- **Small departments.** Rare crimes (homicides) give unstable rates when the population is small.\n"
        "- **Map.** The GeoJSON only contains metropolitan France, overseas departments are only shown in the bar charts."
    )

    st.header("4. Key Insights & Next Steps")
    st.success(
        "- Between 2016 and 2025, **crimes against people rise strongly**: sexual violence +155%, "
        "domestic violence +126%, attempted murders +98%.\n"
        "- **Fraud** (+79%) follows the growth of online payments.\n"
        "- **Most thefts go down**: violent thefts without weapon −48%, armed robberies −28%, vehicle thefts −24%, burglaries −15%.\n"
        "- 2020 is a clear break: lockdowns lowered almost every indicator.\n"
        "- Paris has the highest rates for sexual violence and fraud, overseas departments for domestic violence, "
        "Corsica is often at the bottom."
    )
    st.markdown(
        "**Implications:** according to the SSMSI, part of the rise of sexual and domestic violence comes from more victims "
        "filing a complaint, so these numbers do not prove alone that there is more violence, but they show a growing need "
        "for victim support. "
        "Prevention of thefts seems to work better.\n\n"
        "**Next steps:** compare with the victimisation survey (Vécu et ressenti en matière de sécurité) to separate "
        "real crime from reporting, and go down to the city level with the communal file of the same dataset."
    )
