import pandas as pd
data = {'이름' : ['유정','유나','민영','은지',],
        '나이' : [30,28,31,29],
        '생일' : ['1991.5.2','1993.4.6','1990.9.12','1992.7.19']}

df1 = pd.DataFrame(data)
print(df1, end="\n\n")

print(df1['이름'], end="\n\n")
print(df1.loc[2], end="\n\n")
print("민영의 나이 =", df1.loc[2]['나이'], end="\n\n")
print("===================\n\n")
print("민영 정보 \n", df1['이름']=='민영', end="\n\n")
print("민영 정보 \n", df1.loc[df1['이름']=='민영'], end="\n\n")
print("민영의 나이=", df1.loc[df1['이름']=='민영']['나이'].values[0], end="\n\n")

print("====================================\n\n")
print("행 1:3 \n", df1.loc[1:3], end="\n\n")
print("열 ['이름','나이'] \n", df1[['이름','나이']], end="\n\n")
print("조건1 \n", df1[df1['이름']=='은지'], end="\n\n")
print("조건2 \n", df1[df1['나이']>=30], end="\n\n")