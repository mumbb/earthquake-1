import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff


st.set_page_config(layout="wide")
st.title('EarthQuake')


# html embeded def
def embededHTML(file_path) :
    HtmlFile = open(file_path, 'r', encoding = 'utf-8')
    source_code = HtmlFile.read() 
    components.html(source_code, height = 500)


# plotly graph design set def
def set_format():
    fig.update_layout(plot_bgcolor='#FFFFFF')
    fig.update_yaxes(showline=True, tickformat=',', linewidth=1, linecolor='black', mirror=True,gridcolor='#E1E1E1',zerolinecolor='#E1E1E1', automargin=True)
    fig.update_xaxes(showline=True, linewidth=1, linecolor='black', mirror=True)


"""
### 4. 부산시 지진취약지도 구축

**📄. 데이터 설명**

* [세움터](https://cloud.eais.go.kr/)의 건축물대장 데이터, 주택가격 데이터 그래프 변환
* 행정구역, 지번주소, 기관 등 기반 데이터와 연계
* 파이썬 환경(Jupyter)에서 blazegraph endpoint를 통한 SPARQL 질의로 데이터 추출


**📄. 분석 과정**

* 파이썬 환경(Jupyter)에서 데이터 분석과 시각화 수행
* 건축물 노후도, 내진설계 여부를 고려한 부산시 지진취약지도 도출
    * 노후건축물 : 건축물 사용승인일로부터 25년이 지난 건축물
    * 내진설계 의무대상 : 건축법(2017)에 따른 연면적 200m2 이상의 건축물
    * 지진취약도 : **전체 건축물 대비 노후건축물의 비율**과 **내진설계 의무대상 건축물 수 대비 내진설계 미준수 건축물의 비율**의 평균
* 지진으로 인한 예상 피해액(공동주택 가격, 만원 단위) 계산

"""
#### (1) 시군구별 지진취약지도
"""
#### (1) 시군구별 지진취약지도
"""

embededHTML("data/sgg_buildingOld_map.html")

"""
** 부산시 전체 건축물의 약 63%가 25년 이상의 노후건축물**
* 지진취약도가 가장 높은 시군구는 동구
* 부산에서 지진이 가장 많이 일어나는 기장군의 지진취약도는 41.31로 가장 낮음.
* 강한 지진이 3번 일어난 해운대구는 건축물의 71%가 노후건축물이고, 내진설계 적용이 필요한 건축물의 69%가 내진설계를 갖추고 있지 않음

"""

"""
#### (2) 읍면동별 지진취약지도

"""

embededHTML("data/emd_buildingOld_map.html")

"""
* 읍면동 단위에서는 동래구 칠산동의 지진취약도(96.13)가 가장 높음
* 동래구 칠산동 건축물 중 94%의 건축물이 노후건축물이고, 내진설계 적용 대상이지만 내진설계를 갖추지 못한 건축물이 97%
* 해운대구에서는 반송동의 지진취약도가 가장 높으며(85.25), 내진설계 미준수 건축물 비율(90%)이 높음

🚨 노후건축물에 대한 내진설계 소급적용을 위한 관련 조례의 시행, 재정적 지원이 필요

"""


"""
### 5. 지진 예상 피해액

* **지진 예상 피해액**은 지진 발생 시 붕괴 위험이 있는 건축물 가격의 합을 구함
* 붕괴 위험 건축물 : 노후 건축물이고, 내진설계 의무대상이지만 내진설계를 갖추지 못한 건축물

"""

## height 정보 조정 필요

df = pd.read_csv('data/sgg_building_money.csv')

region = st.multiselect("지역을 선택하세요.", 
                        ['강서구', '금정구', '기장군', '남구', '동구', '동래구', '부산진구', '북구', '사상구', '사하구','서구', '수영구', '연제구', '중구', '해운대구'])

chart_df = df[df['divisionName'].isin(region)]
chart_df.rename(columns = {'divisionName' : '시군구명'}, inplace = True)
chart_df.sort_values(by = '공동주택가격(만원)', ascending= True, inplace= True)

fig = px.bar(chart_df, x = '시군구명', y = '공동주택가격(만원)',  range_y = [0, 600000000], width = 1000)
set_format()
st.plotly_chart(fig)

