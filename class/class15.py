class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def my_function(self):
        print(f'My name is {self.name} - my age is {self.age}')

person = Person('Juan',26)

person.my_function()
person.age = 30
print(f'My new age is {person.age}')

