from multiprocessing import Process


def count_print():
    a = []
    for i in range(5000000):
        a.append(i)

    print("Exit from function")

processes = []

for _ in range(2):
    proc = Process(target=count_print)
    processes.append(proc)
    proc.start()

for proc in processes:
    proc.join()

