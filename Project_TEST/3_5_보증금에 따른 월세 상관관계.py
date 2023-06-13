import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np 

plt.rc('font', family='malgun gothic')

path = "C:\\Users\\hsung\\OneDrive\\바탕 화면\\팀플 데이터\\전월세\\6years_data.csv"
data = pd.read_csv(path, encoding='utf-8', index_col = 0)


data = data[data['전월세구분'] == '월세']
data = data[data['보증금(만원)'] > 0]
# data = data[data['건물용도'] == '단독다가구']

# x_data = data['보증금(만원)']
# y_data = data['임대료(만원)']
# print(np.corrcoef(x_data,y_data)[0,1])
# print(x_data.describe())
# print(y_data.describe())

자치구명 = list(set(data['자치구명']))
건물용도 = list(set(data['건물용도']))

tot_data = {}
corr_list = []
for 구명 in 자치구명:
    tot_data[구명] ={}
    for 용도 in 건물용도:
        tot_data[구명][용도] = data
        tot_data[구명][용도] = tot_data[구명][용도][tot_data[구명][용도]['자치구명'] == 구명]
        tot_data[구명][용도] = tot_data[구명][용도][tot_data[구명][용도]['건물용도'] == 용도]
        x = tot_data[구명][용도]['보증금(만원)']
        y = tot_data[구명][용도]['임대료(만원)']
        print(x.shape)
        print(y.shape)
        print("{} 위치의 {} 상관관계".format(구명,용도),np.corrcoef(x,y)[0,1])
        corr_list.append(np.corrcoef(x,y)[0,1])



corr_list = abs(np.array(corr_list)) 
print(np.count_nonzero(corr_list > 0.5)) #3
print(np.count_nonzero((corr_list <= 0.5) & (corr_list >= 0.3))) #28
print(np.count_nonzero(corr_list < 0.3)) #69