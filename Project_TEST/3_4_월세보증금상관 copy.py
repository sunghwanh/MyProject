import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np 

plt.rc('font', family='malgun gothic')

path = "C:\\Users\\hsung\\OneDrive\\바탕 화면\\팀플 데이터\\전월세\\6years_data.csv"
data = pd.read_csv(path, encoding='utf-8', index_col = 0)


전월세구분 = list(set(data['전월세구분']))
건물용도 = list(set(data['건물용도']))
tot_data = {}
for 전월세 in 전월세구분:
    tot_data[전월세] ={}
    for 용도 in 건물용도:
        tot_data[전월세][용도] = data
        tot_data[전월세][용도] = tot_data[전월세][용도][tot_data[전월세][용도]['전월세구분'] == 전월세]
        tot_data[전월세][용도] = tot_data[전월세][용도][tot_data[전월세][용도]['건물용도'] == 용도]
        
        if tot_data[전월세][용도]['전월세구분'].iloc[1] == "전세":
            tot_data[전월세][용도] = tot_data[전월세][용도][tot_data[전월세][용도]["보증금(만원)"] > 500]
            
            x = tot_data[전월세][용도]["임대면적"]
            y = tot_data[전월세][용도]["보증금(만원)"]
            # print(y.describe().loc[['max']])
            print("전세 보증금: {}임대면적에 따른{} 관련 상관관계".format(전월세,용도),np.corrcoef(x,y)[0,1].round(3))
        else:
            tot_data[전월세][용도] = tot_data[전월세][용도][tot_data[전월세][용도]["임대료(만원)"] > 0]
            tot_data[전월세][용도] = tot_data[전월세][용도][tot_data[전월세][용도]["임대료(만원)"] < 2000]
            x = tot_data[전월세][용도]["임대면적"]
            y = tot_data[전월세][용도]["보증금(만원)"]
            # print(y.describe().loc[['max']])
            print("월세 보증금: {}임대면적에 따른{} 관련 상관관계".format(전월세,용도),np.corrcoef(x,y)[0,1].round(3))
            
            x = tot_data[전월세][용도]["임대면적"]
            y = tot_data[전월세][용도]["임대료(만원)"]
            # print(y.describe().loc[['max']])
            print("월세 임대료: {}임대면적에 따른{} 관련 상관관계".format(전월세,용도),np.corrcoef(x,y)[0,1].round(3))
                       
#보증금=====================================================================================
# 전세 보증금: 전세임대면적에 따른아파트 관련 상관관계 0.627
# 전세 보증금: 전세임대면적에 따른오피스텔 관련 상관관계 0.722
# 전세 보증금: 전세임대면적에 따른단독다가구 관련 상관관계 0.54
# 전세 보증금: 전세임대면적에 따른연립다세대 관련 상관관계 0.392

# 월세 보증금: 월세임대면적에 따른아파트 관련 상관관계 0.574
# 월세 임대료: 월세임대면적에 따른아파트 관련 상관관계 0.499

# 월세 보증금: 월세임대면적에 따른오피스텔 관련 상관관계 0.45 
# 월세 임대료: 월세임대면적에 따른오피스텔 관련 상관관계 0.473

# 월세 보증금: 월세임대면적에 따른단독다가구 관련 상관관계 0.347
# 월세 임대료: 월세임대면적에 따른단독다가구 관련 상관관계 0.292

# 월세 보증금: 월세임대면적에 따른연립다세대 관련 상관관계 0.338
# 월세 임대료: 월세임대면적에 따른연립다세대 관련 상관관계 0.267