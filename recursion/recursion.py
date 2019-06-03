import random
def mystery(array):
    value = random.choice(array)
    l = []
    r = []
    c = []
    for i in array:
        if i < value:
            l.append(i)
        elif i > value:
            r.append(i)
        else:
            c.append(i)
    if len(l) >1:
        l = mystery(l)
    if len(r) >1:
        r = mystery(r)
    return l + c + r

array = [1, 2, 3, 4, 5, 6, 7]
mystery(array)