import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager
import seaborn as sns

hat = pd.read_csv('ch4-2.csv')
print(hat.describe(), end="\n\n")

font_path = "c:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font_name)

# #히스토그램 그리기
plt.figure(figsize=(10,17))
plt.hist(hat.weight, bins=7)
plt.title('B 부화장 병아리 무게 분포 현황', fontsize=17)
plt.xlabel('병아리 무게(g)')
plt.ylabel('마릿수')
sns.distplot(hat.weight)
# #plt.show()

# #상자그림 그리기
plt.figure(figsize=(8,10))
plt.boxplot(hat.weight)
plt.title('B 부화장 병아리 무게 상자그림', fontsize=17)
plt.ylabel('병아리 무게(g)')
plt.show()

#히스토그램과 상자그림 한 번에 표시
# plt.figure(figsize=(10,12))
# plt.subplot(2,1,1) #행, 열, 위치(인덱스)
# plt.hist(hat.weight, bins=7)
# plt.title('B 부화장 병아리 무게 분포 현황', fontsize = 17)
# plt.subplot(2,1,2)
# plt.boxplot(hat.weight, vert = False)
# plt.show()