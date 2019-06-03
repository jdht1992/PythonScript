# # sort a dictionary by its values with the built-in sorted() function and a key argument
# d = {'apple': 10, 'orange':20, 'banana':5, 'rotten tomato':1} 
# print(sorted(d.items(), key=lambda x:x[1]))

# # Chained function call
# def product(a, b):
#     return a * b

# def add(a, b):
#     return a + b

# b = True 
# print((product if b else add)(5, 7))

# data = {"capable":7, "achievement":15, "membership":10}
# # print(sorted(data, key=lambda x:x[1]))
# # print(sorted(data))

# for key, value in sorted(data.items(), key=lambda item: item[1], reverse=True):
#     print(f"{key}: {value}")

l = ["hello", "HELP", "Helo"]
print(l)
# l.sort()
# print(l)
l.sort(key=str.lower)
print(l)
