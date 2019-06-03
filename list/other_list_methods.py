numbers = [1, 4, 7, 2, 3, 9, 5, 4, 9, 2, 3, 1, 8, ]

# Add the items in the list
print(sum(numbers))

# Find the largest number in a list
print(max(numbers))

# Find the smallest number in a list
print(min(numbers))

# Remove duplicates from a list
print(list(set(numbers)))

# Find The Most Frequent Value In A List.
print(max(set(numbers), key = numbers.count))
