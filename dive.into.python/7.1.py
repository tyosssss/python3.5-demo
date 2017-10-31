# -*- coding:utf-8 -*-
# 匹配替换字符串
import re

pattern = r'\bROAD\b'
strs = [
    '100 NORTH MAIN ROAD',
    '100 NORTH BROAD ROAD',
    '100 BROAD',
    '100 BROAD ROAD APT. 3'
]

for s in strs:
    print('%s => %s' % (s, re.sub(pattern, 'RD.', s)))
