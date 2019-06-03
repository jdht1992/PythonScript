fizz_list = []

for x in range(1, 20):
    if x % 15 == 0:
        fizz_list.append('fizzbuzz')
    elif x % 5 == 0:
        fizz_list.append('fizz')
    elif x % 3 == 0:
        fizz_list.append('buzz')
    else:
        fizz_list.append(x)

print(fizz_list)
