from konlpy.tag import Okt
import requests
from bs4 import BeautifulSoup
from collections import Counter #단어 수 count
#http://mbn.mk.co.kr/pages/news/newsView.php?category=mbn00003&news_seq_no=4932950

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('http://mbn.mk.co.kr/pages/news/newsView.php?category=mbn00003&news_seq_no=4932950', headers=headers)
data.encoding = 'utf-8' 
soup = BeautifulSoup(data.text, 'html.parser')
stocks = soup.select('div.detail')            

# print(stocks)
for stock in stocks:
    
    content = stock.text
    # print(content)

voc = content
okt_pos = Okt().pos(voc, norm=True, stem=True)   # 형태소 분석 ( norm : 정규화 )

okt_filtering = [x for x, y in okt_pos if y in ['Noun']]
# okt_filtering = [x for x, y in okt_pos if y in ['Noun', 'Adjective', 'Verb']]
# print(okt_filtering)              # 불용어 처리 - 명사, 형용사, 동사만 선별

count = Counter(okt_filtering)
print(count)