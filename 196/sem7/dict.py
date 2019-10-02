d = {0: 5, 1: 2, 5: 20}  # {key: value}

oil = {
    92: 100,
    95: 100,
}

print(oil.keys())
print(oil.values())
print(oil.items())  # [(key, value),]

for key in oil:
    print(oil[key])

for key, value in oil.items():
    print(key, value)

d = {tuple([1, 2]): 5}

assert len(d) < 5
