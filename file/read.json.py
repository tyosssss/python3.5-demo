# coding = utf-8
# 从指定文件读取JSON字符串 , 转换成Python 字典
import json

with open('./tmp/user.json', 'r') as fp:
    user = json.load(fp)
    print(user)
