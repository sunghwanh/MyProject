import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('http://www.bizhankook.com/bk/article/25680', headers=headers)
data.encoding = 'utf-8'
soup = BeautifulSoup(data.text, 'html.parser')

# br 및 p 태그의 내용만 저장
texts = []

for p in soup.find_all('p'):
    texts.append(p.text)
    
for br in soup.find_all('br'):
    if br.next_sibling: #형제태그 참조
        texts.append(str(br.next_sibling).strip())

# 필요없는 문자 제거
del_text = []
for text in texts:
    text = text.replace("\n", "").replace("\r", "").replace(",", "").replace("\"", "").strip()
    text = text.replace("\t", "").replace("\xa0", "").strip()
    if len(text) > 0:
        del_text.append(text)

print(del_text)
