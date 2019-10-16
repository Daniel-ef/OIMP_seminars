import threading


def count_print():
    a = []
    for i in range(5000000):
        a.append(i)

    print("Exit from function")

# count_print()

threading.Thread(target=count_print).start()
threading.Thread(target=count_print).start()

