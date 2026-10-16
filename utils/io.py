import json
from pathlib import Path

import pandas as pd
import requests

DATA_DIR = Path(__file__).resolve().parent.parent / "data"

DATA_URL = (
    "https://static.data.gouv.fr/resources/"
    "bases-statistiques-communale-departementale-et-regionale-de-la-delinquance-enregistree-par-la-police-et-la-gendarmerie-nationales/"
    "20260709-120038/donnee-dep-data.gouv-2025-geographie2026-produit-le2026-06-25.csv"
)
GEO_URL = "https://raw.githubusercontent.com/gregoiredavid/france-geojson/master/departements-version-simplifiee.geojson"

SOURCE = "Bases statistiques de la délinquance enregistrée par la police et la gendarmerie nationales (SSMSI)"
PORTAL = "data.gouv.fr"
LICENSE = "Licence Ouverte / Open Licence v2.0"


def fetch_and_cache(url, filename):
    path = DATA_DIR / filename
    if not path.exists():
        DATA_DIR.mkdir(exist_ok=True)
        response = requests.get(url, timeout=60)
        response.raise_for_status()
        path.write_bytes(response.content)
    return path


def load_data():
    path = fetch_and_cache(DATA_URL, "delinquance_dep.csv")
    return pd.read_csv(path, sep=";", decimal=",", dtype={"Code_departement": str, "Code_region": str})


def load_geojson():
    path = fetch_and_cache(GEO_URL, "departements.geojson")
    with open(path, encoding="utf-8") as f:
        return json.load(f)
