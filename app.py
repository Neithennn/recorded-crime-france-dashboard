import streamlit as st

from sections import conclusions, deep_dives, intro, overview
from utils.io import LICENSE, PORTAL, SOURCE, load_data, load_geojson
from utils.prep import make_tables

st.set_page_config(page_title="Data Storytelling Dashboard", layout="wide")


@st.cache_data(show_spinner=False)
def get_data():
    df_raw = load_data()
    geo = load_geojson()
    tables = make_tables(df_raw, geo)
    return df_raw, tables, geo


st.title("Fewer Thefts, More Violence: How Crime Changed in France (2016–2025)")
st.caption(f"Source: {SOURCE} — {PORTAL} — {LICENSE}")

raw, tables, geo = get_data()
df = tables["clean"]
indicators = sorted(df["indicator"].unique())

with st.sidebar:
    st.header("Filters")
    indicator = st.selectbox(
        "Indicator",
        indicators,
        index=indicators.index("Violences sexuelles"),
        help="Type of crime. Each indicator has its own unit (victims, offences, vehicles, people charged).",
    )
    years = st.slider(
        "Year range",
        int(df["year"].min()),
        int(df["year"].max()),
        (int(df["year"].min()), int(df["year"].max())),
        help="Changes are computed between the first and the last year of the range.",
    )
    regions = st.multiselect("Region", sorted(df["region"].unique()), help="Leave empty to keep all of France.")

overview.kpi_header(df, indicator, years, regions)
intro.show(df)
overview.show(df, indicator, years, regions)
deep_dives.show(df, geo, indicator, years, regions)
conclusions.show(df, tables["quality"])
