# # bool
# a = True
# b = True
#
# c = 15 <= 3 > 15
# d = 15 != 3
#
# int(True)  # 1
# int(False)  # 0
#
# num = 1
#
# # if elif else
#
# a = 15
#
# if a > 0:
#     print(a)
# else:
#     print(-a)
#
# if a > 0:
#     print(a)
# elif a < -15:
#     print(-a)
# elif a < 0:
#     print(1234)
# else:
#     print(0)
#
# if a > 0:
#     if a > 15:
#         if a > 100500:
#             print(a)
#         else:
#             print(-a)
#
# # while
#
i = 0
while i < 10:
    print(i, end=' ')
    i += 1
else:
    print()

# break, continue

i = 0
while i < 10:
    if i == 5:
        break

# print

print(1, 2, 3, sep=', ', end='')

# ternar
# c++: cond ? a : b;
# python: `a` if `condition` else `b`

a = 1 if 2 > 3 else 4 # int

print(1 if 2 > 3 else 4)

print(abs(-10))

# https://informatics.msk.ru/mod/statements/view3.php?id=3380&chapterid=3506
# var1
is_triangle = a + b > c and a + c > b and b + c > a # bool
# and, or, not

# var2
if not a + b <= c:
    if a + c > b:
        if b + c > a:
            is_triangle = True

abs