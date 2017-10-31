# coding=utf-8
print('------------------------------------ 1')
lst = [1, 2, 3, 4, 5, 6]
lst_len = len(lst)

index = 0
while index < lst_len:
    print(lst[index])
    index += 1
else:
    print('done')

print('------------------------------------ 2')
# 不会输出"while.done"
# => while
index = 0
while index < lst_len:
    x = 100
    y = 100
    print('while', x)
    break
else:
    z = 200
    print('while.done')

# x = 100
# y = 100
# z = error , z is undefined.
print('x', x)
print('y', y)

try:
    print('z', z)
except:
    print('error , z is undefined.')
