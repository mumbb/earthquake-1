# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
import geopandas as gpd
import numpy as np
import os
import pydeck as pdk
import geojson
import time

# SETTING PAGE CONFIG TO WIDE MODE
st.set_page_config(layout="wide")

"""
# 📍 Earthquake in Busan Visualization

### 1. 부산 읍면동(행정동)별 인구수 시각화

"""
DATA_URL = "https://raw.githubusercontent.com/givemetarte/earthquake/main/busan-population-polygon.csv"


@st.cache(persist=True)
def load_data():
    data = pd.read_csv(DATA_URL, encoding="utf-8", index_col=0)
    return data


data = load_data()


def multipolygon_to_coordinates(x):
    if x.geom_type == "MultiPolygon":
        lon, lat = x[0].exterior.xy
    else:
        lon, lat = x.exterior.xy
    return [[x, y] for x, y in zip(lon, lat)]


data["coordinates"] = data["geometry"].apply(multipolygon_to_coordinates)
del data["geometry"]

st.write(data)
