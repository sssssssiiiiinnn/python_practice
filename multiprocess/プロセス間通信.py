from multiprocessing import (
    Lock, RLock, Semaphore, Queue, Event, Condition, Barrier,
    Process, Value, Array, Pipe, Manager
)


import logging
import multiprocessing
import time


logging.basicConfig(
    level=logging.DEBUG, format='%(processName)s; %(message)s'
)


def worker1(d, lock):
    logging.debug('start')
    with lock:
        i = d['x']
        time.sleep(3)
        d['x'] = i + 1
    logging.debug(d)
    logging.debug('end')


def worker2(d, lock):
    logging.debug('start')
    with lock:
        i = d['x']
        time.sleep(3)
        d['x'] = i + 1
    logging.debug(d)
    logging.debug('end')


if __name__ == '__main__':
    d = {'x': 0}

    lock = multiprocessing.Lock()
    t1 = multiprocessing.Process(target=worker1, args=(d, lock))
    t2 = multiprocessing.Process(target=worker2, args=(d, lock))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    logging.debug(d)