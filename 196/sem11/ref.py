import sys

a = []
b = a
print(sys.getrefcount(a))  # количество ссылок
