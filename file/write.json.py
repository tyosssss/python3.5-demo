# coding = utf-8
# 将字典转换为JSON格式 , 并写入到指定的JSON文件
import json

user = {
    "name": "wx",
    "age": 27,
    "tags": ["software engine", "programmer"]
}

with open('./tmp/user.json', 'w') as fp:
    json.dump(user, fp, indent=4)
