#A prime number is one that is only divisible by 1 and itself
# with which only has 2 dividors

cont = 0
prime = []
no_prime = []
for i in range(10+1):#Dividend: is the amount we want to share
    for j in range(1, i+1):# Divisor: is the number by which we will divide the amount indicated in the dividend.
        if i % j == 0:# Rest: is the number that is left over from the division
            cont += 1# cont = cont + 1
    if cont == 2:
        prime.append(i)
        cont=0
    else:
        no_prime.append(i)
        cont = 0
            
print(f'Prime numbers: {prime}')
print(f'No prime numbers: {no_prime}')