# eng - latin words

# 3
# apple - malum, pomum, popula
# fruit - baca, bacca, popum
# punishment - malum, multa


# latin - eng words

# malum - apple, punishment

from collections import defaultdict

n = int(input())
# lat_eng = {}
lat_eng = defaultdict(set)


for _ in range(n):
    s = input()
    eng_word, latin_str = s.split(' - ')

    for latin_word in latin_str.split(', '):

        # not need with defaultdict

        # if latin_word not in lat_eng:
        #     lat_eng[latin_word] = set()

        lat_eng[latin_word].add(eng_word)

for latin_word, eng_words in lat_eng.items():
    print('{} - {}'.format(latin_word, ', '.join(eng_words)))



