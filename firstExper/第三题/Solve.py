# -*- coding: utf-8 -*-
# @Time : 2022/6/17 15:05
# @Author : renyumeng
# @Email : 2035328756@qq.com
# @File : Solve.py
# @Project : ProbabilityTheoryAndMathematicalStatisticsExperiments
import numpy as np
import scipy.stats as sts


class Solve:
    def __init__(self, N) -> None:
        self.n: int = N
        self._random_num: np.ndarray = self.get_normal_num
        self._describe_num: tuple = self.get_describe
        self.mean: float = self.get_mean
        self._describe_variance: float = self._describe_num[-3]
        self.func_variance: float = self.get_variance

    def __str__(self) -> str:
        return f"""使用describe函数得到的方差：{self._describe_variance}\n使用公式计算出的方差：{self.func_variance}"""

    @property
    def get_normal_num(self) -> np.ndarray:
        _normal_num: np.array = sts.norm.rvs(loc=0, scale=1, size=self.n)
        return _normal_num

    @property
    def get_describe(self) -> tuple:
        _describe_ans: tuple = sts.describe(self._random_num)
        return _describe_ans

    @property
    def get_mean(self) -> float:
        _mean: float = self._random_num.mean()
        return _mean

    @property
    def get_variance(self) -> float:
        temp_array: np.ndarray = self._random_num.copy()
        _mean: float = self.mean
        ans: float = 0
        for i in range(len(temp_array)):
            ans += (temp_array[i] - _mean) ** 2
        ans /= (self.n - 1)
        return ans


if __name__ == "__main__":
    newSolve: Solve = Solve(10)
    print(newSolve)
