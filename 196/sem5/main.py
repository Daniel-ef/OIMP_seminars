#  tuples


def foo(n):
    print(n)


a = (1, 'str', 4.5, 'abc', foo)
a[4](5)

print(a[1:4:2])

a = 2
b = 1
#  swap example
if a > b:
    (b, a) = (a, b)
    b, a = a, b

(a, b) = (a, b) if a > b else (b, a)


def foo2():
    return (1, 2)

# range


print(tuple(range(5)))
print(tuple(range(1, 5)))
print(tuple(range(1, 5, 2)))


for i in tuple(range(5)):  # range(5)
    print(i)
print()

# don't do it
i = 0
for el in (1, 5.4, 'abc'):
    print(el)
    i += 1
print()

for i, el in enumerate((1, 5.4, 'abc')):
    print(i, el)


# list
a = [1, 2, 5.4, 'abc']
a.append('str')

for el in a:
    print(el, end=' ')
print('\n')


print(a[0])
a[0] = 2
print(a[0])
a.extend([5, 6])  # add another list to the end
a.pop(5)  # delete by index
a.clear()

b = a  # not a copy

print('##')
b.clear()
print(len(a))
a.copy()  # explicit copy


#
a = [1, 2, 5.4, 'abc']
a[1:5:2]
print(a[::-1])  # reversed list
print(reversed(a))  # iterator
print(list(reversed(a)))  # reversed list

# split, join, map
# split
print('Split join map\n')
print('Hello        world'.split())
splitted_list = 'Hello, world'.split(', ')

# join
print(splitted_list)
print(', '.join(splitted_list))

# map(func, list)
print(list(map(int, [5.4, 1.2, 3.4])))

map_a = map(int, range(10000))
print(type(a), a)
print()
print(map_a.__next__())  # next element
print(map_a.__next__())  # next element again
print(map_a.__next__())  # and again
print(map_a.__next__())  # and again

list(map_a)  # generating the whole list in memory

list_of_int = list(map(int, input()))





