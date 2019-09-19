# len = len("abba")  # dont do it
# len("hola") # exception


def sum_diff(a: int, b: int):
    return a + b, a - b


a = 10
b = 100

sum_a, diff_b = sum_diff(a, b)
# sum_diff(a, 'abc')  # wrong type

print(sum_a, diff_b)


def is_even(a):
    return a % 2 == 0  # return True or False


print(is_even(2), is_even(3))
