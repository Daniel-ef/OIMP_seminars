a = [1, 2, 5.4, 'abc']
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

list_of_str = input().split()
print(list_of_str)
list_of_int = list(map(int, list_of_str))
print(list_of_int)
print(' '.join(map(str, list_of_int)))
