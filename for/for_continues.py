fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)


for x in fruits:
    if x == "banana":
        print(f"found {x}")
        continue
    print(x)


for x in fruits:
    if x == "banana":
        print(f"found {x}")


for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue


for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a number", num)


for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    else:
        print("Found a number", num)
