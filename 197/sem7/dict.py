d = dict()

d = {'Password': 'Пароль', 1: 5, 7: 4.4}

print(d.keys())
print(d.values())

print(d.items())

for key in d:
    print(key, d[key])

for key, value in d.items():
    print(key, value)

print(d.get(2, 0))

d = {
    95: 100,
    98: 200,
    100: 20
}
