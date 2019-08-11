# Differents ways to test multiple flags at once in python 

x, y, z = 0, 1, 0

if x==0 or y==0 or x==0:
    print("True")

if 1 in (x, y, z):
    print("Exist")
else:
    print("Not exist")

# 1 is equivalent to TRUE and 0 is equivalent to FALSE
if x or y or z:
    print("There are some in TRUE")
else:
    print("There aren't any in TRUE")

# if any items is 1 print YES
if any((x, y, z)):
    print("YES")
else:
    print("NOT")