# The get() method returns the value of the item with the specified key.

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1994
}

model = car.get("model")
print(model)

# if value does not exist, return the specified key
color = car.get("color", "Not exist")
print(color)
