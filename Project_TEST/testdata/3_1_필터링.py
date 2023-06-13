import pandas as pd 

years = range(2018, 2024)

data = {}
for year in years:
    read_path = "C:\\Users\\hsung\\OneDrive\\바탕 화면\\팀플 데이터\\전월세\\서울특별시_전월세가_{}.txt".format(year)
    data[year] = pd.read_csv(read_path, sep=',', encoding='cp949')
    
#['접수연도', '자치구코드', '자치구명', '법정동코드', '법정동명', '지번구분', '지번구분명', '본번', '부번','층', '계약일', '전월세 구분', '임대면적(㎡)', '보증금(만원)', '임대료(만원)', '건물명', '건축년도','건물용도', '계약기간', '신규갱신여부', '계약갱신권사용여부', '종전 보증금', '종전 임대료']
#필요 데이터 (자치구명, 법정동명, 계약일, 전월세 구분, 임대면적(㎡), 보증금(만원), 임대료(만원), 건물용도)

filter_data = {}
for year in years:
    filter_data[year] = data[year][["자치구명", "법정동명", "계약일", "전월세구분", "임대면적", "보증금(만원)", "임대료(만원)", "건물용도"]]

#필터 자료 csv 저장
# filter_data2018.to_csv("C:\\Users\\hsung\\OneDrive\\바탕 화면\\팀플 데이터\\전월세\\2018_filter_데이터.csv", encoding="utf-8-sig")
for year in years:
    save_path = "C:\\Users\\hsung\\OneDrive\\바탕 화면\\팀플 데이터\\전월세\\{}_filter_데이터.csv".format(year)
    filter_data[year].to_csv(save_path, encoding="utf-8-sig")
    