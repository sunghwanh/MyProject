import os
import datetime


lasttime = os.path.getmtime('C:\HarryPotter\Project_TEST\Crawling.py') # 경로 지정
useFormatTime = datetime.datetime.fromtimestamp(lasttime)
print(useFormatTime) #2023-05-23 22:59:07.204537