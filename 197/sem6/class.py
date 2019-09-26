class Human:
    age = 0
    name = ''

    def __str__(self):
        return str(self.age) + ' ' + self.name


tuple_list = [
    (20, 'Ivan'),
    (23, 'Alexey'),
    (18, 'Petr'),
    (18, 'Fedor')
]

class_list = []  # empty list
for age, name in tuple_list:

    human = Human()
    human.age = age
    human.name = name

    class_list.append(human)


def key_func(human: Human):
    return len(human.name)


# equal
key_lambda = lambda x: len(human.name)

c = sorted(class_list, key=lambda x: len(human.name))
for el in c:
    print(el)
