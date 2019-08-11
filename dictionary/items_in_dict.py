dic = {
    'name': 'Juan Diego', 
    'last_name': 'Herrera', 
    'age': 26, 
    'greater': True, 
    'state': 'Jalisco', 
    'location': 'Zapopan'
}


# To print the value of an item in a dictionary is accessed through its key
print(dic['name'])

# you can access the elements of a dictionary by referring to its key name, in curlybrackets
dic['name'] = 'Diego'
print(dic)

# If the key is not found in the dictionary, the key and the values are added to the end of the dictionary
dic['nationality'] = 'Mexican'
print(dic)
