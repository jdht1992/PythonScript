class Car:
    # when you declare a variable outside of a method, it’s treated as a class variable.
    wheels = 0
# By prefixing the variable names with self, you tell Python these are attributes. 
# Each instance of the class will have a copy.
    def __init__(self, color, model, year):
        self.color = color
        self.model = model
        self.year = year
