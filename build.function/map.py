# coding:utf-8
numbers = [1, 2, 3, 4, 5, 6]
chinese_numbers = ['一', '二', '三', '四', '五', '六']

# => [2,4,6,8,10,12]
print((list(map(lambda x: x * 2, numbers))))


# 合并两个iterable
def map_function(x, y):
    return str(x) + '_' + y


print(list(map(map_function, numbers, chinese_numbers)))

# 多个iterable , 当耗尽最短的iterable之后 , 结束
iterable1 = [1, 2, 3, 4]
iterable2 = [1, 2, 3, 4, 5, 6]
results = list(map(lambda x, y: x + y, iterable1, iterable2))

# => 4
print('len', len(results))

# => [2,4,6,8]
print(results)
