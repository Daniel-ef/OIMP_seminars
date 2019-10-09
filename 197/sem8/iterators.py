l = [1, 4, 2]
it = iter(l)  # iterator
print(it)
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())

print(sorted(it))


def myRange(n):
    i = 0
    while i < n:
        yield i
        i += 1


my_range = myRange(5)
print(list(my_range))

for i in myRange(3):
    print(i)




