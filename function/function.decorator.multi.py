# coding=utf-8
# 多个装饰器的调用顺序


def func1(func):
    def wrapper():
        print('call func1')
        func()

    return wrapper


def func2(func):
    def wrapper():
        print('call func2')
        func()

    return wrapper


def func3(func):
    def wrapper():
        print('call func3')
        func()

    return wrapper

# 等价于 func(func3(func2(fun1())))
@func1
@func2
@func3
def func():
    print('call func')


func()
