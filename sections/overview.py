import streamlit as st

from utils.prep import by_department, change_by_indicator, filter_data, index_by_category, rate_label, timeseries
from utils.viz import change_chart, line_chart, scissor_chart


def show(df, indicator, years, regions):
    start, end = years
    all_crimes = filter_data(df, years, regions)
    index = index_by_category(all_crimes, start)
    last_index = index[index["year"] == end].set_index("category")["index"]
    people = last_index["Crimes against people"] - 100
    prop = last_index["Crimes against property"] - 100

    st.header("Chapter 1 · Thefts fall, violence rises")
    st.markdown(
        f"**Between {start} and {end}, recorded crimes against people changed by {people:+.0f}%, "
        f"while crimes against property changed by {prop:+.0f}%.**"
    )
    st.markdown(
        "On the national view, the red line starts to climb after #MeToo at the end of 2017, stops during the 2020 "
        "lockdown and then rises even faster from 2021, after the Grenelle on domestic violence. Fraud and drug cases "
        "also go up. On the other side, the blue line of thefts and damage falls in 2020 and never comes back to its "
        "2016 level."
    )
    scissor_chart(
        index,
        years,
        f"Line chart of recorded cases for the four categories of crime, with {start} set to 100. "
        "Dotted lines mark #MeToo, the Grenelle on domestic violence, the first lockdown and the fixed fine for drug use.",
    )

    changes = change_by_indicator(all_crimes, start, end)
    top3 = ", ".join(changes.sort_values("change", ascending=False)["indicator"].head(3))
    st.subheader("Which crimes drive the gap?")
    st.markdown(f"**The three biggest increases are: {top3}.**")
    change_chart(
        changes,
        start,
        end,
        f"Horizontal bar chart of the percentage change in recorded cases for each indicator between {start} and {end}, "
        "coloured by category. Bars on the right of the grey line are increases, bars on the left are decreases.",
    )

    label = rate_label(indicator)
    data = filter_data(df, years, regions, indicator)
    ts = timeseries(data)
    first = ts.iloc[0]
    last = ts.iloc[-1]
    change = (last["count"] / first["count"] - 1) * 100 if first["count"] > 0 else 0
    peak = ts.loc[ts["rate"].idxmax(), "year"]
    top = by_department(data, end).sort_values("rate", ascending=False).iloc[0]

    st.subheader(f"Zoom on one crime: {indicator}")
    st.markdown(
        f"**{indicator}: {change:+.0f}% recorded cases between {start} and {end}, the highest rate is reached in {peak}.** "
        "Choose another crime in the sidebar to follow its own story."
    )

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

    line_chart(
        ts,
        years,
        f"Rate {label}",
        f"{indicator}: rate {label}",
        f"Line chart of the yearly rate of {indicator} {label} from {start} to {end}, "
        "with the same dotted event lines as the chart above.",
    )

    st.markdown("*These are national numbers. But is it the same story everywhere? →*")
