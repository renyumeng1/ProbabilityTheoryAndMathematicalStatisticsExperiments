# -*- coding: utf-8 -*-
# @Time : 2022/6/14 15:24
# @Author : renyumeng
# @Email : 2035328756@qq.com
# @File : Solve.py
# @Project : ProbabilityTheoryAndMathematicalStatisticsExperiments

class berNouLli:
    def __init__(self, x: int, p: float, n: int) -> None:
        self.x: int = x
        self.p: float = p
        self.n: int = n

    @property
    def pmf(self) -> float:
        f: float = self.factorial(self.n) / (self.factorial(self.x) * self.factorial((self.n - self.x))) * (
                self.p ** self.x * (1 - self.p) ** (self.n - self.x))
        return f

    def factorial(self, n: int) -> int:
        if n == 1 or n == 0:
            return 1
        else:
            return n * self.factorial(n - 1)


if __name__ == "__main__":
    newObj: berNouLli = berNouLli(3, 0.5, 6)
    print(newObj.pmf)
