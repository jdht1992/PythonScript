colors = ['red', 'green', 'blue']
colors2 = colors

# With the type word we know what kind of object it is
print(type(colors))

# with len we know the length of an element
print(len(colors))

#To convert to a tuple we use the list property
print(list((9, 8, 7, 6, 5, 4)))

#To convert a number range into a list
lista_numeros = list(range(11))
print(lista_numeros)

#dir gives us information about what methods we can use in a list
print(dir(lista_numeros))

#To find out if an item exists within a list
print("red" in colors)

print(colors2 is colors)

print(colors2 == colors)
