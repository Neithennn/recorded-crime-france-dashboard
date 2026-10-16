import streamlit as st

from utils.prep import by_department, by_region, filter_data, rate_label
from utils.viz import bar_chart, map_chart


def show(df, geo, indicator, years, regions):
    end = years[1]
    label = rate_label(indicator)
    data = filter_data(df, years, regions, indicator)
    departments = by_department(data, end)

    st.header("2. Deep dive: where?")
    st.markdown("**The rate is not the same everywhere: big cities and overseas departments are often at the top.**")

    st.subheader("Compare regions")
    bar_chart(
        by_region(data, end),
        "rate",
        "region",
        f"Rate {label}",
        "Region",
        f"{indicator} by region in {end}",
        f"Horizontal bar chart of the rate of {indicator} {label} for each region in {end}, sorted from lowest to highest.",
    )

    st.subheader("Map view")
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
