# -*- encoding:utf-8 -*-
# __hash__

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __hash__(self):
        return 100


user1 = User('test', 'test')
user2 = User('test', 'aa')

d = {user1: "1", user2: "2"}

print(hash(user1))
print(hash(user2))
print(d)
print(str(user1))
print(str(user2))

for k in d.keys():
    print(type(k))

print(d[user1])
print(d[user2])
