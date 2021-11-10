import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff


st.set_page_config(layout="wide")
st.title('EarthQuake')


# html upload def
def embededHTMl(file_path) :
    HtmlFile = open(file_path, 'r', encoding = 'utf-8')
    source_code = HtmlFile.read() 
    components.html(source_code, height = 500)

@st.cache
def load_data(DATA_URL):
    data = pd.read_csv(DATA_URL)
    return data

def set_format():
    fig.update_layout(plot_bgcolor='#FFFFFF')
    fig.update_yaxes(showline=True, linewidth=1, linecolor='black', mirror=True,gridcolor='#E1E1E1',zerolinecolor='#E1E1E1')
    fig.update_xaxes(showline=True, linewidth=1, linecolor='black', mirror=True)



"""
### 4. 부산시 건물 노후지도(지진 취약도)

**📄. 데이터 설명**

* 세움터의 건축물대장 데이터 그래프 변환
* 행정구역, 지번주소, 기관 등 기반 데이터와 연계
* blazegraph의 SPARQL 질의로 데이터 추출
-> 쿼리 이미지?, 데이터셋 이미지 등..?


**📄. 분석 과정**

* 파이썬 환경(Jupyter)에서 데이터 분석과 시각화 수행
* 건축물 노후도, 내진설계 여부를 고려한 데이터 분석과 시각화 수행
* 지진으로 인한 건축물 피해액(공동주택 가격, 만원 단위) 도출

"""

"""
#### (1) 부산시 시군구별 노후지도

"""


embededHTMl("data/sgg_buildingOld_map.html")
"""
* 설명 작성
"""

"""
#### (2) 부산시 읍면동별 노후지도

"""

embededHTMl("data/emd_buildingOld_map.html")

"""
* 설명 작성

"""


"""
### 5. 부산시 지진 피해액 계산


"""

## (1) 지진이 많이 일어나는 노후 지역에 대해 계산 (표, 차트)

df = load_data('data/sgg_building_money.csv')

region = st.multiselect("보고 싶은 지역은?", 
                        ['강서구', '금정구', '기장군', '남구', '동구', '동래구', '부산진구', '북구', '사상구', '사하구','서구', '수영구', '연제구', '중구', '해운대구'])

chart_df = df[df['divisionName'].isin(region)]

fig = px.bar(chart_df, x = 'divisionName', y = '공동주택가격(만원)',  width = 1000)
set_format()
st.plotly_chart(fig)

