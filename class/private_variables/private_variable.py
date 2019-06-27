# Python doesn’t have the same notion of private or protected data that Java does. 
# Everything in Python is public.

# Python has a notion of a non-public instance variable. 
# Any variable which starts with an underscore character is defined to be non-public.

import car
my_car = car.Car("yellow", "Beetle", "1969")
print(f"It was built in {my_car.year}")

my_car.year = 1966
print(f"It was built in {my_car.year}")

print(f"It has {my_car._cupholders} cupholders.")
# You can access the ._cupholders variable directly:

