import requests
from bs4 import BeautifulSoup
import json
import pandas as pd 

def get_sido_info():
    down_url = 'https://address.dawul.co.kr/'
    r = requests.get(down_url,data={"sameAddressGroup":"false"},headers={
        "Accept-Encoding": "gzip",
        "Host": "address.dawul.co.kr",
        "Referer": "https://address.dawul.co.kr/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    })
    r.encoding = "utf-8-sig"
    soup = BeautifulSoup(r.Preview)
    print(soup)



print(get_sido_info())
