import streamlit as st

from utils.prep import by_department, change_by_indicator, filter_data, rate_label, timeseries
from utils.viz import change_chart, line_chart


def show(df, indicator, years, regions):
    start, end = years
    label = rate_label(indicator)
    data = filter_data(df, years, regions, indicator)
    ts = timeseries(data)
    first = ts.iloc[0]
    last = ts.iloc[-1]
    change = (last["count"] / first["count"] - 1) * 100 if first["count"] > 0 else 0
    top = by_department(data, end).sort_values("rate", ascending=False).iloc[0]

    st.header("1. Overview: what is changing?")
    st.markdown(f"**{indicator}: {change:+.0f}% recorded cases between {start} and {end}.**")

    c1, c2, c3 = st.columns(3)
    c1.metric(f"Recorded cases in {end}", f"{last['count']:,.0f}", f"{change:+.1f}% vs {start}", delta_color="inverse")
    c2.metric(
        f"Rate in {end}",
        f"{last['rate']:.2f}",
        f"{last['rate'] - first['rate']:+.2f} vs {start}",
        delta_color="inverse",
        help=f"Recorded cases {label}",
    )
    c3.metric(f"Highest rate in {end}", top["department"], f"{top['rate']:.2f}", delta_color="off", help=f"Rate {label}")

    st.subheader("Trends over time")
    line_chart(
        ts,
        f"Rate {label}",
        f"{indicator}: rate {label}",
        f"Line chart of the yearly rate of {indicator} {label} from {start} to {end}. "
        "The grey band marks 2020, the year of the COVID-19 lockdowns.",
    )

    st.subheader("Which crimes are rising?")
    st.markdown("**Crimes against people and fraud rise sharply, while most thefts go down.**")
    changes = change_by_indicator(filter_data(df, years, regions), start, end)
    change_chart(
        changes,
        start,
        end,
        f"Horizontal bar chart of the percentage change in recorded cases for each indicator between {start} and {end}, "
        "coloured by category. Bars on the right of the grey line are increases, bars on the left are decreases.",
    )
