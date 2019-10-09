import functools

binStrToInt = functools.partial(int, base=2)
binStrToIntLambda = lambda x: int(x, base=2)

print(binStrToInt('1001'))
print(binStrToIntLambda('1001'))

my_sum = functools.reduce(lambda sum, x: sum + x, [1, 2, 3])
print(my_sum)


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


print(functools.reduce(gcd, [40, 25, 15]))

