# 3
# apple - malum, pomum, popula
# fruit - baca, bacca, popum
# punishment - malum, multa
# 3
# apple - malum, pomum, popula
# fruit - baca, bacca, popum
# punishment - malum, multa



# malum - apple, punishment
# ...

from collections import defaultdict
n = int(input())

d = defaultdict(set)
# d = {}

for _ in range(n):
    s = input()
    eng_key, latin_values = s.split(' - ')
    for latin_word in latin_values.split(', '):

        # if latin_word not in d:
        #     d[latin_word] = set()

        d[latin_word].add(eng_key)


for latin_word, eng_words in d.items():
    print('{} - {}'.format(latin_word, ', '.join(eng_words)))


