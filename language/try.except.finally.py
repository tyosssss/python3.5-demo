# conding=utf-8
import sys

# try未发生异常 , 会执行else子句
# => try
# => else,ok
# => finally
def fn1():
    try:
        print('try')
    except TypeError:
        print('handle TypeError')
    else:
        print('else,ok')
    finally:
        print('finally')


# try发生异常
#   不会执行else子句
#   执行对应的except子句 , 如果except子句发生异常 , 不会被后续的except捕获
# => try
# => handle TypeError
# => finally
# => 抛出异常
def fn2():
    try:
        print('try')
        raise TypeError('typerror')
    except TypeError:
        print('handle TypeError')
        raise IOError
    except IOError:
        print('handle IOError')
    else:
        print('else,ok')
    finally:
        print('finally')

# finally 如果有return语句 , 抛弃之前捕获的异常信息
# => try
# => handle TypeError
# => finally
def fn3():
    try:
        print('try')
        raise TypeError('typerror')
    except TypeError:
        print('handle TypeError')
        raise IOError
    finally:
        print('finally')
        return

fn1()
fn2()
fn3()