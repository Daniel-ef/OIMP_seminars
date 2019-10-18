import pickle
import random

from map_reduce.decorators import benchmark


@benchmark
def generate_data(size, filename='data'):  # size in GB
    with open(filename, 'wb') as f:
        pickle.dump(
            [random.randint(0, 300000)
             for _ in range(size)],
            f)


def load_data(filename='data'):
    with open(filename, 'rb') as f:
        data = pickle.load(f)
        print(f'Data len: {len(data)}')
        return data


