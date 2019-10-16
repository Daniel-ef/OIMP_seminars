import threading
import time

def print_count():
    # a = [el for el in range(10000000)]
    time.sleep(1)

# print_count()

threading.Thread(target=print_count).start()
threading.Thread(target=print_count).start()
