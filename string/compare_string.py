string1 = 'hello world'
string2 = 'hello world'

# way of comparation two string
if string1 in string2:
    print(True)
    print(f'{string1} - it is equals to - {string2}')

if string1 == string2:
    print(True)
    print(f'{string1} - it is equals to - {string2}')

if string1 is string2:
    print(True)
    print(f'{string1} - it is equals to - {string2}')

one = 'oso'
two = 'oso'

if one == two[::-1]:
    print('it is equals')
else:
    print('it is different')

# iterating over string contents in reverse efficiently
for one in reversed(two):
    print(one, end=' ')