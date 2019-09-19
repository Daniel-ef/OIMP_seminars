import math

print(.1 + .2 == 0.3)
print(2. + 2. == 4.)

print('{} + {} = {}'.format('hola', 2, 4))
print(2, '+', 2, '=', 4, sep='')

print('{0:.25f} == 0.2'.format(0.2))
print('{0:.25f}'.format(5.17e-17))

print("0.2 = {0:.25f} 0.3={1:.30f}".format(0.2, 0.3))

print("{0:} {1:}".format("mama", "myla"))  # {argument number:.signs after dot`f`}

#  mama myla
print("{1:} {0:} {1:}".format("mama", "myla"))
#  myla mama myla


print(math.floor(2.5), math.ceil(2.5),
      int(2.6), math.trunc(2.6), round(2.5))

#  string

print('\nStrings\n')

a = 'abc'
b = 'abc'
'abc' + 'd'

a = 'Hello, world!'
print(a)
print(len(a))

print(a[0])
print(a[1:])
print(a[1:3])
print(a[:3])  # == a[0:3]

print(a[1:-1])
print('abababababa'[1:-1:2])
print('abababababa'[::2])

# find, rfind

print(a.find(','))
print(a.find('$'))

b = 'hello hello'
print(b.find('hello'))
print(b.rfind('hello'))

# replace, count

a = 'Hello, world!'
b = 'hello hello'
print(a.replace('Hello', ''))
print(b.replace('hello', '', 1))  # replace(old, new, count)

print(b.count('hello'))

