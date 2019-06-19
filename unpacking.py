a, *b, c = range(5)

print(a)
print(c)
print(b)

# Many algorithms require splitting a sequence in a "first, rest" pair. With the new syntax,
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

first, rest = numbers[0], numbers[1:]
print(first)
print(rest)

# is replaced by the cleaner and probably more efficient:
first, *rest = numbers
print(first)
print(rest)
