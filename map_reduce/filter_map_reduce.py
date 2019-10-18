import multiprocessing

from map_reduce.map_reduce import map_reduce


def map_func(data: list, queue: multiprocessing.Queue):
    print('Start putting data')
    queue.put_nowait(list(filter(lambda x: x % 7 == 0, data)))
    print('Put data')


def get_fold(folders):
    while True:
        try:
            return folders.get_nowait()
        except:
            continue


def reduce_func(queue: multiprocessing.Queue, folds):
    ans = []
    for _ in range(folds):
        fold = get_fold(queue)
        print('Got new fold')
        ans.extend(fold)

    ans.sort()

# generate_data(500 * 1024**2 // 8)


map_reduce('data', map_func, reduce_func, 4)

