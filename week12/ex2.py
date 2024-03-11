import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

w = pd.read_csv('ch5-1.csv')
w_n = w.iloc[:,1:5]

model_lm = smf.ols(formula = 'weight ~ movement', data = w_n)
result_lm = model_lm.fit()
result_lm.summary()
print(result_lm.summary())

plt.figure(figsize = (10,7))
plt.scatter(w.movement, w.weight, alpha = .5)
plt.plot(w.movement, w.movement*0.1277 +120.0223 , color = 'red')
plt.text(100, 132, 'weight = 0.1277emovement +120.0223', fontsize =12)
plt.title('Scateer plot')
plt.xlabel('movement')
plt.ylabel ('weight')
plt.show()