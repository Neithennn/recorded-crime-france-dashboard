import streamlit as st

from utils.lang import t
from utils.prep import by_department, by_region, filter_data, rate_label, timeseries
from utils.viz import bar_chart, map_chart


def show(df, geo, indicator, years, regions):
    end = years[1]
    label = rate_label(indicator)
    rate_axis = t("rate_axis", label=label)
    data = filter_data(df, years, regions, indicator)
    departments = by_department(data, end)
    region_rates = by_region(data, end)
    top_region = region_rates.loc[region_rates["rate"].idxmax()]
    france = timeseries(filter_data(df, years, [], indicator))
    france_rate = france.loc[france["year"] == end, "rate"].iloc[0]
    top = departments.loc[departments["rate"].idxmax()]
    bottom = departments.loc[departments["rate"].idxmin()]

    st.header(t("ch2_title"))
    st.markdown(
        t(
            "ch2_headline",
            end=end,
            region=top_region["region"],
            indicator=indicator,
            rate=top_region["rate"],
            label=label,
            france=france_rate,
        )
    )

    st.subheader(t("compare_regions"))
    bar_chart(
        region_rates,
        "rate",
        "region",
        rate_axis,
        t("region_axis"),
        t("region_title", indicator=indicator, end=end),
        t("region_alt", indicator=indicator, label=label, end=end),
    )

    st.subheader(t("map_view"))
    if bottom["rate"] > 0:
        st.markdown(
            t(
                "map_ratio",
                top=top["department"],
                top_rate=top["rate"],
                ratio=top["rate"] / bottom["rate"],
                bottom=bottom["department"],
                bottom_rate=bottom["rate"],
            )
        )
    else:
        st.markdown(t("map_top", top=top["department"], top_rate=top["rate"]))
    map_chart(
        departments,
        geo,
        rate_axis,
        t("map_title", indicator=indicator, end=end),
        t("map_alt", indicator=indicator, label=label, end=end),
    )

    st.subheader(t("top_bottom"))
    n = min(10, len(departments))
    c1, c2 = st.columns(2)
    with c1:
        bar_chart(
            departments.nlargest(n, "rate"),
            "rate",
            "department",
            rate_axis,
            t("department_axis"),
            t("highest", n=n, end=end),
            t("highest_alt", n=n, indicator=indicator, end=end),
            height=400,
        )
    with c2:
        bar_chart(
            departments.nsmallest(n, "rate"),
            "rate",
            "department",
            rate_axis,
            t("department_axis"),
            t("lowest", n=n, end=end),
            t("lowest_alt", n=n, indicator=indicator, end=end),
            height=400,
        )

    st.markdown(t("ch2_transition"))
