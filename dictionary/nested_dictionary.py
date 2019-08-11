dic = {
    'diego': {
        'name': 'Juan Diego', 
        'last_name': 'Herrera', 
        'age': 26, 
        'greater': True, 
        'state': 'Jalisco', 
        'location': 'Zapopan'
        },

    'arturo': {
        'name':'Arturo',
        'last_name':'Trinidad',
        'age':29,
        'gender':'Masculino',
        'address' : {
            'house1':'Los arboles verdes',
            'house2':'Los lirios'
        }
    }
}

for k in dic.keys():
    if 'arturo' in k:
        if 'address' in dic['arturo']:
            print('Si esta')
            print(dic['arturo']['address']['house1'])