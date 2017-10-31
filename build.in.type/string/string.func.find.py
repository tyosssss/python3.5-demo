# coding=utf-8
import json


# --------------------------
# 处理非Ascii码
dictionary = {"a":"你好","b":2}

print(json.dumps(dictionary , ensure_ascii=False))
