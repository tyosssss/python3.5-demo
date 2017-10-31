# -*- coding:utf-8 -*-
# 标识符合法性检查
# 1. 首个字符必须是 字母或下划线
# 2. 其他字符必须是(数字|字母|下划线)
import string


def id_check(id):
    if len(id) > 0:
        first_char = id[0]
        if not (is_alphas(first_char) or is_underline(first_char)):
            return False

        others_char = id[1:]
        for c in others_char:
            if not (is_alphas(c) or is_underline(c) or is_digit(c)):
                return False

        return True
    else:
        return False


def is_alphas(c):
    return c in string.ascii_letters


def is_underline(c):
    return c == '_'


def is_digit(c):
    return c in string.digits


print(id_check('abcd'))
print(id_check('_abcd'))
print(id_check('_abc%d'))

enumerate()