import pandas as pd
data = {'이름' : ['유정','유나','민영','은지',],
        '나이' : [30,28,31,29],
        '생일' : ['1991.5.2','1993.4.6','1990.9.12','1992.7.19']}
df1 = pd.DataFrame(data)
print(df1,end="\n\n")
print(type(df1))
print("========================")
df2=pd.DataFrame(data,index=['하나','둘','셋','넷'])
print(df2)

print("==================")
sr_name = df2['이름']
print(sr_name,end="\n\n")
print(type(sr_name))
# 행 추출
sr_two = df2.loc['둘']
print(sr_two, end="\n\n")
print(type(sr_two))
# 셀 추출
print(df2.loc['넷']['이름'], end="\n\n")
print(df2.iloc[3][1], end="\n\n")

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
eunji_row = df2[df2['이름'] == '은지']
print(eunji_row)
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
eunji_birth = df2.loc[df2['이름']=='은지','생일']
print(eunji_birth)
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print('생일', eunji_birth.values[0])
print("================")

df2.loc['하나', '생일'] = '2000.03.03'
print(df2, end="\n\n")
df2.loc[df2['이름'] == '은지', '생일'] = '1990.01.01'
print("========================")
df2['키'] = [163, 165, 168, 166]
print(df2)
sr_vision = pd.Series([1.8,0.9,1.2], index = ['셋', '하나', '넷'])
print(df2, end="\n\n")
df2['시력'] = sr_vision

print(df2)
print("=========================")
df2.loc['다섯'] = ['재남', 33, '1988.8.8', 177, 1.1]
print(df2, end="\n\n")
new_data = {'이름' : ['리사'], '나이' : [23]}
new_df = pd.DataFrame(new_data, index=['블핑'])
df2=pd.concat([df2,new_df])
print(df2, end="\n\n")
print("=================")
#열 삭제
df2 = df2.drop(['키'], axis=1)
#행 삭제
print(df2, end="\n\n")
df2 = df2.drop(['셋'], axis=0)
print(df2)
print("====================")
