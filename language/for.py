# coding=utf-8
print('------------------------------------ 1')
list = [1, 2, 3, 4, 5, 6]

for x in map(lambda x: x * 2, list):
    print(x)
else:
    print('done')


print('------------------------------------ 2')
# 不会输出"for.done"
# => for
for x in range(5):
    x = 100
    y = 100
    print('for', x)
    break
else:
    z = 200
    print('for.done')

# for语句的target_list作用域不会随着for循环的结束而结束
# 但是else子句之后的suite中定义的变量会
# x = 100
# y = 100
# z = error , z is undefined.
print('x', x)
print('y', y)

try:
    print('z', z)
except:
    print('error , z is undefined.')
