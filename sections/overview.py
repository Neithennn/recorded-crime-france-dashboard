import streamlit as st

from utils.lang import t
from utils.prep import by_department, change_by_indicator, filter_data, index_by_category, rate_label, timeseries
from utils.viz import change_chart, line_chart, scissor_chart


def kpi_header(df, indicator, years, regions):
    start, end = years
    label = rate_label(indicator)
    data = filter_data(df, years, regions, indicator)
    ts = timeseries(data)
    first = ts.iloc[0]
    last = ts.iloc[-1]
    change = (last["count"] / first["count"] - 1) * 100 if first["count"] > 0 else 0
    top = by_department(data, end).sort_values("rate", ascending=False).iloc[0]
    scope = ", ".join(regions) if regions else t("all_france")

    st.caption(t("selection", indicator=indicator, start=start, end=end, scope=scope))
    c1, c2, c3 = st.columns(3)
    c1.metric(t("kpi_cases", end=end), f"{last['count']:,.0f}", f"{change:+.1f}% vs {start}", delta_color="inverse")
    c2.metric(
        t("kpi_rate", end=end),
        f"{last['rate']:.2f}",
        f"{last['rate'] - first['rate']:+.2f} vs {start}",
        delta_color="inverse",
        help=t("kpi_rate_help", label=label),
    )
    c3.metric(
        t("kpi_top", end=end),
        top["department"],
        f"{top['rate']:.2f}",
        delta_color="off",
        help=t("kpi_top_help", label=label),
    )
    st.divider()


def show(df, indicator, years, regions):
    start, end = years
    all_crimes = filter_data(df, years, regions)
    index = index_by_category(all_crimes, start)
    last_index = index[index["year"] == end].set_index("category")["index"]
    people = last_index["Crimes against people"] - 100
    prop = last_index["Crimes against property"] - 100

    st.header(t("ch1_title"))
    st.markdown(t("ch1_headline", start=start, end=end, people=people, prop=prop))
    st.markdown(t("ch1_text"))
    scissor_chart(index, years, t("scissor_alt", start=start))

    changes = change_by_indicator(all_crimes, start, end)
    top3 = ", ".join(changes.sort_values("change", ascending=False)["indicator"].head(3))
    st.subheader(t("ch1_drive"))
    st.markdown(t("ch1_top3", top3=top3))
    change_chart(changes, start, end, t("change_alt", start=start, end=end))

    label = rate_label(indicator)
    ts = timeseries(filter_data(df, years, regions, indicator))
    first = ts.iloc[0]
    last = ts.iloc[-1]
    change = (last["count"] / first["count"] - 1) * 100 if first["count"] > 0 else 0
    peak = ts.loc[ts["rate"].idxmax(), "year"]

    st.subheader(t("zoom_title", indicator=indicator))
    st.markdown(t("zoom_headline", indicator=indicator, change=change, start=start, end=end, peak=peak))

    line_chart(
        ts,
        years,
        t("rate_axis", label=label),
        t("line_title", indicator=indicator, label=label),
        t("line_alt", indicator=indicator, label=label, start=start, end=end),
    )

    st.markdown(t("ch1_transition"))
