# A dictionary is a collection that is not ordered, that can be changed and indexed.
# # In Python, dictionaries are written with brackets, and they have keys and values.

dictionary = {
    'name':'juan',
    'last name':'herrera',
    'age':26,
    'state':'jalisco',
    'location':'zapopan',
    'merried': False,
    'greater': True
}

# If you want to know what type of object is dictionary
print(type(dictionary))

# To determine how many elements (key-value pairs) a dictionary has
print(len(dictionary))

# To know in what memory space is the dictionary
print(id(dictionary))

# Is you need to know what methods you can use in a dictionary
print(dir(dictionary))
