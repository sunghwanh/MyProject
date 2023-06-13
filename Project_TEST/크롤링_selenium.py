import requests
import json
import pandas as pd 
import time 
from user_agent import generate_user_agent, generate_navigator

down_url = 'https://m.land.naver.com/map/getRegionList?cortarNo=1100000000&mycortarNo=1100000000'
r = requests.get(down_url,data={"sameAddressGroup":"false"},headers={
    "Accept-Encoding": "gzip",
    "Host": "new.land.naver.com",
    "Referer": "https://m.land.naver.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
})

r.encoding = "utf-8-sig"
con_info=json.loads(r.text) 
# print(con_info)   # {'CortarNo': '1168000000', 'CortarNm': '강남구', 'MapXCrdn': '127.047313', 'MapYCrdn': '37.517408', 'CortarType': 'dvsn'}
con_info=con_info['result']['list']
# 경도s=con_info[0]['MapXCrdn']
# 위도s=con_info[0]['MapYCrdn']
CortarNm = []
MapXCrdn = []
MapYCrdn = []
CortarNo = []
for datas in con_info:
    CortarNm.append(datas["CortarNm"])
    MapXCrdn.append(datas["MapXCrdn"])
    MapYCrdn.append(datas["MapYCrdn"])
    CortarNo.append(datas["CortarNo"])
# print(CortarNm) #지역명
# print(MapXCrdn) #경도
# print(MapYCrdn) #위도
# print(CortarNo) #지역코드
gu_data = pd.DataFrame((CortarNm,MapXCrdn,MapYCrdn,CortarNo)).transpose()
gu_data.columns = '지역구','경도','위도','지역코드'
print(gu_data)
# print(gu_data.shape)
#=======================================================지역별 코드 

#=========================================================매물 개수 카운트
# coun_main_url = "https://m.land.naver.com/cluster/clusterList?view=atcl&"
# count_hap = 0
# for gu_name, gu_lon, gu_lat, gu_num in gu_data.values: 
#     # print(gu_name)
#     btm = str(float(gu_lat) - 0.0938547)
#     left = str(float(gu_lon) - 0.1148415)
#     top = str(float(gu_lat) +  0.0937368)
#     right = str(float(gu_lon) + 0.1148415)
#     count_url = f"{coun_main_url}cortarNo={gu_num}&rletTpCd=OPST%3AVL%3AJWJT%3ADDDGG&tradTpCd=B1%3AB2&z=12&lat={gu_lat}&lon={gu_lon}&btm={btm}&lft={left}&top={top}&rgt={right}&pCortarNo=12_{gu_num}"
#     print(count_url)
#     r2 = requests.get(coun_main_url,data={"sameAddressGroup":"false"},headers={
#         "Accept-Encoding": "gzip",
#         "Host": "m.land.naver.com",
#         "Referer": "https://m.land.naver.com/",
#         "Sec-Fetch-Dest": "empty",
#         "Sec-Fetch-Mode": "cors",
#         "Sec-Fetch-Site": "same-origin",
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
#     })

#     r2.encoding = "utf-8-sig"
#     count_info=json.loads(r2.text)
#     count_data = count_info["data"]["ARTICLE"]
#     print(gu_name)
#     print(count_info)
    # for count in count_info:
    #     count_hap += count["count"]
    # print(count_hap)
        
# 매물 수집==============================================================
mainurl = 'https://m.land.naver.com/cluster/ajax/articleList?itemId=&mapKey=&lgeo=&showR0=&rletTpCd=OPST%3AVL%3AJWJT%3ADDDGG&tradTpCd=B1%3AB2&z=12&'
url_datas = []
gu_datas = []

for gu_name, gu_lon, gu_lat, gu_num in gu_data.values: 
    # print(gu_name)
    btm = str(float(gu_lat) - 0.1038547)
    left = str(float(gu_lon) - 0.1148415)
    top = str(float(gu_lat) +  0.1037368)
    right = str(float(gu_lon) + 0.1148415)
    urlp = f'{mainurl}lat={gu_lat}&lon={gu_lon}&btm={btm}&lft={left}&top={top}&rgt={right}&cortarNo={gu_num}&sort=rank&page='
    url_datas.append(urlp)
    gu_datas.append(gu_name)

url_df = pd.DataFrame((gu_datas,url_datas)).transpose()
url_df.columns=["지역구","url_data"]
print(url_df)

