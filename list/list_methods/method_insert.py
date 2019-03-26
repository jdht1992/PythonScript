colors = ['red', 'green', 'blue']

# Necessary. A number that specifies in which position the value should be inserted
# Necessary. An element of any type (string, number, object, ect.)
#list.insert(pos, elment)

# Insert the specofied value at the specified position
colors.insert(0, 'orange')
print(colors)

# If you want to insert an item in the last position of a list
colors.insert(len(colors), 'violet')
print(colors)
