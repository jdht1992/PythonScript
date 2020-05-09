colors = ['green', 'blue', 'yellow', 'black', 'red', 'golden']

index = 0
for i in colors:
    print (f"{index} - {colors[index]}")
    index +=1
print('-------------')

for index, c in enumerate(colors):
    print (f"{index} - {c}")
print('-------------')

for c in range(len(colors)):
    print (f"{c} - {colors[c]}")
