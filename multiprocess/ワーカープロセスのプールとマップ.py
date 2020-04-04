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
        # 両方の結果が返ってきてから次の行に進む
        r = p.map(worker1, [100, 100])
        logging.debug('executed apply')
        logging.debug(r)

        # 実行してから結果が返ってきた時点で表示する
        r = p.map_async(worker1, [100, 100])
        logging.debug('executed apply')
        logging.debug(r.get())

        # 実行してから結果が返ってきた時点で表示する
        r = p.imap(worker1, [100, 200])
        logging.debug('executed apply')
        logging.debug([i for i in r])