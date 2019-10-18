import math
import multiprocessing

from map_reduce.benchmark import benchmark
from map_reduce.data_utils import *


@benchmark
def map_reduce(filename, map_func, reduce_func, folds=4):
    data = load_data(filename)
    fold_size = math.ceil(len(data) / folds)
    queue = multiprocessing.Queue()

    procs = []

    proc = multiprocessing.Process(
        target=reduce_func,
        args=(queue, folds, )
    )
    procs.append(proc)
    proc.start()

    for i in range(folds):
        proc = multiprocessing.Process(
            target=map_func,
            args=(data[i * fold_size: (i+1) * fold_size], queue)
        )
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()


@benchmark
def single_process(filename, func):
    data = load_data(filename)
    return func(data)




