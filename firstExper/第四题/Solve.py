# -*- coding: utf-8 -*-
# @Time : 2022/6/17 15:34
# @Author : renyumeng
# @Email : 2035328756@qq.com
# @File : Solve.py
# @Project : ProbabilityTheoryAndMathematicalStatisticsExperiments
from math import sqrt
from typing import List, Union
import scipy.stats
from scipy.stats import kstest


class Solve:
    def __init__(self, data: list = None) -> None:
        if data is None:
            data: List[Union[int, float]] = [87, 77, 92, 68, 80, 78, 84, 77, 81, 80, 80, 77, 92, 86, 76, 80, 81, 75, 77,
                                             72, 81, 72, 84, 86,
                                             80, 68, 77, 87,
                                             76, 77, 78, 92, 75, 80, 78]
        self.data: List[Union[int, float]] = data
        self.n: int = self.get_n
        self.mean: float = self.get_mean
        self.std: float = self.get_std
        self.p_value: float = self.normality_test
        self.scale: float = self.get_scale

    @property
    def get_n(self) -> int:
        return len(self.data)

    @property
    def get_scale(self) -> float:
        return self.std / sqrt(self.n)

    @property
    def get_mean(self) -> float:
        return sum(self.data) / self.n

    @property
    def get_std(self) -> float:
        temp_array: List[int] = self.data.copy()
        _mean: float = self.mean
        ans: Union[int, float] = 0
        for i in range(len(temp_array)):
            ans += (temp_array[i] - _mean) ** 2
        ans /= self.n
        ans = sqrt(ans)
        return ans

    @property
    def normality_test(self) -> float:
        test_state, p_value = kstest(self.data, 'norm', args=(self.mean, self.std))
        return p_value

    @property
    def judge_norm(self) -> str:
        if self.p_value > 0.05:
            return 'p值大于0.05，为正态分布'
        return 'p值小于或等于0.05，不是正太分布'

    def confidence_interval(self, x: float) -> tuple:
        CI: tuple = scipy.stats.norm.interval(x, loc=self.mean, scale=self.scale)
        return CI

    def __str__(self):
        return self.judge_norm


if __name__ == "__main__":
    newSolve: Solve = Solve()
    print(newSolve)
    print(f'置信区间为：{newSolve.confidence_interval(0.95)}')