url_data = url_df["url_data"]
print(url_data)

# {'atclNo': '2324460320', 'cortarNo': '1168010800', 'atclNm': '빌라', 'atclStatCd': 'R0', 'rletTpCd': 'C02', 'uprRletTpCd': 'C03', 'rletTpNm': '빌라', 
# 'tradTpCd': 'B1', 'tradTpNm': '전세', 'vrfcTpCd': 'SITE', 'flrInfo': '2/5', 'prc': 30000, 'rentPrc': 0, 'hanPrc': '3억', 'spc1': '31', 'spc2': '23.48', 'direction': '서향', 
# 'atclCfmYmd': '23.06.09.', 'repImgUrl': '/20230609_75/land_naver_16862985179174txDS_JPEG/cd4987afbc90c3fe1d0787b7adb48638.JPG', 'repImgTpCd': 'SITE', 
# 'repImgThumb': 'f130_98', 'lat': 37.509299, 'lng': 127.030823, 'tagList': ['4년이내', '융자금없는', '역세권'], 'bildNm': '', 'minute': 0, 'sameAddrCnt': 1, 'sameAddrDirectCnt': 0, 'cpid': 'SERVE', 'cpNm': '부동산써브', 
# 'cpCnt': 1, 'rltrNm': '주식회사큐앤에이부동산중개', 'directTradYn': 'N', 'minMviFee': 0, 'maxMviFee': 0, 'etRoomCnt': 0, 'tradePriceHan': '', 'tradeRentPrice': 0, 'tradeCheckedByOwner': False, 
# 'cpLinkVO': {'cpId': 'SERVE', 'mobileArticleUrl': 'http://m.serve.co.kr/naver/rd.asp?UID=', 'mobileArticleLinkTypeCode': 'CPNAMEONLY', 'mobileBmsInspectPassYn': 'Y', 'pcArticleLinkUseAtArticleTitle': False, 
# 'pcArticleLinkUseAtCpName': False, 'mobileArticleLinkUseAtArticleTitle': False, 'mobileArticleLinkUseAtCpName': True}, 'dtlAddrYn': 'N', 'dtlAddr': ''},
page = 187
atclNm = []
tradTpNm = []
flrInfo = []
prc = []
hanPrc = []
spc1 = []
spc2 = []
lat = []
lng = []
tagList = []
try:
    while True:
        time.sleep(3)
        # navigator = generate_navigator()
        # new_user_agent = generate_user_agent()
        # print(new_user_agent)
        get_url = url_data + str(page)
        # print(get_url)
        r2 = requests.get(get_url,data={"sameAddressGroup":"false"},headers={
            "Accept-Encoding": "gzip",
            "Host": "new.land.naver.com",
            "Referer": "https://m.land.naver.com/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
        })

        r.encoding = "utf-8-sig"
        bui_info=json.loads(r2.text) 
        bui_info=bui_info['body']
        
        for datas in bui_info:
            atclNm.append(datas["atclNm"])
            tradTpNm.append(datas["tradTpNm"])
            flrInfo.append(datas["flrInfo"])
            prc.append(datas["prc"])
            hanPrc.append(datas["hanPrc"])
            spc1.append(datas["spc1"])
            spc2.append(datas["spc2"])
            lat.append(datas["lat"])
            lng.append(datas["lng"])
            tagList.append(datas["tagList"])
            
        total_data = pd.DataFrame((atclNm,tradTpNm,flrInfo,prc,hanPrc,spc1,spc2,lat,lng,tagList)).transpose()
        total_data.columns = ['atclNm','tradTpNm','flrInfo','prc','hanPrc','spc1','spc2','lat','lng','tagList']
        total_data.index =["강남구"] * total_data.shape[0]
        
        # print(total_data)
        print(page)
        page = page+1
        if len(bui_info) == 0:
            
            save_path = "C:\\Users\\hsung\\OneDrive\\바탕 화면\\팀플 데이터\\전월세\\실시간매물.csv"
            total_data.to_csv(save_path, encoding="utf-8-sig")
            break
        
except:
    print('종료')
    
    save_path = "C:\\Users\\hsung\\OneDrive\\바탕 화면\\팀플 데이터\\전월세\\실시간매물.csv"
    total_data.to_csv(save_path, encoding="utf-8-sig")