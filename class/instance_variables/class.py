import car

my_car = car.Car("yellow", "beetle", 1967)
print(f"My car is {my_car.color}")

# You can also create instance variables outside of .__init__(), 
# but it’s not a best practice as their scope is often confusing.

# my_car.wheels = 5
# print(f"Wheels: {my_car.wheels}")

# Instead of referring to it using an object, you refer to it using the class name:
print(f"It has {car.Car.wheels} wheels")


print(f"It has {my_car.wheels} wheels")
