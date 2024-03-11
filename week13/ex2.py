import pandas as pd

#1. 데이터 로딩
w = pd.read_csv("ch5-1.csv")
print(w.head(), end="\n\n")

#상관분석 실시
from sklearn.model_selection import train_test_split

#독립변수/종속변수 데이터셋 x,y로 분할
x_data = w.iloc[:,2:5].values
y_data = w.iloc[:,1].values

#훈련용과 테스트용 8:2로 분할 실시
x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.2)
print(len(pd.DataFrame(x_train)), len(pd.DataFrame(x_test)), end='\n\n')
print(len(pd.DataFrame(y_train)), len(pd.DataFrame(y_test)), end='\n\n')

#3. 학습 수행 : MLP 알고리즘 수행을 위한 함수 불러오기
from sklearn.neural_network import MLPRegressor
model_mlp = MLPRegressor().fit(x_train, y_train)

# 모델 확인
print(model_mlp.get_params(), end='\n\n')

#4. 예측값 생성 (시험)
y_pred_mlp = model_mlp.predict(x_test)
print(y_train, end='\n\n')
print(y_pred_mlp, end='\n\n')

df_x_test = pd.DataFrame(x_test, columns=['egg_weight','movement','food'])
df_y_pred = pd.DataFrame(y_pred_mlp, columns=['predict'])
df_y_test = pd.DataFrame(y_test, columns=['real'])
df = pd.concat([df_x_test, df_y_test, df_y_pred], axis=1)
print(df, end='\n\n')

# 희귀성능 지표 계산용 함수 불러오기 및 계산
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

MAE = mean_absolute_error(y_test, y_pred_mlp)
R2 = r2_score(y_test, y_pred_mlp)

print("MAE = ", MAE, end='\n\n')
print("R2 = ", R2, end='\n\n')