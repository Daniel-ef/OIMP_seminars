print(*zip([1, 2, 3], [4, 5, 6], [7, 8, 9, 1]))

zip_l = zip([1, 2, 3], [4, 5, 6], [7, 8, 9])

print(*(zip(*zip_l)))

names = ['Vasya', 'Petr', 'Ekaterina']
ages = [20, 47, 58]

print(*zip(names, ages))
