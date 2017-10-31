# coding=utf-8
strings = [
    'exit'.capitalize(),    # ==> Exit
    'Exit'.capitalize(),    # ==> Exit
    '_exit'.capitalize(),   # ==> _exit
    '1exit'.capitalize()    # ==> 1exit
]

for s in strings:
    print(s)
