# -*- coding:utf-8 -*-
# 管理登录系统的用户信息 : 账号和密码
#   1. 登录账号建立后 , 已存在用户可以用登录名称和密码重发系统
#   2. 新用户不能用别人的登录名建立用户账号
#   3. 记录用户上次的登录日期和时间 , 登录成功则更新登录时间
#   4. 登录相差不超过4个小时 , 则 通知用户 "You already logged in at:<最后的登录时间> "
#   5. 添加 "删除用户功能"
#   6. 添加 "用户列表功能"
#   7.
import sys
import time

db = {
    'admin': {
        "password": "admin",
        "uptime": None
    }
}


def cli():
    while True:
        showmenu()
        c = str(input()).strip()[0].lower()

        if c == 'n':
            newuser()
            break
        elif c == 'e':
            olduser()
            break
        elif c == 'q':
            quit()
            break
        else:
            print('\nInput Error, please retry!!!')


def showmenu():
    prompt = '''
(N)ew User Login
(E)xisting User Login
(Q)uit

Enter choice: '''

    sys.stdout.write(prompt)


def newuser():
    prompt = 'login desired:'
    while True:
        username = input(prompt)
        if username in db:
            prompt = 'name taken,try another:'
            continue
        else:
            break

    password = input('password:')

    db[username] = password


def olduser():
    retry_threshold = 3
    retry_count = 0

    while True:
        if retry_count >= retry_threshold:
            print('login incorrect')
            return

        username = input('login:')
        if username not in db:
            print('"%s" not exists , please retry.' % username)
            retry_count += 1
        else:
            break

    password = input('password:')
    if db[username] == password:
        print('welcome back', username)
    else:
        print('login incorrect')


if __name__ == '__main__':
    cli()
