# float

print(0.1 + .2 == .3)  # False
print(2. + 2. == 4.)  # True

a = .000002
b = .000002
eps = 0.0000001

if abs(a - b) < eps:  # not a == b
    pass

print('{0:.25f} == 0.2'.format(a))

print("0.2 = {0:.25f} 0.3={1:.30f}".format(0.2, 0.3))


import math

print(math.floor(2.5), math.ceil(2.5),
      math.trunc(2.5), int(2.5))

# string
print('\n\nStrings \n\n')
a = 'Hello, world!'

print(len(a))  # length

# interval [a, b)
print(a[1:])
print(a[0:5])
print(a[:5])

print(a[:-1])

print('ababababa'[1:-1:2])
print('ababababa'[::2])

print(a[10:5])  # '' empty string
print(a)  # strings are immutable (неизменяемые)

a = 'Hello, world!'
print(a.find('world'))
print(a.find('world', 8))  #  begin find from 8 index

b = 'hello hello'
print(b.find('hello'), b.rfind('hello'))

print(a.replace('Hello', ''))  # ', world!'
b = a.replace('Hello', '')
print(b.count('hello'))  # 2


# Pi


