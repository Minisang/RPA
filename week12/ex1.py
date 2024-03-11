import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

w = pd.read_csv('ch5-1.csv')
w_n = w.iloc[:,1:5]

model_lm = smf.ols(formula = 'weight ~ egg_weight', data = w_n)
#model_lm = smf.ols(formula = 'weight ~ egg_weight+movement+food', data = w_n)

result_lm = model_lm.fit()

result_lm.summary()

print(result_lm.summary())

plt.figure(figsize = (10,7))
plt.scatter(w.egg_weight, w.weight, alpha = .5)
plt.plot(w.egg_weight, w.egg_weight*2.3371 - 14.5475, color = 'red')
plt.text(66, 132, 'weight = 2.3371egg_weight - 14.5475', fontsize =12)
plt.title('Scateer plot')
plt.xlabel('egg_weight')
plt.ylabel ('weight')
plt.show()

from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np

predicted_values = result_lm.predict()

mse = mean_squared_error(w_n['weight'], predicted_values)
mae = mean_absolute_error(w_n['weight'], predicted_values)
rmse = np.sqrt(mse)
r_squared = r2_score(w_n['weight'], predicted_values)

print("Mean Squard Error (MSE)", mse)
print("Mean Absolute Error (MAE)", mae)
print("Root Mean Squard Error (RMSE)", rmse)
print("R-squared", r_squared)