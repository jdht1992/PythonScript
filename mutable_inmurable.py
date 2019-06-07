my_list = [1, 2, 3]
print(my_list)
print(id(my_list))

my_list.append(4)
print(my_list)
print(id(my_list))

my_list[0] = 0
print(my_list)
print(id(my_list))


tuple1 = (4, 5, 6, 1)
print(id(tuple1))

tuple1 += (9,)
print(id(tuple1))

