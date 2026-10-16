import pandas as pd

REGIONS = {
    "01": "Guadeloupe",
    "02": "Martinique",
    "03": "Guyane",
    "04": "La Réunion",
    "06": "Mayotte",
    "11": "Île-de-France",
    "24": "Centre-Val de Loire",
    "27": "Bourgogne-Franche-Comté",
    "28": "Normandie",
    "32": "Hauts-de-France",
    "44": "Grand Est",
    "52": "Pays de la Loire",
    "53": "Bretagne",
    "75": "Nouvelle-Aquitaine",
    "76": "Occitanie",
    "84": "Auvergne-Rhône-Alpes",
    "93": "Provence-Alpes-Côte d'Azur",
    "94": "Corse",
}

OVERSEAS = {
    "971": "Guadeloupe",
    "972": "Martinique",
    "973": "Guyane",
    "974": "La Réunion",
    "976": "Mayotte",
}

CATEGORIES = {
    "Homicides": "Crimes against people",
    "Tentatives d'homicide": "Crimes against people",
    "Violences physiques hors cadre familial": "Crimes against people",
    "Violences physiques intrafamiliales": "Crimes against people",
    "Violences sexuelles": "Crimes against people",
    "Vols avec armes": "Crimes against property",
    "Vols violents sans arme": "Crimes against property",
    "Vols sans violence contre des personnes": "Crimes against property",
    "Cambriolages de logement": "Crimes against property",
    "Vols de véhicule": "Crimes against property",
    "Vols dans les véhicules": "Crimes against property",
    "Vols d'accessoires sur véhicules": "Crimes against property",
    "Destructions et dégradations volontaires": "Crimes against property",
    "Escroqueries et fraudes aux moyens de paiement": "Fraud",
    "Trafic de stupéfiants": "Drugs",
    "Usage de stupéfiants": "Drugs",
}

SUB_INDICATORS = ["Usage de stupéfiants (AFD)", "Usage de stupéfiants (hors AFD)"]
HOUSING_INDICATOR = "Cambriolages de logement"


def quality_report(df_raw):
    expected_rows = df_raw["Code_departement"].nunique() * df_raw["indicateur"].nunique() * df_raw["annee"].nunique()

    base = df_raw["insee_pop"].where(df_raw["indicateur"] != HOUSING_INDICATOR, df_raw["insee_log"])
    rate_error = (df_raw["nombre"] / base * 1000 - df_raw["taux_pour_mille"]).abs().max()

    drugs = df_raw.pivot_table(index=["Code_departement", "annee"], columns="indicateur", values="nombre")
    drugs_gap = (drugs["Usage de stupéfiants"] - drugs[SUB_INDICATORS[0]] - drugs[SUB_INDICATORS[1]]).abs().max()

    population_year = df_raw.groupby("annee")["insee_pop_millesime"].max()
    old_population = population_year[population_year < population_year.index].index

    checks = pd.DataFrame(
        {
            "Check": [
                "Rows = departments x indicators x years",
                "No negative counts",
                "Rate per 1,000 matches count / population",
                "Drug use = AFD + non-AFD",
            ],
            "Result": [
                f"{len(df_raw)} / {expected_rows}",
                str((df_raw["nombre"] < 0).sum() == 0),
                f"max error = {rate_error:.6f}",
                f"max gap = {drugs_gap:.0f}",
            ],
        }
    )

    return {
        "missing": df_raw.isna().sum().rename("Missing values").to_frame(),
        "duplicates": int(df_raw.duplicated().sum()),
        "checks": checks,
        "old_population": sorted(old_population.tolist()),
    }


def clean_data(df_raw, geo):
    df = df_raw.rename(
        columns={
            "Code_departement": "dep_code",
            "Code_region": "reg_code",
            "annee": "year",
            "indicateur": "indicator",
            "unite_de_compte": "unit",
            "nombre": "count",
            "taux_pour_mille": "rate",
            "insee_pop": "population",
            "insee_log": "housing",
        }
    )
    df = df.drop_duplicates()
    df = df[~df["indicator"].isin(SUB_INDICATORS)]

    names = {f["properties"]["code"]: f["properties"]["nom"] for f in geo["features"]}
    names.update(OVERSEAS)

    df["department"] = df["dep_code"].map(names)
    df["region"] = df["reg_code"].map(REGIONS)
    df["category"] = df["indicator"].map(CATEGORIES)
    df["base"] = df["population"].where(df["indicator"] != HOUSING_INDICATOR, df["housing"])
    return df[["dep_code", "department", "region", "year", "category", "indicator", "unit", "count", "base", "rate"]]


def make_tables(df_raw, geo):
    return {"clean": clean_data(df_raw, geo), "quality": quality_report(df_raw)}


def rate_label(indicator):
    if indicator == HOUSING_INDICATOR:
        return "per 1,000 homes"
    return "per 1,000 inhabitants"


def filter_data(df, years, regions, indicator=None):
    out = df[df["year"].between(years[0], years[1])]
    if regions:
        out = out[out["region"].isin(regions)]
    if indicator:
        out = out[out["indicator"] == indicator]
    return out


def add_rate(df):
    df = df.copy()
    df["rate"] = df["count"] / df["base"] * 1000
    return df


def timeseries(df):
    return add_rate(df.groupby("year", as_index=False)[["count", "base"]].sum())


def by_region(df, year):
    return add_rate(df[df["year"] == year].groupby("region", as_index=False)[["count", "base"]].sum())


def by_department(df, year):
    return df[df["year"] == year][["dep_code", "department", "region", "count", "rate"]]


def change_by_indicator(df, start_year, end_year):
    out = df[df["year"].isin([start_year, end_year])]
    out = out.pivot_table(index=["category", "indicator"], columns="year", values="count", aggfunc="sum").reset_index()
    out = out[out[start_year] > 0]
    out["change"] = (out[end_year] / out[start_year] - 1) * 100
    return out.sort_values("change")
