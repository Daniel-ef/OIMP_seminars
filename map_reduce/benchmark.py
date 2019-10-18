import time


def benchmark(func):
    def wrapper(*args, **kwargs):
        t = time.perf_counter()
        func(*args, **kwargs)
        print(f'Time of {func.__name__}: {time.perf_counter() - t}')

    return wrapper

