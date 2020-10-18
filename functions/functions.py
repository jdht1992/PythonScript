# Chained function call
def product(a, b):
    return a * b

def add(a, b):
    return a + b

b = True
print((product if b else add)(5, 7))


numbers = [4, 2, 1, 6, 9, 7]
def squere(x):
        return x*x

print(list(map(squere, numbers)))

print([squere(x) for x in numbers])

def is_odd(x):
    return bool(x % 2)

print(list(filter(is_odd, numbers)))


print([x for x in numbers if is_odd(x)])