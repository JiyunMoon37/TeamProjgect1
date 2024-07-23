#rerminal에 쳐주고 시작하기 -> pip install pandas, pip install openpyxl 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. 2022년 데이터 불러오기

# 원본 데이터(excel)상, 1행과 2행 일부가 병합되어 있음. 
# 원본 데이터의 2행부터 불러오고자 header = 1로 설정하였음. 
df_22 = pd.read_excel('data/domestic_2022.xlsx', header = 1)
df_22.head()


# 2. 변수 이름 바꿔보기
# 데이터 변수 확인
df_22.columns

df_22 = df_22.rename(columns = {'통계분류(1)' : 'class1',
                                '통계분류(2)' : 'class2',
                                '국내전체'    : 'dm_total',
                                '국내숙박'    : 'dm_stay',
                                '국내당일'    : 'dm_1day',
                                '관광전체'    : 'tr_total',
                                '관광숙박'    : 'tr_stay',
                                '관광당일'    : 'tr_1day',
                                '기타전체'    : 'ot_total',
                                '기타숙박'    : 'ot_stay',
                                '기타당일'    : 'ot_1day'
                          })

# 3. 'class1'의 Nan 값에 class에 맞는 값 부여 & 영문명으로 변경
df_22.loc[0, ['class1']] = "category-sum"
df_22.loc[1:2, ['class1']] = "sex"
df_22.loc[3:9, ['class1']] = "age"
df_22.loc[10:16, ['class1']] = "job"
df_22.loc[17:20, ['class1']] = "edu"
df_22.loc[21:23, ['class1']] = "fam"
df_22.loc[24:30, ['class1']] = "income"


# 4. 'class2'도 영문으로 변경
df_22.loc[0, ["class2"]] = "sum_22"

#sex
df_22.loc[df_22["class2"] == "남자", "class2"] = "M"
df_22.loc[df_22["class2"] == "여자", "class2"] = "F"

#age
df_22.loc[df_22["class2"] == "15~19세"  , "class2"] = "10s"
df_22.loc[df_22["class2"] == "20대"     , "class2"] = "20s"
df_22.loc[df_22["class2"] == "30대"     , "class2"] = "30s"
df_22.loc[df_22["class2"] == "40대"     , "class2"] = "40s"
df_22.loc[df_22["class2"] == "50대"     , "class2"] = "50s"
df_22.loc[df_22["class2"] == "60대"     , "class2"] = "60s"
df_22.loc[df_22["class2"] == "70세 이상", "class2"] = "70s~"

#job
df_22.loc[df_22["class2"] == "임금봉급근로자"    , "class2"] = "work"
df_22.loc[df_22["class2"] == "고용원있는사업주"  , "class2"] = "co_ceo"
df_22.loc[df_22["class2"] == "고용원없는자영업자", "class2"] = "self-ceo"
df_22.loc[df_22["class2"] == "무급가족 종사자"   , "class2"] = "fam_work"
df_22.loc[df_22["class2"] == "전업주부"          , "class2"] = "house_work"
df_22.loc[df_22["class2"] == "학생"              , "class2"] = "stu"
df_22.loc[df_22["class2"] == "기타"              , "class2"] = "etc"

#edu
df_22.loc[df_22["class2"] == "초졸 이하" , "class2"] = "~prime_edu"
df_22.loc[df_22["class2"] == "중학교"    , "class2"] = "middle_edu"
df_22.loc[df_22["class2"] == "고등학교"  , "class2"] = "high_edu"
df_22.loc[df_22["class2"] == "대학교이상", "class2"] = "univ_edu~"

#fam
df_22.loc[df_22["class2"] == "1인"    , "class2"] = "1p"
df_22.loc[df_22["class2"] == "2인"    , "class2"] = "2p"
df_22.loc[df_22["class2"] == "3인이상", "class2"] = "3p~"

#income
df_22.loc[df_22["class2"] == "100만원 미만"    , "class2"] = "~100"
df_22.loc[df_22["class2"] == "100~200만원 미만", "class2"] = "100~200"
df_22.loc[df_22["class2"] == "200~300만원 미만", "class2"] = "200~300"
df_22.loc[df_22["class2"] == "300~400만원 미만", "class2"] = "300~400"
df_22.loc[df_22["class2"] == "400~500만원 미만", "class2"] = "400~500"
df_22.loc[df_22["class2"] == "500~600만원 미만", "class2"] = "500~600"
df_22.loc[df_22["class2"] == "600만원 이상"    , "class2"] = "600~"


# class1과 class2를 index로 설정
df_22 = df_22.set_index(['class1', 'class2'])

# 5. 분석에 필요한 부분만 추출
# dm_total, tr_total, ot_total만 추출
df_22_sum = df_22.loc["category-sum", ["dm_total", "tr_total", "ot_total"]]
df_22_sum

