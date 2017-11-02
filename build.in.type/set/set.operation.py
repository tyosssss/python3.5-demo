# -*- coding:utf-8 -*-

A = set((1, 2, 3))
B = set((1, 3, 2))
C = set((1, 2))
D = set((1,5,6))
E = set((5,6))

print(A == B)               # True
print(1 in A)               # True
print(5 not in A)           # True
print(C < A)                # True C是A的真子集
print(set((1,2,3)) <= A)    # True
print(A & C)                # {1,2}
print(A | C)                # {1,2,3}
print(A - D)                # {3}
print(A ^ D)                # {2,3,5,6}
print(A.isdisjoint(B))      # A 和 B有交集 , 返回False
print(A.isdisjoint(E))      # A 和 E无交集 , 返回True

A.update(D)
print(A)

A.discard(10)