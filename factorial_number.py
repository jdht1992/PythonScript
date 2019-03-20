# print(factorial(5))
#factorial multiply all positive integers between that number and 1.

def factorial(n):
    fac = 1
    for y in range(1, n+1):
        fac = fac * y
    return fac

fac = 6
print(f'The factorial of {fac} is {factorial(fac)}')
