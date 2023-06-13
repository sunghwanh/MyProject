import pandas as pd 
from collections import defaultdict
import pickle

path = "C:\\Users\\hsung\\OneDrive\\바탕 화면\\팀플 데이터\\전월세\\6years_data.csv"
years_data = pd.read_csv(path, encoding='utf-8', index_col = 0)

자치구명 = list(set(years_data['자치구명']))
# ['강남구','강동구','강북구','강서구','관악구','광진구','구로구','금천구','노원구',\
#  '도봉구','동대문구','동작구','마포구','서대문구','서초구','성동구','성북구','송파구',\
#  '양천구','영등포구','용산구','은평구','종로구','중구','중랑구']
전월세구분 = list(set(years_data['전월세구분']))
# ['전세','월세']
건물용도 = list(set(years_data['건물용도']))
#'오피스텔', '연립다세대', '아파트', '단독다가구'

총데이터 = {}
for 자치구 in 자치구명:
    총데이터[자치구] = {}
    for 전월세 in 전월세구분:
        총데이터[자치구][전월세] = {}
        for 용도 in 건물용도:
            data_filter_row = (years_data['자치구명'] == 자치구) & (years_data['전월세구분'] == 전월세) & (years_data['건물용도'] == 용도)
            총데이터[자치구][전월세][용도] = years_data[data_filter_row]

with open("총데이터.pkl", "wb") as file:
    pickle.dump(총데이터, file)
    