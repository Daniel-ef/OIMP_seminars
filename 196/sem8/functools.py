import functools
import itertools

binToStr = functools.partial(int, base=2)
binToStrLambda = lambda x: int(x, base=2)

print(binToStr('1001'))
print(binToStrLambda('1001'))


print(functools.reduce(lambda sum, x: sum + x, [5, 3, 4]))


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# [A, B, C] -> f(f(A, B), C)
print(functools.reduce(gcd, [40, 16, 8, 18]))

# [A, B, C] -> A, f(A, B), f(f(A, B), C)
print(*itertools.accumulate([40, 16, 8, 18], gcd))
