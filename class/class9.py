class Dog:
    #Class Attribute
    species = 'mammal'
    #Initializer/Instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
#Instantiate the dog object
jake = Dog("Jake", 7)
doug = Dog("Doug", 3)
william = Dog("William", 6)

#Determine the oldest dog 
def get_biggest_number(*args):
    return max(args)

print(f"The oldest dog is {get_biggest_number(jake.age, doug.age, william.age)} years old")
