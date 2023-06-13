import pandas as pd
import time
from multiprocessing import Pool

# 데이터 로드
read_path = "C:\\Users\\hsung\\OneDrive\\바탕 화면\\팀플 데이터\\전월세\\6years_data_total_pos123.csv"
data = pd.read_csv(read_path, encoding='utf-8')

read_path = "C:\\Users\\hsung\\OneDrive\\바탕 화면\\팀플 데이터\\전월세\\6years_data_pos.csv"
all_data = pd.read_csv(read_path, encoding='utf-8')

# 중복 제거한 주소 데이터로 1번 데이터의 주소 열 채우기
filter_d = all_data.drop_duplicates(subset='addr')
data['addr'] = filter_d['addr'].values

data = data[data['건물용도'] != '아파트']
all_data = all_data[all_data['건물용도'] != '아파트'].reset_index(drop=True)

print(data)
print(all_data)

print(data.shape)
print(all_data.shape)

# 경위도 열 초기화
all_data['경위도'] = None

def update_geolocation(row):
    addr = row['addr']
    geolocation = row['경위도']
    if pd.isna(geolocation):
        matching_rows = data[data['addr'].str.strip() == addr.strip()]
        if len(matching_rows) > 0:
            geolocation = matching_rows['경위도'].values[0]  # 첫 번째 값을 사용하여 할당
            
    return geolocation

def process_data_chunk(chunk):
    print("Processing chunk:", chunk.index[0], "-", chunk.index[-1])
    chunk['경위도'] = chunk.apply(update_geolocation, axis=1)
    return chunk

# 데이터 분할 및 병렬 처리
num_processes = 4
chunk_size = len(all_data) // num_processes

chunks = [all_data[i:i+chunk_size] for i in range(0, len(all_data), chunk_size)]

if __name__ == '__main__':
    with Pool(processes=num_processes) as pool:
        results = pool.map(process_data_chunk, chunks)

    # 결과 병합
    hap_data = pd.concat(results)

    print(hap_data)
    # csv 저장
    save_path = "C:\\Users\\hsung\\OneDrive\\바탕 화면\\팀플 데이터\\전월세\\6years_data_pos100.csv"
    hap_data.to_csv(save_path, encoding="utf-8-sig", index=False)
