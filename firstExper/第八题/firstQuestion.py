# -*- coding: utf-8 -*-
# @Time : 2022/6/21 15:38
# @Author : renyumeng
# @Email : 2035328756@qq.com
# @File : firstQuestion.py
# @Project : ProbabilityTheoryAndMathematicalStatisticsExperiments
import math
import matplotlib.pyplot as plt
from typing import List, Union, TypeVar
import numpy as np


class FirstQuestion:
    T = TypeVar("T", List[int], List[float])

    def __init__(self, _distance: T = None, _loss: T = None):
        if _loss is None and _distance is None:
            self.distance = [0.7, 1.1, 1.8, 2.1, 2.3, 2.6, 3, 3.1, 3.4, 3.8, 4.3, 4.6, 4.8, 5.5, 6.1]
            self.loss = [14.1, 17.3, 17.8, 24, 23.1, 19.6, 22.3, 27.5, 26.2, 26.1, 31.3, 31.3, 36.4, 36, 43.2]
        else:
            self.distance = _distance
            self.loss = _loss

    @staticmethod
    def mean(x):
        return sum(x) / len(x)

    def de_mean(self, x):
        x_bar = self.mean(x)
        return [x_i - x_bar for x_i in x]

    @staticmethod
    def dot(v, w):
        return sum(v_i * w_i for v_i, w_i in zip(v, w))

    @staticmethod
    def sum_of_squares(v):
        return FirstQuestion.dot(v, v)

    def variance(self, x):
        n = len(x)
        deviations = self.de_mean(x)
        return FirstQuestion.sum_of_squares(deviations) / (n - 1)

    def standard_deviation(self, x):
        return math.sqrt(self.variance(x))

    def covariance(self, x, y):
        n = len(x)
        return self.dot(self.de_mean(x), self.de_mean(y)) / (n - 1)

    @property
    def correlation(self):
        st_dev_x = self.standard_deviation(self.distance)
        st_dev_y = self.standard_deviation(self.loss)
        if st_dev_x > 0 and st_dev_y > 0:
            return self.covariance(self.distance, self.loss) / st_dev_x / st_dev_y
        else:
            return 0

    def draw_picture(self, path='./'):
        plt.scatter(self.distance, self.loss)
        plt.savefig(f'{path}散点图.png')
        plt.show()


if __name__ == "__main__":
    newObj: FirstQuestion = FirstQuestion()
    newObj.draw_picture()
    print(newObj.correlation)
