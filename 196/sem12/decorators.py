import time


def my_decorator(func):
    def wrapper():
        print('Before func')
        func()
        print('After func')

    return wrapper


def benchmark(func):
    def wrapper(*args, **kwargs):
        t = time.time()
        func(*args, **kwargs)
        print(time.time() - t)
    return wrapper


def decorator_generator(decorator_name):
    def benchmark(func):
        def wrapper(*args, **kwargs):
            print(f'Decorator name {decorator_name}')
            t = time.time()
            func(*args, **kwargs)
            print(time.time() - t)

        return wrapper
    return benchmark


# @my_decorator  #  my_decorator(func_for_decorator)()
@decorator_generator("Foo_decor")
def func_for_decorator(func_name):
    print(f'I am {func_name} function')
    [el for el in range(5000000)]


func_for_decorator('Foo')
