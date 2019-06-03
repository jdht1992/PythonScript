# # wiht the while loop we can execute a set of statements as long a condition is true

# x = 0 #remember to increment x, or else the loop will continue forever.

array = [3, 2, 6, 2, 5, 9, 2]
x=0
while x < len(array):
    print(f"[{x}] - [{array[x]}]")
    # x = x+1
    x += 1


# With the break statement we can stop the loop even if the while condition is true:

x = 0

while x < 10:
    if x == 5:
        print(x)
        break
    x += 1


# With the continue statement we can stop the current iteration, and continue with the next:

i = 0
while i < 6:
    i += 1 
    if i == 3:
        print(f"encontrado - {i}")
        continue
    print(i)

array = [2, 1, 4 ,2, 5, 6]

x = 0
while x < len(array):
    # print(len(array)-x)
    print(array[x])
    x += 1


array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

x = 0
while x < len(array):
    for y in array[x]:
        print(y, end=" ")
    print("\n")
    x += 1
