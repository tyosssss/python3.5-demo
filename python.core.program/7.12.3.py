# -*- coding:utf-8 -*-
# 创建一个字典
# 1. 按key排序之后 , 打印key,value
# 2. 按value排序之后 , 打印key,value

d = {
    "name": "wx",
    "age": "27",
    "address": "鸿隆世纪广场",
    "birthday": "2017-11-01"
}

# solve 1
sorted_keys = sorted(d.keys())
sorted_values = sorted(d.values())
value_to_key_mapping = {}

print('sorted dictionary ( by key ):')
for key in sorted_keys:
    value = d[key]
    value_to_key_mapping[value] = key
    print("    %s=%s" % (key, value))

# solve 2
print('sorted dictionary ( by value ):')
for value in sorted_values:
    print("    %s=%s" % (value_to_key_mapping[value], value))
