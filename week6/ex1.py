import pandas as pd
import matplotlib.pyplot as plt
# from matplotlib import font_manager
import matplotlib.font_manager as font_manager
import seaborn as sns

hat = pd.read_csv('ch4-1.csv')
print(hat, end="\n\n")

print(hat.head(),end="\n\n")
print(hat.tail(3),end="\n\n")

font_path = "c:/windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font_name)
col7 = sns.color_palette('Pastel2',7)

def addtext(x,y):
    for i in range(len(x)):
        plt.text(i,y[i]+0.5,y[i], ha='center')
        
plt.figure(figsize=(15,10))
plt.bar(hat['hatchery'], hat['chick'], color = ('red','orange','yellow','green','blue','navy','purple'))
#plt.bar(hat['hatchery'], hat['chick'],color = col7)
plt.title('부회장별 병아리 부화현황')
addtext(hat['hatchery'], hat['chick'])
plt.xlabel('부화장')
plt.ylabel('부화마릿수')

plt.show()
#plt.savefig('my_image_1.png')
# 파이차트를 그리기 위해 비율 계산
pct = hat['chick']/hat['chick'].sum()
col7 = sns.color_palette('Pastel2',7)

#파이차트 그리기
plt.figure(figsize=(10,10))
plt.title('부회장별 병아리 분포도')
plt.pie(pct, labels = hat['hatchery'], autopct='%.lf%%', colors=col7, )
plt.show()

#라인 차트 그리기
plt.figure(figsize=(10,7))
plt.plot(hat.hatchery, hat.chick, marker='*', color='y', linestyle='--', linewidth=4)
plt.title('부회장별 병아리 부화현황')
plt.xlabel('부화장')
plt.ylabel('부화마릿수')
plt.grid(True)
plt.legend(['부화마릿수'], fontsize=10,loc='best')
plt.show()