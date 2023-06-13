import pandas as pd 
years = range(2018, 2024)
filter_data = {}
for year in years:
    path = "C:\\Users\\hsung\\OneDrive\\바탕 화면\\팀플 데이터\\전월세\\{}_filter_데이터.csv".format(year)
    filter_data[year] = pd.read_csv(path, encoding='utf-8', index_col = 0)
    filter_data[year]['계약일'] = filter_data[year]['계약일'].apply(lambda x: int(str(x)[:6]))
   
    year_start = int(f"{year}01")
    filter_data[year] = filter_data[year][filter_data[year]['계약일'] >= year_start]
    
#구별 데이터
#강남구,강동구,강북구,강서구,관악구,광진구,구로구,금천구,노원구,도봉구,동대문구,동작구,마포구,서대문구,서초구,성동구,성북구,송파구,양천구,영등포구,용산구,은평구,종로구,중구,중랑구

gu_data = ['강남구','강동구','강북구','강서구','관악구','광진구','구로구','금천구','노원구','도봉구','동대문구',\
    '동작구','마포구','서대문구','서초구','성동구','성북구','송파구','양천구',\
        '영등포구','용산구','은평구','종로구','중구','중랑구']

filter_gu = {}
for year in years:
    filter_gu[year] = {}
    for gu in gu_data:
        gu_rows = filter_data[year]['자치구명'] == gu
        filter_gu[year][gu] = filter_data[year][gu_rows]

all_years = pd.concat(filter_data.values())
type_data = ['전세','월세']
all_gu = {} 

# 초기화된 구 딕셔리 생성
for gu in gu_data:
    all_gu[gu] = {}

# 구별 전월세 구분
for gu in gu_data:
    for tp in type_data:
        data_filter_row = (all_years['자치구명'] == gu) & (all_years['전월세구분'] == tp)
        # print(data_filter_row)
        all_gu[gu][tp] = all_years[data_filter_row]

        # save_path = "C:\\Users\\hsung\\OneDrive\\바탕 화면\\팀플 데이터\\전월세\\gudata\\{}_{}_data.csv".format(gu,tp)
        # all_gu[gu][tp].to_csv(save_path, encoding="utf-8-sig")
        
print(all_gu["강남구"]["월세"][:5])
print(all_gu["강남구"]["전세"][:5])