import xml.etree.ElementTree as ET
import urllib.request as req
import pandas as pd
#http://openapi.seoul.go.kr:8088/705868526e68737531313176414c7542/xml/tbLnOpendataRentV/1/10/

pd.options.display.max_columns = 100

apikey = '705868526e68737531313176414c7542'
startnum = 1
endnum = 10
url = f'http://openapi.seoul.go.kr:8088/{apikey}/xml/tbLnOpendataRentV/{startnum}/{endnum}/'

response = req.urlopen(url)
xml_str = response.read().decode('utf-8')
root = ET.fromstring(xml_str)

rows = []
for row in root.iter('row'):
    row_dict = {}
    for child in row:
        row_dict[child.tag] = child.text
    rows.append(row_dict)

df = pd.DataFrame(rows)
print(df.head())