i = j = k = 50

a, b = 1, 2

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


# NEVER UNPACK MORE THAN THREE VARIABLES WHEN FUNCTIONS RETURN MULTIPLE VALUES

def get_stats(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    return minimum, maximum

lengths = [63, 73, 72, 60, 67, 66, 71, 61, 72, 70]

# The way this works is that multiple values are returned together in a two-item tuple.
minimum, maximum = get_stats(lengths) 

print(f'Min: {minimum}, Max: {maximum}')

