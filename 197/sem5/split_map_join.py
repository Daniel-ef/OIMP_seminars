a = 'Hello        world'.split()  # list of str
print(a)

hello, world, _ = 'Hello, world, omg'.split(', ')
print(hello, world)

# map(function, list)
# map apply function to each element of list
# and return new list

# int(4.3) = 4
print(list(map(int, [4.5, 3.2, 1.1])))

# s = input().split()
# print(s)
# print(map(int, s))
s = list(map(int, input().split()))


print('\njoin')
print(', '.join(['1', '2']))
print(', '.join(map(str, [1, 2])))
