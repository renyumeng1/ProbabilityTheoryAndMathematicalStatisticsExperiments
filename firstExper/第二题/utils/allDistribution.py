# -*- coding: utf-8 -*-
# @Time : 2022/6/14 20:58
# @Author : renyumeng
# @Email : 2035328756@qq.com
# @File : allDistribution.py
# @Project : ProbabilityTheoryAndMathematicalStatisticsExperiments
import sympy
import numpy as np
import math
from abc import abstractmethod, ABC


class berNouLliRule(ABC):
    @abstractmethod
    def pmf(self, x):
        pass

    @abstractmethod
    def factorial(self, n):
        pass


class NormalRule(ABC):
    @abstractmethod
    def Nf(self):
        pass

    @abstractmethod
    def sub_x(self, val):
        pass


class PoissonRule(ABC):
    @abstractmethod
    def Pf(self, k):
        pass

    @abstractmethod
    def get_poisson(self, X, is_equal=True):
        pass

    @abstractmethod
    def factorial(self, n):
        pass


class UniformRule(ABC):
    @abstractmethod
    def Uf(self):
        pass


class berNouLli(berNouLliRule):
    def __init__(self, p, n):
        self.p = p
        self.n = n

    def pmf(self, x):
        f = self.factorial(self.n) / (self.factorial(x) * self.factorial((self.n - x))) * (
                self.p ** x * (1 - self.p) ** (self.n - x))
        return f

    def factorial(self, n):
        if n == 1 or n == 0:
            return 1
        else:
            return n * self.factorial(n - 1)


class Normal(NormalRule):
    def __init__(self, mu, sigma):
        self.x = sympy.Symbol('x')
        self.m = mu
        self.sig = sigma
        self.pi = sympy.pi

    @property
    def Nf(self):
        f = sympy.exp(-((self.x - self.m) ** 2) / (2 * self.sig ** 2))
        inter_f = (1 / (sympy.sqrt(2 * self.pi) * self.sig)) * (sympy.integrate(f, (self.x, -np.inf, self.x)))
        return inter_f

    def sub_x(self, val):
        ans_func = self.Nf
        sub_val = ans_func.subs(self.x, val)
        return sub_val.evalf()


class Poisson(PoissonRule):
    def __init__(self, _lamb):
        self.lamb = _lamb

    def Pf(self, k):
        f = self.lamb ** k * math.exp(-self.lamb) / (self.factorial(k))
        return f

    def get_poisson(self, X, is_equal=True):
        ans = 0
        if is_equal:
            ans = self.Pf(X)
        else:
            for k in range(0, X + 1):
                ans += self.Pf(k)
        return ans

    def factorial(self, n):
        if n == 1 or n == 0:
            return 1
        else:
            return n * self.factorial(n - 1)


class Uniform(UniformRule):
    def __init__(self, a, b, x):
        self.a = a
        self.b = b
        self.x = x

    @property
    def Uf(self):
        if self.x < self.a:
            return 0
        elif self.x >= self.b:
            return 1
        else:
            return (self.x - self.a) / (self.b - self.a)


if __name__ == "__main__":
    NewObj = Poisson(5, 3)
    print(NewObj.get_poisson(is_equal=False))
