import csv
from geopy.geocoders import Nominatim

def get_coordinates(address):
    geolocator = Nominatim(user_agent="my_geocoder")  # 사용자 에이전트를 지정하세요.
    location = geolocator.geocode(address)
    if location:
        latitude = location.latitude
        longitude = location.longitude
        return latitude, longitude
    else:
        return None
print(get_coordinates("서대문구 연희동 136-7"))
# # 입력 CSV 파일명과 출력 CSV 파일명
# input_file = 'C:\\Users\\hsung\\OneDrive\\바탕 화면\\팀플 데이터\\전월세\\6years_data_pos.csv'
# output_file = 'output.csv'

# # 입력 파일 열기
# with open(input_file, encoding='utf-8') as file:
#     reader = csv.reader(file)
#     rows = list(reader)

# # 출력 파일 열기
# with open(output_file, 'w', newline='') as file:
#     writer = csv.writer(file)

#     # 주소를 하나씩 처리하고 경도와 위도를 구하여 출력 파일에 저장
#     for row in rows:
#         address = row[0]  # 주소가 있는 열의 인덱스를 설정하세요.
#         coordinates = get_coordinates(address)
#         if coordinates:
#             row.extend(coordinates)
#         writer.writerow(row)

# print("처리 완료.")
