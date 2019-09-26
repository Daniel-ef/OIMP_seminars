
def sqr_func(x):
    return x ** 2


# equal
# [](int x) { return x * x; } c++
sqr_l = lambda x: x ** 2
print(sqr_l(5))

# list comprehension
# squares of even natural numbers
print([el ** 2 for el in range(10) if el % 2 == 0])
