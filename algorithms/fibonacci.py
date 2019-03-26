# a = 0
# b = 1
# for i in range(10):
#     z = a+b
#     a = b
#     b = z
#     print(z, end=' ')

# this step is removed in python
#a = b
#b = a+b

a, b = 0, 1
for i in range(10):
    print(f'{a}', end=' ')
    a, b = b, a + b
print()

# n = 10
# a, b = 0,1
# while a < n:
#     print(a, end=' ')
#     a, b = b, a+b
# print()

# def fib(n):
#     a, b = 0,1
#     while a < n:
#         print(a, end=' ')
#         a, b = b, a+b
#     print()
# fib(1000)
