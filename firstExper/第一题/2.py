# -*- coding: utf-8 -*-
# @Time : 2022/6/14 15:40
# @Author : renyumeng
# @Email : 2035328756@qq.com
# @File : Solve.py
# @Project : ProbabilityTheoryAndMathematicalStatisticsExperiments
import sympy
import numpy as np


class Normal:
    def __init__(self, sub_val: int, mu: int, sigma: int) -> None:
        self.x: sympy.Symbol = sympy.Symbol('x')
        self.m: int = mu
        self.sig: int = sigma
        self.val: int = sub_val
        self.pi: sympy.pi = sympy.pi

    @property
    def Nf(self) -> sympy.Symbol:
        f: sympy.exp = sympy.exp(-((self.x - self.m) ** 2) / (2 * self.sig ** 2))
        inter_f: sympy.Symbol = (1 / (sympy.sqrt(2 * self.pi) * self.sig)) * (
            sympy.integrate(f, (self.x, -np.inf, self.x)))
        return inter_f

    @property
    def sub_x(self) -> float:
        ans_func: sympy.Symbol = self.Nf
        sub_val: sympy.Symbol = ans_func.subs(self.x, self.val)
        return sub_val.evalf()


if __name__ == "__main__":
    newObj: Normal = Normal(5, 2, 3)
    print(newObj.sub_x)
