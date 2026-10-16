import streamlit as st

from utils.prep import change_by_indicator


def show(df):
    start, end = int(df["year"].min()), int(df["year"].max())
    changes = change_by_indicator(df, start, end)
    up = changes.iloc[-1]
    down = changes.iloc[0]

    st.markdown(
        "Ask people if crime is rising in France and most of them will say yes. "
        "The official numbers tell a more surprising story: **it depends on which crime you look at.**"
    )

    c1, c2 = st.columns(2)
    c1.metric(f"{up['indicator']}, {start} → {end}", f"{up['change']:+.0f}%", help="Change in recorded cases, all of France")
    c2.metric(f"{down['indicator']}, {start} → {end}", f"{down['change']:+.0f}%", help="Change in recorded cases, all of France")

    st.markdown(
        "Two numbers going in opposite directions. This dashboard follows them in four chapters:\n"
        "1. **Thefts fall, violence rises**: which crimes go up and which go down?\n"
        "2. **Not the same story everywhere**: which regions and departments are the most affected?\n"
        "3. **Can we trust these numbers?**: data quality and limits.\n"
        "4. **What it means**: takeaways and next steps."
    )

    with st.expander("About the data and the audience"):
        st.markdown(
            "- **Source:** SSMSI, the statistical service of the Ministry of the Interior, published on data.gouv.fr.\n"
            "- **Coverage:** crimes recorded by the police and gendarmerie, 101 departments, 16 indicators, 2016–2025.\n"
            "- **Units:** each indicator has its own unit (victims, offences, vehicles, people charged) and a rate per "
            "1,000 inhabitants (per 1,000 homes for burglaries).\n"
            "- **Audience:** citizens, students and local decision makers who want facts instead of impressions.\n"
            "- **How to use it:** the sidebar filters change every chart and every sentence written in bold."
        )

    st.warning(
        "Keep in mind: this is **recorded** crime, not real crime. A rise can come from more crimes, "
        "but also from more victims filing a complaint or from changes in how police record offences."
    )
