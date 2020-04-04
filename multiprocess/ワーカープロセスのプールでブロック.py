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
    time.sleep(3)
    logging.debug('end')
    return i


if __name__ == '__main__':
    i = 10
    # 同時に行える非同期処理数
    with multiprocessing.Pool(1) as p:
        # 処理が終了するまで次の行に進まない
        logging.debug(p.apply(worker1, args=(200, )))
        logging.debug('executed apply')
        # 非同期処理
        p1 = p.apply_async(worker1, args=(100, ))
        p2 = p.apply_async(worker1, args=(100, ))
        logging.debug('executed')
        # 1秒しか待たない
        logging.debug(p1.get())
        logging.debug(p2.get())
