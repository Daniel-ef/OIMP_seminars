# [(age, name)]
a = [
     (20, 'Ivan'),
     (23, 'Alexey'),
     (18, 'Petr'),
     (18, 'Fedor')
     ]


def key_1(age_name):
    return age_name[1]


def key_2(age_name):
    return len(age_name[1])


print(sorted(a, key=key_2))

