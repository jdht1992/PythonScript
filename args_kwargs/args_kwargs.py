"""
Understanding *args
In Python, the single-asterisk form of *args can be used as a parameter 
to send a non-keyworded variable-length argument list to functions. It 
is worth noting that the asterisk (*) is the important element here, as the 
word args is the established conventional idiom, though it is not enforced by the language.
"""
def test_var_args(*args):
    for arg in args:
        print("another arg: ", arg)

test_var_args(1,"two",3,"four",5,"six")
print("----------------------------------")

def multiply(*args):
    z=1
    for num in args:
        z *= num
    print(f"El resultado es:{z}")
    
multiply(3,5,6,10)
print("----------------------------------")

def adder(*num):
    sum = 0
    for n in num:
        sum = sum + n
    print("sum: ",sum)

adder(1,2,3,4,5)
print("----------------------------------")


"""
The double asterisk form of **kwargs is used to pass a keyworded, variable-length 
argument dictionary to a function. Again, the two asterisks (**) are the important 
element here, as the word kwargs is conventionally used, though not enforced by the language.
"""

def print_kwagrs(**kwargs):
    print(kwargs)

print_kwagrs(kwargs_1="Shark",kwagrs_2=4.5,kwargs_3=True)

print("----------------------------------")

def print_kwagrs2(**kwargs):
    for key, value in kwargs.items():
        #print(f"La clave: {key} - Valor: {value}")
        print(f"{key}:{value}")

print_kwagrs2(my_name="Diego",last_name="Herrera")
print("----------------------------------")

def intro(**data):
    print("\nData type of argument:",type(data))

    for key, value in data.items():
        print(f"{key} is {value}")

intro(Firstname="Diego", Lastname="Herrera", Age=26, Phone=123456789)
intro(Firstname="Juan", Lastname="Trinidad", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)
