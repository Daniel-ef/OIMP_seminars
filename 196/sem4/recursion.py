def rprint():
    s = input()
    if s == '0':
        return
    rprint()
    print(s)


#  rprint()

def dummy_func():
    dummy_func()


dummy_func()  # max 996 times
