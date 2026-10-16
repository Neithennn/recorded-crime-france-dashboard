import plotly.express as px
import streamlit as st

MAIN_COLOR = "#2e86c1"
CATEGORY_COLORS = {
    "Crimes against people": "#e74c3c",
    "Crimes against property": "#3498db",
    "Fraud": "#f39c12",
    "Drugs": "#a569bd",
}


EVENTS = [
    (2017.8, "#MeToo", 1.0),
    (2019.7, "Domestic violence Grenelle", 0.9),
    (2020.2, "1st lockdown", 0.8),
    (2020.7, "Fixed fine for drug use", 0.7),
]


def show(fig, alt_text):
    fig.update_layout(margin=dict(t=50), font=dict(size=14))
    st.plotly_chart(fig, width="stretch")
    st.caption(alt_text)


def add_events(fig, years):
    for x, text, y in EVENTS:
        if years[0] < x < years[1]:
            fig.add_vline(x=x, line_dash="dot", line_color="grey")
            fig.add_annotation(x=x, y=y, yref="paper", text=text, showarrow=False, xanchor="left", font=dict(size=12))


def scissor_chart(df, years, alt_text):
    fig = px.line(
        df,
        x="year",
        y="index",
        color="category",
        markers=True,
        title=f"Recorded cases by category ({years[0]} = 100)",
        labels={"year": "Year", "index": f"Index ({years[0]} = 100)", "category": "Category", "count": "Recorded cases"},
        hover_data={"count": ":,", "index": ":.0f"},
        color_discrete_map=CATEGORY_COLORS,
        height=500,
    )
    fig.add_hline(y=100, line_dash="dash", line_color="grey")
    add_events(fig, years)
    fig.update_xaxes(dtick=1)
    fig.update_layout(legend=dict(orientation="h", y=-0.2))
    show(fig, alt_text)


def line_chart(df, years, rate_label, title, alt_text):
    fig = px.line(
        df,
        x="year",
        y="rate",
        markers=True,
        title=title,
        labels={"year": "Year", "rate": rate_label, "count": "Recorded cases"},
        hover_data={"count": ":,"},
        color_discrete_sequence=[MAIN_COLOR],
    )
    add_events(fig, years)
    fig.update_yaxes(rangemode="tozero")
    fig.update_xaxes(dtick=1)
    show(fig, alt_text)


def change_chart(df, start_year, end_year, alt_text):
    fig = px.bar(
        df,
        x="change",
        y="indicator",
        color="category",
        orientation="h",
        title=f"Change in recorded cases, {start_year} → {end_year}",
        labels={"change": "Change (%)", "indicator": "Indicator", "category": "Category"},
        color_discrete_map=CATEGORY_COLORS,
        height=550,
    )
    fig.add_vline(x=0, line_color="grey")
    fig.update_traces(hovertemplate="%{y}<br>%{x:.1f} %")
    fig.update_yaxes(categoryorder="total ascending")
    fig.update_layout(legend=dict(orientation="h", y=-0.15))
    show(fig, alt_text)


def bar_chart(df, x, y, x_label, y_label, title, alt_text, height=450):
    fig = px.bar(
        df.sort_values(x),
        x=x,
        y=y,
        orientation="h",
        title=title,
        labels={x: x_label, y: y_label},
        color_discrete_sequence=[MAIN_COLOR],
        height=height,
    )
    fig.update_traces(hovertemplate="%{y}<br>%{x:.2f}")
    fig.update_yaxes(automargin=True, title_standoff=10)
    show(fig, alt_text)


def map_chart(df, geo, rate_label, title, alt_text):
    fig = px.choropleth(
        df,
        geojson=geo,
        locations="dep_code",
        featureidkey="properties.code",
        color="rate",
        color_continuous_scale="OrRd",
        hover_name="department",
        hover_data={"dep_code": False, "region": True, "rate": ":.2f", "count": ":,"},
        labels={"rate": rate_label, "count": "Recorded cases", "region": "Region"},
        title=title,
        height=600,
    )
    fig.update_geos(fitbounds="locations", visible=False, projection_type="mercator", bgcolor="rgba(0,0,0,0)")
    fig.update_layout(margin=dict(l=0, r=0, t=50, b=0))
    show(fig, alt_text)
