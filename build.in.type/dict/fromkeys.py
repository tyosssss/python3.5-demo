# -*- coding:utf-8 -*-

lst = ['a', 'b', 'c']
tpl = ['1', '2', '3']
d = {"a": 1, "b": 2, "c": 3}

print(dict.fromkeys(lst, 1))
print(dict.fromkeys(tpl, 2))
print(iter(d))
