import pandas as pd

ns_df = pd.read_csv('booklist.csv', encoding='euc-kr')
print(ns_df.head(15), end="\n\n")
# ns_df.to_csv("backup.csv")

print("=====================\n\n")

d1_str = """
[
    {"name": "데이터 분석", "author": "홍길동", "year": 2022},
    {"name": "머신러닝+딥러닝", "author": "홍길동", "year": 2020}
]
"""
df1 = pd.read_json(d1_str)
print(df1, end="\n\n")

df2 = pd.read_json('book.json')
print(df2, end="\n\n")

df2.to_json('df2_index.json', orient='index', indent=4, force_ascii=False)