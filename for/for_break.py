# else gets called when for loop does not reach break statment
a = [1, 2, 3, 4, 5]

for n in a: 
    if n == 0: 
        break 
else: 
    print('did not break out of for loop')


fruits = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",  "eighteen", "nineteen", "twenty"]

for x in fruits:
    if x == "thirteen":
        break
    print(x)

for x in fruits:
    if len(x) == 7 :
        break
    print(x)

for x in fruits:
    if len(x) == 7 :
        break
    else:
        print(x)

array = [2, 3, 4, 5, 6, 7, 8, 9, 10]
for n in array:
    for x in range(2, n):
        if n % x == 0:
            # print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
