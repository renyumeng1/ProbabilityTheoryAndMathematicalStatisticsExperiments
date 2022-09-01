# -*- coding: utf-8 -*-
# @Time : 2022/6/16 23:37
# @Author : renyumeng
# @Email : 2035328756@qq.com
# @File : single.py
# @Project : ProbabilityTheoryAndMathematicalStatisticsExperiments

class singleInstance:
    __instance = None

    def __init__(self):
        if singleInstance.__instance:
            print("对象已经被创建")
        else:
            print("对象还未被创立")

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = singleInstance()
        return cls.__instance


if __name__ == "__main__":
    print(singleInstance.get_instance())
    print(singleInstance.get_instance())
    A = singleInstance()
    B = singleInstance()
    print(A)
    print(B)
