# count distinct elements in an array
# Given an unsorted array, count all distinct elements in it. 

arr = [10, 20, 20, 10, 30, 10] 
#arr = [10, 20, 20, 10, 20]
#arr = [10, 20, 20, 10, 20, 40, 50] 

num = []
for x in arr:
    for y in arr:
        if x == y:
            if not x in num:
                num.append(x)

print(f"numbers different: {len(num)} - {num}")

# num = []
# x = 0
# while x < len(arr):
#     y = 0
#     while y < len(arr):
#         num1, num2 = arr[x], arr[y] # pythonic way of value swapping
#         if num1 == num2:
#             if not num1 in num:
#                 num.append(num1)            
#         y = y + 1
#     x = x + 1

# print(num)
