s = 'abcba'  # -> abdba
new_s = s[:2] + 'd' + s[3:]
print(s, new_s)

s_list = list('abcba')
print(s_list)
s_list[2] = 'd'
print(''.join(s_list))
