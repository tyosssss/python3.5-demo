# coding=utf-8
import sys

with open(
        file=r'./tmp/read.file.txt',
        mode='w',
        encoding='utf-8'
) as f:
    f.write('你好python')
    f.write('!!!')
    f.flush()
    f.close()
