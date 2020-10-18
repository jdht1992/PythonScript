class Person:
# Objects can also contain methods. Methods in objects are functions that belongs to the objects 
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def my_function(self):
        print(f'mi nombre es: {self.name}')
# the self parameter is a reference to the class instance itself, and is used to access variables that belongs to the class         
person = Person('Juan',26)

person.my_function()
