# conding=utf-8
# zip()

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

# zip( [1,2,3,4] , [5,6,7,8] , [9,10,11,12] )
print(list(zip(*matrix)))