-----------------------------------------------------------------
# 2018~2021 데이터도 이렇게 작업 진행
-----------------------------------------------------------------
# 2018년
df_18 = pd.read_excel('data/domestic_2018.xlsx', header = 1)
df_18 = df_18.rename(columns = {'통계분류(1)' : 'class1',
                                '통계분류(2)' : 'class2',
                                '국내전체'    : 'dm_total',
                                '국내숙박'    : 'dm_stay',
                                '국내당일'    : 'dm_1day',
                                '관광전체'    : 'tr_total',
                                '관광숙박'    : 'tr_stay',
                                '관광당일'    : 'tr_1day',
                                '기타전체'    : 'ot_total',
                                '기타숙박'    : 'ot_stay',
                                '기타당일'    : 'ot_1day'
                          })

df_18.loc[0, ['class1']] = "category-sum"
df_18.loc[1:2, ['class1']] = "sex"
df_18.loc[3:9, ['class1']] = "age"
df_18.loc[10:16, ['class1']] = "job"
df_18.loc[17:20, ['class1']] = "edu"
df_18.loc[21:23, ['class1']] = "fam"
df_18.loc[24:30, ['class1']] = "income"

df_18.loc[0, ["class2"]] = "sum_18"
df_18.loc[df_18["class2"] == "남자", "class2"] = "M"
df_18.loc[df_18["class2"] == "여자", "class2"] = "F"
df_18.loc[df_18["class2"] == "15~19세"  , "class2"] = "10s"
df_18.loc[df_18["class2"] == "20대"     , "class2"] = "20s"
df_18.loc[df_18["class2"] == "30대"     , "class2"] = "30s"
df_18.loc[df_18["class2"] == "40대"     , "class2"] = "40s"
df_18.loc[df_18["class2"] == "50대"     , "class2"] = "50s"
df_18.loc[df_18["class2"] == "60대"     , "class2"] = "60s"
df_18.loc[df_18["class2"] == "70세 이상", "class2"] = "70s~"
df_18.loc[df_18["class2"] == "임금봉급근로자"    , "class2"] = "work"
df_18.loc[df_18["class2"] == "고용원있는사업주"  , "class2"] = "co_ceo"
df_18.loc[df_18["class2"] == "고용원없는자영업자", "class2"] = "self-ceo"
df_18.loc[df_18["class2"] == "무급가족 종사자"   , "class2"] = "fam_work"
df_18.loc[df_18["class2"] == "전업주부"          , "class2"] = "house_work"
df_18.loc[df_18["class2"] == "학생"              , "class2"] = "stu"
df_18.loc[df_18["class2"] == "기타"              , "class2"] = "etc"
df_18.loc[df_18["class2"] == "초졸 이하" , "class2"] = "~prime_edu"
df_18.loc[df_18["class2"] == "중학교"    , "class2"] = "middle_edu"
df_18.loc[df_18["class2"] == "고등학교"  , "class2"] = "high_edu"
df_18.loc[df_18["class2"] == "대학교이상", "class2"] = "univ_edu~"
df_18.loc[df_18["class2"] == "1인"    , "class2"] = "1p"
df_18.loc[df_18["class2"] == "2인"    , "class2"] = "2p"
df_18.loc[df_18["class2"] == "3인이상", "class2"] = "3p~"
df_18.loc[df_18["class2"] == "100만원 미만"    , "class2"] = "~100"
df_18.loc[df_18["class2"] == "100~200만원 미만", "class2"] = "100~200"
df_18.loc[df_18["class2"] == "200~300만원 미만", "class2"] = "200~300"
df_18.loc[df_18["class2"] == "300~400만원 미만", "class2"] = "300~400"
df_18.loc[df_18["class2"] == "400~500만원 미만", "class2"] = "400~500"
df_18.loc[df_18["class2"] == "500~600만원 미만", "class2"] = "500~600"
df_18.loc[df_18["class2"] == "600만원 이상"    , "class2"] = "600~"

# class1과 class2를 index로 설정
df_18 = df_18.set_index(['class1', 'class2'])

# dm_total, tr_total, ot_total만 추출
df_18_sum = df_18.loc["category-sum", ["dm_total", "tr_total", "ot_total"]]
df_18_sum
-----------------------------------------------------------------
# 2019년
df_19 = pd.read_excel('data/domestic_2019.xlsx', header = 1)
df_19 = df_19.rename(columns = {'통계분류(1)' : 'class1',
                                '통계분류(2)' : 'class2',
                                '국내전체'    : 'dm_total',
                                '국내숙박'    : 'dm_stay',
                                '국내당일'    : 'dm_1day',
                                '관광전체'    : 'tr_total',
                                '관광숙박'    : 'tr_stay',
                                '관광당일'    : 'tr_1day',
                                '기타전체'    : 'ot_total',
                                '기타숙박'    : 'ot_stay',
                                '기타당일'    : 'ot_1day'
                          })

