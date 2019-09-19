a = 1
b = 2
# print(a, b)
a, b = b, a
# print(a, b)

print(1, 2, 3, sep=', ')

print(1, end='\n')  # перевод строки
print(2, end='\t')  # табуляция
print('\n############ bool')


# bool

a = True
b = False

a or b and not a

print(int(a))

1 < 2 > 3
1 <= 2 >= 4  # not =>

# if elif else

a = 15
if a > 0:
    print(a)
else:
    print(-a)

if a > 0:
    print(a)
elif a == 0:
    print(0)
elif a == 15:
    print(15)
else:
    print(-a)

a = 1
if a == 15:
    if a == 100500:
        a = 2
else:
    a = 5

# while
print('while ########')

i = 0
while i < 10:
    print(i)
    i += 1
else:
    print(i)

# break, continue
print('break ########')

i = 0
while i < 10:
    print(i)
    i += 1
    if i == 5:
        break


print('continue #######')
i = 0
while i < 10:
    if i == 5:
        i += 1
        continue
    print(i)
    i += 1
