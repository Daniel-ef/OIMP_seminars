# sort
a = [6, 1, 4, 3]
a.sort()
print(a)

a = [6, 1, 4, 3]
print(sorted(a))

# tuple

print((6, 7) < (3, 8))  # False
print((3, 7) < (3, 8))  # True
print((3, 7, 4) < (3, 7))  # False
print((3, 7, 4) > (3, 7))  # True

print((3, 'abc') > (3, 'cde'))  # False
# print((3, 'abc') > (3, 4))  # Exception






