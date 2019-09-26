def print_(*args, end=' '):
    # print(args)
    for arg in args:
        print(arg, end=end)
    print()


print_(1, 2, 3, 4, 5, end=', ')


def sum_(x, *args):
    result = 0
    for arg in args:
        result += arg * x
    return result


print(sum_(2, 1, 2, 3, 4, 5))
