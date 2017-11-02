# -*- coding:utf-8 -*-
# 建立字典
# 有两个列表lst1,lst2, 使用lst1中的元素作为key , lst2中的元素作为value , 创建一个字典
d = {}

lst1 = input('input keys:').split(' ')
lst2 = input('input values:').split(' ')

lst1_len = len(lst1)
lst2_len = len(lst2)

i = 0
j = 0

while i < lst1_len and j < lst2_len:
    key = lst1[i]
    value = lst2[j]
    d[key] = value

    i += 1
    j += 1

print(d)
