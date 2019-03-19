cadena = str(input('Ingrese una cadena: '))

total = 0
x = 0

while x < len(cadena):
    if cadena[x] == " ":
        total = total + 1
    x += 1

print(f'El total de espacios es: {total}')

print(cadena)
