a = [1, 2., 'str']  # list
tup = (1, 2.)  # tuple

#  tup[0] = 3  doesn't work
s = 'str'
# s[0] = 3  doesn't work

print(a)
a[0] = 'baobab'
print(a)
a.append('pikhta')
print(a)
a.insert(0, 'elka')
print(a)

print(len(a),
      a.index('str'),  # find element index
      a.count(2.),
      )

a.append(a)
print(a == a[-1], a)



