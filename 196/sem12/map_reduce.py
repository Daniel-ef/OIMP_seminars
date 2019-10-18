import math
import multiprocessing
import pickle
import random
import time


def benchmark(func):
    def wrapper(*args, **kwargs):
        t = time.time()
        func(*args, **kwargs)
        print(time.time() - t)
    return wrapper


@benchmark
def generate_data(size):  # size in GB
    with open('data', 'wb') as f:
        pickle.dump(
            [random.randint(0, 1000000)
             for _ in range(size )],
            f)


def load_data(filename='data'):
    with open(filename, 'rb') as f:
        data = pickle.load(f)
        print(f'Data len: {len(data)}')
        return data


def map_filter_7(numbers: list, ans: multiprocessing.Queue):  # map_func
    print('Started filtering')
    filtered = list(filter(lambda x: x % 7 == 0, numbers))
    ans.put_nowait(filtered)
    print('Filtered data put')


def get_fold(folders):
    while True:
        try:
            return folders.get_nowait()
        except:
            continue


def reduce_sort(folders: multiprocessing.Queue, folds: int):
    print('Started reducing')
    mas = []
    for _ in range(folds):
        fold = get_fold(folders)
        print('Got another fold')
        mas.extend(fold)

    return sorted(mas)


@benchmark
def map_reduce(data, map_func, reduce_func, folds=4):
    procs = []
    fold_size = math.ceil(len(data) / folds)
    queue = multiprocessing.Queue()

    # schedule and start map tasks
    print('Starting map tasks')
    for i in range(folds):
        fold = data[i * fold_size:(i+1) * fold_size]
        proc = multiprocessing.Process(
            target=map_func,
            args=(fold, queue, )
        )
        procs.append(proc)
        proc.start()

    # Reducing results from map tasks
    sorted_numbers = reduce_func(queue, folds)
    print(len(sorted_numbers))


@benchmark
def test_it():
    print(len(sorted(filter(lambda x: x % 7 == 0, load_data()))))


# generate_data(500 * 1024**2 // 8)

map_reduce(load_data(), map_filter_7, reduce_sort, 16)
test_it()









