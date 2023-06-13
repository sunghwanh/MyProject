import requests
from bs4 import BeautifulSoup
import csv

try:
    keyword = input("키워드를 입력 하세요")
    page = 1 #시작 페이지 초기화
    date1 = '2023.05.20'
    date2 = '2023.05.28'
    date3 = date1.replace('.', '') + 'to' + date2.replace('.', '')

    #csv 파일 저장
    filename = "C:\HarryPotter\Project_TEST\data_imf.csv"
    with open(filename, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["링크", '제목']) #컬럼명 지정

        previous_links = set() #이전 페이지 체크
        visited_links = set() #방문 페이지 체크

        while True:
            headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
            data = requests.get('https://search.naver.com/search.naver?where=news&query=%s&sm=tab_opt&sort=0&photo=0&field=0&pd=3&ds=%s&de=%s&docid=&related=0&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so%%3Ar%%2Cp%%3Afrom%s&is_sug_officeid=0&start=%s'%(keyword, date1, date2, date3, page), headers=headers)
            soup = BeautifulSoup(data.text, 'html.parser')
            stocks = soup.select('a.news_tit')
            
            #현재 페이지의 모든 뉴스 기사 링크를 저장하는 집합을 생성
            current_links = set(stock.attrs['href'] for stock in stocks)

            if previous_links == current_links:  # 현재 페이지와 이전 페이지가 같으면 종료
                print('조기종료 되었습니다.')
                break

            for stock in stocks:
                url = stock.attrs['href']
                title = stock.text

                # 이미 방문한 링크인지 확인
                if url not in visited_links:
                    row = {
                        'title': title,
                        'url': url
                    }
                    print(title, url)
                    writer.writerow([url, title])
                    visited_links.add(url)  # 방문한 링크에 추가

            page = page+10
            previous_links = current_links

except Exception as e:
    print(e)
