import requests
from bs4 import BeautifulSoup
import csv

try:
    #csv 파일 저장
    # filename = "C:\HarryPotter\Project_TEST\data_imf.csv"
    # with open(filename, 'w', encoding='utf-8-sig', newline='') as f:
    #     writer = csv.writer(f)
    #     writer.writerow(["링크", '제목']) #컬럼명 지정

    # while True:
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get('https://address.dawul.co.kr/', headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    print(soup)
    stocks = soup.select('#insert_data_5')
    print(stocks)
   
except Exception as e:
    print(e)
