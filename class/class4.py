class Person: 
#all classes have a function called __init__(), which is always executed when the class is being initiated

    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person('Juan',16)

print(person.name)
print(person.age)


class Point: 
    def __init__(self, x, y): 
        self.move(x, y) 
 
    def move(self, x, y): 
        self.x = x 
        self.y = y 
 
    def reset(self): 
        self.move(0, 0) 
 
# Constructing a Point 
point = Point(3, 5) 
print(point.x, point.y)
