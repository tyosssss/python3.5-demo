# coding:utf-8
# 列表推导式Demo
source = [1, 2, 3]

# for x in [1,2,3] :
#   numbers.append(x * 2)
# => 2,4,6
print([x * 2 for x in source])

# for x in [1,2,3] :
#   if x % 2 == 0 :
#       numbers.append(x * 2)
# ==> [4]
print([x * 2 for x in source if x % 2 == 0])

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

# for row in range(3)
#   for col in range(4)
#       dulplicate_matrix.append(matrix[row][col])
dulplicate_matrix = [[matrix[row][col] for col in range(4)] for row in range(3)]
print('dulplicate_matrix', dulplicate_matrix)

# for col in range(4)
#   for row in range(3)
#       trans_matrix.append(matrix[row][col])
trans_matrix = [[matrix[row][col] for row in range(3)] for col in range(4)]
print('trans_matrix', trans_matrix)
