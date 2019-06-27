g = (x for x in range(10))

print(sum(g))

print(g)

print(list(g))


def numberGenerator(n):
    try:
        number = 0
        while number < n:
            yield number
            number += 1
    finally:
        yield n

print(list(numberGenerator(10)))


lst = (x*x for x in [1, 2, 3])
print(lst)

for i in lst:
    print(i)

# Nothing is displayed
for i in lst:
    print(i)

lista = [1,2,4]
tupla = (1,2,3)
print(dir(lista))
print()
print(dir(tupla))

print(hasattr(str, '__iter__'))


print(sum([i * i for i in range(1, 1000001)]))

print(sum((i * i for i in range(1, 1000001))))


l = [1, 2, 3]

for method_name in dir(l):
    if callable(getattr(l, method_name)):
        print(method_name)

