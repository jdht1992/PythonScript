class Dog:
    #Class attribute
    species = 'mammal'

    #Initializer/Intance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

#Instantiate the Dog objects
philo = Dog("Philo",5)
mikey = Dog("Mikey",6)

#Access the instance attributes
print(f'{philo.name} is {philo.age} and {mikey.name} is {mikey.age}')

if philo.species == 'mammal':
    print(f'{philo.name} is a {philo.species}')
