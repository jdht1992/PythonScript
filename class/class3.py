class Point:
#“The self argument to a method is a reference to the object that the method is being invoked on. We can access attributes and methods of that object as if it were any another object. This is exactly what we do inside the reset method when we set the x and y attributes of the self object.”
    def reset(self):
        self.y = 1
        self.x = 0

p = Point()
p.reset()
print(p.x, p.y)


#Sin embargo, el método realmente es solo una función que está en una clase. En lugar de llamar al 
#método en el objeto, podríamos invocar la función en la clase, pasando nuestro objeto explícitamente 
#como el argumento propio:

#Point.reset(p)
#print(p.x, p.y)