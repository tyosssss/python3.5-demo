# coding=utf-8
# 自定义异常类
class MyError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return repr(self.message)


try:
    raise MyError('system error')
except MyError as e:
    print('executed with error', e.message)
