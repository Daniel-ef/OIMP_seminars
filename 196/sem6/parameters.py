def print_(*args, sep=' ', end='\n'):
    # print(args)
    for arg in args:
        print(arg, end=sep)
    print(end=end)


print_(1, 2, 3, 4, sep=', ', end='!!')
print()
print(1, 2, 3, 4, sep=', ', end='!!')
