palabra = ['perro', 'gato', 'pavo', 'venado']

for p in palabra[:]:  # hace una copia por rebanada de toda la lista
    if len(p) >= 6:  # si se hace esto for p in palabra se crea un buchle infinito
        palabra.insert(0, p)

print(f'{palabra}')
