import multiprocessing
import os
from queue import PriorityQueue

from map_reduce.data_utils import generate_data
from map_reduce.map_reduce import map_reduce, single_process


def map_func(data: list, queue: multiprocessing.Queue):
    print('Start map func ', os.getpid())
    data.sort()
    queue.put_nowait(data)
    print('Map end')


def get_fold(folders):
    while True:
        try:
            return folders.get_nowait()
        except:
            continue


def reduce_func(queue: multiprocessing.Queue, folds_num):
    folds = []
    for i in range(folds_num):
        fold = get_fold(queue)
        print(f'Got new fold {i+1}\{folds_num}')
        folds.append(fold)

    pq = PriorityQueue()
    ans = []

    # init queue
    for i, fold in enumerate(folds):
        pq.put_nowait((fold[0], i, 0,))

    while not pq.empty():
        min_el = pq.get_nowait()
        print(min_el)
        fold_num = min_el[1]
        ind_in_fold = min_el[2]

        if ind_in_fold + 1 < len(folds[fold_num]):
            next_el = folds[fold_num][ind_in_fold + 1]

            pq.put_nowait((next_el, fold_num, ind_in_fold + 1))

        ans.append(min_el[0])
    return ans


filename = 'data_100mb'
generate_data(100 * 1024**2 // 8, filename)

mr_ans = map_reduce(filename, map_func, reduce_func, 16)
sp_ans = single_process(filename, lambda x: list(sorted(x)))
assert mr_ans == sp_ans






