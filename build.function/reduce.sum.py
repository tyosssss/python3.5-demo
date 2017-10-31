# coding:utf-8
# 使用reduce实现sum函数
from functools import reduce

def sum(sequence):
    def add(x, y):
        return x + y

    return reduce(add, sequence, 0)


print(sum(range(1, 10)))
