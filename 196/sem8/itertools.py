import itertools

print(*itertools.permutations([5, 6, 1]))
print(*itertools.permutations([5, 6, 1], 2))

print()

print(*itertools.combinations([1, 5, 2, -8, 'str'], 3))

