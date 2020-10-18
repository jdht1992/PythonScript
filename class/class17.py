class Person:
    # the self parameter is a reference to the class itself, and is used to access variable that belongs to the class
    def __init__(mysillyobjects, name, age):
        mysillyobjects.name = name
        mysillyobjects.age = age
#it does not have to be named self, you can all it wherever you like, but it has to be the first parameter of any function in the class
    def my_function(abc):
        print(f'My name is: {abc.name} and my age is : {abc.age}')

person = Person('Juan', 26)

person.my_function()



