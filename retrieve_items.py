my_values = {'red': ['5'], 'blue': ['0'], 'green': ['']}

print('Red:     ', my_values.get('red'))
print('Green:   ', my_values.get('green'))
print('Opacity: ', my_values.get('opacity'))

# It’d be nice if a default value of 0 were assigned when a parameter isn’t supplied or is blank.
red = my_values.get('red', [''])[0] or 0
green = my_values.get('green', [''])[0] or 0
opacity = my_values.get('opacity', [''])[0] or 0

print(f'Red:     {red!r}')
print(f'Green:   {green!r}')
print(f'Opacity: {opacity!r}')

# For example, if you know that a tuple is a pair, instead of using indexes to access its values, you can assign it to a tuple of two variable names:
pair = ('Chocolate', 'Peanut butter')
print(pair[0])
print(pair[1])

first, second = pair
print(first, second)


fresh_fruit = {
    'apple': 10,
    'banana': 8,
    'lemon': 5,
}

if fresh_fruit.get('lemon', 0):
    print("Yes")
else:
    print("No")

count = fresh_fruit.get('lemon', 0)
if count:
    print("Yes")
else:
    print("No")

if count := fresh_fruit.get('lemon', 0):
    print("Yes")
else:
    print("No")

def make_cider(count):
    pass
count = fresh_fruit.get('apple', 0)
if count >= 4:
    make_cider(count)
else:
    out_of_stock()


if (count := fresh_fruit.get('apple', 0)) >= 4:
    make_cider(count)
else:
    out_of_stock()