r = 100
suma = 0
dividendos = [3, 5]
rango = 10
multiplos = []

for n in range(1, rango):
    if (n % dividendos[0] == 0) or (n % dividendos[1] == 0):
        multiplos.append(n)
        suma += n
print(f'Los multiplos son: {multiplos}')
print(f'la suma de los numeros es: {suma}')
suma = 0
