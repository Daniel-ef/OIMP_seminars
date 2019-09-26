a = [5, 1, 3, 4]
a.sort()
print(a)

a = [5, 1, 3, 4]
print(sorted(a))

# tuples
print((3, 7) < (4, 3))
print((4, 7) < (4, 3))
print((4, 3) < (4, 3, 1))
print((4, 3, 1, 4) < (4, 3, 1))

# exception
print((4, 'str') < (5, 4))
# no exception, because of lazy comparation
print((4, 'str') < (5, 4))

# sort tuples

# age, name
a = [
    (23, 'Anton'),
    (20, 'Ivan'),
    (30, 'Alex'),
    (18, 'Fedor')
]


def key_1(age_name):
    return len(age_name[1])


print(sorted(a, key=key_1))

