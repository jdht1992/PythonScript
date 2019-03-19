string = 'hello world'

# In Python the strings are inmutables, that is, once they have been initialized their content can not be modified 
# # cadena[0]='j' this can't be

# # Indexes are used to get individual characters
print(string[0])

# Note that -0 is the same as 0, negative indexes start from -1.
print(string[-2])

#Substring. Get the characters from position 0 to position 5 (not included):
print(string[0:4])

# Start from subindice 0 al 3
print(string[:3])

# #Part of subindice 1 and up
print(string[3:])

# reverse a string   
print(string[::-1])