# -*- coding: utf-8 -*-
# @Time : 2022/6/21 14:32
# @Author : renyumeng
# @Email : 2035328756@qq.com
# @File : Solve.py
# @Project : ProbabilityTheoryAndMathematicalStatisticsExperiments
from typing import List, Union, Dict


class Solve:
    def __init__(self, _data: Dict[str, List[Union[int, float]]] = None) -> None:
        if _data is None:
            _data: Dict[str, List[Union[int, float]]] = {
                'A': [9.6, 10.8, 11.3, 10.7, 8.2, 9.0, 11.2],
                'B': [8.2, 9.4, 11.8, 9.1, 9.3, 11.0, 13.1]
            }
        self.data: Dict[str, List[Union[int, float]]] = _data
        self.each_sum: Dict[str, Union[int, float]] = self.get_each_sum  # A，B每一个的和
        self.sum_sum: float = self.get_sum_sum  # 所有的和
        self.sum_square: float = self.get_sum_square  # 所有的平方和
        self.n: int = self.get_length  # 所有的个数

        self.St: float = self.get_s_total
        self.Sa: float = self.get_among
        self.Se: float = self.get_error

        self.f_all: {str, Union[int, float]} = self.get_free
        self.fT: int = self.f_all['fT']
        self.fA: int = self.f_all['fA']
        self.fe: int = self.f_all['fe']

    @property
    def get_each_sum(self) -> Dict[str, Union[int, float]]:
        each_sum: Dict[str, Union[int, float]] = {}
        for key in self.data:
            each_sum[key] = sum(self.data[key])
        return each_sum

    @property
    def get_sum_sum(self) -> float:
        ans: Union[int, float] = 0
        for key in self.each_sum:
            ans += self.each_sum[key]
        return ans

    @property
    def get_sum_square(self) -> float:
        ans: Union[int, float] = 0
        for key in self.data:
            temp_data = self.data[key]
            ans += Solve.get_square(temp_data)
        return ans

    @property
    def get_length(self) -> int:
        length: int = 0
        for key in self.data:
            length += len(self.data[key])
        return length

    @property
    def get_s_total(self) -> float:
        return self.sum_square - ((self.sum_sum ** 2) / self.n)

    @property
    def get_free(self) -> {str, Union[int, float]}:
        total_free: int = self.n - 1
        among_free: int = len(self.data) - 1
        error_free: int = total_free - among_free

        return {
            'fT': total_free,
            'fA': among_free,
            'fe': error_free
        }

    @property
    def get_error(self) -> float:
        return self.St - self.Sa

    @property
    def get_among(self) -> float:
        ans: float = 0
        for key in self.each_sum:
            temp_dict = self.each_sum[key]
            ans += temp_dict ** 2 / (len(self.data[key]))
        ans -= self.sum_sum ** 2 / self.n
        return ans

    @property
    def get_f_proportion(self) -> float:
        return (self.Sa / self.fA) / (self.Se / self.fe)

    @staticmethod
    def get_square(data: List[Union[int, float]]) -> float:
        ans: float = 0
        for i in range(len(data)):
            ans += data[i] ** 2
        return ans


if __name__ == "__main__":
    newSolve: Solve = Solve()
    print(f"F比为：{newSolve.get_f_proportion}")
