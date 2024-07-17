import pandas as pd 
import numpy as np

df = pd.read_excel('data/domestic_2022.xlsx', header = 1) #첫번째 행 빼고 불러올 수 있다. 
df2 = df.copy() #복사
df2.head()

#항목명 변경
df2 = df2.rename(columns = {"통계분류(1)" : "statis", "통계분류(2)" : "statis2", 
                    "국내전체" : "whole_domestic" , "국내숙박" : "domestic_stay", "국내당일" : "domestic_day", 
                    "관광전체" : "whole_tour", "관광숙박" : "tourist_stay", "관광당일" : "tourist_day",
                    "기타전체" : "whole_other", "기타숙박" : "other_stay", "기타당일" : "other_day"})
#결측치 채우기 
df2.loc[2, 'statis'] = '성별' #2행
df2.loc[3:9, 'statis'] = '연령' #4행~9행
df2.loc[10:16, 'statis'] = '직업' #10행~16행 
df2.loc[17:20, 'statis'] = '직업' #18행~20행
df2.loc[21:23, 'statis'] = '가구원수' #22행~23행
df2.loc[24:30, 'statis'] = '가구원수' #25행~30행
