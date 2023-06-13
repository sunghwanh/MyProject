import pandas as pd
import multiprocessing as mp

path = "C:\\Users\\hsung\\OneDrive\\바탕 화면\\팀플 데이터\\전월세\\6years_data_pos_data0.csv"
all_years = pd.read_csv(path, encoding='utf-8', index_col = 0,dtype={ '본번':str, '부번':str })

path2 = "C:\\Users\\hsung\\OneDrive\\바탕 화면\\팀플 데이터\\전월세\\6years_data_pos_data001.csv"
all_years2 = pd.read_csv(path2, encoding='utf-8', index_col = 0,dtype={ '본번':str, '부번':str })

path3 = "C:\\Users\\hsung\\OneDrive\\바탕 화면\\팀플 데이터\\전월세\\6years_data_pos.csv"
all_years3 = pd.read_csv(path3, encoding='utf-8', index_col = 0)
all_years3 = all_years3.drop_duplicates(subset='addr')
all_years3 = all_years3['건물용도']

print(all_years)
print(all_years2)
print(all_years3)
all_years2['경위도'] = all_years.경도위도.str[1:-1]
all_years2['건물용도'] = all_years3

print(all_years2)

# #csv저장
save_path = "C:\\Users\\hsung\\OneDrive\\바탕 화면\\팀플 데이터\\전월세\\6years_data_total_pos123.csv"
all_years2.to_csv(save_path, encoding="utf-8-sig")
