# -*- coding:utf-8 -*-
# 返回一个列表中的所有素数

def create_promise_number_generator(numbers):
    for x in numbers:
        for y in range(2, x):
            if x % y == 0: break
        else:
            yield x


gen = create_promise_number_generator([1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 15, 17, 20, 21, 26])

for x in gen:
    print(x)
