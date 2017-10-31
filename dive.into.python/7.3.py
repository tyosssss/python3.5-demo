# -*- coding:utf-8 -*-
# 校验任意一个字符串是否为一个有效的罗马数字
# I = 1
# V = 5     (不能重复)
# X = 10
# L = 50    (不能重复)
# C = 100
# D = 500   (不能重复)
# M = 1000
# 罗马数字规则 :
#   1. 含十字符(I , X , C , M ) -- 至多可以重复三次
#   2. 含五字符 -- 不能重复
#   3. 从高到低位阅读 , 顺序不同意义不同
#       DC -- D + C = 500 + 100 ( 较大在
#       CD -- D - C = 500 - 400
import re

# 1000 = M
# 2000 = MM
# 3000 = MMM
def is_roman_number_X000(str):
    pattern = r'^M{1,3}$'

    return re.search(pattern, str)

# 100 = C
# 200 = CC
# 300 = CCC
# 400 = CD
# 500 = D
# 600 = DC
# 700 = DCC
# 800 = DCCC
# 900 = CM
def is_roman_number_X00(str):
    pattern = r'^(C{1,3})$|D$|(C[DM])$|(DC{0,3})$'
    return re.search(pattern, str)

print(is_roman_number_X000('M'))
print(is_roman_number_X000('MM'))
print(is_roman_number_X000('MMM'))
print(is_roman_number_X000('MMMM'))

print(is_roman_number_X00('C'))
print(is_roman_number_X00('CC'))
print(is_roman_number_X00('CCC'))
print(is_roman_number_X00('CD'))
print(is_roman_number_X00('D'))
print(is_roman_number_X00('DC'))
print(is_roman_number_X00('DCC'))
print(is_roman_number_X00('DCCC'))
print(is_roman_number_X00('CM'))