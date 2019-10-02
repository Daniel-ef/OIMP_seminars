def make_set_of_set(response):

    # return set(map(lambda x: frozenset(x.items()), response))

    s = set()
    for dict_ in response:
        s.add(frozenset(dict_.items()))
    return s




response = [
 {'score': 10.9, 'driver_id': 'order_id_2'},
 {'driver_id': 'order_id_1', 'score': 50.4},
]

true_response = [
 {'driver_id': 'order_id_1', 'score': 50.4},
 {'driver_id': 'order_id_2', 'score': 10.9},
]

assert make_set_of_set(response) ==\
      make_set_of_set(true_response)

