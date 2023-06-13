import pandas as pd 
import time

read_path = "C:\\Users\\hsung\\OneDrive\\바탕 화면\\팀플 데이터\\전월세\\6years_data_total_pos123.csv"
data = pd.read_csv(read_path, encoding='utf-8')
data = data[data['건물용도'] != '아파트'][:100]

read_path = "C:\\Users\\hsung\\OneDrive\\바탕 화면\\팀플 데이터\\전월세\\6years_data_pos.csv"
all_data = pd.read_csv(read_path, encoding='utf-8')
all_data = all_data[all_data['건물용도'] != '아파트'][:100]
print(data.shape)
print(all_data.shape)

filter_data = all_data
filter_data['경위도'] = None
big_data = filter_data.copy()

print('1', filter_data.shape)

big_data = filter_data[filter_data['경위도'].notnull()]
filter_d = all_data.drop_duplicates(subset='addr')
# data['addr'] = filter_d['addr'].values
# # print(filter_d['addr'])
# # print(data['addr'])
# print(filter_data[filter_data['addr'] == "금천구 독산동 1006 0049"])
# # print('1',filter_data['addr'][20])
# # print('2',data['addr'][0])
# # print('3',filter_data['addr'][20] == data['addr'][10])
# print()
# print()
# print()
# for i in range(len(data)):
#     start = time.perf_counter()
    
#     if filter_data.empty:
#         continue
#     gu = data['자치구명'][i]
#     print(gu)
    
#     filter_data = filter_data[filter_data['경위도'].isnull()]

#     for j in range(len(filter_data)):
#         if all_data['addr'][j] == data['addr'][i]:
#             filter_data.loc[j, '경위도'] = data.loc[i, '경위도']
#             big_data.loc[j, '경위도'] = filter_data.loc[j, '경위도']
            
#     print(filter_data.shape)
#     print(big_data.shape)
    
#     finish = time.perf_counter()
#     print(f'{round(finish-start,2)}초 만에 작업이 완료되었습니다.')
#     print(i, '바퀴')

# print(big_data)
            
# csv 저장
# save_path = "C:\\Users\\hsung\\OneDrive\\바탕 화면\\팀플 데이터\\전월세\\6years_data_pos.csv"
# all_data.to_csv(save_path, encoding="utf-8-sig")