import pandas as pd 
import pickle
import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic')

with open("총데이터.pkl", "rb") as file:
    총데이터 = pickle.load(file)  
구인풋 = "강남구"
전월인풋 = "월세"
용도인풋 = "아파트"
년도인풋 = 2020

data = pd.DataFrame(총데이터["{}".format(구인풋)]["{}".format(전월인풋)]["{}".format(용도인풋)])
data['연도'] = data['계약일'].apply(lambda x: int(str(x)[:4]))
data = data[data['연도'] == 년도인풋]

if data['전월세구분'].iloc[1] == "전세":
    mean_by_rent = data.groupby('계약일').mean('보증금(만원)')
    mean_by_rent['계약월'] = mean_by_rent.index

    plt.figure()
    #전세 전체금액===================================================================
    #===============================================================================
    plt.subplot(2, 1, 1)
    plt.plot(mean_by_rent["계약월"], mean_by_rent["보증금(만원)"])
    plt.xticks(mean_by_rent["계약월"])
    plt.ylim(mean_by_rent["보증금(만원)"].min() - 1000, mean_by_rent["보증금(만원)"].max() + 1000)
    plt.xlabel("계약월")
    plt.ylabel("월별 평균 전세(만원)")
    plt.title("{} {}년 보증금(만원) 평균".format(구인풋,년도인풋))
    plt.tight_layout()
    
    #전세 평당금액===================================================================
    #===============================================================================   
    plt.subplot(2, 1, 2)
    plt.plot(mean_by_rent["계약월"], mean_by_rent["평당보증금(만원)"])
    plt.xticks(mean_by_rent["계약월"])
    plt.xlabel("계약월")
    plt.ylabel("월별 평당금액(만원)")
    plt.title("{} {}년 평당금액(만원) 평균".format(구인풋,년도인풋))
    plt.tight_layout()    
    plt.show()
    
else:
    #월세===========================================================================
    mean_by_rent = data.groupby('계약일').mean('임대료(만원)')
    mean_by_rent['계약월'] = mean_by_rent.index
    plt.figure()
    
    #월세 전체금액===================================================================
    #===============================================================================
    plt.subplot(3, 1, 1)
    plt.plot(mean_by_rent["계약월"], mean_by_rent["임대료(만원)"])
    plt.xticks(mean_by_rent["계약월"])
    plt.ylim(mean_by_rent["임대료(만원)"].min() - 10, mean_by_rent["임대료(만원)"].max() + 10)
    plt.xlabel("계약월")
    plt.ylabel("월별 평균 월세(만원)")
    plt.title("{} {}년 월별 임대료(만원) 평균".format(구인풋,년도인풋))
    plt.tight_layout()
    #월세 평당금액===================================================================
    #===============================================================================
    plt.subplot(3, 1, 2)
    plt.plot(mean_by_rent["계약월"], mean_by_rent["평당임대료(만원)"])
    plt.xticks(mean_by_rent["계약월"])
    plt.xlabel("계약월")
    plt.ylabel("월별 평균 월세(만원)")
    plt.title("{} {}년 월별 평당임대료(만원) 평균".format(구인풋,년도인풋))
    plt.tight_layout()  
    
    #월세 보증금금액===================================================================
    #===============================================================================
    plt.subplot(3, 1, 3)
    plt.plot(mean_by_rent["계약월"], mean_by_rent["평당보증금(만원)"])
    plt.xticks(mean_by_rent["계약월"])
    plt.xlabel("계약월")
    plt.ylabel("월별 평균 보증금(만원)")
    plt.title("{} {}년 월별 평당보증금(만원) 평균".format(구인풋,년도인풋))
    plt.tight_layout()  
    plt.show()