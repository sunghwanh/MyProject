import pandas as pd 

data_2018 = pd.read_csv("C:\\Users\\hsung\\OneDrive\\바탕 화면\\팀플 데이터\\전월세\\서울특별시_전월세가_2018.txt", sep=',', encoding='cp949')
data_2019 = pd.read_csv("C:\\Users\\hsung\\OneDrive\\바탕 화면\\팀플 데이터\\전월세\\서울특별시_전월세가_2019.txt", sep=',', encoding='cp949')
data_2020 = pd.read_csv("C:\\Users\\hsung\\OneDrive\\바탕 화면\\팀플 데이터\\전월세\\서울특별시_전월세가_2020.txt", sep=',', encoding='cp949')
data_2021 = pd.read_csv("C:\\Users\\hsung\\OneDrive\\바탕 화면\\팀플 데이터\\전월세\\서울특별시_전월세가_2021.txt", sep=',', encoding='cp949')
data_2022 = pd.read_csv("C:\\Users\\hsung\\OneDrive\\바탕 화면\\팀플 데이터\\전월세\\서울특별시_전월세가_2022.txt", sep=',', encoding='cp949')
data_2023 = pd.read_csv("C:\\Users\\hsung\\OneDrive\\바탕 화면\\팀플 데이터\\전월세\\서울특별시_전월세가_2023.txt", sep=',', encoding='cp949')

#['접수연도', '자치구코드', '자치구명', '법정동코드', '법정동명', '지번구분', '지번구분명', '본번', '부번','층', '계약일', '전월세 구분', '임대면적(㎡)', '보증금(만원)', '임대료(만원)', '건물명', '건축년도','건물용도', '계약기간', '신규갱신여부', '계약갱신권사용여부', '종전 보증금', '종전 임대료']
#필요 데이터 (자치구명, 법정동명, 계약일, 전월세 구분, 임대면적(㎡), 보증금(만원), 임대료(만원), 건물용도)
# print(data_2018.info())
filter_data2018 = data_2018[["자치구명", "법정동명", "계약일", "전월세구분", "임대면적", "보증금(만원)", "임대료(만원)", "건물용도"]]
filter_data2019 = data_2019[["자치구명", "법정동명", "계약일", "전월세구분", "임대면적", "보증금(만원)", "임대료(만원)", "건물용도"]]
filter_data2020 = data_2020[["자치구명", "법정동명", "계약일", "전월세구분", "임대면적", "보증금(만원)", "임대료(만원)", "건물용도"]]
filter_data2021 = data_2021[["자치구명", "법정동명", "계약일", "전월세구분", "임대면적", "보증금(만원)", "임대료(만원)", "건물용도"]]
filter_data2022 = data_2022[["자치구명", "법정동명", "계약일", "전월세구분", "임대면적", "보증금(만원)", "임대료(만원)", "건물용도"]]
filter_data2023 = data_2023[["자치구명", "법정동명", "계약일", "전월세구분", "임대면적", "보증금(만원)", "임대료(만원)", "건물용도"]]

#필터 자료 csv 저장
filter_data2018.to_csv("C:\\Users\\hsung\\OneDrive\\바탕 화면\\팀플 데이터\\전월세\\2018_filter_데이터.csv", encoding="utf-8-sig")
filter_data2019.to_csv("C:\\Users\\hsung\\OneDrive\\바탕 화면\\팀플 데이터\\전월세\\2019_filter_데이터.csv", encoding="utf-8-sig")
filter_data2020.to_csv("C:\\Users\\hsung\\OneDrive\\바탕 화면\\팀플 데이터\\전월세\\2020_filter_데이터.csv", encoding="utf-8-sig")
filter_data2021.to_csv("C:\\Users\\hsung\\OneDrive\\바탕 화면\\팀플 데이터\\전월세\\2021_filter_데이터.csv", encoding="utf-8-sig")
filter_data2022.to_csv("C:\\Users\\hsung\\OneDrive\\바탕 화면\\팀플 데이터\\전월세\\2022_filter_데이터.csv", encoding="utf-8-sig")
filter_data2023.to_csv("C:\\Users\\hsung\\OneDrive\\바탕 화면\\팀플 데이터\\전월세\\2023_filter_데이터.csv", encoding="utf-8-sig")
