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
DATA_URL = (
    "https://raw.githubusercontent.com/givemetarte/earthquake/main/busan-polygon.csv"
)


@st.cache(allow_output_mutation=True, persist=True)
def load_data():
    data = pd.read_csv(DATA_URL, encoding="utf-8", index_col=0)
    return data
