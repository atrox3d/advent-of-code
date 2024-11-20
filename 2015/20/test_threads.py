# SuperFastPython.com
# example of stopping a new thread
from time import sleep
import threading
from threading import Thread, Lock
from threading import Event

try:
    import gifts
except:
    from . import gifts

# custom task function
def task(target:int, current:int):
    global event
    global lock

    name = threading.current_thread().name
    _id = threading.get_ident()
    # execute a task in a loop
    # print(f'Worker {name = } STARTING...')
    # for i in range(5):
    #     # block for a moment
    #     sleep(1)
    #     # check for stop
    #     with lock:
    #         if event.is_set():
    #             print(f'Worker {name = } event IS SET')
    #             break
    #     if i == 4:
    #         with lock:
    #             print(f'Worker {name = } SETTING EVENT')
    #             event.set()
    #     # report a message
    #     print(f'Worker {name = } running...')
    # print(f'Worker {name = } closing down')
    # with lock:
    if event.is_set():
        print(f'Worker {name = } event IS SET, returning')
        return

    total = gifts.get_presents_per_house(current)
    if total >= target:
        # with lock:
        print(f'Worker {name = } {current = } {total = } event SETTING event')
        event.set()
    else:
        # print(f'Worker {name = } target not reached: exiting')
        return

def nope():
    # create the event
    event = Event()
    lock = Lock()
    threads = []
    # create and configure a new thread
    house = 1
    while not event.is_set():
        thread = Thread(target=task, args=(33_100_000, house))
        threads.append(thread)
        # start the new thread
        thread.start()
        house += 1
        # sleep(1)
    # block for a while
    # sleep(10)
    # stop the worker thread
    print('Main stopping thread')
    # event.set()
    # wait for the new thread to finish
    for thread in threads:
        thread.join()
