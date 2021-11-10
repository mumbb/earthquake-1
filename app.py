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


data = load_data()

st.write(data)

# Make layer
layer = pdk.Layer(
    "PolygonLayer",  # 사용할 Layer 타입
    data,  # 시각화에 쓰일 데이터프레임
    get_polygon="coordinates",  # geometry 정보를 담고있는 컬럼 이름
    get_fill_color="[0, 255*정규화인구, 0]",  # 각 데이터 별 rgb 또는 rgba 값 (0~255)
    pickable=True,  # 지도와 interactive 한 동작 on
    auto_highlight=True,  # 마우스 오버(hover) 시 박스 출력
)

# Set the viewport location
center = [129.05562775, 35.1379222]
view_state = pdk.ViewState(longitude=center[0], latitude=center[1], zoom=10)