df_19.loc[0,     ['class1']] = "category-sum"
df_19.loc[1:2,   ['class1']] = "sex"
df_19.loc[3:9,   ['class1']] = "age"
df_19.loc[10:16, ['class1']] = "job"
df_19.loc[17:20, ['class1']] = "edu"
df_19.loc[21:23, ['class1']] = "fam"
df_19.loc[24:30, ['class1']] = "income"

df_19.loc[0, ["class2"]] = "sum_19"
df_19.loc[df_19["class2"] == "남자", "class2"] = "M"
df_19.loc[df_19["class2"] == "여자", "class2"] = "F"
df_19.loc[df_19["class2"] == "15~19세"  , "class2"] = "10s"
df_19.loc[df_19["class2"] == "20대"     , "class2"] = "20s"
df_19.loc[df_19["class2"] == "30대"     , "class2"] = "30s"
df_19.loc[df_19["class2"] == "40대"     , "class2"] = "40s"
df_19.loc[df_19["class2"] == "50대"     , "class2"] = "50s"
df_19.loc[df_19["class2"] == "60대"     , "class2"] = "60s"
df_19.loc[df_19["class2"] == "70세 이상", "class2"] = "70s~"
df_19.loc[df_19["class2"] == "임금봉급근로자"    , "class2"] = "work"
df_19.loc[df_19["class2"] == "고용원있는사업주"  , "class2"] = "co_ceo"
df_19.loc[df_19["class2"] == "고용원없는자영업자", "class2"] = "self-ceo"
df_19.loc[df_19["class2"] == "무급가족 종사자"   , "class2"] = "fam_work"
df_19.loc[df_19["class2"] == "전업주부"          , "class2"] = "house_work"
df_19.loc[df_19["class2"] == "학생"              , "class2"] = "stu"
df_19.loc[df_19["class2"] == "기타"              , "class2"] = "etc"
df_19.loc[df_19["class2"] == "초졸 이하" , "class2"] = "~prime_edu"
df_19.loc[df_19["class2"] == "중학교"    , "class2"] = "middle_edu"
df_19.loc[df_19["class2"] == "고등학교"  , "class2"] = "high_edu"
df_19.loc[df_19["class2"] == "대학교이상", "class2"] = "univ_edu~"
df_19.loc[df_19["class2"] == "1인"    , "class2"] = "1p"
df_19.loc[df_19["class2"] == "2인"    , "class2"] = "2p"
df_19.loc[df_19["class2"] == "3인이상", "class2"] = "3p~"
df_19.loc[df_19["class2"] == "100만원 미만"    , "class2"] = "~100"
df_19.loc[df_19["class2"] == "100~200만원 미만", "class2"] = "100~200"
df_19.loc[df_19["class2"] == "200~300만원 미만", "class2"] = "200~300"
df_19.loc[df_19["class2"] == "300~400만원 미만", "class2"] = "300~400"
df_19.loc[df_19["class2"] == "400~500만원 미만", "class2"] = "400~500"
df_19.loc[df_19["class2"] == "500~600만원 미만", "class2"] = "500~600"
df_19.loc[df_19["class2"] == "600만원 이상"    , "class2"] = "600~"

# class1과 class2를 index로 설정
df_19 = df_19.set_index(['class1', 'class2'])

# dm_total, tr_total, ot_total만 추출
df_19_sum = df_19.loc["category-sum", ["dm_total", "tr_total", "ot_total"]]
df_19_sum

df_18_sum
df_19_sum

-----여기부터----

#2018 
people_2018 = 48000

#2018_1인 평균 지출액_관광 
avg_spend_tr2018 = (df_18_sum.loc['sum_18', 'dm_total'] * 1000000000) / people_2018

#loc는 행과 열을 선택하는 함수, loc["행 이름", "열 이름"]
print(f"{avg_spend_tr2018: .0f}원") 
#여기서 .0f는 출력 형식을 의미, 소수점 이하 0의 자리까지 출력하고 반올림한다는 의미이다. 

#2018_1인 평균 지출액_기타 
avg_spend_ot2018 = (df_18_sum.loc['sum_18', 'ot_total'] * 1000000000) / people_2018
print(f"{avg_spend_ot2018: .0f}원") 

#2019
people_2019 = 50400

#2019_1인 평균 지출액_관광 
avg_spend_tr2019 = (df_19_sum.loc['sum_19', 'dm_total'] * 1000000000) / people_2019

#loc는 행과 열을 선택하는 함수, loc["행 이름", "열 이름"]
print(f"{avg_spend_tr2019: .0f}원") 

#2019_1인 평균 지출액_기타 
avg_spend_ot2019 = (df_19_sum.loc['sum_19', 'ot_total'] * 1000000000) / people_2019
print(f"{avg_spend_ot2019: .0f}원") 

#분석 기간별로 데이터 그룹화
#before covid
bf_covid = pd.concat([df_18_sum, df_19_sum])
bf_covid





