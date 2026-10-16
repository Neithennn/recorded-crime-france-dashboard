import streamlit as st


def show():
    st.header("Why this matters")
    st.markdown(
        "Crime is one of the main concerns of French people, but the debate is often based on "
        "impressions. This dashboard uses the official figures of the police and gendarmerie to answer "
        "a simple question: **has crime really increased in France since 2016, and where?**"
    )

    st.subheader("Context")
    st.markdown(
        "- The data comes from the SSMSI (statistical service of the Ministry of the Interior).\n"
        "- It counts crimes **recorded** by the police and gendarmerie, for 101 departments, 16 indicators and 10 years (2016–2025).\n"
        "- Each indicator has a unit (victims, offences, vehicles, people charged) and a rate per 1,000 inhabitants "
        "(per 1,000 homes for burglaries)."
    )

    st.subheader("Audience and questions")
    st.markdown(
        "**Audience:** citizens, students and local decision makers who want a factual view of crime.\n\n"
        "1. Which types of crime are rising and which are falling?\n"
        "2. Which regions and departments are the most affected?\n"
        "3. What are the limits of these numbers?"
    )

    st.warning(
        "Caveat: recorded crime is not the same as real crime. A rise can come from more crimes, "
        "but also from more victims filing a complaint or from changes in how police record offences."
    )
