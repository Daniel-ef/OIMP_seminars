print(tuple(range(5)))
print(tuple(range(1, 5)))
print(tuple(range(1, 5, 2)))
print(tuple(range(5, -1, -1)))

print(range(5))

print()
for i in range(5):
    print(i)

print()
tup = (1, 5.4, 'str')  # tuple
for element in tup:  # tuple
    print(element * 2)
print(tup * 2)  # (1, 5.4, 'str', 1, 5.4, 'str')

print()
for (i, element) in enumerate(tup):
    print(i, element)
print()

# equal
for i in range(len(tup)):
    print(i, tup[i])
