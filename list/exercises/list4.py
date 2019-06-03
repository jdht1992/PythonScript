numbers = [1, 2, 2, 5, 3, 8, 7, 9, 1]

mayor = numbers[0]

for num in numbers:
    if num > mayor:
        mayor = num

print(mayor)


def bigger_number(list_numers):
    bigger = list_numers[0]
    for num in list_numers:
        if num > bigger:
            bigger = num
    print(mayor)
    

list_numers = [1, 2, 2, 5, 3, 8, 7, 9, 1]
bigger_number(list_numers)


class Number:
    def __init__(self, list_numers):
        self.list_n = list_numers

    def bigger_number(self):
        mayor = self.list_n[0]
        for n in self.list_n:
            if n > mayor:
                mayor=n
        return mayor

numbers=[1, 2, 2, 5, 3, 8, 7, 9, 1]        
number = Number(numbers)

print(number.bigger_number())


print(max(list_numers))
