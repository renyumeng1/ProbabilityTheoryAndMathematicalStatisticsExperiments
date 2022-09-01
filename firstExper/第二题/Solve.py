# -*- coding: utf-8 -*-
# @Time : 2022/6/14 21:22
# @Author : renyumeng
# @Email : 2035328756@qq.com
# @File : Solve.py
# @Project : ProbabilityTheoryAndMathematicalStatisticsExperiments
from typing import Union, List, TypeVar, Dict

from utils.allDistribution import berNouLli, Poisson
import matplotlib.pyplot as plt


class Solve:
    T = TypeVar("T", int, str)

    def __init__(self, n: int, _lambda: Union[int, float]) -> None:
        self.n: int = n
        self._lambda: Union[int, float] = _lambda
        self.freezy_bernoulli: berNouLli = berNouLli(self.get_p, self.n)
        self.freezy_poisson: Poisson = Poisson(self._lambda)

    @property
    def get_p(self) -> float:
        return self._lambda / self.n

    @property
    def get_x(self) -> List[int]:
        temp_lst: List[int] = list(range(0, self.n + 1))
        return temp_lst

    @property
    def get_all_data(self) -> {str: Union[str, List[float]]}:
        x: List[int] = self.get_x
        _all_data: {str: Union[str, List[float]]} = {
            'x': x,
            'poisson': [],
            'bernoulli': []
        }
        for i in range(len(x)):
            _all_data['poisson'].append(self.freezy_poisson.get_poisson(i))
            _all_data['bernoulli'].append(self.freezy_bernoulli.pmf(i))
        return _all_data

    @staticmethod
    def draw_picture(path: str, data: Dict[str, Union[List[int], list]], x_data: T, *y_data: str) -> None:
        L1, = plt.plot((data[x_data]), data[y_data[0]])
        L2, = plt.plot(data[x_data], data[y_data[1]])
        plt.legend([L1, L2], ['泊松分布', '二项分布'])
        plt.xlabel('试验次数')
        plt.ylabel('概率')
        plt.savefig(path)
        plt.show()


if __name__ == '__main__':
    plt.rcParams['font.sans-serif'] = ['SimHei']
    eightNewObj: Solve = Solve(8, 4)
    eight_all_data: {str: Union[str, List[float]]} = eightNewObj.get_all_data
    Solve.draw_picture('实验8次.png', eight_all_data, 'x', 'poisson', 'bernoulli')
    hundredNewObj: Solve = Solve(100, 4)
    hundred_all_data: {str: Union[str, List[float]]} = hundredNewObj.get_all_data
    Solve.draw_picture('实验100次.png', hundred_all_data, 'x', 'poisson', 'bernoulli')
