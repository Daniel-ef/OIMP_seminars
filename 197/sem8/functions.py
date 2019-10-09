l = [-1, 2, 0, -4, 5]

# filter
# create list of elements if f(el) == True
print(min(filter(lambda x: x > 0, l)))

# all, any
print(all([0, 1, 2]))  # all elements are True
print(any([0, 1, 2]))  # At least one element is True

# enumerate
for i, el in enumerate([1, 3, 'str']):
    print(i, el)


