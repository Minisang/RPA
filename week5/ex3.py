import pandas as pd

data = {'열1':[1,2,2,3,4],
        '열2':['A','B','B','C',"D"],
        '열3':[10,20,30,40,50],
        '열4':['A','B','B','F','F']}

df = pd.DataFrame(data)
df.drop_duplicates(subset=['열2','열4'], keep='first', inplace=True)
print(df)