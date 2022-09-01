# -*- coding: utf-8 -*-
# @Time : 2022/6/21 15:29
# @Author : renyumeng
# @Email : 2035328756@qq.com
# @File : Solve.py
# @Project : ProbabilityTheoryAndMathematicalStatisticsExperiments
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import MultiComparison

df = pd.DataFrame({
    'A': [133.8, 125.3, 143.1, 128.9, 135.7],
    'B': [151.2, 149.0, 162.7, 143.8, 153.5],
    'C': [193.4, 185.3, 182.8, 188.5, 198.6, ],
    'D': [225.8, 224.6, 220.4, 212.3, 223.5, ]
})
df_melt = pd.melt(df, var_name='Treat', value_name='value')

model = ols(formula='value ~ C(Treat)', data=df_melt).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
print(anova_table)

mc = MultiComparison(df_melt['value'], df_melt['Treat'])

tukey_result = mc.tukeyhsd(alpha=0.05)
print("均值的多重比较")
print(tukey_result)
