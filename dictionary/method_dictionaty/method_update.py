car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1994
}

print(car)

car.update({"year": 1990})
print(car)

# The update() method insert the specifed items to the dictionary.
car.update({"color": "red"})
print(car)


# The specified items can be dictionary, or an iterable object.
car.update({"year": 1989, "color": "blue"})
print(car)
