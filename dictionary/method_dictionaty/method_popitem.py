car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1994
}

print(car)

# Remove the last item from the dictionary
year = car.popitem()
print(year)

# return value as a tuple
a, b, = year
print(a)
print(b)

print(car)
