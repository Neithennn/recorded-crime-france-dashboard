import plotly.express as px
import streamlit as st

MAIN_COLOR = "#2e86c1"
CATEGORY_COLORS = {
    "Crimes against people": "#e74c3c",
    "Crimes against property": "#3498db",
    "Fraud": "#f39c12",
    "Drugs": "#a569bd",
}


def show(fig, alt_text):
    fig.update_layout(margin=dict(t=50), font=dict(size=14))
    st.plotly_chart(fig, width="stretch")
    st.caption(alt_text)


def line_chart(df, rate_label, title, alt_text):
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
    if df["year"].min() <= 2020 <= df["year"].max():
        fig.add_vrect(x0=2019.5, x1=2020.5, fillcolor="grey", opacity=0.2, line_width=0)
        fig.add_annotation(x=2020, y=df["rate"].max(), text="COVID-19 lockdowns", showarrow=False, yshift=10)
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
