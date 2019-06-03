def lugares(array, target):
    for x2, x in enumerate(array):
        for y2, y in enumerate(array):
            if x2 and y2 in l:
                break
            else:
                num = x + y
                if num == target:
                    l.append(x2)
                    l.append(y2)
        


# array1 = [2, 7, 11, 15]
array1 = [1, 7, 11, 8, 9, 10]
lugares(array1, 17)
print(l)