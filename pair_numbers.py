# An even number is an integer that is divisible by two

pair = []
no_pair = []
for num in range(1, 10):
    if num % 2 == 0:
        pair.append(num)
    else: #elif num % 2 != 0:
        no_pair.append(num)

print(f'Numbers pair {pair}')
print(f'No Numbers pair {no_pair}')

