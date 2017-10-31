# coding=utf-8

ljust_strings = [
    'A'.ljust(5, '#'),
    'AA'.ljust(5, '#'),
    'AA'.ljust(5, '#'),
    'AAA'.ljust(5, '#'),
    'AAAA'.ljust(5, '#'),
    'AAAAA'.ljust(5, '#')
]

center_strings = [
    'A'.center(5, '#'),
    'AA'.center(5, '#'),
    'AA'.center(5, '#'),
    'AAA'.center(5, '#'),
    'AAAA'.center(5, '#'),
    'AAAAA'.center(5, '#')
]

rjust_strings = [
    'A'.rjust(5, '#'),
    'AA'.rjust(5, '#'),
    'AA'.rjust(5, '#'),
    'AAA'.rjust(5, '#'),
    'AAAA'.rjust(5, '#'),
    'AAAAA'.rjust(5, '#')
]

for s in ljust_strings:
    print(s)

for s in center_strings:
    print(s)

for s in rjust_strings:
    print(s)