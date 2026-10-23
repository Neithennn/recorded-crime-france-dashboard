import streamlit as st

from sections import conclusions, deep_dives, header, intro, overview
from utils.io import LICENSE, PORTAL, SOURCE, load_data, load_geojson
from utils.lang import t
from utils.prep import make_tables

# Page setup
st.set_page_config(page_title="Data Storytelling Dashboard", layout="wide")


# Load and clean the data only once (cached)
@st.cache_data(show_spinner=False)
def get_data():
    df_raw = load_data()
    geo = load_geojson()
    tables = make_tables(df_raw, geo)
    return df_raw, tables, geo


# Language switch (has to come first so every text uses it)
with st.sidebar:
    language = st.radio("Language / Langue", ["English", "Français"], horizontal=True)
    st.session_state["lang"] = "fr" if language == "Français" else "en"

# Header and title
header.show()
st.title(t("title"))
st.caption(t("source", source=SOURCE, portal=PORTAL, license=LICENSE))

raw, tables, geo = get_data()
df = tables["clean"]
indicators = sorted(df["indicator"].unique())

# Sidebar filters
with st.sidebar:
    st.header(t("filters"))
    indicator = st.selectbox(
        t("indicator"),
        indicators,
        index=indicators.index("Violences sexuelles"),
        help=t("indicator_help"),
    )
    years = st.slider(
        t("years"),
        int(df["year"].min()),
        int(df["year"].max()),
        (int(df["year"].min()), int(df["year"].max())),
        help=t("years_help"),
    )
    regions = st.multiselect(t("region"), sorted(df["region"].unique()), help=t("region_help"))

# KPIs linked to the filters
overview.kpi_header(df, indicator, years, regions)

# Story: hook, then the four chapters
intro.show(df)
overview.show(df, indicator, years, regions)
deep_dives.show(df, geo, indicator, years, regions)
conclusions.show(df, tables["quality"])
