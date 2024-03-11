import pandas as pd

data = {'열1':[1,2,2,3,4],
        '열2':['A','B','B','C',"D"],
        '열3':[-10,20,30,40,150],
        '열4':['X','Y','X','Z','Z']}
df=pd.DataFrame(data)

df.loc[df['열4']=='Z','열4']='F'
df.loc[(df['열3']>100)|(df['열3']<0), '열3']=0

print(df)