from pathlib import Path

import streamlit as st

from utils.lang import t

LOGO = Path(__file__).resolve().parent.parent / "assets" / "efrei_logo.png"


def show():
    c1, c2 = st.columns([1, 3], vertical_alignment="center")
    with c1:
        st.image(str(LOGO), width=220)
    with c2:
        st.markdown(
            "**Nathan CHEVAUCHE** · nathan.chevauche@efrei.net  \n"
            f"**{t('program')}:** PGE – Data Engineering · **{t('year')}:** M1 – 2026-2027  \n"
            "[LinkedIn](https://www.linkedin.com/in/nathan-chevauch%C3%A9/) · [GitHub](https://github.com/Neithennn)  \n"
            f"**{t('course')}:** ST2DVZ-2627PSA01 - Data Analysis & Visualization  \n"
            f"**{t('professor')}:** Mano Joseph MATHEW · mano.mathew@efrei.fr"
        )
    st.divider()
