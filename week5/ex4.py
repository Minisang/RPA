import pandas as pd

data = {'열1':[1,2,2,3,4],
        '열2':['A','B','B','C',"D"],
        '열3':[-10,20,30,40,150],
        '열4':['X','Y','X','Z','Z']}

df = pd.DataFrame(data)
print(df.describe(), end="\n\n")

print("평균 : ")
print(df['열3'].mean(), end="\n\n")

print("중앙값 : ")
print(df['열3'].median(), end="\n\n")

print("최소값 : ")
print(df['열3'].min(), end="\n\n")

print("최대값 : ")
print(df['열3'].max(), end="\n\n")


print("평균 : ")
print(df['열3'].mean(), end="\n\n")

print("사분위수 : ")
print(df['열3'].quantile([0.25,0.5,0.75]), end="\n\n")


print("분산 : ")
print(df['열3'].var(), end="\n\n")

print("표준편차 : ")
print(df['열3'].std(), end="\n\n")