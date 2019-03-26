# La lista es una colección que es ordenada y cambiable. Permite duplicar miembros.
demo_list = [1, 'hello', 1.43, True, [1, 2, 3], 2, ['juan', 'pedro', 'luis']]
colors = ['red', 'green', 'blue', 'yellow', 'orange', 'black', 'white', 'violet', 'grey']
numbers = [1, 4, 7, 2, 3, 9, 5, 4, 9, 2, 3, 1, 8]
print()

# If a value is not indicated, delete the last position
colors.pop()
print(colors)

# Removes the element at the specified position
colors.pop(0)
print(colors)
