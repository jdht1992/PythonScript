colors = ['red', 'green' ,'blue', 'yellow' ,'orange', 'purple', 'black']

index = 0
for c in colors:
    print(f'{index} - {colors[index]}')
    index += 1

print('-------------')

for index, c in enumerate(colors):
    #print(f'[{index}] - [{c}]')
    print(f'{index} - {colors[index]}')


print('--------------')

for c in range(len(colors)):
    print(f'{c} - {colors[c]}')


names = ['Peter Parker', 'Clark kent', 'Wade wilson', 'Bruce Wayne']
heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']
universes = ['MV', 'DC', 'MV', 'DC']

for name, hero, universe in zip(names, heroes, universes):
    print(f'{name} is actually {hero} from {universe}')


for values in zip(names, heroes, universes):
    print(f'{values}')


# import time
# start = time.time()

# a = range(10000000)
# b = []
# for i in a:
#     b.append(i*2)

# end = time.time()
# print(end - start)