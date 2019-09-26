sqr = lambda x: x ** 2

# [](int x) { return x * x; }  c++
print((lambda x: x ** 2)(2))


# list comprehension
# squares of even natural number
print([i ** 2 for i in range(10) if i % 2])
