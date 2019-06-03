#not finished, improve

a = "()"
b = "[]"
c = "{}"

inp = "{([[]])}"
total = len(inp)
m = int(total / 2)

x = 0
cont1 = 0
cont2 = 1

if m==0:
    print(True)
else:
    for i in range(m):
        z = str(inp[cont1] + inp[cont2]) 
        y = str(inp[i] + inp[total-cont2])
        if (z == a) or (z == b) or (z == c):  # if z in [a,b,c] or y in [a,b,c]
            cont1 = cont1 + 2  # cont1 += 2
            cont2 = cont2 + 2
            x += 1
        elif (y == a) or (y == b) or (y == c):  # if y in [a,b,c]
            cont2 = cont2 + 1
            x += 1

    if x == m:
        print(True)
    else:
        print(False)
