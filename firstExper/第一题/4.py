# -*- coding: utf-8 -*-
# @Time : 2022/6/14 16:50
# @Author : renyumeng
# @Email : 2035328756@qq.com
# @File : 4.py
# @Project : ProbabilityTheoryAndMathematicalStatisticsExperiments
from typing import Union


class Uniform:
    def __init__(self, a: Union[int, float], b: Union[int, float], x: Union[int, float]) -> None:
        self.a: Union[int, float] = a
        self.b: Union[int, float] = b
        self.x: Union[int, float] = x

    @property
    def Uf(self) -> Union[int, float]:
        if self.x < self.a:
            return 0
        elif self.x >= self.b:
            return 1
        else:
            return (self.x - self.a) / (self.b - self.a)


if __name__ == "__main__":
    newObj: Uniform = Uniform(3, 9, 5)
    print(newObj.Uf)
