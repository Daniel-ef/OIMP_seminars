def make_set_of_set(a):
    s = set()
    for dict_ in a:
        fs = frozenset(dict_.items())
        s.add(fs)
    return s
    # set(frozenset(tuple))
    # return set(map(lambda x: frozenset(x.items()), a))


response = [
 {'score': 10.9, 'order_id': 'order_id_2'},
 {'order_id': 'order_id_1', 'score': 50.4},
]


assert make_set_of_set(response) == make_set_of_set([
 {'order_id': 'order_id_1', 'score': 50.4},
 {'order_id': 'order_id_2', 'score': 10.9},
])

