import threading
import time

resource_1 = threading.Lock()
resource_2 = threading.Lock()


def thread_1():
    with resource_1:
        print("thread 1 acquire res 1 ")
        time.sleep(1)
        print("thread 1 wating for res 2 ")
    with resource_2:
        print("thread 1 Acquire res 2 complete ")


def thread_2():
    with resource_2:
        print("thread 2 acquire res 2 ")
        time.sleep(1)
        print("thread 2 wating for res 1 ")
        with resource_1:
            print("thread 2 Acquire res 1 complete ")


A = threading.Thread(target=thread_1)
B = threading.Thread(target=thread_2)

A.start()
B.start()
