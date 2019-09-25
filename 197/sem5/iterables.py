# iterable object

iter_range = range(500000000).__iter__()  # iterable object
print(iter_range.__next__())
print(iter_range.__next__())
print(iter_range.__next__())
print(iter_range.__next__())
print(iter_range.__next__())

print(range(500000000).__sizeof__())  # 48 bytes
print(list(range(500000000)).__sizeof__())  # 4 GB

