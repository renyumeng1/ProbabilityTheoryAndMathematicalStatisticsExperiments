# -*- coding: utf-8 -*-
# @Time : 2022/6/21 16:06
# @Author : renyumeng
# @Email : 2035328756@qq.com
# @File : second.py
# @Project : ProbabilityTheoryAndMathematicalStatisticsExperiments
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.sandbox.regression.predstd import wls_prediction_std

x1 = [i for i in range(15)]
yTrue = [0.7, 1.1, 1.8, 2.1, 2.3, 2.6, 3, 3.1, 3.4, 3.8, 4.3, 4.6, 4.8, 5.5, 6.1]
yTest = [14.1, 17.3, 17.8, 24, 23.1, 19.6, 22.3, 27.5, 26.2, 26.1, 31.3, 31.3, 36.4, 36, 43.2]

X = sm.add_constant(x1)
model = sm.OLS(yTest, X)
results = model.fit()
yFit = results.fittedvalues
prstd, ivLow, ivUp = wls_prediction_std(results)
print("\nOLS model: Y = b0 + b1 * x")
print('Parameters: ', results.params)
plt.plot(x1, yTest, 'o', label="data")
plt.plot(x1, yFit, 'r-', label="OLS")
plt.plot(x1, ivUp, '--', color='orange', label="upConf")
print(ivUp,ivLow)
plt.plot(x1, ivLow, '--', color='orange', label="lowConf")
plt.legend(loc='best')
plt.title('OLS linear regression ')
plt.savefig('散点图1.png')
plt.show()
print(results.summary())
