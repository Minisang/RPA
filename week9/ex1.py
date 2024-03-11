import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
import seaborn as sns

df = pd.read_csv("moving_keyword.csv")
print(df, end="\n\n")

font_path = "c:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font_name)
col7 = sns.color_palette('Pastel2', 7)

df_n = df.iloc[:,1:4]
print(df_n,end="\n\n")

df_cor = df_n.corr(method = 'pearson')

print(df_cor,end="\n\n")

sns.pairplot(df_n)

plt.figure(figsize = (10,7))
sns.heatmap(df_cor, annot = True, cmap = 'Blues')
plt.show()