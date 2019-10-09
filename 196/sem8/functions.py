print(*filter(lambda x: x > 0, [5, -1, 2, -4]))

print(*enumerate(['a1', 'b2', 'c3']))
for i, el in enumerate(['a1', 'b2', 'c3']):
    print(i, el)

a = 5
b = 2

conditions = [a > 2 + 4, b < 5 - 10]
if all(conditions):
    print('success')

print(all([0, 2, 1]))
print(any([0, 2, 1]))
