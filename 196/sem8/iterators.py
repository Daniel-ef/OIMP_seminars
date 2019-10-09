l = [5, 1, 2]

it = iter(l)

print(range(3))
print(iter(range(3)))

it = iter(range(3))
print('Range iterator')

print(it.__next__())
print(it.__next__())
print(next(it))


class MyRangeClass:
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __next__(self):
        i = self.i
        self.i += 1
        return i

print('MyRangeClass iterator')
my_range = MyRangeClass(5)
print(next(my_range))
print(next(my_range))
print(next(my_range))
print(next(my_range))


def myRangeGenerator(n):
    i = 0
    while i < n:
        yield i
        i += 1

print('myRangeGenerator iterator')
my_range = myRangeGenerator(5)

for i in my_range:
    print(i)

# iterators: range, map

print()
print(map(int, ['1', '2']))

print(sorted(range(5)))
print(sum(range(5)))
