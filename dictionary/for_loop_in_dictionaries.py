dictionary = {
    'name':'juan',
    'last name':'herrera',
    'age':26,
    'state':'jalisco',
    'location':'zapopan',
    'merried': False,
    'greater': True
}


# print the keys of dictionary
for k in dictionary:
    print(k)

for k in dictionary.keys():
    print(k)

# print the values of dictionary
for v in dictionary:
    print(dictionary[v])

for v in dictionary.values():
    print(v)

# print the keys and values of dictionary
for x in dictionary.items():
    print(x)

for k, v in dictionary.items():
    print(f"{k} - {v}")
