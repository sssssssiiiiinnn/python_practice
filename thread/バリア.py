import threading
import time
import logging
"""
threading.Barrier(num)
numの数だけスレッドが同時に立ち上がる(barrier.wait())まで待つ
"""

format = '%(threadName)s;%(message)s'
logging.basicConfig(level=logging.DEBUG, format=format)


def worker1(barrier):
    logging.debug('waiting another thread')
    r = barrier.wait()
    logging.debug('num = {}'.format(r))
    while True:
        logging.debug('start')
        time.sleep(3)
        logging.debug('end')


def worker2(barrier):
    logging.debug('waiting another thread')
    r = barrier.wait()
    logging.debug('num = {}'.format(r))
    while True:
        logging.debug('start')
        time.sleep(3)
        logging.debug('end')


if __name__ == '__main__':
    barrier = threading.Barrier(2)
    t1 = threading.Thread(target=worker1, args=(barrier, ))
    t2 = threading.Thread(target=worker2, args=(barrier, ))
    t1.start()
    t2.start()