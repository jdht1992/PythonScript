#A prime number is one that is only divisible by 1 and itself
# with which only has 2 dividors

cont = 0
prime = []
no_prime = []
for i in range(100+1):#Dividend: is the amount we want to share
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

# cont = 0
# for i in range(1, 100+1):
#     for j in range(1, i+1):
#         if i % j == 0:
#             cont += 1
#     if cont == 2:
#         print(i)
#         cont=0
#     else:
#         cont = 0

# for x in range(1,1000):    
#     primo = True
#     for y in range(2, x):
#         if x % y == 0:            
#             primo = False
#             break
#     if primo: 
#         print(x)