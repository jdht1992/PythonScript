numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
for x in numbers:
    print(x, "\n")


number = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
for x in number:
    for i, y in enumerate(x):
        print(y, end=" ")
        if i == len(x)-1:
            print(f" - {x.upper()}")
    print()


for x in "seven":
    print(x, end=" ")

numbers = [3, 1, 6, 5, 2, 8]

for n in numbers:
    print(n)

for n in range(len(numbers)):
    print(n, numbers[n])

for i, n in enumerate(numbers):
    if i == 3:
        break
    print(n)  
