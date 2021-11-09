# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
import numpy as np
import os
from mapboxgl.utils import create_color_stops
import mapboxgl
from mapboxgl.viz import *
import geojson
import time

# SETTING PAGE CONFIG TO WIDE MODE
st.set_page_config(layout="wide")

"""
# 📍 Earthquake in Busan Visualization

### 1. 부산 읍면동(행정동)별 인구수 시각화

"""
DATA_URL = ""


@st.cache(persist=True)
def load_data():
    with open(DATA_URL, "rt", encoding="utf-8") as f:
        data = geojson.load(f)
    return data


st.write(data)
