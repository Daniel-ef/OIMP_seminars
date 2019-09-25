def foo():
    print(1)


a = (1, 5.4, 'str', foo)
a[3]()
print(a[0:2])
print(a[-2::-1])

a = 2
b = 1
(a, b) = (b, a)  # swap
a, b = 2, 1

print(a, b)
a, b = (a, b) if a < b else (b, a)
# equal
if a > b:
    a, b = b, a

print(a, b)

