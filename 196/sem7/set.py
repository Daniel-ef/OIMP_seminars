s = {1.5, 2, 'abc', 1}
print(s)

s = set()  # {} - dict
s = {1.5, 2, 5.6, 1}

print(sorted(s))

# A | B - объединение
# A & B - пересечение

print({5, 6} == {6, 5})
print({5, 6} <= {5, 6, 7})  # подмножество
print({5, 6} < {5, 6})  # Строгое

for el in s:
    print(el)

s.add(5)
s.remove(5)

if 5 in s:
    print(s)

a = frozenset([5, 4])  # immutable set


s = {{5, 4}, {4, 5}}
set_of_set = {frozenset({1, 2}), frozenset({5, 6})}
