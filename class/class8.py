class Pets:

    dogs = []

    def __init__(self, dogs):
        self.dogs = dogs


# Parent class
class Dog:

    # Class attribute
    species = 'mammal'

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_hungry = True

    # Instance method
    def description(self):
        return self.name, self.age

    # Instance method
    def speak(self, sound):
        return f"{self.name} says {self.sound}"

    # Instance method
    def eat(self):
        self.is_hungry = False


# Child class (inherits from Dog class)
class RussellTerrier(Dog):
    def run(self, speed):
        return f"{self.name} runs {self.speed}" 


# Child class (inherits from Dog class)
class Bulldog(Dog):
    def run(self, speed):
        return f"{self.name} runs {self.speed}" 

# Create instances of dogs
my_dogs = [
    Bulldog("Tom", 6), 
    RussellTerrier("Fletcher", 7), 
    Dog("Larry", 9)
]

# Instantiate the Pets class
my_pets = Pets(my_dogs)

# Output
print(f"I have {len(my_pets.dogs)} dogs.")
for dog in my_pets.dogs:
    dog.eat()
    print(f"{dog.name} is {dog.age}.")

print(f"And they're all {dog.species}s, of course.")

are_my_dogs_hungry = False
for dog in my_pets.dogs:
    if dog.is_hungry:
        are_my_dogs_hungry = True

if are_my_dogs_hungry:
    print("My dogs are hungry.")
else:
    print("My dogs are not hungry.")