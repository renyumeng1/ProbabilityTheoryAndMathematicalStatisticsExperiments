# -*- coding: utf-8 -*-
# @Time : 2022/6/17 16:01
# @Author : renyumeng
# @Email : 2035328756@qq.com
# @File : Solve.py
# @Project : ProbabilityTheoryAndMathematicalStatisticsExperiments
import scipy.stats as sts
from typing import List

data: List[float] = [15.6, 16.2, 22.5, 20.5, 16.4, 19.4, 16.6, 17.9, 12.7, 13.9]
t, p_twoTail = sts.ttest_1samp(data, 20, nan_policy='propagate', alternative='two-sided')
print(t, p_twoTail)
