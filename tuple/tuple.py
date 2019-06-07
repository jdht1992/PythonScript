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
