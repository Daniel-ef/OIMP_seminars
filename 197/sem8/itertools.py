import functools
import itertools

l = [0, 5, 1, 'str', {5}]

# Перестановки
print(*itertools.permutations(l))
print(*itertools.permutations(l, 2))
print()
# All unique combinations of elements with size = 4
print(*itertools.combinations(l, 4))

print('accumulate')
# [A, B, C]
# A, f(A, B), f(f(A, B), C)
print(*itertools.accumulate([5, 2, 10], max))

print('reduce')
# f(f(A, B), C)
print(functools.reduce(max, [5, 2, 10]))
