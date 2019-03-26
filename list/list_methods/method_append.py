colors = ['red', 'green', 'blue']
numbers = [1, 4, 7, 2, 3, 9, 5, 4, 9, 2, 3, 1, 8]

# appends an element to the end of the list.
colors.append('yellow')
print(colors)

# Only one element can be added to a list
#colors.append('violet', 'orange') 

# If you want to enter more than one item in a list, it is means of  tuple or list
colors.append(['orange', 'violet'])
print(colors)

# Also be can appending other string 
colors.append(numbers)
print(colors)

# With the + sign you can concatenate two strings
cadena_concatenada = colors + numbers
print(cadena_concatenada)
