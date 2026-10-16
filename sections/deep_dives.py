import streamlit as st

from utils.prep import by_department, by_region, filter_data, rate_label, timeseries
from utils.viz import bar_chart, map_chart


def show(df, geo, indicator, years, regions):
    end = years[1]
    label = rate_label(indicator)
    data = filter_data(df, years, regions, indicator)
    departments = by_department(data, end)
    region_rates = by_region(data, end)
    top_region = region_rates.loc[region_rates["rate"].idxmax()]
    france = timeseries(filter_data(df, years, [], indicator))
    france_rate = france.loc[france["year"] == end, "rate"].iloc[0]
    top = departments.loc[departments["rate"].idxmax()]
    bottom = departments.loc[departments["rate"].idxmin()]

    st.header("Chapter 2 · Not the same story everywhere")
    st.markdown(
        f"**In {end}, {top_region['region']} has the highest rate of {indicator} "
        f"({top_region['rate']:.2f} {label}), against {france_rate:.2f} for all of France.**"
    )

    st.subheader("Compare regions")
    bar_chart(
        region_rates,
        "rate",
        "region",
        f"Rate {label}",
        "Region",
        f"{indicator} by region in {end}",
        f"Horizontal bar chart of the rate of {indicator} {label} for each region in {end}, sorted from lowest to highest.",
    )

    st.subheader("Map view")
    if bottom["rate"] > 0:
        st.markdown(
            f"**At department level, {top['department']} ({top['rate']:.2f}) has "
            f"{top['rate'] / bottom['rate']:.1f} times the rate of {bottom['department']} ({bottom['rate']:.2f}).**"
        )
    else:
        st.markdown(f"**At department level, {top['department']} has the highest rate ({top['rate']:.2f}).**")
    map_chart(
        departments,
        geo,
        f"Rate {label}",
        f"{indicator} by department in {end}",
        f"Map of metropolitan France where each department is coloured by its rate of {indicator} {label} in {end}. "
        "Darker means higher. Overseas departments are not on the map but are in the other charts.",
    )

    st.subheader("Top and bottom 10 departments")
    n = min(10, len(departments))
    c1, c2 = st.columns(2)
    with c1:
        bar_chart(
            departments.nlargest(n, "rate"),
            "rate",
            "department",
            f"Rate {label}",
            "Department",
            f"Highest {n} in {end}",
            f"Bar chart of the {n} departments with the highest rate of {indicator} in {end}.",
            height=400,
        )
    with c2:
        bar_chart(
            departments.nsmallest(n, "rate"),
            "rate",
            "department",
            f"Rate {label}",
            "Department",
            f"Lowest {n} in {end}",
            f"Bar chart of the {n} departments with the lowest rate of {indicator} in {end}.",
            height=400,
        )

    st.markdown("*Before drawing conclusions, one question remains: can we trust these numbers? →*")
