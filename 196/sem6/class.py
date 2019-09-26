class Human:
    age = 0
    name = ''

    def __str__(self):
        return str(self.age) + ' ' + self.name


tuple_humans = [
    (23, 'Anton'),
    (20, 'Ivan'),
    (30, 'Alex'),
    (18, 'Fedor')
]

class_humans = []
for age, name in tuple_humans:
    human = Human()
    human.age = age
    human.name = name
    class_humans.append(human)

for human in class_humans:
    print(human)


def key_(human: Human):
    return human.name


class_humans.sort(key=key_, reverse=True)
class_humans.sort(key=lambda human: human.name, reverse=True)

print()
for human in class_humans:
    print(human)
