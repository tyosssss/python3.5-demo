# -*- coding:utf-8 -*-

# 1. 第一种处理key缺失的方法
class Counter(dict):
    def __missing__(self, key):
        self[key] = 0
        return self[key]


counter1 = Counter()
counter1['red'] += 1
print(counter1)

# 2 . 第二种处理key缺失的方法
counter2 = dict()
counter2['red'] = counter2.get('red') + 1
print(counter2)
