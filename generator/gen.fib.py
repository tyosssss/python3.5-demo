# -*- coding:utf-8 -*-
# 使用生成器实现 , 菲波那切数列数列

def create_fib_gen(n):
    f1 = 0
    f2 = 1

    for i in range(0, n):
        yield f2
        (f1, f2) = (f2, f1 + f2)


print([x for x in create_fib_gen(10)])
