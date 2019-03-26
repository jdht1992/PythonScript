# pythonic way of value swapping
print('hello')

a, b = 5, 10
print(a,b)
a, b = b, a
print(a, b)

# Create a single string from all the elements in list
a = ["Python", "is", "awesome"]
print(" ".join(a))


a = 'abcdefghij'
print(a[::-1])

# iterating over string contents in reverse efficiently
for char in reversed(a):
    print(char, end=' ')

# reversing an integer through type conversion and slicing 
num = 123456789 
print(int(str(num)[::-1]))

original = [['a', 'b'], ['c', 'd'], ['e', 'f']]
transposed = zip(*original) 
print(list(transposed))

# Chained function call
def product(a, b):
    return a * b

def add(a, b):
    return a + b

b = False 
print((product if b else add)(5, 7))

# sort a dictionary by its values with the built-in sorted() function and a key argument
d = {'apple': 10, 'orange':20, 'banana':5, 'rotten tomato':1} 
print(sorted(d.items(), key=lambda x:x[1]))

# else gets called when for loop does not reach break statment
a = [1, 2, 3, 4, 5]

for el in a: 
    if el == 0: 
        break 
else: 
    print('did not break out of for loop')
