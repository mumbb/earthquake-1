# -*- coding: utf-8 -*-

import streamlit as st
import streamlit.components.v1 as components
import os
from koad_viz import koad_viz


# SETTING PAGE CONFIG TO WIDE MODE
st.set_page_config(layout="wide")

"""
# 📍 Earthquake in Busan Visualization

### 1. 부산 읍면동(행정동)별 인구수 시각화

"""

# SIDEBAR
st.sidebar.image("./static/hike.png")
add_selectbox = st.sidebar.selectbox(
    "What would you like to see?", ("행정구역 인구수", "지진 시나리오")
)


# busan population viz
koad_viz(600)


# @st.cache(allow_output_mutation=True, persist=True)
