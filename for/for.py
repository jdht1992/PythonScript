numbers = [1, 3, 8, 4, 5, 2]

for n in numbers:
    for x in n:
        if x % 2 == 0:
            print(f"Par {x}")
        else:
            print(f"No par {x}")


for n in numbers:
    for x in n:
        if x % 2 == 0:
            print(f"Par {x}")
            continue
        print(f"No par {x}")
