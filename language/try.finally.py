# conding=utf-8

# finally 无论如何也会被执行
# => try
# => finally
# => finally
def fn1():
    try:
        print('try')
    finally:
        print('finally')
        return 'finally'


print(fn1())
