s = set()

s = {5, 1, 2, 1}
print(s)

# Creating new set
print({5, 6} | {1})
print({5, 6} & {4, 6})
print({5, 6, 7} - {5, 6})

print({5, 6} <= {5, 6, 7})  # Включение
print({5, 6, 7} < {5, 6, 7})  # Строгое включение
print({5, 6} != {5, 6, 7})

s.add(4)
s.remove(4)

# Change s
# s == {1, 2, 5}
s.difference({4, 5})
print(s)

for el in sorted(s):
    print(el)

# doesn't work
# {{4, 5}, {4}}
# {[1, 4]}

frozenset  # - immutable set

{frozenset({4, 5})}
