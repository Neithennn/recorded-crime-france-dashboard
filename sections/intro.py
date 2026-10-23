import streamlit as st

from utils.io import DATASET_PAGE, LICENSE, PORTAL, SOURCE
from utils.lang import t
from utils.prep import change_by_indicator


def show(df):
    start, end = int(df["year"].min()), int(df["year"].max())
    changes = change_by_indicator(df, start, end)
    up = changes.iloc[-1]
    down = changes.iloc[0]

    st.markdown(t("hook"))

    c1, c2 = st.columns(2)
    c1.metric(f"{up['indicator']}, {start} → {end}", f"{up['change']:+.0f}%", help=t("hook_help"))
    c2.metric(f"{down['indicator']}, {start} → {end}", f"{down['change']:+.0f}%", help=t("hook_help"))

    st.markdown(t("roadmap"))
    st.markdown(t("dataset", name=SOURCE, url=DATASET_PAGE, portal=PORTAL, license=LICENSE))

    with st.expander(t("about_title")):
        st.markdown(t("about"))

    st.warning(t("caveat"))
