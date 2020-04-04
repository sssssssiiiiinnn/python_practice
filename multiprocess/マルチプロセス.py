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


def worker1(i):
    logging.debug('start')
    logging.debug(i)
    time.sleep(3)
    logging.debug('end')


def worker2(i):
    logging.debug('start')
    logging.debug(i)
    logging.debug('end')


if __name__ == '__main__':
    i = 10
    t1 = multiprocessing.Process(target=worker1, args=(i, ))
    t2 = multiprocessing.Process(target=worker2, args=(i, ))
    t1.daemon = True
    t1.start()
    t2.start()
    # 終了を待つことを明示する
    t1.join()
    t2.join()