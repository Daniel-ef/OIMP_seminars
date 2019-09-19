def rprint():
    s = input()
    if s == '0':
        return
    rprint()
    print(s)


# rprint()


def factorial(n):
    if n > 1:
        n = n * factorial(n - 1)
    return n


def factorial2(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


def damn_function():
    damn_function()  # max 996 times

