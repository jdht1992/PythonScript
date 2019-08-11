data = {"capable":7, "achievment":15, "membership":10}
print(data)


print(sorted(data))


print(sorted(data, key=lambda x:x[3]))


for k, v in sorted(data.items(), key=lambda item: item[1], reverse=True):
    print(f"{k} - {v}")


# sort a dictionary by its values with the built-in sorted() function and a key argument
print(sorted(data.items(), key=lambda x:x[1]))

animals = [
        {'type': 'penguin', 'name': 'Stephanie', 'age': 8},
        {'type': 'elephant', 'name': 'Devon', 'age': 3},
        {'type': 'puma', 'name': 'Moe', 'age': 5},
        ]

print(sorted(animals, key=lambda animal: animal['age']))
