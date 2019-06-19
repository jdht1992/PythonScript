# Tuples are an ordered sequences of items, just like lists. The main difference between 
# tuples and lists is that tuples cannot be changed (immutable) unlike lists which can (mutable).

my_list = [1, 2, 3]
print(my_list)
print(id(my_list))

my_list.append(4)
print(my_list)
print(id(my_list))

my_list[0] = 0
print(my_list)
print(id(my_list))


# Tuples are immutable which means that after initializing a tuple, 
# it is impossible to update individual items in a tuple.

t = (3, 7, 4, 2)

# this is impossible
# t[0] = 's'

# Initialize tuple
tup1 = ('Python', 'SQL')

# Initialize another Tuple
tup2 = ('R',)

# Create new tuple based on existing tuples
new_tuple = tup1 + tup2
print(new_tuple)

tuple1 = (4, 5, 6, 1)
print(tuple1)
print(id(tuple1))

# changed its id
tuple1 += (9,)
print(tuple1)
print(id(tuple1))
