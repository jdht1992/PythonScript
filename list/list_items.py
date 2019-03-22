# The list is a collection that is ordered and changeable. It allows to duplicate members.
demo_list = [1, 'hello', 1.43, True, [1, 2, 3, 'Another'], 2, True, ['juan', 'pedro', 'luis']]
colors = ['red', 'green', 'blue']
numbers = [1, 4, 7, 2, 3, 9, 5, 4, 9, 2, 3, 1, 8]

# Print items from a list
print(demo_list)

# All items in the list are printed
print(numbers[:])

# Access an item in a specific list
print(numbers[0])

# print two items from the list
print(numbers[0], numbers[-1])

# Access items within a sublist within a list
print(demo_list[4][1])

# From a list you can extract sublists, using the notation nameoflist [start: limit]
print(numbers[0:4])

# prints from the first list item to the end [: 5]
print(numbers[:5])

# Print from item 1 to the end of the list
print(numbers[0:])
print(numbers[-6:])

# reverses items in a list
print(numbers[::-1])

# Print the item in the first position until the last in a sequence of two
print(numbers[0:12:2])

#Print the last item in the list
print(numbers[-1])
print(numbers[-1:])

# Changes the value of a list item
colors[0] = 'purple'
print(colors)

#the keyword removes the specified index
del numbers[0]

del numbers[1:6]
print(numbers)
