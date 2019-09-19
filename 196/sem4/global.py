def foo():
    global a
    a = 20
    print(a)

a = 30

foo()

print(a)