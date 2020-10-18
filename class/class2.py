class Person:

    piel = 'Moreno'
    
    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def datos(self):
        print(f'{self.name} - {self.age} - {self.piel}')

person = Person('Juan',16)

print(person.piel)
print(person.name)
print(person.age)
person.datos()

