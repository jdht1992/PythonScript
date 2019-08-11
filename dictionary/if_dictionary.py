data = {
    'name':'juan',
    'last name':'herrera',
    'age':26,
    'state':'jalisco',
    'location':'zapopan',
    'merried': False,
    'greater': True
}

for d in data:
    if 'age' in d:
        print("exist")
        break
    else:
        print("no exixt")