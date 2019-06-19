my_list = ['red', 'blue', 'green']
# Get the last item with brute force using len
last_item1 = my_list[len(my_list) - 1]
print(last_item1)

# Remove the last item from the list using pop
last_item2 = my_list.pop() 
print(last_item2)

# Get the last item using negative indices *preferred method*
last_item3 = my_list[-1]
print(last_item3)

# Get the last item using iterable unpacking
*_, last_item4 = my_list
print(last_item4)
