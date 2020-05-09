def sum(a, b):
    return a + b

print(sum(5,5))

print((lambda a, b: a + b)(6,6))
sum = (lambda a, b: a + b)(6,6)
print(sum) 

Because a lambda function is an expression, it can be named
sum_num = lambda a: a * 4
print(sum_num(4))

The example above returns the string 'odd' when the lambda argument is odd, and 'even' when the argument is even.
print((lambda x:(x % 2 and 'odd' or 'even'))(4))


def exercise(num):
    min = (15 / 100) * num
    return round(min, 2)
print(exercise(550))

p2 = (lambda num: (15 / 100) * num)(550)
print(f"con lambda2 {p2}")


example = (lambda *args: [p for p in args])(1, 2, 3)
example = (lambda *args: [x for x in args if x % 2 == 0])(1, 2, 3)
example = (lambda *args: args[0] if args[0] else args[1] if args[1] else args[2])(0, 1, 0)
print(example)

operation = {"Sale":0, "Rent":0, "Transfer":1}
op = (lambda x:'mxn' if x['Sale'] else ('usd' if x['Rent'] else ''))(operation).upper()
print(op)
