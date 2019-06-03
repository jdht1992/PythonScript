# # Assingning function to variable
# def append_somehting(name):
#     return "Appending to {}".format(name)

# #Assiging function to a variable 
# append_var = append_somehting

# print(append_somehting("Diego"))

# #Output Appending to "Diego"

# # calling one function as a parameter of another function 
# def append_something(name):
#     return "Appending to {}".format(name)

# def calling_function(func):
#     name = "Diego"
#     return func(name)

# print(calling_function(append_somehting))
# #Output: Appending to Diego


# # def out_func():
# #     def inner_func():
# #         return "This function will be return by out_func"
# #     return inner_func

# # out = out_func()
# # print(out())

# def out_func(name):
#     def inner_func():
#         return f"We are using the name {name} inside inner_func"
#     return inner_func

# out = out_func("Diego")
# print(out())


# #Decorating function using another function
# def get_txt(name):
#     return f"My name is {name}"

# def lets_decorate(func):
#     def func_wrapper(name):
#         return f"Hi there {name}. How are you?"
#     return func_wrapper

# my_outout = lets_decorate(get_txt)
# print(my_outout("Diego"))

# Creating and using decoratirs in python using syntactic sugar
# def lets_decorate(func):
#     def func_wrapper(name):
#         return f"Hi there {name}. How are you"
#     return func_wrapper

# @lets_decorate
# def get_txt(name):
#     return f"My name is {name}"

# print(get_txt("Diego"))

# # Using decorators on method 
# def lets_decorate(func):
#     def func_wrapper(self):
#         print("Something before the method execution")
#         print(func(self))#         print(func(*args, **kwargs))
#         print("Something after the method execution")
#     return func_wrapper

# class Example:
#     def __init__(self):
#         self.firststr = "first"
#         self.secondstr = "second"

#     @lets_decorate
#     def concat_string(self):
#         return f"Full string is {self.firststr} {self.secondstr}"

# out = Example()
# out.concat_string()

