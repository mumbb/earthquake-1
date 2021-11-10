import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np

st.set_page_config(layout="wide")

st.title("EarthQuake")

"""
행정구역, 기관, 주소 그래프 데이터와 일반 테이블 데이터를 결합할 수 있다.


예시로 전국 지진 발생현황 데이터와 기반 그래프 데이터를 활용한 지진 취약 지역을 예측할 수 있다.

"""


st.header("1. 전국 지진 발생현황 (1978~2021)")

"""
🌤 [기상청 날씨누리]("https://www.weather.go.kr/w/eqk-vol/search/korea.do")에서 공개하는 국내지진조회 데이터를 통해 약 40년(1978-2021)간의 지진 현황을 알 수 있다.

"""

HtmlFile = open("./data/korea_earth(1978-2021)-geo.html", "r", encoding="utf-8")
source_code = HtmlFile.read()
print(source_code)
components.html(source_code, height=600)


"""
위 그래프를 보면 2015년 이후 경상북도를 포함하여 모든 시도의 지진 빈도가 급격히 늘고 있습니다.

"""

HtmlFile = open("./data/korea_earthquake_detail-line.html", "r", encoding="utf-8")
source_code = HtmlFile.read()
print(source_code)
components.html(source_code, height=500)


st.header("2. 전국 지진 누적 빈도")

col3, col4 = st.columns(2)
with col3:
    st.subheader("전국 시도별 지진 누적 빈도")
    st.caption("미소지진을 제외한 규모 2.0 이상의 지진 누적빈도")
    HtmlFile = open("./data/sido_earthquake.html", "r", encoding="utf-8")
    source_code = HtmlFile.read()
    print(source_code)
    components.html(source_code, height=600)
    """
    전국 시도 중 경상북도가 가장 지진이 많이 일어났음.
    부산은 2.0 이상의 지진이 13번 일어났으며, 미소지진을 포함하면 총 23번의 지진이 일어났다.
    """

with col4:
    st.subheader("전국 시군구별 지진 누적 빈도")
    st.caption("미소지진을 제외한 규모 2.0 이상의 지진 누적빈도")
    HtmlFile = open("./data/sigungu_earthquake.html", "r", encoding="utf-8")
    source_code = HtmlFile.read()
    print(source_code)
    components.html(source_code, height=600)
    """
    전국 시군구 중에서는 경주시가 가장 지진이 많이 일어났다.
    부산 시구군 중에서는 기장군이 8번, 해운대구가 3번, 금정구가 2번으로 총 13번의 지진이 발생했다.
    """
st.subheader("3. 지진 대피소 scatter plot")
