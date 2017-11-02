# -*- coding:utf-8 -*-

# 合法的
print(set("123"))
print(set([1, 2, 3]))
print(set({"a": 1, "b": 2}))
print(set((1, 2, 3, 4)))

# 不合法的
try:
    print(set(1))
except:
    print('set(1) error')

try:
    print(set(True))
except:
    print('set(True) error')


try:
    print(set((1)))
except:
    print('set((1) error')