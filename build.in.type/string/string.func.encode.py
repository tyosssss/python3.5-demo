# -*- coding:utf-8 -*-
FILE = 'unicode.txt'
CODEC = 'utf-8'

str_out = u'你好 Python\n'
bytes_out = str_out.encode(CODEC)

with open(FILE, "wb") as fp:
    fp.write(bytes_out)

with open(FILE, "rb") as fp:
    bytes_in = fp.read()
    str_in = bytes_in.decode(encoding='utf-8')

print('from file : ', str_in)
