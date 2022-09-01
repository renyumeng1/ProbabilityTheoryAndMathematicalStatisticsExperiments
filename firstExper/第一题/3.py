# -*- coding: utf-8 -*-
# @Time : 2022/6/14 16:30
# @Author : renyumeng
# @Email : 2035328756@qq.com
# @File : 3.py
# @Project : ProbabilityTheoryAndMathematicalStatisticsExperiments
import math
from typing import Union


class Poisson:
    def __init__(self, x: int, _lamb: Union[int, float]) -> None:
        self.X: int = x
        self.lamb: Union[int, float] = _lamb

    def Pf(self, k: int) -> float:
        f: float = self.lamb ** k * math.exp(-self.lamb) / (self.factorial(k))
        return f

    @property
    def get_poisson(self) -> float:
        ans: Union[int, float] = 0
        for k in range(0, self.X + 1):
            ans += self.Pf(k)
        return ans

    def factorial(self, n: int) -> int:
        if n == 1 or n == 0:
            return 1
        else:
            return n * self.factorial(n - 1)


if __name__ == "__main__":
    newObj: Poisson = Poisson(5, 3)
    print(newObj.get_poisson)
