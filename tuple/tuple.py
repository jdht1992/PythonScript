#A tuple with values can be initialized by making a sequence of values separated by commas.  

z = (3, 7, 4, 2)
print(type(z))

# Tuple also can be created without parentheses
z1 = 3, 7, 4, 2
print(type(z))

# It is important to keep in mind that if you want to create a tuple containing only one value, 
# you need a trailing comma after your item. 
tup1 = ('Michael',)
print(type(tup1))

tup2 = 'Michael',
print(type(tup2))

# This is a string, NOT a tuple
notTuple = ('Michael')
print(type(notTuple))


# Access the first item of a tuple at index 0
print(z[0])

print(z[-1])

color = ['red', 'blue', 'black']
print(tuple(color))

tuple_example = tuple('ABCDEFGHIJK')
print(tuple_example)

number1 = ('one', 'two', 'three',)
number2 = ('four', 'five', 'six')
number3 = (number1, number2)
#number3 = (number1 + number2)
print(number3)

data = ('one', 'two', 'three', 'four')
data += ('five',)
print(data)

print(data[0])


# Tuple Unpacking
# Tuples are useful for sequence unpacking.

x, y = ('2', '3')
print(f'{x} - {y}') 


# iterate tuple
#data1 = [('Diego', 'Herrera'), ('Jose', 'Perez'), ('Manuel', 'Reyes')]
data1 = (('Diego', 'Herrera'), ('Jose', 'Perez'), ('Manuel', 'Reyes'))
print(dir(data1))

for k, v in data1:
    print(f"{k} - {v}")

for x in data1:
    for y in x:
        print(f"{y}", end=" ")
    print()

# Tuple method


# Initialize a tuple
animals = ('lama', 'sheep', 'lama', 48)

# The index method returns the first index at which a value occurs.
print(animals.index('lama'))

# The count method returns the number of times a value occurs in a tuple.
print(animals.count('lama'))
