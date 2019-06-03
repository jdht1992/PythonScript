numbers = [[2, 1, 3], [6, 5, 1], [9, 2, 1]]

for n in numbers:
    for x in n:
        print(x, end=" ")
    print()


for n in range(1, len(numbers)+1):
    print(n)


for i, n in enumerate(numbers):
    i += 1
    print(i, n)


for n in numbers:
    for j, x in enumerate(n):
        if j == (len(n) - len(n)):
            print("*", end=" ")
            continue
        print(x, end=" ")
    print()


for i, n in enumerate(numbers):
    for x in n:
        if i == 0:
            print("*", end=" ")
            continue
        print(x, end=" ")
    print()


for n in numbers:
    for i, x in enumerate(n):
        if i == len(numbers)-1:
            print("*", end=" ")
            continue
        print(x, end=" ")
    print()


for i, n in enumerate(numbers):
    for j, x in enumerate(n):
        if i == j:
            print("*", end=" ")
            continue
        print(x, end=" ")
    print()


cont = 0
for n in numbers:
    cont += 1
    for i, x in enumerate(n):
        if i <= len(numbers)-cont:
            print("*", end=" ")
            continue
        print(x, end=" ")
    print()

print(len(numbers) - len(numbers))
print(numbers[len(numbers)-1])
