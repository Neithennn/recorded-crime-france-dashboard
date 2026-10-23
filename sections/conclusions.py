import pandas as pd
import streamlit as st

from utils.lang import t
from utils.prep import change_by_indicator


def top_department(df, indicator, year):
    rows = df[(df["indicator"] == indicator) & (df["year"] == year)]
    return rows.loc[rows["rate"].idxmax(), "department"]


def show(df, quality):
    st.header(t("ch3_title"))
    st.markdown(t("ch3_headline"))

    checks = pd.DataFrame(
        {
            t("check_col"): [t("check_rows"), t("check_negative"), t("check_rate"), t("check_drugs")],
            t("result_col"): [
                f"{quality['rows']} / {quality['expected_rows']}",
                str(quality["no_negative"]),
                t("max_error", value=quality["rate_error"]),
                t("max_gap", value=quality["drugs_gap"]),
            ],
        }
    )

    c1, c2 = st.columns([1, 2])
    with c1:
        st.markdown(t("missing_title"))
        st.dataframe(quality["missing"].rename(t("missing_col")).to_frame())
        st.metric(t("duplicates"), quality["duplicates"])
    with c2:
        st.markdown(t("checks_title"))
        st.dataframe(checks, hide_index=True)

    st.info(t("limits", years=", ".join(str(y) for y in quality["old_population"])))

    start, end = int(df["year"].min()), int(df["year"].max())
    changes = change_by_indicator(df, start, end).set_index("indicator")["change"]

    st.header(t("ch4_title"))
    st.markdown(t("ch4_headline"))
    st.success(
        t(
            "insights",
            start=start,
            end=end,
            sexual=changes["Violences sexuelles"],
            domestic=changes["Violences physiques intrafamiliales"],
            attempts=changes["Tentatives d'homicide"],
            fraud=changes["Escroqueries et fraudes aux moyens de paiement"],
            violent=changes["Vols violents sans arme"],
            armed=changes["Vols avec armes"],
            vehicles=changes["Vols de véhicule"],
            burglaries=changes["Cambriolages de logement"],
            top_sexual=top_department(df, "Violences sexuelles", end),
            top_fraud=top_department(df, "Escroqueries et fraudes aux moyens de paiement", end),
            top_domestic=top_department(df, "Violences physiques intrafamiliales", end),
        )
    )
    st.markdown(t("implications"))
