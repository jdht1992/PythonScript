colors = ['red', 'green', 'blue', 'yellow', 'orange']
print(colors)
print(id(colors))

# #In the first case, the variables list1 and list2 refer to the same list stored in the computer's memory
colors2 = colors
print(colors2)
print(id(colors2))

#In the second case list1 and list2 make reference to different lists are stored in different places of the computer memory
colors3 = colors[:]

print(colors3)
print(id(colors3))

# The copy() method returns a copy of the specified list.
c = colors.copy()
print(c)
print(id(c))
