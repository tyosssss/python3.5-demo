# coding=utf-8
def is_odd(x): return x % 2 != 0
is_event = lambda x: x % 2 == 0

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_numbers = filter(is_odd, numbers)
print('奇数:', list(odd_numbers))

event_numbers = filter(is_event, numbers)
print('偶数:', list(event_numbers))



