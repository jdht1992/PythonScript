car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1994
}

print(car)

# The setdefault method returns the value of the item with the specified key
model = car.setdefault("model", "Bronco")
print(model)

# if the ket does not exist, insert the key, with the specified value
# If the key does not exist, this value becomes the key's value
color = car.setdefault("color", "Golden")
print(color)

print(car)
