import json
import requests
import pandas as pd
import multiprocessing as mp
import time

api_key = "6900291ad1abb5455af2b904dde0193f"
max_retries = 100

def addr_to_lat_lon(addr):
    url = 'https://dapi.kakao.com/v2/local/search/address.json?query={address}'.format(address=addr)
    headers = {"Authorization": "KakaoAK " + api_key}
    retries = 0
    while retries < max_retries:
        try:
            result = json.loads(str(requests.get(url, headers=headers).text))
            if 'documents' in result and len(result['documents']) > 0:
                match_first = result['documents'][0]['address']
                return float(match_first['y']), float(match_first['x'])
            else:
                print("Warning: No result found for address:", addr)
                return None, None
        except (IndexError, KeyError):
            print("Error: Failed to retrieve address:", addr)
            retries += 1
            time.sleep(1)  # wait for 1 second before retrying
    return None, None

years = range(2019, 2022)

data = {}


path = "C:\\Users\\hsung\\OneDrive\\바탕 화면\\팀플 데이터\\전월세\\6years_data_pos.csv"

all_years = pd.read_csv(path, encoding='utf-8', index_col = 0)
all_years['본번'] = all_years['본번'].astype(str)
all_years['부번'] = all_years['부번'].astype(str)
all_years = all_years[all_years['계약일'] >= 201801]
all_years = all_years[all_years['본번'] != "nan"]
all_years = all_years[all_years['부번'] != "nan"]
all_years = all_years[all_years['부번'] != "nan"]
all_years = all_years.drop_duplicates(subset='addr')
all_years = all_years[all_years['부번'] != "nan"]

print(all_years)

all_years['경도위도'] = None
lat_lon_list = []
i = 0
for gu, dong, bon, bu in all_years[["자치구명", "법정동명", "본번", "부번"]].values:
    # time.sleep(0.3)
    addr = "{} {} {} {}".format(gu, dong, bon, bu)
    lat, lon = addr_to_lat_lon(addr)
    if lat is not None and lon is not None:
        lat_lon_list.append((lat, lon))
    else:
        lat_lon_list.append((None, None))
    i = i +1
    print(lat, lon,i)
    
all_years['경도위도'] = lat_lon_list

all_years = all_years[["자치구명","법정동명", "계약일", "전월세구분", "임대면적", "보증금(만원)", "임대료(만원)", "건물용도",'경도위도']]
all_years = all_years[['경도위도']]
print(all_years)

#csv저장
save_path = "C:\\Users\\hsung\\OneDrive\\바탕 화면\\팀플 데이터\\전월세\\6years_data_pos_data0.csv"
all_years.to_csv(save_path, encoding="utf-8-sig")
