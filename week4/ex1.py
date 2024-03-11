import pandas as pd
data = {'이름': ['Kim','Park','Lee','Ho'],
        '국어' : [90,58,88,100],
        '영어' : [100,60,80,70],
        '수학' : [55,65,76,88]}
df1 = pd.DataFrame(data)
print(df1,end="\n\n")
df1 = pd.DataFrame(data,index=[1,2,3,4])
print(df1,end="\n\n")
print(df1['이름'])
df1.loc[df1['이름'] == 'Ho','수학'] = 90
print(df1)
df1.loc[5] = ['Oh',100,70,80]
print(df1)
df1 = df1.drop([3], axis=0)
print(df1)