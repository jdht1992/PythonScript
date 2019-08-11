# the id changes with tha two type of sort

num = [2, 3, 1, 6, 5, 8, 3, 2]
print(id(num))

print(id(num.sort()))

print(id(sorted(num)))

# sorted() returns a new sorted list, leaving the original list 
# unaffected. list.sort() sorts the list in-place, mutating the 
# list indices, and returns None (like all in-place operations).

print(sorted(num))
print(num)

num.sort()
print(num)

number = [3, 1, 3, 8, 6, 5]

print(sorted([6, 5, 3, 7, 2, 4, 1]))

print(sorted(['cat', 'dog', 'cheetah', 'rhino', 'bear']))

print(sorted(['cat', 'dog', 'cheetah', 'rhino', 'bear'], reverse=True))

animals = [
        {'type': 'penguin', 'name': 'Stephanie', 'age': 8},
        {'type': 'elephant', 'name': 'Devon', 'age': 3},
        {'type': 'puma', 'name': 'Moe', 'age': 5},
        ]

print(sorted(animals, key=lambda animal: animal['age']))

datos = {'name': 'juan', 'edad': 27, 'domicilio': 'donde sea'}

print(sorted(datos))

