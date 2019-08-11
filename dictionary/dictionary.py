data1 = {'name': 'juan'}
data2 = {'apellido': 'herrera'}


for key, value in data2.items():
    data1[key] = value
print(data1)


powers = {**data1, **data2}
print(powers)
