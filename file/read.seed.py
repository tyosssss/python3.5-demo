# coding=utf-8
FILE_PATH = './tmp/read.seed.txt'
# 二进制形式 , 随机读

FROM_FILE_BEGIN = 0
FROM_CURRENT_OFFSET = 1
FROM_FILE_END = 2

with open(file=FILE_PATH, mode='w') as f:
    f.write('py__th__on!!!')

with open(
        file=FILE_PATH,
        mode='rb'
)as f:
    f.seek(0,FROM_FILE_BEGIN)           # 从0开始
    print(f.read(2))                    # ==> py

    f.seek(2, FROM_CURRENT_OFFSET)      # 跳过 __
    print(f.read(2))                    # ==> th

    f.seek(-5, FROM_FILE_END)           # 跳过 __
    print(f.read(2))                    # ==> on

