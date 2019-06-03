# def sum_me(list):
#     if len(list) == 1:
#         return list[0]
#     else:
#         return list[0] + sum_me(list[1:])

# print(sum_me([1, 2, 3])) 

# result = []
# for i in range(10):
#     if i%2 == 0:
#         result.append(i)
# print(result)

# print([i for i in range(10) if i%2 == 0])

# print("--------------------------")
# mylist = [1,2,3,4,5]

# # For Loop Version
# result = []
# for i in mylist:
#     result.append(i**2)
# print(result)

# print([i**2 for i in range(10)])

# print("--------------------------")

# mylist = [1,2,3,4,5]

# result = []
# for i in mylist:
#     if i%2==0:
#         result.append(i**2)
# print(result)

# print([i**2 for i in range(10) if i % 2== 0])

# print("--------------------------")

# mylist = [1,2,3,4,5, 6, 7, 8, 9, 10]

# result = []
# for i in mylist:
#     if i % 2 ==0:
#         result.append(i**2)
#     else:
#         result.append(i**3)

# print(result)

# print([i**2 if i % 2 == 0 else i**3 for i in range(10)])

# print("--------------------------")

# mat = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
# result = []
# for row in mat:
#     for i in row:
#         if i%2 == 0:
#             result.append(i)

# print(result)

# mat = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
# result = []
# for row in range(len(mat)):
#     for i in mat[row]:
#         if i%2 == 0:
#             result.append(i)

# print(result)


# print([i for row in mat for i in row if i % 2 == 0])

# fizz_list = []
# for x in range(1, 101):
#     if x % 15 == 0:
#         fizz_list.append("fizzbuzz")
#     elif x % 5 == 0:
#         fizz_list.append("fizz")
#     elif x % 3 == 0:
#         fizz_list.append("buzz")
#     else:
#         fizz_list.append(x)

# print("---------")
# print(["fizzbuzz" if x % 5 == 0 else "fizz" if x % 5 == 0 else "buzz" if x % 3 == 0 else x for x in range(1, 101)])

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]

# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16],
# ]

# transposed = []
# for i in range(len(matrix)):
# # the following 3 lines implement the nested listcomp
#     transposed_row = []
#     for row in matrix:
#         if row[i] % 2 == 0:
#             transposed_row.append(row[i])
#         else: 
#             transposed_row.append(row[i])
#     transposed.append(transposed_row)

# print(transposed)

# print([[row[i] if row[i] % 2 == 0 else row[i] for row in matrix] for i in range(4)])

# n = Dividendo
# x = Divisor
# % modulo "residuo"
# //cociente

# for n in range(2, 11):
#     for x in range(2, n):
#         if n % x == 0:
#             # print(n, 'equals', x, '*', n//x)
#             break
#     else:
#         # loop fell through without finding a factor
#         print(n, 'is a prime number')
