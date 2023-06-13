import pandas as pd 

years = range(2018, 2024)

data = {}
for year in years:
    read_path = "C:\\Users\\hsung\\OneDrive\\바탕 화면\\팀플 데이터\\전월세\\서울특별시_전월세가_{}.txt".format(year)
    data[year] = pd.read_csv(read_path, sep=',', encoding='cp949')
    
#(자치구명, 법정동명, 계약일, 전월세구분, 임대면적, 보증금(만원), 임대료(만원), 건물용도)

filter_data = {}
for year in years:
    filter_data[year] = data[year][["자치구명", "법정동명", "계약일", "전월세구분", "임대면적", "보증금(만원)", "임대료(만원)", "건물용도"]]
    filter_data[year]['계약일'] = filter_data[year]['계약일'].apply(lambda x: int(str(x)[:6]))
    filter_data[year]['평당보증금(만원)'] = filter_data[year]['보증금(만원)'] / (filter_data[year]['임대면적'] / 3.305785)
    filter_data[year]['평당임대료(만원)'] = filter_data[year]['임대료(만원)'] / (filter_data[year]['임대면적'] / 3.305785)

all_years = pd.concat(filter_data.values())
all_years = all_years[all_years['계약일'] >= 201801]
#csv저장
save_path = "C:\\Users\\hsung\\OneDrive\\바탕 화면\\팀플 데이터\\전월세\\6years_data.csv"
all_years.to_csv(save_path, encoding="utf-8-sig")
