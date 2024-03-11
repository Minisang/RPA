import pandas as pd
air = pd.read_csv('ch3-1.csv')
print(air, end="\n\n")

#결측치 확인하기1
air.info()
#결측치 확인하기2
print(air.isnull().sum(), end="\n\n")
#결측치 제거(axis=0 : 행 제거, axis=1: 열 제거)
air_d = air.dropna(axis=0)
print(air_d, end="\n\n")

air_d2 = air.dropna(axis=1)
print(air_d2, end="\n\n")
#결측치 0 대체
air_m1 = air.fillna(0)
print(air_m1, end="\n\n")

print(air.mean(), end="\n\n")
air_m2 = air.fillna(air.mean())
print(air_m2, end="\n\n")