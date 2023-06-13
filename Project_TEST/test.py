import pandas as pd

# 데이터 로드
path = "C:\\Users\\hsung\\OneDrive\\바탕 화면\\temp.csv"
data = pd.read_csv(path, encoding='utf-8',index_col=0)
#,'공원개수','1역세권','2역세권'

print(data['대형점포개수'])
data = data.iloc[:,1:]
data['대형점포개수'] = data['대형점포개수'].apply(lambda x : 1 if x > 1 else x)
data['공원개수'] = data['공원개수'].apply(lambda x : 1 if x > 1 else x)
data['1역세권'] = data['1역세권'].apply(lambda x : 1 if x > 1 else x)
data['2역세권'] = data['2역세권'].apply(lambda x : 1 if x > 1 else x)

print(data[data['대형점포개수'] > 1])
print(data[data['공원개수'] > 1])
print(data[data['1역세권'] > 1])
print(data[data['2역세권'] > 1])

save_path = "C:\\Users\\hsung\\OneDrive\\바탕 화면\\temp.csv"
data.to_csv(save_path, encoding="utf-8-sig")