import multiprocessing

def print_count():
    while True:
        continue


# print_count()

multiprocessing.Process(target=print_count).start()
print(1)
multiprocessing.Process(target=print_count).start()
